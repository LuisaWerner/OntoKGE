# Created with DLV 
NOTE: doesn't contain self-connections 

### base dataset 
* family/train.txt
* family/valid.txt
* family/test.txt
* family/all.txt

### augment all datasets with the rules
```
sibling(X,Y):- brother(X,Y).
sibling(X,Y):- sister(X,Y).
partner(X,Y):- wife(X,Y).
partner(X,Y):- husband(X,Y).
child(X,Y):- daughter(X,Y).
child(X,Y):- son(X,Y).
parent(X,Y):- mother(X,Y).
parent(X,Y):- father(X,Y).
child(X,Y):- parent(Y,X).
parent(X,Y):- child(Y,X).
sibling(X,Y):- sibling(Y,X).
partner(X,Y):- partner(Y,X).
grandfather(X,Y):- father(X,Z),parent(Y,Z).
grandmother(X,Y):- mother(X,Z),parent(Y,Z).
grandmother(X,Y):- mother(X,Z),father(Y,Z).
grandmother(X,Y):- mother(X,Z),mother(Y,Z).
grandfather(X,Y):- father(X,Z),father(Y,Z).
grandfather(X,Y):- father(X,Z),mother(Y,Z).
grandparent(X,Y):- parent(X,Z),parent(Z,Y).
```

* train.txt : 12445 triples
* valid.txt: 4307 triples
* test.txt:  6046 triples 
* all.txt: 50017 triples