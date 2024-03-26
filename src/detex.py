#! /usr/bin/env python3

import argparse
import fileinput
import re
import sys

sticks = re.compile(r'\\([Ss]ti?c?k|hbox|hbox to \S+|centerline|rightline|short){(.*)}(\\\\(\[-?\d+pt\])?)?\s*\Z')
vskips = re.compile(r'\\(baseline|par|v)skip\s*-?\s*(\d+|\d*\.\d+)(pt|ex)\s*\Z')
catches = re.compile(r'\\[npc]atch(\[[^]]*\])?{(.*)}\s*\Z')

plain_tags = '''
topstrut chapstrut boxstrut etp null noindent bgroup egroup footnotesize selectfont par vfill
smaller small large Large huge Huge footnotesize Big
itshape frenchspacing obeylines
'''.split()

container_tags = '''
ls lss lsss vcenter halign
tight tighter rlap llap smash struck
Gothic gothic i smallit s ss sss g textnormal textsc mini
fbox hbox'''.split()
container_tags.append('hbox to [^{]+')

dimen = r'-?(\d+|\d*\.\d+)(pt|em|ex)'

dimen_tags_to_ignore = re.compile(rf'\\(raise|lower|tstrut|parindent)\s*{dimen}\s*')
plain_tags_to_ignore = re.compile(rf'\\({'|'.join(plain_tags)})\b\s*')
arg_tags_to_ignore = re.compile(r'\\(pagestyle|thispagestyle){[a-z]+}\s*\Z')
space_tags = re.compile(rf'\\(enspace|tspace|qquad|quad|indent|thinspace|hfill|hss|kern\s*{dimen}|cr|phantom{{.}}| )\s*')
quote_tags = re.compile(r'\\lqq\s*')
content_tags = re.compile(rf'\\({'|'.join(container_tags)}){{(.*?)}}')
chapters = re.compile(r'\\chap{([LXVI♣︎]+)}{\d+pt}{\d+pt}')
chapterx = re.compile(r'\\chapx{(.*)}{\d+pt}{\d+pt}')
graphics = re.compile(r'\\includegraphics(\[[^]]+\])?{([^}]+)}')
dumptwos = re.compile(r'\\(fontsize|setlength|setcounter){[^}]+}{[^}]+}')
initials = re.compile(r'\\initial(\[[^]]+\])?{([^}]+)}{([^}]+)}(.*)\Z')
dropcaps = re.compile(r'\\dropcap(\[[^]]+\])?{([^}]+)}{([^}]+)}(.*)\Z')
dropcapt = re.compile(r'\\dropcaptight(\[[^]]+\])?{([^}]+)}{([^}]+)}(.*)\Z')
alterna = re.compile(r'\\alt{([a-z]+)}{([a-z ]+)(\\hss)?}')
alternb = re.compile(r'\\alt{([a-z]+)}{\\c{([a-z ]+)}}')
vastfills = re.compile(rf'\\vastfill{{{dimen}}}')
lsvs = re.compile(r'\\lsv{[0-9.]+}{(.*?)}')
buzz = re.compile(r'\\bzz{([a-zA-Z]+)}')

vertical_skips = 'bigskip medskip smallskip vfill vss null'.split()
rule = '-' * 39

def make_catch_line(mark):
    '''create a catch line with "mark" text'''
    return rule[:-len(mark)-2] + '[' + mark + ']'

subs = {
    '~': ' ',
    '$': '',
    '#': '',
    '\\wastiv': '* * * *',
    '\\wastfill': '* * * * * * * * * * * * *',
    '\\tskk': ' -- ',
    '\\tsk': ' -- ',
    '\\tshh': '--- ',
    '\\tsh': ' --- ',
    '\\tsfill': ' -------- ',
    '\\crfill': ' - - ', 
    '\\trim': 'Trim',
    '\\toby': 'Toby',
    '\\tbrace': '}',
    '\\tsbrace': '}',
    '\\susannah': 'Susannah',
    '\\stickrule': rule,
    '\\snapp': ' ... ',
    '\\snap': ' .. ',
    '\\slop': 'Slop',
    '\\sic': '♣︎',
    '\\nastv': '*****',
    '\\lowastiv': '* * * *',
    '\\hrule': rule,
    '\\fnast': '*',
    '\\fist': ' ☞ ',
    '\\etc': '&c.',
    '\\et': '&',
    '\\drslop': 'Dr. Slop',
    '\\ddagger': '‡',
    '\\dagger': '†',
    '\\astWW6': '* * * * * *',
    '\\astW2': '**',
    '\\astW3': '***',
    '\\astW4': '****',
    '\\astW6': '******',
    '\\astW7': '*******',
    '\\astw3': '***',
    '\\astw5': '*****',
    '\\astw6': '******',
    '\\astw7': '*******',
    '\\astvi': '******',
    '\\astv': '*****',
    '\\astiv': '****',
    '\\ast': '*',
    '\\@': '',
    '\\;': ' ',
    '\\/': '',
    '\\,': ' ',
    '\\&': '&',
    '\\&': '&',
    '\\!': '',
    '\\{': '{',
    '\\}': '}',
}

