#! /usr/bin/env python3

import argparse
import fileinput

n = 0;
lines = []

for line in fileinput.input():
    line = line.strip()
    if line.endswith("\\break"):
        line = line[:-6]
    lines.append(line)

print(lines[0] + "\\break")

for line in lines[1:-1]:

    if line.startswith("\\natch{"):
        print(line)
        continue

    if line.startswith("\\stick{"):
        print(line)
        continue

    if line.startswith("\\stck{"):
        print(line)
        continue
    
    if line.startswith("\\sck{"):
        print(line)
        continue

    if line.startswith("\\tight{"):
        print("\\stck{" + line[7:])
        continue

    print("\\stick{" + line + "}")

print(lines[-1])


