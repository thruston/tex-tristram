#! /usr/bin/env python3

import argparse
import fileinput
import re
import sys
import textwrap

def get_nested_contents(text, start):
    '''Extract nested brace content
    >>> get_nested_contents('Hello \hbox{Toby} how are you doing?', 6)
    ('Hello ', 'Toby', ' how are you doing?')
    >>> get_nested_contents('Hello \hbox{Toby how are you doing?', 6)
    ('Hello ', 'Toby how are you doing?', '')
    >>> get_nested_contents('Hello \hbox{', 6)
    ('Hello ', '', '')

    '''

    prefix, remainder = text[:start], text[start:]
    
    nest = 0
    content = []
    suffix = ''
    for i, c in enumerate(remainder):
        if c == '{':
            nest += 1
        elif c == '}':
            nest -= 1

        if nest == 1 and c == '{':
            continue

        if nest == 0 and c == '}':
            continue

        if nest > 0:
            content.append(c)
        elif content:
            suffix = remainder[i:]
            break

    return (prefix, ''.join(content), suffix)


def unbox(tag, para):
    '''Extract content from boxes
    >>> unbox('hbox', ' \\hbox{T H E}\\cr \\hbox{ L I F E}\\cr') 
    ' T H E\\\\cr  L I F E\\\\cr'
    >>> unbox('textit', '\\\\textit{Jo-\\catch{seph} seph Scaliger}')
    'Jo-\\\\catch{seph} seph Scaliger'
    '''

    while True:
        p = para.find(f'\\{tag}{{')
        if p < 0:
            break
        prefix, content, suffix = get_nested_contents(para, p)
        if tag == 'halign':
            content = content.replace('&', ' ')
        para = prefix + content + suffix
    return para[:]

def unstick(para):
    '''Extract content from \sticks{}
    >>> unstick("-- My father was a \stck{philosopher in grain, -- speculative, -- } \stick{systematical; -- and my aunt Dinah’s af-} fair was")
    '-- My father was a philosopher in grain, -- speculative, --\\\\break systematical; -- and my aunt Dinah’s af-\\\\break fair was'
    
    '''
    while True:
        m = re.search(r'\\[Ss]ti?c?k{', para)
        if m is None:
            break
        prefix, content, suffix = get_nested_contents(para, m.start())
        para = prefix + content.rstrip() + '\\break' + suffix
    return para[:]

