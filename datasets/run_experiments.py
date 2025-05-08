import torch.cuda
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from onto_kge import run
import wandb
import torch
import yaml
import argparse

parser = argparse.ArgumentParser(description='Experiments')
parser.add_argument('grid_config', metavar='file', type=str, help='config file in yaml format')
args = parser.parse_args()

with open(args.grid_config, 'r') as file:
    experiment_config = yaml.safe_load(file)


def run_with_conf(config=None):
    """ execute multiple runs without having to specify all the different combinations of config """
    # Initialize a new wandb run
    with wandb.init(config=config, tags=[]):  # set tag here if sweep grid config is used
        # If called by wandb.agent, as below, this config will be set by Sweep Controller
        config = wandb.config
        run([dict(config)])

wandb_runs = wandb.sweep(sweep=experiment_config, project="tests_onto_kge")
wandb.agent(wandb_runs, function=run_with_conf)
