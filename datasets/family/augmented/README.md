# Created with DLV 
NOTE: doesn't contain self-connections 

### base dataset 
* family/train.txt
* family/valid.txt
* family/test.txt

### augment all datasets with the rules
```
parent(X,Y) :- father(X,Y).
parent(X,Y) :- mother(X,Y).
sibling(X,Y) :- sister(X,Y).
sibling(X,Y) :- brother(X,Y).
partner(X,Y) :- wife(X,Y).
partner(X,Y) :- husband(X,Y).
child(X,Y) :- daughter(X,Y).
child(X,Y) :- son(X,Y).
```