def get_prefix(option_string):
    '''find the "ante" part of a dropcap'''
    m = re.search(r'ante=([^,\]]+)', option_string)
    return m.group(1)
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("source", nargs='+')
    args = parser.parse_args()

    out = []
    skipping = True
    for line in fileinput.input(files=args.source):
        t = line.strip()
        if not t:   # blank to start with
            out.append("")
            continue

        t = t.split('%')[0]  # decomment first

        if t == '\\begin{document}':
            skipping = False
            continue
        elif t == '\\end{document}':
            skipping = True
        elif "begin{mplibcode}" in t:
            skipping = True
            out.append("<< drawing >>")
        elif "end{mplibcode}" in t:
            skipping = False
            continue

        if skipping:
            continue

        end_of_page_mark = ''
        add_blank = False

        if t.startswith('\\') and t[1:] in vertical_skips:
            continue
        
        t = plain_tags_to_ignore.sub('', t)
        t = arg_tags_to_ignore.sub('', t)
        t = dumptwos.sub('', t)
        t = vastfills.sub('* * * * * * * * * * * * * *', t)
        t = lsvs.sub(r'\1', t)
        
        if t == '\\hrule width \\hsize height 0pt depth 280pt':
            for i in range(20):
                out.append('◼︎' * 39)
            continue

        for old, new in subs.items():
            t = t.replace(old, new)

        m = vskips.match(t)
        if m is not None:
            continue

        m = sticks.match(t)
        if m is not None:
            t = m.group(2)
            if m.group(4) is not None:
                add_blank = True

        while True:
            m = content_tags.search(t)
            if m is None:
                break
            t = content_tags.sub(r'\2', t)

        t = alterna.sub(r'\1<\2>', t)
        t = alternb.sub(r'\1<\2>', t)

        t = dimen_tags_to_ignore.sub('', t)
        t = space_tags.sub(' ', t)
        t = quote_tags.sub('“ ', t)

        m = buzz.search(t)
        if m is not None:
            t = buzz.sub('-' * len(m.group(1)), t)

        m = catches.match(t)
        if m is not None:
            out.append(make_catch_line(m.group(2)))
            continue

        m = catches.search(t)
        if m is not None:
            end_of_page_mark = m.group(2)
            t = t[:m.start()]

        if t == '\\eject':
            out.append(rule)
            continue

        m = chapters.match(t)
        if m is not None:
            out.append('')
            out.append(f'CHAP. {m.group(1)}.'.center(42))
            continue

        m = chapterx.match(t)
        if m is not None:
            out.append('')
            out.append(f'{m.group(1)}'.center(42))
            continue

        m = graphics.search(t)
        if m is not None:
            t = graphics.sub(f'<<{m.group(2)}>>', t)

        m = initials.match(t)
        if m is not None:
            t = m.group(2) + ' ' + m.group(3) + ' ' + m.group(4)
            t = t.rstrip()
            if m.group(1) is not None and "ante=" in m.group(1):
                t = get_prefix(m.group(1)) + ' ' + t

        m = dropcaps.match(t)
        if m is not None:
            t = m.group(2) + '' + m.group(3).upper() + ' ' + m.group(4)
            t = t.rstrip()
            if m.group(1) is not None and "ante=" in m.group(1):
                t = get_prefix(m.group(1)) + ' ' + t

        m = dropcapt.match(t)
        if m is not None:
            t = m.group(2) + '' + m.group(3).upper() + ' ' + m.group(4)
            t = t.rstrip()
            if m.group(1) is not None and "ante=" in m.group(1):
                t = get_prefix(m.group(1)) + ' ' + t

        t = t.removesuffix('\\break')
        t = t.removesuffix('\\\\')

        t = ' '.join(t.split())
        if t:    # skip lines that have *become* blank
            out.append(t)

        if end_of_page_mark:
            out.append(make_catch_line(end_of_page_mark))
            end_of_page_mark = ''
        if add_blank:
            out.append('')

    print("\n".join(out))
