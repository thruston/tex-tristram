#! /usr/bin/env python3

import fileinput
import re
patch = re.compile(r"(.*)(\\patch{.*})\s*$")

lines = []
raw = []

for line in fileinput.input():
    line = line.strip()
    raw.append(line)
    line = line.removesuffix("\\break")
    p = patch.match(line)
    if p is not None:
        lines.append(p.group(1))
        lines.append(p.group(2))
    elif line:
        lines.append(line)

if len(lines) == 3:
    print(f"\\stick{{{lines[0]}\\hfill}}")
    print(lines[1].replace("patch{", "catch{"))
    print(f"\\stick{{\\indent {lines[2]}}}")

else:
    print("\n".join(raw))
