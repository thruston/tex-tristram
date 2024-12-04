#! /usr/bin/env python3

import argparse
import fileinput

if __name__ == "__main__":
    for i, line in enumerate(fileinput.input()):
        print(f'{i+1:6d}  {len(line)-1:6d}  {line.rstrip()}')



