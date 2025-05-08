# TransE

Model: TransE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: both.optimistic.hits_at_10
                      0.1          0.25         0.5
------------  -----------  ------------  ----------
no reasoning   0.641361     0.620242     0.543843
reasoning      0.640025     0.619426     0.545627
delta         -0.00133607  -0.000816063  0.00178395 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 0.8098767647786345, 0.25: 0.6506676402784313, 0.5: 0.2486841897063457} 

 ************************************************************ 

Model: TransE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: both.optimistic.hits_at_5
                      0.1         0.25         0.5
------------  -----------  -----------  ----------
no reasoning   0.466283    0.444253     0.376019
reasoning      0.46486     0.444891     0.379276
delta         -0.00142337  0.000637668  0.00325666 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 0.7954328277830505, 0.25: 0.3861504726802487, 0.5: 0.08956713200755023} 

 ************************************************************ 

Model: TransE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: tail.optimistic.hits_at_10
                      0.1         0.25         0.5
------------  -----------  -----------  ----------
no reasoning   0.649799    0.627313     0.550846
reasoning      0.648774    0.627564     0.55342
delta         -0.00102482  0.000250512  0.00257345 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 0.7350323961355558, 0.25: 0.45804015266750864, 0.5: 0.16808699153486845} 

 ************************************************************ 

Model: TransE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: tail.optimistic.hits_at_5
                      0.1        0.25         0.5
------------  -----------  ----------  ----------
no reasoning   0.483831    0.45969     0.387467
reasoning      0.482639    0.46259     0.391308
delta         -0.00119183  0.00289987  0.00384119 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 0.7161222679895365, 0.25: 0.1304267004641789, 0.5: 0.06771821015124242} 

 ************************************************************ 

Model: TransE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: head.optimistic.hits_at_10
                      0.1         0.25          0.5
------------  -----------  -----------  -----------
no reasoning   0.632923     0.613171    0.536841
reasoning      0.631276     0.611288    0.537835
delta         -0.00164731  -0.00188264  0.000994458 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 0.8370469343858227, 0.25: 0.8042145078735817, 0.5: 0.3635258775478878} 

 ************************************************************ 

Model: TransE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: head.optimistic.hits_at_5
                     0.1         0.25         0.5
------------  ----------  -----------  ----------
no reasoning   0.448736    0.428817    0.364571
reasoning      0.447081    0.427192    0.367244
delta         -0.0016549  -0.00162454  0.00267213 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 0.8112957283022608, 0.25: 0.759825222256431, 0.5: 0.1609759682570718} 

 ************************************************************

# TransH

Model: TransH 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: both.optimistic.hits_at_10
                    0.1       0.25        0.5
------------  ---------  ---------  ---------
no reasoning  0.380779   0.352896   0.22006
reasoning     0.445183   0.416431   0.292283
delta         0.0644045  0.0635353  0.0722235 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 2.8201414897532835e-07, 0.25: 1.5787988415465933e-05, 0.5: 7.277569360617422e-06} 

 ************************************************************ 

Model: TransH 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: both.optimistic.hits_at_5
                    0.1       0.25        0.5
------------  ---------  ---------  ---------
no reasoning  0.304209   0.27994    0.171229
reasoning     0.3552     0.330369   0.230824
delta         0.0509907  0.0504289  0.0595954 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 3.2992001854337523e-07, 0.25: 1.043335948149879e-05, 0.5: 3.249335272596915e-06} 

 ************************************************************ 

Model: TransH 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: tail.optimistic.hits_at_10
                    0.1       0.25        0.5
------------  ---------  ---------  ---------
no reasoning  0.37627    0.346815   0.211721
reasoning     0.441866   0.411167   0.282882
delta         0.0655963  0.0643513  0.0711607 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 4.242603825091931e-07, 0.25: 1.65868260225102e-05, 0.5: 1.2063716962349032e-05} 

 ************************************************************ 

Model: TransH 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: tail.optimistic.hits_at_5
                    0.1       0.25        0.5
------------  ---------  ---------  ---------
no reasoning  0.300061   0.274645   0.163531
reasoning     0.3509     0.322979   0.221385
delta         0.0508388  0.0483337  0.0578532 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 6.411951341398543e-07, 0.25: 1.8341946605137577e-05, 0.5: 5.93582413757153e-06} 

 ************************************************************ 

Model: TransH 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: head.optimistic.hits_at_10
                    0.1       0.25        0.5
------------  ---------  ---------  ---------
no reasoning  0.385288   0.358977   0.228399
reasoning     0.448501   0.421696   0.301685
delta         0.0632126  0.0627192  0.0732863 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 2.164474149116911e-07, 0.25: 1.60132725959648e-05, 0.5: 4.529668823124023e-06} 

 ************************************************************ 

Model: TransH 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: head.optimistic.hits_at_5
                    0.1       0.25        0.5
------------  ---------  ---------  ---------
no reasoning  0.308358   0.285235   0.178927
reasoning     0.3595     0.337759   0.240264
delta         0.0511425  0.0525241  0.0613376 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 2.0991910008987327e-07, 0.25: 7.047282544682798e-06, 0.5: 1.894889346459226e-06} 

 ************************************************************

# TransR


Model: TransR 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: both.optimistic.hits_at_10
                    0.1        0.25         0.5
------------  ---------  ----------  ----------
no reasoning  0.0108366  0.00894253  0.00770895
reasoning     0.0320049  0.0153989   0.0118917
delta         0.0211683  0.00645639  0.0041828 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 3.60135896814024e-07, 0.25: 2.1657278226810602e-19, 0.5: 3.036454515590486e-18} 

 ************************************************************ 

