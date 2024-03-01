#! /usr/bin/env python3

import argparse
import fileinput
import re 

tight = re.compile(r'\\stick{\\tight{(.*)}}')
tighter = re.compile(r'\\stick{\\tighter{(.*)}}')

n = 0;

paras = []
lines = []

for line in fileinput.input():
    line = line.strip()
    if line == "" and lines:
        paras.append(lines[:])
        lines.clear()
    else:
        line = line.removesuffix("\\break")
        lines.append(line)

if lines:
    paras.append(lines[:])

for p in paras:
   
    if len(p) == 1:
        print(p[0])
        continue

    print(p[0] + "\\break")

    for line in p[1:-1]:

        if line.startswith("\\catch{"):
            print(line)
            continue

        if line.startswith("\\patch{"):
            print(line)
            continue

        m = tight.match(line)
        if m is not None:
            print("\\stck{" + m.group(1) + "}")
            continue

        m = tighter.match(line)
        if m is not None:
            print("\\stk{" + m.group(1) + "}")
            continue

        if line.startswith("\\stick{"):
            print(line)
            continue

        if line.startswith("\\stck{"):
            print(line)
            continue
        
        if line.startswith("\\stk{"):
            print(line)
            continue

        if line.startswith("\\tight{"):
            print("\\stck{" + line[7:])
            continue

        print("\\stick{" + line + "}")

    print(p[-1])
    print()


