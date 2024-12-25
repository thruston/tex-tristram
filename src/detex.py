#! /usr/bin/env python3

import argparse
import collections
import fileinput
import re
import sys
import textwrap

unit = r'(pt|em|ex|cm|in|bp)\s*'
dimen = rf'(-\s*)?\d+(\.\d*)?{unit}'
stretch = rf'plus {dimen}\s*'
shrink = rf'minus {dimen}\s*'
skipdefs = re.compile(rf'\\(baseline|par)skip\s*{dimen}({stretch})?({shrink})?')
vskips = re.compile(rf'\\vskip\s*({dimen}|-?\\baselineskip)\s*\Z')

sticks = re.compile(r'\\([Ss]ti?c?k|hbox|hbox to \S+|centerline|rightline|short){(.*)}(\\\\(\[-?\d+pt\])?)?\s*\Z')
catches = re.compile(r'\\[pc]atch(\[[^]]*\])?{(.*)}\s*\Z')
catchex = re.compile(r'\\[pc]atch[vsn](\[[^]]*\])?{([A-Pa234 ]+)}{(.*)}\s*\Z')


plain_tags = '''
topstrut chapstrut boxstrut etp etpp null noindent bgroup egroup footnotesize selectfont par vfill
smaller small large Large huge Huge footnotesize Big thinspace raggedbottom scriptsize
scshape itshape frenchspacing obeylines porson tspace donol
'''.split()

container_tags = '''
ls lss lsss vcenter halign lo
tight tighter rlap llap smash struck
Gothic gothic i smallit s ss sss g textnormal textsc mini
fbox hbox'''.split()
container_tags.append('hbox to [^{]+')

dimen = r'-?(\d+|\d*\.\d+)(pt|em|ex)'

dimen_tags_to_ignore = re.compile(rf'\\(raise|lower|tstrut|parindent)\s*{dimen}\s*')
plain_tags_to_ignore = re.compile(rf'\\({"|".join(plain_tags)})\b\s*')
pagination_tags = re.compile(r'\\(pagestyle|thispagestyle|pagenumbering){([a-z]+)}\s*\Z')
space_tags = re.compile(rf'\\(enspace|qquad|quad|indent|hfill?|hss|kern\s*{dimen}|cr|phantom{{.}}| )\s*')
quote_tags = re.compile(r'\\lqq\s*')
content_tags = re.compile(rf'\\({"|".join(container_tags)}){{(.*?)}}')
chapters = re.compile(r'\\chap{([LXVI♣︎]+)}{\d+pt}{\d+pt}')
chapterx = re.compile(r'\\chapx{(.*)}{\d+pt}{\d+pt}')
headers = re.compile(r'\\head{\d+pt}{\d+}{(.*)}')
graphics = re.compile(r'\\includegraphics(\[[^]]+\])?{([^}]+)}')
dumptwos = re.compile(r'\\(fontsize|setlength|setcounter){[^}]+}{[^}]+}')
initials = re.compile(r'\\initial(\[[^]]+\])?{([^}]+)}{([^}]+)}(.*)\Z')
dropcaps = re.compile(r'\\dropcap(\[[^]]+\])?{([^}]+)}{([^}]+)}(.*)\Z')
dropcapt = re.compile(r'\\dropcaptight(\[[^]]+\])?{([^}]+)}{([^}]+)}(.*)\Z')
alterna = re.compile(r'\\alt{([a-z]+)}{([a-z ]+)(\\hss)?}')
alternb = re.compile(r'\\alt{([a-z]+)}{\\c{([a-z ]+)}}')
vastfills = re.compile(rf'\\vastfill{{{dimen}}}')
lsvs = re.compile(r'\\lsv{[0-9.]+}{(.*?)}')
buzz = re.compile(r'\\bzz{([a-zA-Z’]+)}')
defvol = re.compile(r'\\def\\vol{([XVI]+)}\s*\Z')