Model: TransR 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: both.optimistic.hits_at_5
                     0.1        0.25         0.5
------------  ----------  ----------  ----------
no reasoning  0.00549609  0.00466864  0.00417521
reasoning     0.0175169   0.0082783   0.00637288
delta         0.0120208   0.00360966  0.00219768 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 1.1760419811776236e-06, 0.25: 3.4022433014735157e-17, 0.5: 8.748424759519129e-12} 

 ************************************************************ 

Model: TransR 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: tail.optimistic.hits_at_10
                     0.1        0.25         0.5
------------  ----------  ----------  ----------
no reasoning  0.00904881  0.00703712  0.00631595
reasoning     0.0295984   0.0128293   0.00952706
delta         0.0205496   0.00579215  0.00321111 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 6.920749967445061e-07, 0.25: 2.743165261319592e-16, 0.5: 3.795124122840131e-12} 

 ************************************************************ 

Model: TransR 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: tail.optimistic.hits_at_5
                     0.1        0.25         0.5
------------  ----------  ----------  ----------
no reasoning  0.00450163  0.00371973  0.00349958
reasoning     0.0160708   0.00695362  0.00508616
delta         0.0115691   0.00323389  0.00158658 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 2.381185722124546e-06, 0.25: 4.829411686097124e-13, 0.5: 7.850784432707166e-08} 

 ************************************************************ 

Model: TransR 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: head.optimistic.hits_at_10
                    0.1        0.25         0.5
------------  ---------  ----------  ----------
no reasoning  0.0126243  0.0108479   0.00910195
reasoning     0.0344113  0.0179686   0.0142564
delta         0.021787   0.00712063  0.00515448 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 2.0724048914321273e-07, 0.25: 1.1696291997958119e-17, 0.5: 2.084474617216857e-18} 

 ************************************************************ 

Model: TransR 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: head.optimistic.hits_at_5
                     0.1        0.25         0.5
------------  ----------  ----------  ----------
no reasoning  0.00649055  0.00561755  0.00485083
reasoning     0.018963    0.00960298  0.00765961
delta         0.0124725   0.00398542  0.00280878 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 6.958096673387902e-07, 0.25: 1.73484483708117e-15, 0.5: 9.988495367229018e-12} 

 ************************************************************

# SE 

Model: SE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: both.optimistic.hits_at_10
                    0.1       0.25        0.5
------------  ---------  ---------  ---------
no reasoning  0.0556365  0.0388674  0.0246413
reasoning     0.102312   0.0723336  0.0446785
delta         0.046675   0.0334662  0.0200372 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 5.507707234216326e-31, 0.25: 1.1419685963444267e-29, 0.5: 7.457110975636011e-34} 

 ************************************************************ 

Model: SE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: both.optimistic.hits_at_5
                    0.1       0.25        0.5
------------  ---------  ---------  ---------
no reasoning  0.0350452  0.023662   0.0142906
reasoning     0.0712404  0.0484096  0.0304107
delta         0.0361952  0.0247476  0.0161201 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 3.961680587818471e-31, 0.25: 6.642724028777089e-31, 0.5: 2.8557732272472264e-34} 

 ************************************************************ 

Model: SE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: tail.optimistic.hits_at_10
                    0.1       0.25        0.5
------------  ---------  ---------  ---------
no reasoning  0.0481743  0.0325438  0.0206255
reasoning     0.0897442  0.0608062  0.0375996
delta         0.0415699  0.0282624  0.0169741 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 4.309082412964279e-28, 0.25: 6.27544804198418e-27, 0.5: 1.3245790532034781e-31} 

 ************************************************************ 

Model: SE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: tail.optimistic.hits_at_5
                    0.1       0.25        0.5
------------  ---------  ---------  ---------
no reasoning  0.0301754  0.0196614  0.0121233
reasoning     0.0604646  0.0395658  0.0251272
delta         0.0302892  0.0199043  0.0130039 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 2.3156724468278237e-27, 0.25: 4.826284464805057e-27, 0.5: 1.323169891503284e-29} 

 ************************************************************ 

Model: SE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: head.optimistic.hits_at_10
                    0.1       0.25        0.5
------------  ---------  ---------  ---------
no reasoning  0.0630988  0.0451909  0.0286571
reasoning     0.114879   0.0838609  0.0517574
delta         0.0517802  0.03867    0.0231003 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 1.670516598797759e-32, 0.25: 4.61705511878645e-30, 0.5: 5.616614017544448e-32} 

 ************************************************************ 

Model: SE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: head.optimistic.hits_at_5
                    0.1       0.25        0.5
------------  ---------  ---------  ---------
no reasoning  0.039915   0.0276626  0.0164579
reasoning     0.0820162  0.0572535  0.0356942
delta         0.0421013  0.0295908  0.0192363 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 8.940007359441429e-33, 0.25: 2.1913281954525226e-31, 0.5: 4.438924521554496e-33} 

 ************************************************************

# RotatE

Model: RotatE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: both.optimistic.hits_at_10
                    0.1       0.25        0.5
------------  ---------  ---------  ---------
no reasoning  0.15457    0.108768   0.0512753
reasoning     0.172337   0.127215   0.0665035
delta         0.0177674  0.0184468  0.0152281 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 0.09513504286846348, 0.25: 0.046096434482792874, 0.5: 0.004464081133300097} 

 ************************************************************ 

Model: RotatE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: both.optimistic.hits_at_5
                    0.1       0.25        0.5
------------  ---------  ---------  ---------
no reasoning  0.113068   0.0794124  0.0368101
reasoning     0.128403   0.0936081  0.0491042
delta         0.0153344  0.0141957  0.0122941 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 0.04829860218713171, 0.25: 0.026810082922026156, 0.5: 0.0010902414553005837} 

 ************************************************************ 

