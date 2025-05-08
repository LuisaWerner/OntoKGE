"""
use scallop inside training loop to reason additional triples and add them to batch
(Option 2 of my notes)
"""
import pathlib
from typing import List, Dict, Optional, Any, Union, TextIO, Mapping
import os
import inspect
import re
import gc
import warnings
from collections import defaultdict
from time import time
import argparse
import json
from pathlib import Path
import random
import numpy as np
import pykeen.utils
import torch.cuda
from pykeen.typing import LabeledTriples, EntityMapping, RelationMapping
from tqdm import tqdm
import wandb
from pykeen.pipeline import pipeline
from class_resolver import HintOrType
from pykeen.triples import TriplesFactory
from pykeen.models import ConvE, TransE, BoxE, QuatE
from pykeen.models import ERModel
from torch.optim import Adam, Adadelta
from pykeen.evaluation import MetricResults
from pykeen.evaluation import RankBasedEvaluator
from pykeen.triples import CoreTriplesFactory
from torch.optim.optimizer import Optimizer
from torch.utils.data import DataLoader, Dataset
from torch.utils.data.dataloader import default_collate
import scallopy
from torch import IntTensor, Tensor
from typing import TypedDict
from pykeen.sampling import BasicNegativeSampler
from torch.utils.data.sampler import SequentialSampler
from tqdm import tqdm
from pykeen.losses import BCEWithLogitsLoss, Loss
from pykeen.trackers import WANDBResultTracker
from pykeen.triples.utils import compute_compressed_adjacency_list
from metric.heuristics import *
from metric.parser import parse_rule, parse_rule_file
from metric.grounding import HerbrandBase

def diff(triples1, triples2):
    """compute the difference of two triple lists
        --> slow! Quadratic complexity and lists..."""
    assert len(triples2) >= len(triples1)
    diff = []
    trp1 = triples1.tolist()
    trp2 = triples2.tolist()
    for el in trp2:
        if el not in trp1:
            diff.append(el)
    return diff


class ExperimentConf(object):
    """transforms conf_dict to object"""

    def __init__(self, conf_dict: dict):
        self.optimizer = None
        self.log_embeddings = None
        self.silent = None
        self.es_patience = None
        self.es_delta = None
        self.use_early_stopping = None
        self.reason = None
        self.log_intermediate_concept = None
        self.log_redundant = None
        self.log_time_and_facts = None
        self.dataset_name = None
        self.datalog_file = None
        self.iter_limit = None
        self.num_triples_to_drop = None
        for key, value in conf_dict.items():
            setattr(self, key, value)


