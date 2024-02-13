#! /usr/bin/env python3

import argparse
import collections
import fileinput
import re

its = re.compile(r"\bit['’]?s\b")

seen = dict()
plain = collections.defaultdict(int)
aposs = collections.defaultdict(int)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("source_files", nargs='+')
    args = parser.parse_args()

    for line in fileinput.input(files=args.source_files):

        fn = fileinput.filename()
        seen[fn] = True

        for m in its.findall(line):
            if m == 'its':
                plain[fn] += 1
                print(fn, plain[fn], aposs[fn], line.strip())
            else:
                aposs[fn] += 1
                print(fn, plain[fn], aposs[fn], line.strip())


print()
for f in seen:
    print(f'{f}  {plain[f]}  {aposs[f]}')