vertical_skips = 'bigskip medskip smallskip vfill vss null'.split()
rule = '-' * 39
vol = 'X'


def make_catch_line(sig, mark):
    '''create a catch line with "mark" text

    >>> make_catch_line('', 'Toby')
    '---------------------------------[Toby]'

    >>> make_catch_line('A', 'Toby')
    '-Vol.X.------------A-------------[Toby]'

    >>> make_catch_line('L 3', 'Now')
    '------------------L 3-------------[Now]'

    '''
    if sig == '':
        return rule[:-len(mark)-2] + '[' + mark + ']'

    if len(sig) == 1:
        lhs = f'{rule[0]}Vol.{vol}.'
        rhs = f'[{mark}]'
        t = sig.center(len(rule), rule[0])
        return lhs + t[len(lhs):-len(rhs)] + rhs

    if len(sig) == 3:
        rhs = f'[{mark}]'
        t = sig.center(len(rule), rule[0])
        return t[:-len(rhs)] + rhs



subs = {
    '~': ' ',
    '$': '',
    '#': '',
    '\\wastiv': '* * * *',
    '\\wastfill': '* * * * * * * * * * * * *',
    '\\tskk': ' -- ',
    '\\tsk': ' -- ',
    '\\tush': '----- ',
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
    '\\sicc': '♣︎',
    '\\nastv': '*****',
    '\\lowastiv': '* * * *',
    '\\hrulefill': rule,
    '\\hrule': rule,
    '\\fnast': '*',
    '\\fist': ' ☞ ',
    '\\etc': '&c.',
    '\\et': '&',
    '\\drslop': 'Dr. Slop',
    '\\ddagger': '‡',
    '\\dagger': '†',
    '\\astWW3': '* * *',
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
    '\\astiii': '***',
    '\\anon': '****',
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
    '\\rqq': '”',
}

def get_prefix(option_string):
    '''find the "ante" part of a dropcap'''
    m = re.search(r'ante=([^,\]]+)', option_string)
    return m.group(1)

hyphenated_words = '''above-named all-four arm-chair band-box bandy-leg’d
bank-note before-hand bend-sinister bowling-green broken-winded button-hole
camp-bed candle-ends candle-light cannon-ball cast-almanack chaise-vamper
chaise-vamper’s chamber-maid chamber-maids cherry-stone child-bearing
christen-names Christian-name church-lawyers day-shifts demi-bastions
demi-culverins Serjeant-Surgeon purchase-money pink’d-doublet kindly-hearted
gerund-grinders wicker-basket travel-readers travel-writers silver-fringed
school-divines Christ-cross-row clock-work coach-horse coach-man coat-pocket
crimson-sattin day-light demi-bastion fellow-feeling fish-kettle
five-and-twenty fore-finger four-footed grainge-house half-moon high-way
Hobby-Horse Hobby-Horses horn-works horse-guards Ill-timed ink-horn inn-keeper
jack-boots left-hand love-making May-poles Montero-cap night-gown oft-times
over-against parlour-door placket-holes post-chaise prayer-book school-divinity
school-men self-same self-taught semi-parameter sentry-box smoak-jack
strait-hearted street-door sun-shine tea-things to-morrow tobacco-pipe
town-clerk twenty-four un-scholar-like water-drinker water-stop where-ever
wind-mill'''.split()

tst = '''ran like wild-fire. -- “ The parson had “ in this act of charity.”'''


def remove_running_quotes(p):
    '''get rid of lqqs

    >>> remove_running_quotes(tst)
    'ran like wild-fire. -- “ The parson had  in this act of charity.”'
    '''

    inquote = False
    out = []
    for c in p:
        if c == '“' and not inquote:
            inquote = True
        elif c == '“':
            continue
        elif c == '”':
            inquote = False
        out.append(c)

    p = ''.join(out)
    p = re.sub(r'“\s+', '“', p)
    p = re.sub(r'\s+”', '”', p)
    return p