Model: RotatE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: tail.optimistic.hits_at_10
                    0.1       0.25        0.5
------------  ---------  ---------  ---------
no reasoning  0.155599   0.108745   0.0500949
reasoning     0.17195    0.125871   0.0641084
delta         0.0163516  0.0171259  0.0140135 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 0.11940783884620271, 0.25: 0.06339530359705811, 0.5: 0.009304343277544645} 

 ************************************************************ 

Model: RotatE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: tail.optimistic.hits_at_5
                   0.1       0.25        0.5
------------  --------  ---------  ---------
no reasoning  0.114583  0.0790632  0.0358764
reasoning     0.127845  0.0921886  0.0466409
delta         0.013262  0.0131253  0.0107644 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 0.08211424997520496, 0.25: 0.04416361521247547, 0.5: 0.004534317317359621} 

 ************************************************************ 

Model: RotatE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: head.optimistic.hits_at_10
                    0.1       0.25        0.5
------------  ---------  ---------  ---------
no reasoning  0.153541   0.108791   0.0524558
reasoning     0.172725   0.128558   0.0688985
delta         0.0191832  0.0197677  0.0164427 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 0.07477296608240201, 0.25: 0.03287747216983872, 0.5: 0.002085098359542907} 

 ************************************************************ 

Model: RotatE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: head.optimistic.hits_at_5
                    0.1       0.25        0.5
------------  ---------  ---------  ---------
no reasoning  0.111554   0.0797616  0.0377439
reasoning     0.128961   0.0950277  0.0515676
delta         0.0174068  0.0152661  0.0138237 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 0.026801962645356846, 0.25: 0.015572334706145774, 0.5: 0.0002512510025957654} 

 ************************************************************

# BoxE

Model: BoxE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: both.optimistic.hits_at_10
                     0.1        0.25         0.5
------------  ----------  ----------  ----------
no reasoning  0.577363    0.537949    0.409538
reasoning     0.581003    0.543991    0.417323
delta         0.00364002  0.00604266  0.00778486 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 0.01032710303840575, 0.25: 0.0009395874656841824, 0.5: 0.004021229813873368} 

 ************************************************************ 

Model: BoxE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: both.optimistic.hits_at_5
                     0.1        0.25         0.5
------------  ----------  ----------  ----------
no reasoning  0.43377     0.398402    0.293783
reasoning     0.434897    0.404031    0.300429
delta         0.00112731  0.00562894  0.00664617 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 0.22868416182753865, 0.25: 0.000995951799170898, 0.5: 0.0029719826446723374} 

 ************************************************************ 

Model: BoxE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: tail.optimistic.hits_at_10
                     0.1       0.25         0.5
------------  ----------  ---------  ----------
no reasoning  0.582555    0.542617   0.414393
reasoning     0.587907    0.549503   0.422402
delta         0.00535186  0.0068853  0.00800881 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 0.000910701309457572, 0.25: 0.0006417664276455069, 0.5: 0.004617640262189624} 

 ************************************************************ 

Model: BoxE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: tail.optimistic.hits_at_5
                     0.1        0.25         0.5
------------  ----------  ----------  ----------
no reasoning  0.444288    0.407508    0.298603
reasoning     0.446299    0.412943    0.306521
delta         0.00201169  0.00543536  0.00791771 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 0.102232962846504, 0.25: 0.006274178436677112, 0.5: 0.0013376148968576704} 

 ************************************************************ 

Model: BoxE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: head.optimistic.hits_at_10
                     0.1        0.25         0.5
------------  ----------  ----------  ----------
no reasoning  0.57217     0.53328     0.404684
reasoning     0.574099    0.53848     0.412245
delta         0.00192819  0.00520003  0.00756092 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 0.1268913166333582, 0.25: 0.004603976603650589, 0.5: 0.006853855053041164} 

 ************************************************************ 

Model: BoxE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: head.optimistic.hits_at_5
                      0.1        0.25         0.5
------------  -----------  ----------  ----------
no reasoning  0.423252     0.389296    0.288962
reasoning     0.423495     0.395119    0.294337
delta         0.000242921  0.00582252  0.00537463 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 0.4501605026005766, 0.25: 0.00119229528267913, 0.5: 0.013833753824096707} 

 ************************************************************

# RGCN

Model: RGCN 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: both.optimistic.hits_at_10
                    0.1        0.25         0.5
------------  ---------  ----------  ----------
no reasoning  0.145669   0.0732787   0.025632
reasoning     0.158988   0.077173    0.0276133
delta         0.0133189  0.00389433  0.00198133 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 0.024463826300722406, 0.25: 0.15589272171468477, 0.5: 0.005176436278552369} 

 ************************************************************ 

Model: RGCN 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: both.optimistic.hits_at_5
                     0.1        0.25         0.5
------------  ----------  ----------  ----------
no reasoning  0.0913877   0.0437941   0.0140211
reasoning     0.0998178   0.04595     0.0153344
delta         0.00843012  0.00215592  0.00131329 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 0.029248887861945103, 0.25: 0.1896215452807536, 0.5: 0.003538024779135826} 

 ************************************************************ 

Model: RGCN 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: tail.optimistic.hits_at_10
                    0.1        0.25        0.5
------------  ---------  ----------  ---------
no reasoning  0.132992   0.0650497   0.0222728
reasoning     0.145608   0.0683747   0.0234039
delta         0.0126167  0.00332498  0.0011311 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 0.03260972153124739, 0.25: 0.1913272403131756, 0.5: 0.07729355745741351} 

 ************************************************************ 

