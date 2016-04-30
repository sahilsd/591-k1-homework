#!/usr/bin/env python

import sys
from itertools import groupby

data = [line.rstrip().split('\t') for line in sys.stdin]

for r in data:
    u = r[0]
    for v1 in xrange(1,len(r)):
	print u+'\t'+r[v1]
        for v2 in xrange(v1,len(r)): 
	    if v1 == v2:
                continue
	    print u+'\t'+r[v2]
 	    print r[v1]+'\t'+r[v2]+'\t'+u   

#for w,c in groupby(data, lambda x:x[0]):
    #print w
    #for w1,c1 in groupby(c, lambda x:x[0]):
        #print w1
    #listu = [v for _,v in c] 
    #print w, listu
    #print w+"\t"+str(sum(int(cc) for _, cc in c))

