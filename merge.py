#!/usr/bin/python

import csv
import glob

weather = glob.glob('*city*.csv')[0]
flow = glob.glob('*river*.csv')[0]

w_reader = csv.reader(open(weather, 'rb'), delimiter=',', quotechar='"')
f_reader = csv.reader(open(flow, 'rb'), delimiter=',', quotechar='"')
w_rows = [row for row in w_reader]
f_rows = [row for row in f_reader]

for n, w in enumerate(w_rows):
    datetime = w[0]
    for l in f_rows:
        if datetime in l:
            [w.append(l[1])
             for r in f_rows
             if r[0] == datetime]
        w_rows[n] = w
# ?csv
print "\n".join([", ".join(['"%s"' % i for i in r]) for r in w_rows])