Model: RGCN 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: tail.optimistic.hits_at_5
                     0.1        0.25         0.5
------------  ----------  ----------  ----------
no reasoning  0.0813862   0.0386472   0.0120701
reasoning     0.0891824   0.0402262   0.0130722
delta         0.00779625  0.00157899  0.00100205 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 0.03766457449990089, 0.25: 0.25349917586645665, 0.5: 0.03187913115546561} 

 ************************************************************ 

Model: RGCN 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: head.optimistic.hits_at_10
                    0.1        0.25         0.5
------------  ---------  ----------  ----------
no reasoning  0.158347   0.0815076   0.0289911
reasoning     0.172368   0.0859713   0.0318227
delta         0.0140211  0.00446368  0.00283155 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 0.019449359444203587, 0.25: 0.13488128325887003, 0.5: 0.0028459008054898273} 

 ************************************************************ 

Model: RGCN 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: head.optimistic.hits_at_5
                     0.1        0.25         0.5
------------  ----------  ----------  ----------
no reasoning  0.101389    0.048941    0.0159721
reasoning     0.110453    0.0516739   0.0175966
delta         0.00906399  0.00273286  0.00162454 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 0.02545585223898047, 0.25: 0.1557790374978678, 0.5: 0.008939266562154144} 

# NTN 

Model: NTN 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: both.optimistic.hits_at_10
                      0.1          0.25           0.5
------------  -----------  ------------  ------------
no reasoning  0.0464093     0.0465004     0.0481439
reasoning     0.0466674     0.0462765     0.0474417
delta         0.000258104  -0.000223943  -0.000702194 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 0.39499119825906004, 0.25: 0.5966739061622708, 0.5: 0.8059173181850583} 

 ************************************************************ 

Model: NTN 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: both.optimistic.hits_at_5
                      0.1          0.25           0.5
------------  -----------  ------------  ------------
no reasoning  0.0464093     0.0465004     0.0481439
reasoning     0.0466674     0.0462765     0.0474417
delta         0.000258104  -0.000223943  -0.000702194 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 0.39499119825906004, 0.25: 0.5966739061622708, 0.5: 0.8059173181850583} 

 ************************************************************ 

Model: NTN 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: tail.optimistic.hits_at_10
                      0.1          0.25           0.5
------------  -----------  ------------  ------------
no reasoning  0.0464966     0.0464738     0.0480984
reasoning     0.046694      0.0462917     0.0474
delta         0.000197373  -0.000182191  -0.000698398 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 0.4192923192761111, 0.25: 0.5793448406421071, 0.5: 0.8035082364146009} 

 ************************************************************ 

Model: NTN 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: tail.optimistic.hits_at_5
                      0.1          0.25           0.5
------------  -----------  ------------  ------------
no reasoning  0.0464966     0.0464738     0.0480984
reasoning     0.046694      0.0462917     0.0474
delta         0.000197373  -0.000182191  -0.000698398 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 0.4192923192761111, 0.25: 0.5793448406421071, 0.5: 0.8035082364146009} 

 ************************************************************ 

Model: NTN 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: head.optimistic.hits_at_10
                      0.1          0.25          0.5
------------  -----------  ------------  -----------
no reasoning  0.046322      0.046527      0.0481895
reasoning     0.0466409     0.0462613     0.0474835
delta         0.000318834  -0.000265695  -0.00070599 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 0.371458897088609, 0.25: 0.6132729456100879, 0.5: 0.8072076188678556} 

 ************************************************************ 

Model: NTN 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: head.optimistic.hits_at_5
                      0.1          0.25          0.5
------------  -----------  ------------  -----------
no reasoning  0.046322      0.046527      0.0481895
reasoning     0.0466409     0.0462613     0.0474835
delta         0.000318834  -0.000265695  -0.00070599 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 0.371458897088609, 0.25: 0.6132729456100879, 0.5: 0.8072076188678556} 

 ************************************************************

# SimplE 
Model: SimplE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: both.optimistic.hits_at_10
                      0.1          0.25           0.5
------------  -----------  ------------  ------------
no reasoning  0.00343126    0.00347681    0.00362863
reasoning     0.0037463     0.00342747    0.00345783
delta         0.000315038  -4.93434e-05  -0.000170804 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 0.22203384039573104, 0.25: 0.5786444129637227, 0.5: 0.7603104477355029} 

 ************************************************************ 

Model: SimplE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: both.optimistic.hits_at_5
                       0.1        0.25           0.5
------------  ------------  ----------  ------------
no reasoning   0.00177257   0.00176497   0.00179154
reasoning      0.0017422    0.00176497   0.00170804
delta         -3.03651e-05  0           -8.35041e-05 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 0.5641154060383109, 0.25: 0.5, 0.5: 0.7033727241971162} 

 ************************************************************ 

Model: SimplE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: tail.optimistic.hits_at_10
                      0.1          0.25           0.5
------------  -----------  ------------  ------------
no reasoning  0.00345403    0.00345403    0.00359827
reasoning     0.00378805    0.00337053    0.00346922
delta         0.000334017  -8.35041e-05  -0.000129052 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 0.2256195331960018, 0.25: 0.6199383527483114, 0.5: 0.6868148675951153} 

 ************************************************************ 

Model: SimplE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: tail.optimistic.hits_at_5
                       0.1          0.25           0.5
------------  ------------  ------------  ------------
no reasoning   0.00187505    0.00190541    0.00187505
reasoning      0.00181432    0.00188264    0.00179154
delta         -6.07303e-05  -2.27739e-05  -8.35041e-05 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 0.6235497245561996, 0.25: 0.5548802397390215, 0.5: 0.6995366895308639} 

 ************************************************************ 

