#! /usr/bin/env python3

import os
import os.path
import pdb

fdir = '/Users/xiuc/logs/search_neiwang'
fout = open('/Users/xiuc/logs/earchResult', 'a')
for i in os.listdir(fdir):
    if os.path.isfile(os.path.join(fdir, i)):
        fin = open(os.path.join(fdir, i), 'r')
        done = 0
        while not done:
            line = fin.readline()
            if line != '':
                if line.find('/goods/lid') >= 0:
                    fout.write(line)
            else:
                done = 1
        fin.close()
fout.close()