class DatalogReasoner:
    def __new__(cls, conf: ExperimentConf, relation_dict: Dict[str, int], **kwargs):
        """ Return None if we don't need a reasoner """
        if not conf.reason:
            return None
        return super().__new__(cls)

    def __init__(self, conf: ExperimentConf, relation_dict: dict, initial_score=1.0,
                 provenance: str = 'topkproofs', k: int = 5):
        """
        define the Scallop Program
        creates a positive and negative reasoner
        given the datalog file

        Parameters:
        - conf (ExperimentConf): Experiment configuration object.
        - relation_dict (Dict[str, int]): Dictionary mapping relation names to IDs.
        - initial_score (float): Initial score for facts.
        - provenance (str): Provenance type for ScallopContext.
        - k (int): Parameter k for ScallopContext.
        """
        self.relation_dict = relation_dict
        self.relation_dict_inverse = {v: k for k, v in relation_dict.items()}
        self.initial_score = initial_score
        self.iter_limit = conf.iter_limit
        self.num_rules = 0
        self.rule_scores = []
        self.num_neg_rules = 0
        self.num_pos_rules = 0
        self.datalog_file = conf.datalog_file
        self.dataset_file = conf.dataset_name

        self.log_time_and_facts = conf.log_time_and_facts
        self.log_redundant = conf.log_redundant
        self.log_intermediate_concept = conf.log_intermediate_concept
        self.log_time_and_facts = conf.log_time_and_facts

        self.datalog_str = ""
        self.stats = {}
        self.debug = False

        # initialize base scallop programs with rules and relations but no facts yet
        if self.datalog_file is not None:
            self.ctx = scallopy.ScallopContext(provenance=provenance, k=k)
            self.ctx_neg = scallopy.ScallopContext(provenance=provenance, k=k)

            for rel in self.relation_dict.keys():
                self.ctx.add_relation(rel, (int, int))
                self.ctx_neg.add_relation(rel, (int, int))

            self._parse_datalog_file()
        else:
            warnings.warn("No datalog file specified")
            self.datalog_str = ''

    def _parse_datalog_file(self):
        """
        Parses the datalog program from rule file into self.ctx instance
        The following format is expected
        Rules start with a score and the rule: <score>:<rule>, separated by a ":"
        If there's no score, we put a placeholder "_"
        Empty lines are skipped
        commented lines start with #
        negative rules start with a capital NOT in the head predicate
        confidence scores. Rules have to start with <score>:<rule>.
        If the rule does not have a score, put _:<rule>
        at first, isolate part before : and after :
        """

        _path = Path.cwd().parent / "datasets" / self.dataset_file / 'datalog_program' / self.datalog_file

        with open(_path, "r") as file:

            for line in file:
                if line.startswith("#"):
                    continue
                if line.strip() == "":  # ignore empty lines
                    continue

                assert line.count(":") == 1
                score, rule = line.split(":")

                if rule.startswith("NOT"):
                    self.ctx_neg.add_rule(rule.strip())
                    self.datalog_str += rule
                    self.num_neg_rules += 1
                else:
                    self.ctx.add_rule(rule.strip())
                    self.datalog_str += rule
                    self.num_pos_rules += 1

        self.negative_relations = [rel for rel in self.ctx_neg.relations() if rel.startswith('NOT')]
        self.num_rules = self.num_neg_rules + self.num_pos_rules
        self.rule_scores.append(score)

        # log information about datalog program
        self.stats['neg_num_rules'] = self.num_neg_rules
        self.stats['num_rules'] = self.num_rules
        self.stats['neg_relations'] = self.negative_relations
        self.stats['datalog_program'] = self.datalog_str
        self.stats['relation_names'] = list(self.relation_dict.keys())
        self.stats['pos_num_rules'] = self.num_pos_rules

    def parse_triple_to_tuple(self, _batch: IntTensor) -> dict[list[tuple]]:
        """ Groups triples by relation and puts them in a dictionary where  the relation is the key.
        For each key a list of tuples that are contained in the batch are stored. """
        # transform batch triples to facts
        in_facts = {k: [] for k in self.relation_dict.keys()}
        # group triples by relation
        for triple in _batch:
            head, rel, tail = triple
            in_facts[self.relation_dict_inverse[rel.item()]].append((head.item(), tail.item()))
        return in_facts

    def parse_tuple_to_triple(self, facts: dict[list[tuple]]) -> Tensor:
        """
        transforms dictionary back to a triple tensor
        """
        out_triples = []
        for key, value in facts.items():
            for _tuple in value:
                _tuple = _tuple[1]
                # if added as negative samples, the not needs to be removed, it is implicitly taken into account by
                # adding the triple to the set of negative triples
                if key.startswith('NOT'):
                    key = key.split("_")[1]
                out_triples.append(torch.IntTensor([_tuple[0], self.relation_dict[key], _tuple[1]]))

        out_triples = torch.vstack(out_triples)

        return out_triples

    def log_num_added_triples_per_rel(self, added_triples: [[]]) -> dict:
        """counts how many triples have been added grouped by relation type.
        Returns result as dictionary """
        num_added_triples_per_rel = {}
        added_triples = torch.IntTensor(added_triples)
        for rel in self.relation_dict.keys():
            try:
                filtered = added_triples[added_triples[:, 1] == self.relation_dict[rel]]
                num_added_triples_per_rel[rel] = len(filtered)
            except IndexError:
                num_added_triples_per_rel[rel] = 0

        return num_added_triples_per_rel

    def reason_negative_samples(self, _batch: IntTensor) -> [IntTensor, dict]:
        """ add negative samples with negative reasoner """
        in_facts = self.parse_triple_to_tuple(_batch)
        batch_ctx_neg = self.ctx_neg.clone()
        for rel in self.relation_dict.keys():
            batch_ctx_neg.add_facts(rel, [(self.initial_score, _tuple) for _tuple in in_facts[rel]])
        # run scallop program
        start = time()
        try:
            batch_ctx_neg.run(iter_limit=self.iter_limit)
        except TypeError:
            batch_ctx_neg.run()
            warnings.warn(
                "Argument iter_limit is ignored because it is not available in the used scallopy version. "
                "Use scallopy 0.1.4 with Python 3.9 to access this parameter."
            )
        end = time()

        # collect results
        out_facts = {k: [] for k in self.negative_relations}
        for rel in self.negative_relations:
            out_facts[rel] = list(batch_ctx_neg.relation(rel))

        out_triples = self.parse_tuple_to_triple(out_facts)

        self.stats['neg_reasoning_time'] = end - start
        self.stats['neg_num_added_triples_per_rel'] = self.log_num_added_triples_per_rel(out_triples)
        self.stats['neg_num_added_triples'] = len(out_triples)

        return out_triples

    def __call__(self, _batch: IntTensor) -> [IntTensor, dict]:
        """ infers new triples with Scallop """
        in_facts = self.parse_triple_to_tuple(_batch)

        # Add facts to the reasoning context
        batch_ctx = self.ctx.clone()
        for rel in self.relation_dict.keys():
            batch_ctx.add_facts(rel, [(self.initial_score, _tuple) for _tuple in in_facts[rel]])

        # Run Scallop program
        start = time()
        try:
            batch_ctx.run(iter_limit=self.iter_limit)
        except TypeError:
            batch_ctx.run()
            warnings.warn(
                "Argument iter_limit is ignored because it is not available in the used scallopy version. "
                "Use scallopy 0.1.4 with Python 3.9 to access this parameter."
            )
        end = time()

        # Collect reasoned triples
        out_facts = {k: [] for k in self.relation_dict.keys()}
        for rel in self.relation_dict.keys():
            out_facts[rel] = list(batch_ctx.relation(str(rel)))
        out_triples = self.parse_tuple_to_triple(out_facts)

        # self-connections added?
        if self.debug:
            num_self_connections = sum([trp[0] == trp[2] for trp in out_triples])
            types = []
            for trp in out_triples:
                if trp[0] == trp[2]:
                    types.append(trp[1].item())
            types = list(set(types))
            rels = [self.relation_dict_inverse.get(r) for r in types]

        # logging
        # check how many of the reasoned triples exist in other train batch, or even valid/test
        if self.log_redundant:
            _diff = diff(_batch, out_triples)
            train_mask, val_mask, test_mask = Preprocesser.triple_filter(trp_checker=triple_checker, triples=_diff)
            self.stats['num_redundant_train'] = sum(train_mask)
            self.stats['num_redundant_valid'] = sum(val_mask)
            self.stats['num_redundant_test'] = sum(test_mask)

        if self.log_intermediate_concept:
            if not self.dataset_file == 'Family':
                warnings.warn(f"Intermediate concept only logged for the family dataset. "
                              f"Your using the {self.dataset_file} dataset. Logs for the intermediate concept will not be created. ")
                pass

            else:
                females = [x[1][0] for x in list(self.ctx.relation('female'))]
                males = [x[1][0] for x in list(self.ctx.relation('male'))]
                out_heads = out_triples[:, 0]
                out_tails = out_triples[:, 1]
                unique_out_entities = torch.unique(torch.hstack([out_heads, out_tails]))

                self.stats['num_intersection_fm'] = len(list(set(males) & set(females)))
                self.stats['num_male'] = len(males)
                self.stats['num_female'] = len(females)
                self.stats['num_missing_gender'] = len(unique_out_entities) - len(males) - len(females)
                self.stats['num_missing_gender'] = len(unique_out_entities) - len(males) - len(females)

        if self.log_time_and_facts:
            self.stats['num_added_triples_per_rel'] = self.log_num_added_triples_per_rel(diff(_batch, out_triples))
            self.stats['num_added_triples'] = len(out_triples) - len(_batch)
            self.stats['reasoning_time'] = end - start
        return out_triples