Model: SimplE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: head.optimistic.hits_at_10
                     0.1          0.25           0.5
------------  ----------  ------------  ------------
no reasoning  0.00340849   0.00349958    0.003659
reasoning     0.00370455   0.0034844     0.00344644
delta         0.00029606  -1.51826e-05  -0.000212556 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 0.23080349424653912, 0.25: 0.5238279975675753, 0.5: 0.803721676990261} 

 ************************************************************ 

Model: SimplE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: head.optimistic.hits_at_5
                      0.1         0.25           0.5
------------  -----------  -----------  ------------
no reasoning  0.00167008   0.00162454    0.00170804
reasoning     0.00167008   0.00164731    0.00162454
delta         6.50521e-19  2.27739e-05  -8.35041e-05 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 0.49999999999999883, 0.25: 0.4497561337696869, 0.5: 0.6704329522187928} 

 ************************************************************

# DistMult 

Model: DistMult 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: both.optimistic.hits_at_10
                    0.1       0.25        0.5
------------  ---------  ---------  ---------
no reasoning  0.151951   0.115976   0.0536704
reasoning     0.229648   0.181158   0.0981629
delta         0.0776968  0.0651826  0.0444925 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 5.5318548109648614e-17, 0.25: 5.475679913358863e-18, 0.5: 3.8467884136791455e-14} 

 ************************************************************ 

Model: DistMult 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: both.optimistic.hits_at_5
                    0.1       0.25        0.5
------------  ---------  ---------  ---------
no reasoning  0.118769   0.0919077  0.0428262
reasoning     0.17742    0.140834   0.0781371
delta         0.0586503  0.0489258  0.0353109 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 7.989872210493599e-19, 0.25: 4.448254353444445e-19, 0.5: 8.166365799554345e-15} 

 ************************************************************ 

Model: DistMult 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: tail.optimistic.hits_at_10
                    0.1       0.25        0.5
------------  ---------  ---------  ---------
no reasoning  0.152942   0.116678   0.0541031
reasoning     0.23038    0.181409   0.0985501
delta         0.0774387  0.0647309  0.044447 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 2.4641690887794203e-16, 0.25: 5.208087913011928e-17, 0.5: 7.282259533122719e-14} 

 ************************************************************ 

Model: DistMult 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: tail.optimistic.hits_at_5
                    0.1       0.25        0.5
------------  ---------  ---------  ---------
no reasoning  0.120466   0.0932058  0.0433159
reasoning     0.178934   0.140963   0.0781599
delta         0.0584681  0.0477568  0.034844 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 6.167144797454099e-18, 0.25: 3.023940578499614e-17, 0.5: 2.242301761151853e-14} 

 ************************************************************ 

Model: DistMult 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: head.optimistic.hits_at_10
                    0.1       0.25        0.5
------------  ---------  ---------  ---------
no reasoning  0.15096    0.115274   0.0532377
reasoning     0.228915   0.180908   0.0977758
delta         0.0779549  0.0656343  0.0445381 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 1.4051634675438616e-17, 0.25: 7.775918871235311e-19, 0.5: 2.33839650042721e-14} 

 ************************************************************ 

Model: DistMult 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: head.optimistic.hits_at_5
                    0.1       0.25        0.5
------------  ---------  ---------  ---------
no reasoning  0.117073   0.0906096  0.0423366
reasoning     0.175905   0.140704   0.0781143
delta         0.0588325  0.0500949  0.0357777 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 1.4744509234458264e-19, 0.25: 9.266081671801406e-21, 0.5: 4.191807725565412e-15} 

 ************************************************************


# QuatE
Model: QuatE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: both.optimistic.hits_at_10
                   0.1       0.25       0.5
------------  --------  ---------  --------
no reasoning  0.619768  0.545867   0.333887
reasoning     0.673279  0.619737   0.448117
delta         0.053511  0.0738708  0.11423 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 4.07185606506096e-20, 0.25: 2.4279907518352313e-25, 0.5: 3.272021164204394e-29} 

 ************************************************************ 

Model: QuatE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: both.optimistic.hits_at_5
                    0.1       0.25        0.5
------------  ---------  ---------  ---------
no reasoning  0.500672   0.436142   0.265517
reasoning     0.543145   0.492397   0.35263
delta         0.0424732  0.0562552  0.0871138 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 4.31592491198455e-20, 0.25: 8.451367001303466e-26, 0.5: 2.5251582425936823e-30} 

 ************************************************************ 

Model: QuatE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: tail.optimistic.hits_at_10
                    0.1       0.25       0.5
------------  ---------  ---------  --------
no reasoning  0.62534    0.550277   0.336188
reasoning     0.679549   0.626334   0.452387
delta         0.0542094  0.0760571  0.1162 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 7.23533279892272e-21, 0.25: 1.28645273864663e-25, 0.5: 1.1084660205372919e-29} 

 ************************************************************ 

Model: QuatE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: tail.optimistic.hits_at_5
                    0.1      0.25        0.5
------------  ---------  --------  ---------
no reasoning  0.515      0.445434  0.268413
reasoning     0.561307   0.506392  0.360449
delta         0.0463068  0.060958  0.0920367 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 3.030039629722544e-21, 0.25: 5.428684141580436e-26, 0.5: 3.038302454278695e-31} 

 ************************************************************ 

Model: QuatE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: head.optimistic.hits_at_10
                    0.1       0.25       0.5
------------  ---------  ---------  --------
no reasoning  0.614196   0.541456   0.331587
reasoning     0.667008   0.613141   0.443847
delta         0.0528126  0.0716845  0.11226 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 3.444141412263305e-19, 0.25: 1.1300159820716997e-24, 0.5: 1.480917944719108e-28} 

 ************************************************************ 