def remove_line_splits(p):
    '''join lines taking account of hyphenation'''
    # first make sure dashes have space around them
    p = re.sub(r'(--+)', r' \1 ', p)
    # with exceptions
    p = p.replace('sh -- t-a-beds', 'sh--t-a-beds')
    # now mark breaks
    p = re.sub(r'([a-zOAοæœ]-)\n\s*', r'\1@', p)
    p = ' '.join(p.split())

    out = []
    for w in p.split():
        n = w.count('@')
        if n == 0:
            out.append(w)
            continue

        hyphenated_candidate = w.replace('@', '')
        clean_candidate = w.replace('-@', '')

        if hyphenated_candidate.rstrip(',.;:!’') in hyphenated_words:
            out.append(hyphenated_candidate)
        else:
            out.append(clean_candidate)

    return ' '.join(out)

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

def make_page_header(numerals, style, number):
    if style == "folio":
        if numerals == "roman":
            n = to_roman(number)
        else:
            n = str(number)
        return f"[{n}]".center(len(rule), rule[0])

    return ""


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("source", nargs='+')
    parser.add_argument("--paginate", action='store_true', help="Show text as is, without flowing")
    parser.add_argument("--width", type=int, default=72, help="How wide?  Ignored with --paginate")
    args = parser.parse_args()

    if args.paginate:
        trap = None
    else:
        trap = textwrap.TextWrapper(width=args.width, break_long_words=False, break_on_hyphens=False)

    out = []
    skipping = True
    folio = 0
    numeration = "none"
    page_style = "empty"
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

        add_blank = False

        m = defvol.match(t)
        if m is not None:
            vol = m.group(1)
            continue

        if t.startswith('\\') and t[1:] in vertical_skips:
            continue

        m = skipdefs.match(t)
        if m is not None:
            continue

        t = plain_tags_to_ignore.sub('', t)
        t = dumptwos.sub('', t)
        t = vastfills.sub('* * * * * * * * * * * * * *', t)
        t = lsvs.sub(r'\1', t)

        if t == '\\hrule width \\hsize height 0pt depth 280pt':
            for i in range(20):
                out.append('◼︎' * 39)
            continue

        m = pagination_tags.match(t)
        if m is not None:
            tag = m.group(1)
            if tag == "pagestyle":
                page_style = m.group(2)
            elif tag == "pagenumbering":
                numeration = m.group(2)
                folio = 1
            continue

        m = buzz.search(t)
        if m is not None:
            t = buzz.sub('–' * len(m.group(1)), t)

        t = t.replace('\\vol', vol)
        for old, new in subs.items():
            t = t.replace(old, new)

        m = vskips.match(t)
        if m is not None:
            continue

        m = sticks.match(t)
        if m is not None:
            t = m.group(2)
            if m.group(4) is not None:
                if not m.group(4).startswith("[-"):
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

        if t == rule:
            out.append('')
            out.append(t)
            out.append('')
            continue

        m = catchex.match(t)
        if m is not None:
            if args.paginate:
                out.append(make_catch_line(m.group(2), m.group(3)))
                folio += 1
                out.append(make_page_header(numeration, page_style, folio))
            continue

        m = catches.match(t)
        if m is not None:
            if args.paginate:
                out.append(make_catch_line('', m.group(2)))
                folio += 1
                out.append(make_page_header(numeration, page_style, folio))
            continue

        if t == '\\eject' or t == "\\newpage":
            if args.paginate:
                out.append(rule)
                folio += 1
                out.append(make_page_header(numeration, page_style, folio))
            else:
                out.append('')
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

        m = headers.match(t)
        if m is not None:
            out.append('')
            out.append(f'{m.group(1)}.'.center(42))
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

        if add_blank:
            out.append('')

    text = '\n'.join(out)
    if trap is None:
        print(text)
        sys.exit(0)

    # Now we are going to re-flow
    for par in re.split(r"\n{2,}", text):
        par = remove_running_quotes(par)
        par = remove_line_splits(par)
        print(trap.fill(par))
        print()
