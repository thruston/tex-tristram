#! /usr/bin/env python3

import argparse
import fileinput
import re 

lines = []
raw = []

for line in fileinput.input():
    line = line.strip()
    raw.append(line)
    if line:
        lines.append(line.removesuffix("\\break"))

if len(lines) == 3:
    print(f"\\stick{{{lines[0]}\\hfill}}")
    print(lines[1].replace("patch{", "catch{"))
    print(f"\\stick{{\\indent {lines[2]}}}")

else:
    print("\n".join(raw))