Model: QuatE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: head.optimistic.hits_at_5
                    0.1       0.25        0.5
------------  ---------  ---------  ---------
no reasoning  0.486343   0.42685    0.262621
reasoning     0.524983   0.478403   0.344811
delta         0.0386396  0.0515524  0.0821908 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 8.260069639255514e-18, 0.25: 5.1567269713395016e-24, 0.5: 9.980709440912011e-29} 

 ************************************************************ 

## Margin Ranking Loss 

Model: BoxE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: both.optimistic.hits_at_10
                      0
------------  ---------
no reasoning  0.469563
reasoning     0.494876
delta         0.0253131 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0], 0: 2.960548532814501e-35} 

 ************************************************************ 

Model: BoxE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: both.optimistic.hits_at_5
                      0
------------  ---------
no reasoning  0.322258
reasoning     0.339342
delta         0.0170842 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0], 0: 1.3761365590830575e-25} 

 ************************************************************ 

Model: BoxE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: tail.optimistic.hits_at_10
                      0
------------  ---------
no reasoning  0.454498
reasoning     0.483481
delta         0.0289835 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0], 0: 3.8497408179616283e-36} 

 ************************************************************ 

Model: BoxE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: tail.optimistic.hits_at_5
                      0
------------  ---------
no reasoning  0.31437
reasoning     0.335026
delta         0.0206559 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0], 0: 6.3722228603354846e-27} 

 ************************************************************ 

Model: BoxE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: head.optimistic.hits_at_10
                      0
------------  ---------
no reasoning  0.484628
reasoning     0.50627
delta         0.0216428 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0], 0: 5.27438495266356e-25} 

 ************************************************************ 

Model: BoxE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: head.optimistic.hits_at_5
                      0
------------  ---------
no reasoning  0.330145
reasoning     0.343657
delta         0.0135125 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0], 0: 9.235960606894173e-17} 

 ************************************************************ 

Model: TransE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: both.optimistic.hits_at_10
                      0
------------  ---------
no reasoning  0.103481
reasoning     0.146417
delta         0.0429363 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0], 0: 1.3843467509689352e-11} 

 ************************************************************ 

Model: TransE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: both.optimistic.hits_at_5
                      0
------------  ---------
no reasoning  0.0621878
reasoning     0.0943141
delta         0.0321263 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0], 0: 1.0638293722237984e-11} 

 ************************************************************ 

Model: TransE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: tail.optimistic.hits_at_10
                      0
------------  ---------
no reasoning  0.104395
reasoning     0.146087
delta         0.0416913 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0], 0: 1.3299518202227929e-10} 

 ************************************************************ 

Model: TransE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: tail.optimistic.hits_at_5
                      0
------------  ---------
no reasoning  0.0630153
reasoning     0.0943141
delta         0.0312989 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0], 0: 6.089847208881456e-11} 

 ************************************************************ 

Model: TransE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: head.optimistic.hits_at_10
                      0
------------  ---------
no reasoning  0.102566
reasoning     0.146747
delta         0.0441813 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0], 0: 1.9067473910708004e-12} 

 ************************************************************ 

Model: TransE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: head.optimistic.hits_at_5
                      0
------------  ---------
no reasoning  0.0613604
reasoning     0.0943141
delta         0.0329538 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0], 0: 3.2333294282755383e-12} 

 ************************************************************ 

Model: TransH 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: both.optimistic.hits_at_10
                      0
------------  ---------
no reasoning  0.492849
reasoning     0.547582
delta         0.0547332 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0], 0: 0.0007736809911334608} 

 ************************************************************ 

Model: TransH 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: both.optimistic.hits_at_5
                      0
------------  ---------
no reasoning  0.374615
reasoning     0.418887
delta         0.0442724 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0], 0: 3.083058519000347e-05} 

 ************************************************************ 

Model: TransH 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: tail.optimistic.hits_at_10
                      0
------------  ---------
no reasoning  0.487907
reasoning     0.544682
delta         0.0567752 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0], 0: 0.0006152396431092955} 

 ************************************************************ 

Model: TransH 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: tail.optimistic.hits_at_5
                      0
------------  ---------
no reasoning  0.369658
reasoning     0.413922
delta         0.0442648 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0], 0: 5.9493307284281565e-05} 

 ************************************************************ 

Model: TransH 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: head.optimistic.hits_at_10
                      0
------------  ---------
no reasoning  0.497791
reasoning     0.550482
delta         0.0526911 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0], 0: 0.0009956410193955945} 

 ************************************************************ 

Model: TransH 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: head.optimistic.hits_at_5
                     0
------------  --------
no reasoning  0.379572
reasoning     0.423852
delta         0.04428 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0], 0: 1.7734334900525694e-05} 

 ************************************************************ 
Model: RotatE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: both.optimistic.hits_at_10
                     0
------------  --------
no reasoning  0.400486
reasoning     0.570629
delta         0.170143 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0], 0: 9.16768941565875e-17} 

 ************************************************************ 

Model: RotatE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: both.optimistic.hits_at_5
                     0
------------  --------
no reasoning  0.310685
reasoning     0.470459
delta         0.159774 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0], 0: 2.2561507845216177e-19} 

 ************************************************************ 

Model: RotatE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: tail.optimistic.hits_at_10
                     0
------------  --------
no reasoning  0.399772
reasoning     0.572087
delta         0.172315 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0], 0: 3.4411314885056413e-17} 

 ************************************************************ 

Model: RotatE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: tail.optimistic.hits_at_5
                     0