class Logger:
    def __init__(self, conf: ExperimentConf):
        self._dict_triples_per_rel = None
        self._neg_dict_triples_per_rel = None
        self._reasoning_time = []
        self._num_added_triples = []
        self._neg_reasoning_time = []
        self._neg_num_added_triples = []
        self._neg_relations = []
        self._num_redundant_train = []
        self._num_redundant_valid = []
        self._num_redundant_test = []
        self._num_male = []
        self._num_female = []
        self._num_missing_gender = []
        self._num_intersection = []
        self.conf = conf
        self.epoch = 0
        self.use_early_stopping = conf.use_early_stopping
        self.patience = conf.es_patience
        self.es_delta = conf.es_delta
        self.print_steps = 1
        self.valid_losses = []
        self.reason = conf.reason
        self.silent = conf.silent
        self.log_time_and_facts = conf.log_time_and_facts
        self.log_redundant = conf.log_redundant
        self.log_intermediate_concept = conf.log_intermediate_concept
        self.log_embeddings = conf.log_embeddings

        wandb.init(project=conf.wandb_project, config=conf, mode=conf.wandb_mode,
                   allow_val_change=True)
        wandb.define_metric("train_loss", summary="last")
        wandb.define_metric("valid_loss", summary="last")
        wandb.define_metric("epoch_time", summary="mean")

        if conf.silent:
            os.environ['WANDB_SILENT'] = 'true'
            print('logger set to silent. There are no prints. Training will start now')

        if conf.reason:
            # reasoning logs
            wandb.define_metric("reason.avg_reasoning_time", summary="mean")
            wandb.define_metric("reason.num_added_triples", summary="mean")
            wandb.config.update({'fbk_weight_filter': self.extract_weight_filter(conf.datalog_file)},
                                allow_val_change=True)

    @staticmethod
    def log_device(device):
        """ logs the device that was chosen """
        wandb.config.update({'device': device}, allow_val_change=True)

    @staticmethod
    def extract_weight_filter(input_string):
        # Check if the string starts with 'fb15k237'
        if input_string.startswith("fb15k237"):
            # Find the number before 'txt'
            match = re.search(r'(\d+(\.\d+)?)\.txt', input_string)
            if match:
                # Convert the matched number to float and return it
                return float(match.group(1))
        return None

    @staticmethod
    def log_model(model: ERModel):
        try:
            wandb.config.update({'model.num_parameters': model.num_parameters}, allow_val_change=True)
            wandb.config.update({'model.num_parameter_bytes': model.num_parameter_bytes}, allow_val_change=True)
        except AttributeError:
            pass

    def save_embeddings(self, model) -> None:
        """ saves embeddings locally after training if log_embeddings = True in config.json or grid_config.yaml
        the embedding vectors can be loaded with
        test = torch.load(_path / str(_k + ".pt"))
        """

        # make directory for embeddings if it doesn't exist
        _path = Path.cwd() / 'embeddings' / model.name
        Path(_path).mkdir(parents=True, exist_ok=True)

        # store config to be sure with which parameters the respective embedding has been trained
        with open(_path / 'config.json', 'w') as f:
            json.dump(vars(self.conf), f)

        for _k, _v in model.state_dict().items():
            torch.save(_v, _path / str(_k + ".pt"))

    def log_epoch(self, train_loss: float, valid_loss: float, epoch_time: float) -> None:
        """ logs stats per epoch """
        wandb.log({'train_loss': train_loss})
        wandb.log({'valid_loss': valid_loss})
        wandb.log({'epoch_time': epoch_time})
        self.valid_losses.append(valid_loss)

        if not self.silent and self.epoch % self.print_steps == 0:
            print(
                f"Epoch {self.epoch} | Train Loss: {train_loss} | Validation loss {valid_loss} | Epoch Time {epoch_time}s")
        self.epoch += 1

    def log_reasoner(self, reasoner):
        """log reasoning statistics"""
        stats = reasoner.stats

        # if there are negative rules
        if stats['neg_num_rules'] > 0:
            try:
                self._neg_reasoning_time.append(stats['neg_reasoning_time'])
                self._neg_num_added_triples.append(stats['neg_num_added_triples'])
                self._neg_num_added_triples.append(stats['neg_numD_added_triples'])

                if self._neg_dict_triples_per_rel is None:
                    self._neg_dict_triples_per_rel = {key: [] for key in stats['neg_num_added_triples_per_rel'].keys()}
                for key, value in stats['neg_num_added_triples_per_rel'].items():
                    _wandb_key = 'neg_num_added_triples_' + str(key)
                    self._neg_dict_triples_per_rel[key].append(value)
            except KeyError:
                pass

        # if there are positive rules
        if stats['pos_num_rules'] > 0:
            try:
                self._reasoning_time.append(stats['reasoning_time'])
                self._num_added_triples.append(stats['num_added_triples'])
            except KeyError:
                pass

            # log number of added relations per relation type
            if self._dict_triples_per_rel is None:
                self._dict_triples_per_rel = {key: [] for key in stats['num_added_triples_per_rel'].keys()}
            for key, value in stats['num_added_triples_per_rel'].items():
                _wandb_key = 'num_added_triples_' + str(key)
                self._dict_triples_per_rel[key].append(value)

            # log how many triples have been reasoned that are duplicates in train or valid or test
            if self.log_redundant and 'num_redundant_train' in stats:
                self._num_redundant_train.append(stats['num_redundant_train'])
                self._num_redundant_valid.append(stats['num_redundant_valid'])
                self._num_redundant_test.append(stats['num_redundant_test'])

            # log stats for intermediate concept
            if self.log_intermediate_concept and 'num_intersection_fm' in stats:
                self._num_intersection.append(stats['num_intersection_fm'])
                self._num_male.append(stats['num_male'])
                self._num_female.append(stats['num_female'])
                self._num_missing_gender.append(stats['num_missing_gender'])

        try:
            wandb.config.update({'reason.num_rules': stats['num_rules']}, allow_val_change=True)
            wandb.config.update({'reason.datalog_program': stats['datalog_program']}, allow_val_change=True)
            wandb.config.update({'reason.relation_names': stats['relation_names']}, allow_val_change=True)
            wandb.config.update({'reason.neg_relations': stats['neg_relations']}, allow_val_change=True)
            wandb.config.update({'reason.num_neg_rules': stats['neg_num_rules']}, allow_val_change=True)
        except KeyError:
            # if the data is not there, no need to log it
            pass

    def stop_early(self, valid_loss: float) -> bool:
        """ early stopping. Stop training if validation loss doesn't decrease"""
        if not self.use_early_stopping or self.epoch < self.patience:
            return False
        # check if this makes sense
        elif np.mean(self.valid_losses[-self.patience:]) - valid_loss > self.es_delta:
            return False
        else:
            if not self.silent:
                print(f'Logger: Early Stopping at epoch {self.epoch}')
            wandb.log({"epoch_stopped": self.epoch})
            return True

    def end_experiment(self, _results: MetricResults, model: ERModel, _zeroshot_results: MetricResults = None) -> None:
        """ summarizes and uploads the logged stats to wandb """
        for key, value in _results.to_flat_dict().items():
            wandb.run.summary[key] = value

        if _zeroshot_results is not None:
            for key, value in _zeroshot_results.to_flat_dict().items():
                wandb.run.summary["zeroshot_" + key] = value

        # store embeddings
        if self.log_embeddings:
            self.save_embeddings(model)

        if self.reason:

            # if we have negative knowledge
            if len(self._neg_reasoning_time) > 0:
                wandb.run.summary['reason.avg_neg_reasoning_time'] = np.mean(self._neg_reasoning_time)
                wandb.run.summary['reason.avg_neg_num_added_triples_all'] = np.mean(self._neg_num_added_triples)

                if self._neg_dict_triples_per_rel is not None:
                    for key, value in self._neg_dict_triples_per_rel.items():
                        _key = 'reason.avg_neg_num_added_triples_' + str(key)
                        wandb.run.summary[_key] = np.mean(value)

            # if we have negative knowledge
            if len(self._reasoning_time) > 0:

                if self._dict_triples_per_rel is not None:
                    for key, value in self._dict_triples_per_rel.items():
                        _key = 'reason.avg_num_added_triples_' + str(key)
                        wandb.run.summary[_key] = np.mean(value)

                wandb.run.summary['reason.avg_reasoning_time'] = np.mean(self._reasoning_time)
                wandb.run.summary['reason.avg_num_added_triples_all'] = np.mean(self._num_added_triples)

                if self.log_redundant and len(self._num_redundant_train) > 0:
                    wandb.run.summary['reason.avg_num_redundant_train'] = np.mean(self._num_redundant_train)
                    wandb.run.summary['reason.avg_num_redundant_valid'] = np.mean(self._num_redundant_valid)
                    wandb.run.summary['reason.avg_num_redundant_test'] = np.mean(self._num_redundant_test)
                    wandb.run.summary['reason.max_num_redundant_train'] = max(self._num_redundant_train)
                    wandb.run.summary['reason.max_num_redundant_valid'] = max(self._num_redundant_valid)
                    wandb.run.summary['reason.max_num_redundant_test'] = max(self._num_redundant_test)

                if self.log_intermediate_concept:
                    wandb.run.summary['reason.avg_num_male'] = np.mean(self._num_male)
                    wandb.run.summary['reason.avg_num_female'] = np.mean(self._num_female)
                    wandb.run.summary['reason.max_num_intersection'] = max(
                        self._num_intersection)  # there should be no intersection, that means contradiction
                    wandb.run.summary['reason.avg_num_missing_gender'] = np.mean(self._num_missing_gender)

        wandb.finish()


