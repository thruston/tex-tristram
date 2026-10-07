#! /usr/bin/env python3

import argparse
import collections
import fileinput
import re
import sys

def to_roman(num):
    roman = collections.OrderedDict()
    roman[1000] = "m"
    roman[900] = "cm"
    roman[500] = "d"
    roman[400] = "cd"
    roman[100] = "c"
    roman[90] = "xc"
    roman[50] = "l"
    roman[40] = "xl"
    roman[10] = "x"
    roman[9] = "ix"
    roman[5] = "v"
    roman[4] = "iv"
    roman[1] = "i"

    def roman_num(num):
        for r in roman.keys():
            x, y = divmod(num, r)
            yield roman[r] * x
            num -= (r * x)
            if num <= 0:
                break

    return "".join([a for a in roman_num(num)])


catches = re.compile(r'\\[pc]atch[sv]?(\[[^]]*\])?{(.*)}\s*\Z')
change_folio = re.compile(r'\\setcounter{page}{(\d)}')
start_folio  = re.compile(r'\\pagenumbering{(roman|arabic)}')
defvol = re.compile(r'\\def\\vol{([XVI]+)}')
alphabet = 'ABCDEFGHIKLMNOPQRST'   # no J for sigs... 

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("source", nargs='+')
    parser.add_argument("--offset", default=0, type=int)
    parser.add_argument("--changes", action='store_true')
    parser.add_argument("--rewrite", action='store_true')
    args = parser.parse_args()

    skipping = True
    folio = 0
    numerals = 'arabic'
    volume = 'X'
    out = []
    sig = 0
    lines_on_page = 0
    for line in fileinput.input(files=args.source):
        if args.rewrite:
            out.append(line.rstrip())

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

        if m := start_folio.search(t):
            folio = 1
            numerals = m.group(1)
            continue

        m = change_folio.search(t)
        if m is not None:
            folio = int(m.group(1))
            continue

        m = catches.search(t)
        if m is None and not (t in '\\eject \\newpage'.split()):
            lines_on_page += 1
            continue

        # only here if making new page
        mark = ''
        sig, n = divmod(args.offset + folio, 16)
        if n == 1:
            mark = alphabet[sig]
        elif n == 3:
            mark = alphabet[sig] + ' 2'
        elif n == 5:
            mark = alphabet[sig] + ' 3'
        elif n == 7:
            mark = alphabet[sig] + ' 4'

        if args.changes:
            if args.rewrite:
                _ = out.pop()
            if len(mark) == 0:
                out.append(t)
            elif len(mark) == 1:
                out.append(re.sub(r'(catch|patch)(\[[^[]+\])?', rf'\1v\2{{{mark}}}',t))
            elif len(mark) == 3:
                out.append(re.sub(r'(catch|patch)(\[[^[]+\])?', rf'\1s\2{{{mark}}}',t))
        else:
            if numerals == 'roman':
                n = f'{to_roman(folio):<4}'
            else:
                n = f'{str(folio):>4}'

            out.append(f'{volume} {n} {mark:<4} {lines_on_page} {t.strip()}')
            lines_on_page = 0

        if folio > 0:
            folio += 1

    print("\n".join(out))