------------  --------
no reasoning  0.309087
reasoning     0.467638
delta         0.158552 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0], 0: 1.4206850432155938e-19} 

 ************************************************************ 

Model: RotatE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: head.optimistic.hits_at_10
                     0
------------  --------
no reasoning  0.401199
reasoning     0.569172
delta         0.167972 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0], 0: 2.51954756265474e-16} 

 ************************************************************ 

Model: RotatE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: head.optimistic.hits_at_5
                     0
------------  --------
no reasoning  0.312283
reasoning     0.473279
delta         0.160996 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0], 0: 4.523504483818442e-19} 

 ************************************************************ 

Model: TransE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: both.optimistic.hits_at_10
                    0.1       0.25         0.5
------------  ---------  ---------  ----------
no reasoning  0.0776816  0.0479314  0.0177978
reasoning     0.11836    0.0737038  0.0241934
delta         0.0406779  0.0257724  0.00639566 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 2.3444491065101352e-12, 0.25: 2.729259138674518e-08, 0.5: 5.056466237851825e-07} 

 ************************************************************ 

Model: TransE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: both.optimistic.hits_at_5
                    0.1       0.25         0.5
------------  ---------  ---------  ----------
no reasoning  0.0455933  0.0272527  0.00915129
reasoning     0.0739239  0.0441357  0.0124725
delta         0.0283307  0.016883   0.00332119 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 2.070424183095253e-11, 0.25: 1.075355684680947e-07, 0.5: 1.574183072950611e-05} 

 ************************************************************ 

Model: TransE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: tail.optimistic.hits_at_10
                    0.1       0.25         0.5
------------  ---------  ---------  ----------
no reasoning  0.077841   0.0480301  0.0181432
reasoning     0.117931   0.0726258  0.0234419
delta         0.0400896  0.0245958  0.00529872 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 4.156885181665618e-12, 0.25: 8.549230835217675e-08, 0.5: 2.074247304763035e-05} 

 ************************************************************ 

Model: TransE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: tail.optimistic.hits_at_5
                    0.1       0.25         0.5
------------  ---------  ---------  ----------
no reasoning  0.0461246  0.0276854  0.00938283
reasoning     0.0735216  0.0433007  0.0120777
delta         0.0273969  0.0156153  0.00269491 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 4.8681109904088855e-11, 0.25: 4.933607564012121e-07, 0.5: 0.0001995646338415824} 

 ************************************************************ 

Model: TransE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: head.optimistic.hits_at_10
                    0.1       0.25        0.5
------------  ---------  ---------  ---------
no reasoning  0.0775222  0.0478327  0.0174524
reasoning     0.118788   0.0747818  0.024945
delta         0.0412662  0.0269491  0.0074926 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 2.1751896663659707e-12, 0.25: 1.2347352491310798e-08, 0.5: 4.4552401906062256e-08} 

 ************************************************************ 

Model: TransE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: head.optimistic.hits_at_5
                    0.1       0.25         0.5
------------  ---------  ---------  ----------
no reasoning  0.0450619  0.02682    0.00891976
reasoning     0.0743263  0.0449708  0.0128672
delta         0.0292644  0.0181508  0.00394747 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 1.5557667709242968e-11, 0.25: 3.2785275780128604e-08, 0.5: 8.479861446052573e-06} 

 ************************************************************ 

Model: TransH 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: both.optimistic.hits_at_10
                    0.1       0.25         0.5
------------  ---------  ---------  ----------
no reasoning  0.498421   0.503883   0.4653
reasoning     0.531287   0.524854   0.47222
delta         0.0328665  0.0209709  0.00691946 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 0.023914286045276324, 0.25: 0.05729049767156502, 0.5: 0.20218280222148527} 

 ************************************************************ 

Model: TransH 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: both.optimistic.hits_at_5
                    0.1       0.25        0.5
------------  ---------  ---------  ---------
no reasoning  0.373529   0.360616   0.320045
reasoning     0.403853   0.388066   0.335588
delta         0.0303234  0.0274501  0.0155432 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 0.0023449074713524343, 0.25: 0.00024093534753307657, 0.5: 0.000596357106394239} 

 ************************************************************ 

Model: TransH 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: tail.optimistic.hits_at_10
                    0.1       0.25        0.5
------------  ---------  ---------  ---------
no reasoning  0.493676   0.497852   0.458316
reasoning     0.527936   0.52159    0.467988
delta         0.0342595  0.0237379  0.0096713 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 0.021267266090350227, 0.25: 0.03808951562436347, 0.5: 0.1255602973590452} 

 ************************************************************ 

Model: TransH 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: tail.optimistic.hits_at_5
                    0.1       0.25        0.5
------------  ---------  ---------  ---------
no reasoning  0.367562   0.353928   0.311098
reasoning     0.398163   0.383079   0.330388
delta         0.0306005  0.0291505  0.0192895 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 0.0030599007115871143, 0.25: 0.000188543649404551, 0.5: 0.0001198612355722093} 

 ************************************************************ 

Model: TransH 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: head.optimistic.hits_at_10
                    0.1       0.25         0.5
------------  ---------  ---------  ----------
no reasoning  0.503166   0.509914   0.472284
reasoning     0.534639   0.528118   0.476452
delta         0.0314735  0.0182039  0.00416762 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 0.027293049873111624, 0.25: 0.08511224595373074, 0.5: 0.3070352068185517} 

 ************************************************************ 

Model: TransH 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: head.optimistic.hits_at_5
                    0.1       0.25        0.5