class TriplesFactoryWithTypes(TriplesFactory):
    # Not in use
    """ TriplesFactory that Stores types """

    def __init__(self,
                 triples,
                 entity_to_type: Optional[Dict] = None,
                 **kwargs):
        super().__init__(triples, **kwargs)
        self.entity_to_type = entity_to_type or {}

    @property
    def num_types(self) -> int:
        """The number of triples."""
        return len(set(self.entity_to_type.values()))


class TripleDataset(Dataset):
    """ inherited from torch.data.Dataset"""

    def __init__(self, triples_factory: TriplesFactory, neg_sampler_filtered: bool = True,
                 neg_sampler_num_negs_per_pos: int = 1):
        super().__init__()
        self.triples_factory = triples_factory
        self.mapped_triples = triples_factory.mapped_triples
        self.num_entities = triples_factory.num_entities
        self.num_triples = triples_factory.num_triples
        self.num_relations = triples_factory.num_relations
        self.relation_dict = triples_factory.relation_to_id
        self.negative_sampler = BasicNegativeSampler(mapped_triples=self.mapped_triples, filtered=neg_sampler_filtered,
                                                     num_negs_per_pos=neg_sampler_num_negs_per_pos)

    def __len__(self):
        return self.num_triples

    def __getitem__(self, idx):
        return self.mapped_triples[idx]


