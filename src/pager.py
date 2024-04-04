#! /usr/bin/env python3

import argparse
import fileinput
import re
import sys

catches = re.compile(r'\\[pc]atch[sv]?(\[[^]]*\])?{(.*)}\s*\Z')
counter = re.compile(r'\\setcounter{page}{(\d)}')
defvol = re.compile(r'\\def\\vol{([XVI]+)}')
alphabet = 'ABCDEFGHIKLMNOPQRST'   # no J for sigs... 


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("source", nargs='+')
    parser.add_argument("--offset", default=0, type=int)
    parser.add_argument("--changes", action='store_true')
    args = parser.parse_args()

    skipping = True
    folio = 0
    volume = 'X'
    out = []
    sig = 0
    for line in fileinput.input(files=args.source):
        t = line.strip()
        if not t:
            continue

        t = t.split('%')[0]  # decomment first

        if t == '\\begin{document}':
            skipping = False
            folio = 0
            continue
        elif t == '\\end{document}':
            skipping = True
        elif "begin{mplibcode}" in t:
            skipping = True
        elif "end{mplibcode}" in t:
            skipping = False
            continue

        if skipping:
            continue

        m = defvol.search(t)
        if m is not None:
            volume = m.group(1)
            continue

        m = counter.search(t)
        if m is not None:
            folio = int(m.group(1))
            continue

        m = catches.search(t)
        if m is None and t != '\\eject':
            continue

        # only here if making new page
        mark = ''
        n = (args.offset + folio) % 16
        if n == 1:
            mark = alphabet[sig]
        elif n == 3:
            mark = alphabet[sig] + ' 2'
        elif n == 5:
            mark = alphabet[sig] + ' 3'
        elif n == 7:
            mark = alphabet[sig] + ' 4'
        elif folio > 0 and n == 0:
            sig += 1

        if args.changes:
            if len(mark) == 1:
                out.append(re.sub(r'(catch|patch)(\[[^[]+\])?', rf'\1v\2{{{mark}}}',t.strip()))
            elif len(mark) == 3:
                out.append(re.sub(r'(catch|patch)(\[[^[]+\])?', rf'\1s\2{{{mark}}}',t.strip()))
        else:
            out.append(f'{volume} {folio} {mark:<4} {t.strip()}')

        if folio > 0:
            folio += 1

    print("\n".join(out))