------------  ---------  ---------  ---------
no reasoning  0.379496   0.367304   0.328991
reasoning     0.409542   0.393054   0.340788
delta         0.0300463  0.0257496  0.0117969 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 0.0019181394083509881, 0.25: 0.00040743322525855054, 0.5: 0.0047025441547248956} 

 ************************************************************ 

Model: RotatE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: both.optimistic.hits_at_10
                   0.1       0.25        0.5
------------  --------  ---------  ---------
no reasoning  0.195445  0.0662757  0.0220868
reasoning     0.527431  0.389372   0.0495217
delta         0.331986  0.323096   0.0274349 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 1.1949069295916235e-22, 0.25: 1.8760686070325213e-22, 0.5: 8.06160767521985e-26} 

 ************************************************************ 

Model: RotatE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: both.optimistic.hits_at_5
                   0.1       0.25        0.5
------------  --------  ---------  ---------
no reasoning  0.144861  0.0443862  0.0128786
reasoning     0.428687  0.308479   0.036962
delta         0.283827  0.264093   0.0240834 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 1.4755345838155233e-24, 0.25: 7.803656447913068e-23, 0.5: 1.72405950111653e-28} 

 ************************************************************ 

Model: RotatE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: tail.optimistic.hits_at_10
                   0.1       0.25        0.5
------------  --------  ---------  ---------
no reasoning  0.195362  0.0672132  0.0229257
reasoning     0.528642  0.389547   0.0477795
delta         0.33328   0.322334   0.0248539 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 7.425511795989631e-23, 0.25: 3.7617888038045265e-22, 0.5: 3.0826995812202963e-21} 

 ************************************************************ 

Model: RotatE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: tail.optimistic.hits_at_5
                   0.1       0.25        0.5
------------  --------  ---------  ---------
no reasoning  0.143961  0.0450467  0.0135429
reasoning     0.425332  0.304851   0.0351021
delta         0.281371  0.259804   0.0215592 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 1.0038485264582768e-24, 0.25: 2.0600327065960478e-22, 0.5: 2.7798038964174367e-23} 

 ************************************************************ 

Model: RotatE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: head.optimistic.hits_at_10
                   0.1       0.25        0.5
------------  --------  ---------  ---------
no reasoning  0.195529  0.0653382  0.021248
reasoning     0.52622   0.389198   0.0512639
delta         0.330692  0.323859   0.0300159 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 1.974927950926491e-22, 0.25: 9.647537280681068e-23, 0.5: 8.159021504511555e-29} 

 ************************************************************ 

Model: RotatE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: head.optimistic.hits_at_5
                   0.1       0.25        0.5
------------  --------  ---------  ---------
no reasoning  0.14576   0.0437258  0.0122144
reasoning     0.432043  0.312108   0.0388218
delta         0.286283  0.268382   0.0266075 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 2.3476564929288228e-24, 0.25: 3.1229292032911866e-23, 0.5: 1.8717930908871404e-32} 

 ************************************************************ 

Model: BoxE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: both.optimistic.hits_at_10
                    0.1       0.25        0.5
------------  ---------  ---------  ---------
no reasoning  0.444918   0.397351   0.27307
reasoning     0.470519   0.423218   0.303272
delta         0.0256016  0.0258673  0.0302019 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 1.6540808329695112e-26, 0.25: 3.111926028082777e-22, 0.5: 2.2470082424660507e-17} 

 ************************************************************ 

Model: BoxE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: both.optimistic.hits_at_5
                    0.1       0.25        0.5
------------  ---------  ---------  ---------
no reasoning  0.304893   0.270527   0.194405
reasoning     0.320155   0.285417   0.207477
delta         0.0152623  0.0148903  0.0130722 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 2.6787580359178813e-18, 0.25: 8.567191196071942e-17, 0.5: 1.2983938794532529e-11} 

 ************************************************************ 

Model: BoxE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: tail.optimistic.hits_at_10
                    0.1       0.25       0.5
------------  ---------  ---------  --------
no reasoning  0.429932   0.383474   0.261421
reasoning     0.458741   0.41084    0.290731
delta         0.0288089  0.0273666  0.02931 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 1.032043085433976e-26, 0.25: 2.303505512471236e-21, 0.5: 5.914128532658761e-17} 

 ************************************************************ 

Model: BoxE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: tail.optimistic.hits_at_5
                    0.1      0.25        0.5
------------  ---------  --------  ---------
no reasoning  0.297282   0.262772  0.187732
reasoning     0.31683    0.281773  0.20334
delta         0.0195476  0.019001  0.0156077 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 1.219812691769143e-21, 0.25: 2.6351574347542278e-18, 0.5: 1.2523065282859253e-13} 

 ************************************************************ 

Model: BoxE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: head.optimistic.hits_at_10
                    0.1      0.25        0.5
------------  ---------  --------  ---------
no reasoning  0.459903   0.411228  0.284719
reasoning     0.482297   0.435596  0.315813
delta         0.0223943  0.024368  0.0310939 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 1.5848935744212848e-21, 0.25: 3.9773819752125056e-20, 0.5: 1.5666407075333818e-16} 

 ************************************************************ 

Model: BoxE 
Datalog Program: datalog_program/intermediate_concept_generalized.txt
Metric: head.optimistic.hits_at_5
                   0.1       0.25        0.5
------------  --------  ---------  ---------
no reasoning  0.312503  0.278281   0.201078
reasoning     0.32348   0.289061   0.211615
delta         0.010977  0.0107796  0.0105367 

p-value two-sided t-test. H1: reasoning > no reasoning
{'keys': [0.1, 0.25, 0.5], 0.1: 1.4816218049664643e-10, 0.25: 1.0057751801484567e-10, 0.5: 6.895314448933385e-08} 

 ************************************************************ 