class BatchWithLabels(object):
    """ stores batch as tuple of triples and their labels (corrupted or true labels)"""

    def __init__(self, triples: torch.Tensor, labels: torch.FloatTensor):
        self.triples = triples
        self.labels = labels

    def __len__(self):
        return len(self.triples)

    def to(self, device: str):
        """ components of batch to device """
        self.triples = self.triples.to(device)
        self.labels = self.labels.to(device)
        return self


class BatchCollation:
    """ The collate function puts the samples in the batch together
    Reasoned examples are only added if training = True """

    def __init__(self, dataset: TripleDataset, reasoner: DatalogReasoner, training: bool = True, logger: Logger = None):
        self.dataset = dataset
        self.training = training
        self.logger = logger
        self.reasoner = reasoner
        self.debug = False

    def __call__(self, _batch):
        """ default collate function just stacks list of tensors to a Tensor with higher dimension"""
        return default_collate(_batch)

    def collate_fn(self, _batch: list[IntTensor]) -> BatchWithLabels:
        """
        determines how the batch is collated. _batch is the next batch returned by the dataloader.
        in collate_fn, the Scallop pos_reasoner inferrs additional triples according to the scallop program
        Then the negative sampler adds corrupted triples to the batch.
        Labels for true and false triples are also returned
        """
        batch = self(_batch)

        # some stats for debug
        if self.debug:
            unique_heads = len(torch.unique(batch[:, 0]))
            unique_tails = len(torch.unique(batch[:, 2]))
            unique_entities = len(torch.unique(torch.hstack([batch[:, 2], batch[:, 0]])))
            # entities_head_or_tail = # entities that appear as well as head and tail
            all = torch.hstack([batch[:, 2], batch[:, 0]])
            num_all_unique = len(torch.unique(all))
            num_head_entities_also_in_tail = sum([batch[:, 2].__contains__(x) for x in batch[:, 0]])
            num_tail_entities_also_in_head = sum([batch[:, 0].__contains__(x) for x in batch[:, 2]])

        neg_samples_ls = []
        num_remaining_samples = len(batch)

        # reason missing triples in training
        if self.training and self.reasoner is not None:

            if self.reasoner.num_pos_rules > 0:
                batch = self.reasoner(batch)
                num_remaining_samples = len(batch)

            if self.reasoner.num_neg_rules > 0:
                neg_batch = self.reasoner.reason_negative_samples(batch)
                neg_samples_ls.append(neg_batch)
                # decide how many examples are still missing
                num_remaining_samples = len(batch) - len(neg_batch)

            if self.logger is not None and self.reasoner.log_time_and_facts:
                self.logger.log_reasoner(self.reasoner)

            # if we have too many negative samples, randomly select some  (relevant for mutual exclusion for example)
            if num_remaining_samples < 0:
                neg_samples_ls.clear()
                neg_samples_ls.append(neg_batch[torch.randperm(len(neg_batch))][:len(batch)])

        # sample negative triples because some are missing
        if num_remaining_samples > 0:
            neg_samples_ls.append(self.dataset.negative_sampler.corrupt_batch(
                batch[np.random.permutation(len(batch))][:num_remaining_samples]).squeeze())

        neg_samples = torch.vstack(neg_samples_ls)

        complete_batch = torch.vstack([batch, neg_samples])

        # create labels for true and false triples
        pos_labels = torch.ones(len(batch))
        neg_labels = torch.zeros(len(neg_samples))
        batch_labels = torch.hstack([pos_labels, neg_labels]).unsqueeze(1)

        # shuffle so that negative/positive examples as well as reasoned/original examples are not recognizable by order
        ids = torch.randperm(len(complete_batch))
        complete_batch = complete_batch[ids]
        batch_labels = batch_labels[ids]

        return BatchWithLabels(complete_batch, batch_labels)


class TripleDataLoader(DataLoader):
    """ inherits from torch.data.DataLoader """

    def __init__(self, triples: TripleDataset, reasoner: DatalogReasoner = None, batch_size: int = 1000, drop_last=True,
                 training=True, logger: Logger = None, **kwargs):
        self.triples = triples
        self.batch_size = batch_size

        # set droplast to false for validation and if batch_size exceeds number of triples because
        # otherwise the  number of batches is zero
        if len(triples) <= batch_size or not training:
            self.drop_last = False
        else:
            self.drop_last = drop_last

        self.batch_collation = BatchCollation(triples, reasoner, training=training, logger=logger)
        super().__init__(dataset=triples, batch_size=batch_size, drop_last=self.drop_last,
                         shuffle=training,
                         collate_fn=self.batch_collation.collate_fn)

    def __len__(self):
        """ Return the number of batches """
        num_batches, remainder = divmod(len(self.triples), self.batch_size)
        if not self.drop_last and remainder > 0:
            num_batches += 1
        return num_batches