def fix_initial(m):
    '''Tidy up using contents of matchobj m
    '''
    a, b = m.groups()
    a = a.replace('“', '').strip()
    b = b.lower() if a != 'O' else b
    space = ' ' if a[-1] in 'A I O'.split() else ''
    return a + space + b


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("source", nargs='+')
    args = parser.parse_args()

    buffer = []
    paragraphs = []
    skipping = False
    for line in fileinput.input(files=args.source):
        t = line.strip()
        t = t.split('%')[0]  # decomment before joining in paragraph

        m = re.match(r'\\(baseline|par)skip\s*(\d+|\d+\.\d+)\s*pt\s*$', t)
        if m is not None:
            continue

        m = re.match(r'\\chap{([^}]+)}', t)
        if m is not None:
            if buffer:
                paragraphs.append(' '.join(buffer))
                buffer.clear()
            paragraphs.append('CHAP ' + m.group(1) + '.')
            continue

        m = re.match(r'\\chapx{(.*?)}{\d+pt}{\d+pt}', t)
        if m is not None:
            if buffer:
                paragraphs.append(' '.join(buffer))
                buffer.clear()
            paragraphs.append(m.group(1))
            continue

        if skipping:
            i = t.find('\\end{mplibcode}')
            if i < 0:
                continue
            skipping = False
            t = t[i + 15:]
        else:
            i = t.find('\\begin{mplibcode}')
            if i < 0:
                pass
            else:
                skipping = True
                t = t[:i]

        if t:
            buffer.append(t)
            continue

        if buffer:
            paragraphs.append(' '.join(buffer))
            buffer.clear()

    if buffer:
        paragraphs.append(' '.join(buffer))

    simple_tags = '''
    vfill upshape smallskip smaller small sic selectfont qquad quad par Big
    null normalsize normalshape noindent newpage Large large itshape indent huge Huge
    hss vss hfill hfil vfill vfil footnotesize etpp etp enspace eject egroup egb
    club bigskip bgroup cr leaders thinspace clearpage begingroup endgroup medskip
    sloppy xleaders bnq strut chapstrut topstrut cleardoublepage obeylines nobreak leavevmode
    offinterlineskip frenchspacing
    '''.strip().split()

    dimen_tags = '''
    enlargethispage vskip hskip kern lower raise openup vspace moveright hsize
    parfillskip parindent tstrut 
    '''.strip().split()

    dump_ones = '''
    documentclass usepackage pagestyle thispagestyle begin end date title author includegraphics
    addfontfeature phantom noalign mplibtextextlabel
    '''.strip().split()

    dump_twos = '''
    setlength fontsize setcounter
    '''.strip().split()

    text_decor = '''
    smallit lsss lss ls textit textsc textscl gothic rlap i s g textnormal 
    '''.strip().split()

    subs = {
        '\\fist': ' ☞ ',
        '\\tsk': ' -- ',
        '\\tsh': ' --- ',
        '\\tsfill': ' -------- ',
        '\\crfill': ' - - ',
        '\\lqq': '“ ',
        '\\wastiv': '* * * *',
        '\\astfill': '********',
        '\\wastfill': '********',
        '\\astvi': '******',
        '\\astiv': '****',
        '\\lowastiv': '****',
        '\\astv': '*****',
        '\\nastv': '*****',
        '\\astw2': '**',
        '\\astw3': '***',
        '\\astw4': '****',
        '\\astw5': '*****',
        '\\astw6': '******',
        '\\astw7': '*******',
        '\\astW2': ' * * ',
        '\\astW3': ' * * * ',
        '\\astW4': ' * * * * ',
        '\\astW5': ' * * * * * ',
        '\\astW6': ' * * * * * * ',
        '\\starfill': ' * * * * * * * * * * * * * ',
        '\\ast': '*',
        '\\dagger': '†',
        '\\ddagger': '‡',
        '\\etc': '&c',
        '\\et': '&',
        '\\&': '&',
        '\\/': '',
        '\\fnast': '*',
        '\\\\': '',
        '\\ ': ' ',
        '~': ' ',
        '#': ' ',
        '$': '',
        '\\toby': 'Toby',
        '\\trim': 'Trim',
        '\\drslop': 'Dr. Slop',
        '\\slop': 'Slop',
        '\\susannah': 'Susannah',
    }

    for p in paragraphs:

        p = p.replace("\\ ", " ")   # forced space
        p = p.replace("\\,", " ")   # small space
        p = p.replace("\\;", " ")   # small space
        p = p.replace("\\!", "")    # small negative space
        p = p.replace("\\@", "")    # french spacing after .
        p = p.replace("\\-", "")    # optional hyphenation
        p = p.replace("\\tspace ", "")    # invisible space
        p = re.sub(r'\\\\\[-?\d+pt\]', " ", p)  # forced break with space
        p = p.replace("\\[", "")    # start math
        p = p.replace("\\]", "")    # stop math
        p = p.replace("\\{", "")    # big brace
        p = p.replace("\\}", "")    # big brace

        # specific to Vol 5. (Trim snapping his fingers)
        p = re.sub(r'\\xleaders\\hbox to \.3em{\\hss\.\\hss}', ' .. ', p) 

        p = re.sub(r'\\vastfill{(\d+|\d\.\d+|\.\d+)em}', '* * * * * * * * *', p)

        for t in simple_tags:
            p = re.sub(rf'\\{t}\b\s*', ' ', p)

        for t in dimen_tags:
            p = re.sub(rf'\\{t}\s*-?(\d+|\.\d+|\d+\.\d*)?(pt|em|ex)', '', p)

        p = re.sub(r'\\lsv{(\d+|\d\.\d+)}{(.*?)}', r'\2', p)

        p = re.sub(r'(-|\d)\\baselineskip', '12pt', p)
        p = re.sub(r'\\parskip', '12pt', p)
        for t in dimen_tags:
            p = re.sub(rf'\\{t}\s*-?(\d+|\.\d+|\d+\.\d*)?(pt|em|ex)', '', p)

        for t in dump_ones:
            p = re.sub(rf'\\{t}(\[.*?\])?{{.*?}}', '', p)

        for t in dump_twos:
            p = re.sub(rf'\\{t}{{[^}}]+}}{{[^}}]+}}', '', p)

        for t in text_decor:
            p = unbox(t, p)
            # p = re.sub(rf'\\{t}{{(.*?)}}', r' \1', p)

        for k, v in subs.items():
            p = p.replace(k, v)

        p = re.sub(r'\\Usk{(\d+|\d+\.\d+)pt}', '--', p)
        p = re.sub(r'\\Tsk', '--', p)
        p = re.sub(r'\\rotatebox\[origin=c\].180.{(.)}', r'\1', p)

        # boxes
        p = re.sub(r'\\hbox to [^{]+\s*{', r'\\hbox{', p)
        p = re.sub(r'\\vbox to [^{]+\s*{', r'\\vbox{', p)
        p = re.sub(r'\\halign to [^{]+\s*{', r'\\halign{', p)
        for t in 'hbox vbox fbox tight tighter centerline footnote halign c vcenter smash'.split():
            p = unbox(t, p)

        # lettrines...
        p = re.sub(r'\A\\dropcap(?:\[[^]]+\])?{\s*([A-Z])}{\s*([a-z]+)}', r'\1\2', p)
        p = re.sub(r'\A\\dropcap{\s*([A-Z])}{} ', r'\1', p)
        p = re.sub(r'\A\\dropcap(?:\[[^]]+\])?{(.*?)}{(.*?)}', r'\1\2', p)
        p = re.sub(r'\A\\dropcaptight{(.*?)}{(.*?)}', r'\1\2', p)
        p = re.sub(r'\\initial(?:\[[^]]+\])?{([-A-Z“ ]+)}{\s*([A-Za-z!, ]+)}', fix_initial, p)

        # alternative text in the anathema
        p = re.sub(r'\\alt{(.*?)}{(.*?)}', r'\1[\2]', p)

        # rules
        p = re.sub(r'\\[vh]rule (width \S+\s+)?(depth \S+\s+)?(height \S+\s+)?(depth \S+\s+)?', '', p)
        p = re.sub(r'\\[vh]rule', '', p)

        # catches...
        p = re.sub(r'\\[cpn]atch(\[\d+pt\])?{[-A-Za-zéæÆ:;,.‘’“?!()\]*— ]+}', r'\\break', p)
        p = re.sub(r'\\rightline{[-A-Za-zé:;,.’“ ]{,9}}', r'\\break', p)

        # make sticks into breaks
        p = unstick(p)

        # join broken lines with care
        p = re.sub(r'(\w)-\\break “\s+', r'\1', p) 
        p = re.sub(r'\\break “\s+', ' ', p)

        p = re.sub(r'(\w)-\\break\s+', r'\1', p) 
        p = re.sub(r'\\break\s*', ' ', p)

        # remaining rightlines need the content
        p = unbox('rightline', p)

        # remove remaining {} groups
        p = p.replace('{', ' ').replace('}', ' ')

        # regularize the spaces
        p = ' '.join(p.split())

        # remove any remaining hyphenated words
        p = re.sub(r'([a-z])- ([a-z])', r'\1\2', p)
        p = re.sub(r'([a-z])- “ ([a-z])', r'\1\2', p)
        p = re.sub(r'([a-z])- ([A-Z])', r'\1-\2', p)  # retain - in Hobby-Horse...
        # note the "move- -ment" in Vol 4
        if p.startswith('ODE'):
            p = p.replace('move- - ment', 'movement')

        if p:
            print(textwrap.fill(p))
            print()

