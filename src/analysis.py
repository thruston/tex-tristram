#! /usr/bin/env python3

import argparse
import fileinput
import re
import collections

def convert(R):
    ''' Roman to int
    >>> convert('X')
    10
    >>> convert('XLIV')
    44
    >>> convert('MMI')
    2001
    >>> convert('MCMLXII')
    1962
    '''
    values = collections.OrderedDict(cm=900, cd=400, xc=90, xl=40, ix=9, iv=4, 
                                     m=1000, d=500, c=100, l=50, x=10, v=5, i=1)

    roman = R.lower()
    n = 0
    while roman:
        for k, v in values.items():
            if roman.startswith(k):
                n += v
                roman = roman[len(k):]
                break
    return n

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("plain", nargs='*')
    args = parser.parse_args()


    cap = '0'
    vol = 'I'
    counts = collections.defaultdict(int)
    # what counts as a word?
    extra_letters = "ÆàáâæçèéêîòôùúûüŒœ"
    greek_letters = "ΔΕΘΙΚΠΣΤΦΧάίαβγδεζηθικλμνξοπρςστυφχωόώϕἀἄἅἈἐἣἰἵἶὅὉὐὑὖὠὰάὲέὴὶίὸόὺώᾶῆῖῦῶῷ"
    leaders = "A-Za-z" + extra_letters + greek_letters + '&'
    followers = '-' + leaders + "0-9" + "'—’"
    word = re.compile(rf"[{leaders}][{followers}]+")
    for line in fileinput.input(files=args.plain):
        m = re.match(r'VOL\. ([XVI]+)', line)
        if m is not None:
            vol = m.group(1)
            cap = '0'

        m = re.match(r'CHAP\. ([LXVI]+)', line)
        if m is not None:
            cap = convert(m.group(1))

        for w in word.findall(line):
            counts[(w, vol, cap)] += 1

    print("Word  Vol  Cap  Count")
    for k in sorted(counts, key=lambda a: a[0].casefold()):
        w, v, c = k
        print(f"{w:<50}  {v:<4}  {int(c):4d}  {counts[k]}")



