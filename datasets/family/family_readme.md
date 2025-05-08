# The Family Dataset
Knowledge Graph with Family relations

Data Source: [LERP Github](https://github.com/Glaciohound/LERP) 

**12 different relation types:** 
* aunt
* brother
* daughter
* father
* husband
* mother
* nephew
* niece
* sister
* son
* uncle
* wife

**3007 unique entities**, 
**average node degree 9.41**, 
**maximum node degree 52** 


### Files
* all.txt contains 28.356 triples
* `facts.txt` contains 17.615 triples
* `valid.txt` contains 2.038 triples
* `test.txt` contains 2.835 triples
* `truth.pckl` is a pickle file that seems to contain queries (9274 head queries, 14.017 tail queries, eg. ('aunt', '7') and a list of 35 ids.)

**Counts** 
| all.txt                                                                                                                                                | facts.txt                                                                                                                                           | train.txt                                                                                                                                  | valid.txt                                                                                                                                | test.txt                                                                                                                                  |
|--------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| aunt, 2990 brother, 3076 daughter, 1589 father, 2010 husband, 1138 mother, 1714 nephew, 3633 niece, 2815 sister, 2658 son, 2110 uncle, 3485 wife, 1138 | aunt, 1866 brother, 1902 daughter, 978 father, 1236 husband, 717 mother, 1056 nephew, 2272 niece, 1735 sister, 1659 son, 1320 uncle, 2163 wife, 711 | aunt, 622 brother, 633 daughter, 325 father, 412 husband, 239 mother, 352 nephew, 757 niece, 578 sister, 552 son, 440 uncle, 721 wife, 237 | aunt, 216 brother, 220 daughter, 113 father, 143 husband, 83 mother, 122 nephew, 263 niece, 201 sister, 192 son, 153 uncle, 250 wife, 82 | aunt, 286 brother, 321 daughter, 173 father, 219 husband, 99 mother, 184 nephew, 341 niece, 301 sister, 255 son, 197 uncle, 351 wife, 108 |



**Snippet to count in `edge_type` as list
```python
for v in sorted(set(edge_type)):
    print(f'{v}, {edge_type.count(v)}')
```


### Load Files
Code snippet to load `.txt` files and stores lists of `edge_index`  as tuples of head and tail id and `edge_type`. 
```python
from pathlib import Path

triples = open('./family/facts.txt').readlines()
edge_index, edge_type = [], []

for line in triples:
    head, relation, tail = line.split('\t')
    if tail.endswith('\n'):
        tail = tail[:-1]
    edge_index.append([int(head), int(tail)])
    edge_type.append(relation)
```

### Subdirectories
* **augmented**   
added triples according the following rules
```python
parent(X,Y) :- father(X,Y).
parent(X,Y) :- mother(X,Y).
sibling(X,Y) :- sister(X,Y).
sibling(X,Y) :- brother(X,Y).
partner(X,Y) :- wife(X,Y).
partner(X,Y) :- husband(X,Y).
child(X,Y) :- daughter(X,Y).
child(X,Y) :- son(X,Y).
```

* **augmented2**
added triples according to the following rules
```python
sibling(X,Y):-brother(X,Y).
sibling(X,Y):-sister(X,Y).
partner(X,Y) :- wife(X,Y).
partner(X,Y) :- husband(X,Y).
child(X,Y) :- daughter(X,Y).
child(X,Y) :- son(X,Y).
grandfather(X,Y):- father(X,Z),parent(Y,Z).
grandmother(X,Y):- mother(X,Z),parent(Y,Z).
grandmother(X,Y):- mother(X,Z),father(Y,Z).
grandmother(X,Y):- mother(X,Z),mother(Y,Z).
grandfather(X,Y):- father(X,Z),father(Y,Z).
grandfather(X,Y):- father(X,Z),mother(Y,Z).
grandparent(X,Y):- parent(X,Z),parent(Z,Y).
sibling(X,Y):-sibling(X,Z),sibling(Z,Y).
```


