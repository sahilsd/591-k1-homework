#!/usr/bin/env python

import sys
from collections import defaultdict

vertices = defaultdict(list)

for line in sys.stdin:
    if line[0] == '#':
	continue
    words = line.strip().split('\t')	
    try:
	vertices[words[0]].append( words[1])
    except:
	vertices[words[0]] = [words[1]]
for k in vertices.keys():
    gammaK = ""
    for v in vertices[k]:
        gammaK = gammaK+'\t'+v

    print k+gammaK
    
