---------------------------------------------- 
-- WORDNET TENSOR DATA -- A. Bordes -- 2013 --
----------------------------------------------

------------------
OUTLINE:
1. Introduction
2. Content
3. Data Format
4. Data Statistics
5. How to Cite
6. License
7. Contact
-------------------


1. INTRODUCTION:

This WORDNET TENSOR DATA consists of a collection of triplets (synset, relation_type, 
triplet) extracted from WordNet 3.0 (http://wordnet.princeton.edu). This data set can 
be seen as a 3-mode tensor depicting ternary relationships between synsets. 


2. CONTENT:

The data archive contains 6 files:
  - README 3K
  - wordnet-mlj12-definitions.txt 4,2M
  - wordnet-mlj12-train.txt 4,5M
  - wordnet-mlj12-valid.txt 165K
  - wordnet-mlj12-test.txt 165K

The 3 files wordnet-mlj12-*.txt contain the triplets (training, validation
and test sets), while the file wordnet-mlj12-definitions.txt lists the WordNet 
synsets definitions.


3. DATA FORMAT

The definitions file (wordnet-mlj12-definitions.txt) contains one synset 
per line with the following format: synset_id (a 8-digit unique identifier)
intelligible name (word+POS_tag+sense_index), definition. The previous 3
pieces of information are separated by a tab ('\t').

All wordnet-mlj12-*.txt files contain one triplet per line, with 2 synset_ids 
and relation type identifier in a tab separated format. The first element is the 
synset_id of the left hand side of the relation triple, the third one is the 
synset_id of the right hand side and the second element is the name of the type 
of relations between them.


4. DATA STATISTICS

There are 40,943 synsets and 18 relation types among them. The training set contains 
141,442 triplets, the validation set 5,000 and the test set 5,000.

All triplets are unique and we made sure that all synsets appearing in
the validation or test sets were occurring in the training set.

5. HOW TO CITE

When using this data, one should cite the original paper:
  @article{bordes-mlj13,
    title = {A Semantic Matching Energy Function for Learning with Multi-relational Data},
    author = {Antoine Bordes and Xavier Glorot and Jason Weston and Yoshua Bengio},
    journal={Machine Learning},
    publisher={Springer},
    year={2013},
    note={to appear}
  }

One should also point at the project page with either the long URL:
https://www.hds.utc.fr/everest/doku.php?id=en:smemlj12 , or the short
one: http://goo.gl/bHWsK .

6. LICENSE:

WordNet data follows the attach license agreement.

7. CONTACT

For all remarks or questions please contact Antoine Bordes: antoine
(dot) bordes (at) utc (dot) fr .


# Some notes
## Number of triples in each file:
* train.txt: 141442
* valid.txt: 5000
* test.txt: 5000

## Total number of unique entities: 40943
## Total number of unique relations: 18

## Node degree statistics (considering all facts):
* Average degree: 7.40
*  Max degree: 1040
*  Min degree: 1

## Relation frequencies:
* _hyponym: 37221
* _hypernym: 37221
* _member_holonym: 7928
* _derivationally_related_form: 31867
*  _instance_hypernym: 3150
* _also_see: 1396
* _member_meronym: 7928
* _member_of_domain_topic: 3341
* _part_of: 5148
* _instance_hyponym: 3150
* _synset_domain_topic_of: 3335
* _has_part: 5142
* _member_of_domain_usage: 675
* _member_of_domain_region: 983
* _synset_domain_usage_of: 669
* _synset_domain_region_of: 982
* _verb_group: 1220
* _similar_to: 86