class TrainingLoop:

    def __init__(self, model: ERModel, conf: ExperimentConf, logger: Logger, reasoner: DatalogReasoner = None):
        self.model = model
        self.reasoner = reasoner

        torch_optimizers = __import__('torch').optim
        try:
            cls = getattr(torch_optimizers, conf.optimizer)
            self.optimizer = cls(params=model.get_grad_params(), lr=conf.learning_rate)
        except AttributeError:
            raise AttributeError(f'The specified model {conf.model} does not exists in {torch_optimizers}.')

        self.batch_size = conf.batch_size
        self.epochs = conf.epochs
        self.logger = logger
        self.device_num = conf.device_num

        if torch.cuda.is_available() and conf.use_gpu:
            self.device = self.device_num

        # elif torch.backends.mps.is_available():
        #     self.device = 'mps'
        else:
            self.device = 'cpu'
        if not self.logger.silent:
            print(f'Device: {self.device}, Number of GPUs available: {torch.cuda.device_count()}')
        self.logger.log_device(self.device)
        self.set_seeds(conf.seed)

    def set_seeds(self, seed: int = 1234):
        """ sets random seeds for reproducibility """
        random.seed(seed)
        np.random.seed(seed)
        torch.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)
        if self.device == 'mps':
            torch.mps.manual_seed(seed)

    def train_step(self, triples: TriplesFactory) -> tuple[float, float]:
        """ One epoch on the training set """
        start = time()
        train_data_loader = TripleDataLoader(triples=TripleDataset(triples),
                                             reasoner=self.reasoner,
                                             batch_size=self.batch_size, training=True, logger=self.logger)
        self.model.train()
        train_loss = 0

        for i_batch, batch in tqdm(enumerate(train_data_loader), desc='Batch Evaluation', disable=self.logger.silent):

            self.optimizer.zero_grad()
            batch = batch.to(self.device)
            self.model.to(self.device)
            pred_scores = self.model.score_hrt(batch.triples)

            if str(self.model.loss).startswith('MarginRankingLoss') or str(self.model.loss).startswith('NSSALoss'):
                positive_scores = pred_scores[batch.labels == 1]
                negative_scores = pred_scores[batch.labels == 0]
                batch_loss = self.model.loss(positive_scores, negative_scores)

            else:
                batch_loss = self.model.loss(scores=pred_scores, labels=batch.labels)

            batch_loss.backward()
            self.optimizer.step()

            if self.model.name == 'RGCN':
                self.model.post_parameter_update()

            train_loss += batch_loss.detach().cpu().item()

        end = time()
        return train_loss, end - start

    @torch.no_grad()
    def validation_step(self, triples: TriplesFactory) -> tuple[float, float]:
        """ One epoch on the validation set """
        start = time()

        validation_data_loader = TripleDataLoader(triples=TripleDataset(triples), batch_size=self.batch_size,
                                                  training=False)
        self.model.eval()
        valid_loss = 0
        for i_batch, batch in enumerate(validation_data_loader):
            batch = batch.to(self.device)
            self.model.to(self.device)
            pred_scores = self.model.score_hrt(batch.triples)

            if str(self.model.loss).startswith('MarginRankingLoss') or str(self.model.loss).startswith('NSSALoss'):
                positive_scores = pred_scores[batch.labels == 1]
                negative_scores = pred_scores[batch.labels == 0]
                batch_loss = self.model.loss(positive_scores, negative_scores)

            else:
                batch_loss = self.model.loss(scores=pred_scores, labels=batch.labels)

            # batch_loss = self.model.loss(scores=pred_scores, labels=batch.labels)
            valid_loss += batch_loss.detach().cpu().item()

        end = time()

        return valid_loss, end - start

    def train_and_validate(self, train_triples: TriplesFactory, validation_triples: TriplesFactory) -> None:
        """ Training loop : Consists of a train and an evaluation step """
        for epoch in range(self.epochs):
            train_loss, train_step_time = self.train_step(triples=train_triples)
            valid_loss, valid_step_time = self.validation_step(triples=validation_triples)

            if self.logger.stop_early(valid_loss):
                break

            self.logger.log_epoch(train_loss=train_loss, valid_loss=valid_loss,
                                  epoch_time=valid_step_time + train_step_time)


def resolve_model(triples_factory: TriplesFactory, conf: ExperimentConf,
                  logger: Logger = None) -> ERModel:
    """ returns instance from class specified in conf.model"""
    pykeen_models = __import__('pykeen').models
    pykeen_losses = __import__('pykeen').losses
    try:
        _model = getattr(pykeen_models, conf.model)
    except AttributeError:
        raise AttributeError(f'The specified model {conf.model} does not exists in {pykeen_models}.')
    try:
        _loss = getattr(pykeen_losses, conf.loss)
    except AttributeError:
        raise AttributeError(f'The specified loss {conf.loss} does not exists in {pykeen_losses}.')
    if hasattr(conf, "embedding_dim"):
        model = _model(triples_factory=triples_factory, loss=_loss, random_seed=conf.seed,
                       embedding_dim=conf.embedding_dim)
    else:
        # use default embedding dim
        model = _model(triples_factory=triples_factory, loss=_loss, random_seed=conf.seed)
    model.name = conf.model
    logger.log_model(model)
    return model


class TripleChecker:
    """ keep track of train,valid,test to check later if triples are reasoned that are from other dataset """

    def __init__(self, train, valid, test):
        self.train = train.mapped_triples.tolist()
        self.valid = valid.mapped_triples.tolist()
        self.test = test.mapped_triples.tolist()


