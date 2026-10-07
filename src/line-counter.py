#! /usr/bin/env python3

import argparse
import re
import sys

n = 0
p = 0
s = 0

header = re.compile(r"---+\[(\d+|[ivx]+)\]-----+\Z")
catch  = re.compile(r"-[-.VolaA-S1-5 ]+\[.*\]\Z")


for line in sys.stdin:
    w = line.rstrip()

    if m := header.match(w):
        print(w)
        p = m.group(1)
        n = 0
        s = 0
    elif catch.match(w):
        print(w, "@@@", p, n, s)
    elif w:
        n += 1
        print(f'{n:2d} {w}')
    else:
        s += 1
        print()
    
