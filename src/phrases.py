#! /usr/bin/env python3

import argparse
import collections
import fileinput
import re
import sys
    
# what counts as a word?
extra_letters = "ÆàáâæçèéêîòôùúûüŒœ"
greek_letters = "ΔΕΘΙΚΠΣΤΦΧάίαβγδεζηθικλμνξοπρςστυφχωόώϕἀἄἅἈἐἣἰἵἶὅὉὐὑὖὠὰάὲέὴὶίὸόὺώᾶῆῖῦῶῷ"
leaders = "A-Za-z" + extra_letters + greek_letters + "'’&"
followers = '-' + leaders + "0-9" + "—'’"
word = re.compile(rf"(?:[{leaders}][{followers}]+|[AIOVXLa]|-+)")

def clean(text):
    text = text.replace("'s", "’s")
    return ' '.join(word.findall(text))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs='*')
    parser.add_argument("--length", type=int, default=2)
    parser.add_argument("--clean", action="store_true")
    parser.add_argument("--count", type=int, default=20)
    args = parser.parse_args()

    
    paragraphs = []
    buffer = []

    for line in fileinput.input(files=args.files):
        line = line.strip()

        if line:
            buffer.append(line)
        else:
            par = ' '.join(buffer)
            if args.clean:
                par = clean(par)
            paragraphs.append(par)
            buffer.clear()


    phrases = []
    for p in paragraphs:
        words = p.split()
        for i, w in enumerate(words[:1-args.length]):
            ph = [words[i+j] for j in range(args.length)]
            phrases.append(tuple(ph))

    c = collections.Counter(phrases)
   
    for t, n in c.most_common(args.count):
        print(n, ' '.join(t))