class Preprocesser:

    def __init__(self, conf: ExperimentConf):
        self.num_triples_to_drop = conf.num_triples_to_drop
        self.avoid_isolated_entities = conf.avoid_isolated_entities
        self.min_degree = conf.min_degree
        self.create_inverse_triples = conf.create_inverse_triples
        self.silent = conf.silent
        self.dataset = conf.dataset_name
        self.path = Path.cwd().parent / 'datasets' / self.dataset

        if hasattr(conf, "subdir"):
            self.path = self.path / conf.subdir
            print(
                f'Preprocesser: Load data for dataset {self.dataset} from subdirectory {self.path} which is specified in config.')
        if hasattr(conf, "filter_relations"):
            self.filter_relations = conf.filter_relations

    @staticmethod
    def check_self_connections(triples_factory: TriplesFactory) -> bool:
        """Check for self-connections in the given triples factory."""
        return (triples_factory.mapped_triples[:, 0] == triples_factory.mapped_triples[:, 2]).sum() > 0

    def add_class_dict(self, triples_factories: List[TriplesFactory]) -> List[TriplesFactory]:
        """Add class dictionary and number of unique classes to the list of triples factories."""
        entity_to_class = self.load_entity_to_class()
        num_classes = self.get_num_classes(entity_to_class)

        if entity_to_class is None:
            warnings.warn('No class dict loaded.')
            return triples_factories
        else:
            for triples_factory in triples_factories:
                triples_factory.entity_to_class = entity_to_class
                triples_factory.num_classes = num_classes
        return triples_factories

    @staticmethod
    def get_num_classes(entity_to_class: Optional[Dict[int, List[int]]]) -> Optional[int]:
        """Return the number of unique classes in the entity_to_class dictionary."""
        if entity_to_class is None:
            return None

        unique_classes = set()
        for classes in entity_to_class.values():
            unique_classes.update(classes)

        return len(unique_classes)

    @staticmethod
    def triple_filter(trp_checker: TripleChecker, triples: list):
        """
        This method is used to check if reasoner leaks triples from valid/test into train or
        duplicates triples from other train batches
        returns masks if true if a triple is added from another dataset (to be verified)
        @param trp_checker: A TripleChecker instance that stores the train,valid, test triples
        @param triples: The triple factory to be checked for duplicates/leakage
        """
        train_mask, val_mask, test_mask = [], [], []
        for trp in triples:
            if trp in trp_checker.test:
                # if trp in trp_checker.test.mapped_triples:
                test_mask.append(True)
            else:
                test_mask.append(False)
            if trp in trp_checker.valid:
                # if trp in trp_checker.valid.mapped_triples:
                val_mask.append(True)
            else:
                val_mask.append(False)
            if trp in trp_checker.train:
                # if trp in trp_checker.train.mapped_triples:
                train_mask.append(True)
            else:
                train_mask.append(False)
        # for each  new triple return a mask if it is in train, valid, test or none of them
        return train_mask, val_mask, test_mask

    def _degree_filter(self, triples: TriplesFactory) -> [IntTensor, IntTensor]:
        """
        filter triples by the minimum degree of the entities that form head and tail of the triples
        The objective is not to produce isolated nodes by sampling the training set
        """
        entity_degree = compute_compressed_adjacency_list(triples.mapped_triples)[0]
        triple_degree_mask = []
        for i, trip in enumerate(triples.mapped_triples):
            head, rel, tail = trip
            triple_degree_mask.append(torch.min(entity_degree[head], entity_degree[tail]))
        triple_degree_mask = torch.IntTensor(triple_degree_mask)
        indices_to_drop = (
                triple_degree_mask >= self.min_degree).nonzero().squeeze()  # indices of triples that can be dropped
        protected_triples = (triple_degree_mask < self.min_degree).nonzero().squeeze()
        shuffle_indices_to_drop = torch.randperm(len(indices_to_drop))

        if len(indices_to_drop) < self.num_triples_to_drop:
            raise Exception('degree to restrictive or n too large')

        idx = indices_to_drop[shuffle_indices_to_drop]
        idx_drop, idx_keep = idx.split(split_size=[self.num_triples_to_drop, len(idx) - self.num_triples_to_drop],
                                       dim=0)
        idx_keep = torch.cat([protected_triples, idx_keep])
        return idx_keep, idx_drop

    def randomly_drop_triples(self, triples: TriplesFactory) -> TriplesFactory:
        """
        Randomly remove triples from the training set
        """
        if triples.create_inverse_triples:
            # this should only become relevant for ConvE
            raise NotImplementedError

        if isinstance(self.num_triples_to_drop, float):
            if self.num_triples_to_drop < 0 or 1 <= self.num_triples_to_drop:
                raise ValueError
            if self.num_triples_to_drop > 0.9:
                self.num_triples_to_drop = 0.9
                raise Warning(
                    f'The drop_score was initialized with {self.num_triples_to_drop}. this value is too high, it was automatically reset to {0.9}')
            self.num_triples_to_drop = int(self.num_triples_to_drop * triples.num_triples)

        if self.avoid_isolated_entities:
            if not self.silent:
                print('avoid_isolated_entites == True. Preprocessing might take a bit longer.')
            idx_keep, idx_drop = self._degree_filter(triples)
        else:
            idx = torch.randperm(triples.num_triples)
            idx_drop, idx_keep = idx.split(
                split_size=[self.num_triples_to_drop, triples.num_triples - self.num_triples_to_drop], dim=0)

        out_triples = triples.clone_and_exchange_triples(mapped_triples=triples.mapped_triples[idx_keep])
        return out_triples

    def load_entity_to_class(self) -> Optional[Dict[int, List[int]]]:
        """Check if the entity2class.txt file exists and read it into a dictionary if it does."""
        entity_to_class_path = self.path / 'entity2class.txt'
        entity_to_class = {}

        if entity_to_class_path.is_file():
            with open(entity_to_class_path, 'r') as file:
                for line in file:
                    entity, cls = map(int, line.strip().split('\t'))
                    if entity not in entity_to_class:
                        entity_to_class[entity] = []
                    entity_to_class[entity].append(cls)
            return entity_to_class
        else:
            return None

    def load_txt_to_dict(self, filepath):
        """
        Loads a text file into a dictionary where:
        - Keys are the first column (URIs in angle brackets).
        - Values are the second column (integers).

        Parameters:
        - filepath (str): Path to the text file.

        Returns:
        - dict: A dictionary mapping URIs to integers.
        """
        data_dict = {}
        output_dict = {}

        with open(filepath, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split("\t")  # Split by tab
                if len(parts) == 2:  # Ensure there are exactly two parts
                    key, value = parts[0], int(parts[1])  # Convert value to int
                    data_dict[key] = value

        for key, value in data_dict.items():
            output_dict.update({f'rel_{value}': int(value)})

        return output_dict

    def filter_triples(self, triples: TriplesFactory) -> TriplesFactory:
        """ removes triples with relations defined in self.filter_relations """
        try:
            filter_relations_id = set(triples.relation_to_id.values()) - set(
                [triples.relation_to_id[k] for k in self.filter_relations])
            filtered_triples = triples.new_with_restriction(relations=filter_relations_id)
            return filtered_triples
        except KeyError as error_msg:
            print(error_msg,
                  "Relations in dataset that should be filtered do not appear in relation_id of the triple factory. Check if the right dataset of filter_relations are chosen.")

    def load_data(self) -> [TriplesFactory, TriplesFactory, TriplesFactory]:
        """ load train, valid and test set from the specified path and conduct preprocessing steps """
        # TODO add type dict to the triple factory
        try:
            all_triples = TriplesFactory.from_path(self.path / 'all.txt')

            if Path(self.path / "relation2id.txt").exists():
                relation_to_id = self.load_txt_to_dict(self.path / "relation2id.txt")
            else:
                relation_to_id = all_triples.relation_to_id

            entity_to_id = all_triples.entity_to_id

            all_triples = TriplesFactory.from_path(self.path / 'all.txt', entity_to_id=entity_to_id,
                                             relation_to_id=relation_to_id,
                                             create_inverse_triples=self.create_inverse_triples)
            train = TriplesFactory.from_path(self.path / 'train.txt', entity_to_id=entity_to_id,
                                             relation_to_id=relation_to_id,
                                             create_inverse_triples=self.create_inverse_triples)
            valid = TriplesFactory.from_path(self.path / 'valid.txt', entity_to_id=entity_to_id,
                                             relation_to_id=relation_to_id)
            test = TriplesFactory.from_path(self.path / 'test.txt', entity_to_id=entity_to_id,
                                            relation_to_id=relation_to_id)

        except FileNotFoundError:
            raise FileNotFoundError(f'Make sure the path {self.path} to the dataset {self.dataset} exists.')

        # Todo solve this better with another attribute in TripleFactory
        train, valid, test, all_triples = self.add_class_dict(triples_factories=[train, valid, test, all_triples])

        # Check for self-connections
        if (self.check_self_connections(all_triples) or
                self.check_self_connections(train) or
                self.check_self_connections(valid) or
                self.check_self_connections(test)):
            warnings.warn("Warning: There are self-connections in the input dataset")

        # zero shot learning: remove all links with a certain relation from test
        if hasattr(self, "filter_relations"):
            print(f'Preprocesser: Zero shot learning. Filter relations: {self.filter_relations}')
            train = self.filter_triples(train)

        # delete triples from train test to see behavior with incomplete data
        if self.num_triples_to_drop > 0:
            train = self.randomly_drop_triples(train)
            if not self.silent:
                print(f"\nRandomly dropped {self.num_triples_to_drop} training triples.")
        if not self.silent:
            print(f"Data loaded.\nTrain: {train}\nValid: {valid}\nTest: {test}\nAll: {all_triples}")

        # this is to keep train\val\test available to check if data from test has been reasoned
        global triple_checker
        triple_checker = TripleChecker(train, valid, test)

        return train, valid, test, relation_to_id


def run(_config_list):
    for i, conf in enumerate(_config_list):
        conf = ExperimentConf(conf)
        logger = Logger(conf)
        train, valid, test, relation_dict = Preprocesser(conf).load_data()
        model = resolve_model(triples_factory=train, conf=conf, logger=logger)
        reasoner = DatalogReasoner(conf, relation_dict)

        # training loop
        training_loop = TrainingLoop(model=model, conf=conf, logger=logger, reasoner=reasoner)
        training_loop.train_and_validate(train_triples=train, validation_triples=valid)

        # final evaluation
        evaluator = RankBasedEvaluator()  # filtered = true, false?
        results = evaluator.evaluate(
            model=model,
            mapped_triples=test.mapped_triples,
            batch_size=None,
            additional_filter_triples=[
                train.mapped_triples,
                valid.mapped_triples,
            ]
        )

        if conf.evaluate_rcs:
            rule_scores = defaultdict(lambda: defaultdict(list))
            rules = parse_rule_file(conf.datalog_file, conf.dataset_name)

            for _logic in conf.rcs_logic:
                for r in rules:
                    rule = parse_rule(r, logic=_logic, norm=conf.rcs_normalization, agg=conf.rcs_aggregation)
                    heuristic = RandomHeuristic(n_samples=100, seed=conf.seed)
                    herbrand_base = HerbrandBase(test, rule.arity, heuristic)
                    score = rule.evaluate(hb=herbrand_base, model=model)
                    rule_scores[conf.datalog_file][str(rule)].append(score)
                    wandb.run.summary[f'rcs_{_logic}_{rule}'] = score
                wandb.run.summary[f'ocs_{_logic}'] = np.mean([s[0] for s in rule_scores[conf.datalog_file].values()])



            # evaluate performance only filtered out relations
        if hasattr(conf, "filter_relations"):
            filter_relations_id = [test.relation_to_id[i] for i in conf.filter_relations]
            results_filtered = evaluator.evaluate(
                model=model,
                mapped_triples=test.mapped_triples[
                    sum(test.mapped_triples[:, 1] == i for i in filter_relations_id).bool()],
                batch_size=None,
                additional_filter_triples=[
                    train.mapped_triples,
                    valid.mapped_triples,
                ]
            )

            logger.end_experiment(results, model, results_filtered)
        else:
            logger.end_experiment(results, model)




if __name__ == '__main__':
    # load configurations
    parser = argparse.ArgumentParser(description='Experiments')
    parser.add_argument('config', metavar='file', type=str, help='config file in json format')
    args = parser.parse_args()

    with open(args.config, 'r') as f:
        json_content = json.loads(f.read())
    run(_config_list=json_content['configs'])
