#! /usr/bin/env python3

import os
import os.path
import pdb

fdir = '/Users/xiuc/logs/201602'
fout = open('/Users/xiuc/logs/201602/crmandorder.log', 'a')
for i in os.listdir(fdir):
    if os.path.isfile(os.path.join(fdir, i)):
        fin = open(os.path.join(fdir, i), 'r')
        done = 0
        while not done:
            line = fin.readline()
            if line != '':
            	fout.write(line)
            else:
                done = 1
        fin.close()
fout.close()
