#!/usr/bin/env python

import sys
from collections import defaultdict

vertices = defaultdict(list)
data = [line.rstrip().split('\t') for line in sys.stdin]
#data = (line.rstrip().split('\t') for line in sys.stdin)


#red2dict = defaultdict(list)
for r in data:
    #k = r[0]+'\t'+r[1]
    try:
        print r[0]+'\t'+r[1]+'\t'+r[2]
    except IndexError:
        print r[0]+'\t'+r[1]+'\t$'
"""
for k in red2dict.keys():    
    if '$' in red2dict[k] and len(red2dict[k])>1:
        ret = ""
        for v in red2dict[k]:
            if v != '$':
                ret = ret+'\t'+v

	print k+ret

"""
