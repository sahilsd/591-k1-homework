import sys
from itertools import groupby

data = (line.rstrip().split('\t') for line in sys.stdin)
for v1v2, ui in groupby(data, lambda x: x[0:2]):
    #print v1v2
    for u in ui:
       #print v+'\t'+'1'
       if '$' in u[2:] and len(list(set(u[2:])))>1:
           #print u
           for c in list(set(u[2:])):
               if c != '$':
       	           print u[0]+"\t"+str(1)
