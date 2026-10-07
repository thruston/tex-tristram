#! /usr/bin/env python3

import re
import sys

text = []
para = []
for line in sys.stdin:
    t = line.strip()
    if t:
        para.append(t)
    elif para:
        text.append(para[:])
        para.clear()

if para:
    text.append(para[:])

for para in text:
    n = len(para)
    if n > 1:
        print(para[0] + "\\break")
        for i in range(1, n - 1):
            tag = "stick"
            if re.match(r'[A-Z] [1-4]}{', para[i]):
                tag = "catchs"
            elif re.match(r'[A-Z]}{', para[i]):
                tag = "catchv"
            elif len(para[i]) < 12:
                tag = "catch"
            elif set(para[i]) == {"-"}:
                para[i] = "\\hrulefill"

            print("\\" + tag + "{" + para[i] + "}")

    else:
        if re.match(r'[A-Z] [1-4]}{', para[0]):
            para[0] = "\\patchs{" + para[0] + "}"
        elif re.match(r'[A-Z]}{', para[0]):
            para[0] = "\\patchv{" + para[0] + "}"
        elif len(para[0]) < 12:
            para[0] = "\\patch{" + para[0] + "}"

    print(para[n-1])
    print()
