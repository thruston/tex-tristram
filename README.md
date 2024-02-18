# tex-tristram

This project is an attempt to produce an accurate and useable unannotated
text of Laurence Sterne's "Tristram Shandy" for general reading or study.

Part of the joy of the original work is that each of the nine volumes is a
work of art in itself, and that the pagination, the decorations, and even in
some cases the hyphenation of the lines are all meaningful.  

This project therefore presents the text in nine separate PDF files, designed
to be read in a PDF viewer that allows you to see two pages at once, like an
open book.  Each page faithfully follows the line and page breaks in the
originals, and the text includes all the dashes, asterisks, blanks, and
catch-words.

The spelling and punctuation is all Sterne's (as far as human proof-reading can
be sure), but the medial long-s characters are replaced with modern ones.  The
font used is Linux Libertine, with historical swash ligatures for ct and st.

The same font is used for the occasional bits of Greek so the characters are
slightly more contemporary than Sterne's printers used; I have not attempted to
correct any of the (appallingly bad) grammar nor the slightly random accents
and breathing marks, nor the occasional terminal sigma in the middle of a
word, etc, but I have rendered the archaic letter forms used for "γ", "τ",
"π","ου" etc into modern equivalents. 

The text is derived from the Project Gutenberg source for Sterne's work,
extensively corrected by hand using scanned copies of the real first edition
volumes that are available through Google Books, and listed (as of June 2023)
at [Laurence Sterne in Cyberspace](https://www1.gifu-u.ac.jp/~masaru/Sterne_on_the_Net.html).

The text is marked up with LaTeX and compiled into PDFs using the
`lualatex` engine.

If you find this project entertaining or useful please consider supporting
[Shandy Hall](https://www.laurencesternetrust.org.uk/join-in/donations/)
which is run as a museum and study-center in Coxwold, North Yorkshire, by
the Laurence Sterne Trust.

## Typographical accidentals

Accidents of type-setting are marked with a marginal Ace of Clubs ♣︎ (like the
poor squashed nose).  I cannot pretend that my marks are comprehensive or
complete.  If you look at a different edition, you may spot more of them; or
you may think I have wrongly called out some of those that I have marked.  The
originals I used are the scanned copies linked above.

I have not attempted to mark variations of spelling -- only those where the
mis-spelled word is apparently mis-printed.  I've also ignored the more or less
random variation between -ic and -ick suffixes, and the "grocer's apostrophes"
that abound -- with the exception of "it's" which occurs once in Vol. V and at
random throughout Vol. VII and Vol. VIII

### Vol. I - 1760 Dodsley (first London edition)

- p.16, last line  "ate very" --> "at every"
- p.20, lines 7,8  "left it, seems," --> "left, it seems,"
- p.28, line 1     "form" --> "form," to match the comma on the previous catch word
- p.35, line 16    "uudoubtedly" --> "undoubtedly", compositor confused u and n
- p.57, line 1     "folly;" but previous catch-word has "folly:" (colon for semicolon)
- p.144, line 8    opening paren in roman, but closing in italic type
- p.166, line 9    "ofter" --> "after", compositor confused o and a
- p.170, line 16   "his own" --> "their own", Sterne's revision error?

### Vol. II - 1760 Dodsley (first London edition)

- p.39, line 6    opening paren in roman, but closing in italic type
- p.64, line 15   opening paren in italic, but closing in roman type
- p.75, line 2    "aliks" --> "alike", compositor confused s and e
- p.78, line 5    "fifth" --> "second" - Sterne's revision error?
- p.150, line 15  opening paren in roman, but closing in italic type
- p.169, line 8   opening paren in roman, but closing in italic type
- p.177, line 7   "pref-" --> "pres-", compositor confused f and long-s
- p.182, line 7   "Alquise" --> "Alquife", compositor confused long-s and f

### Vol. III - 1761 Dodsley

- p.5, 2nd last line   "quoth" should not be in italics
- p.19, third para.    "my uncle" --> "my father"
- p.46, line 1         closing paren should have been a comma
- p.51, line 5         opening paren in roman, but closing in italic type
- p.55, line 5         unwanted space in "Hamet"
- p.70, catch word     Catch is set to the right of the margin
- p.72, line 15        unwanted , before ; 
- p.81, line 15        unwanted space in "regions"
- p.86, line 3         "Agalastes" --> "Agelastes" - Sterne's error here?
- p.94, line 10        "your" --> "you"
- p.99. line 14, 15    final "a" repeated on next line
- p.99. line 16, 17    final "the" repeated on next line
- p.110, lines 7,8     "elegant" --> "eloquent" ?
- p.117, line 10       "fitst" --> "first"
- p.123, line 11       "would laid down" --> "would have laid down"
- p.138, second para.  "brothet" --> "brother"
- p.138, catch word    Catch has "CHAP," instead of "CHAP."
- p.144, line 15       "or" --> "nor" (maybe?)
- p.167, line 18       opening paren in italic, but closing in roman type
- p.171, line 1        "poenitet" --> "paenitet", comp confused ae and oe ligatures
- p.171, line 3        closing quote is single ’ instead of double ”
- p.171, line 4        "poeniteat" --> "paeniteat", comp confused ae and oe ligatures
- p.177, line 12       "dialectially" --> "dialectically", comp missed "c"
- p.191, line 5        closing paren is in italic font

### Vol. IV - 1761 Dodsley

- p.3, line 8          "entred" --> "entered" (as two lines later...)
- p.8, line 4          "titigimus" -> "tetigimus" 
- p.20, line 11        "perveneo" -> "pervenio" 
- p.21, line 17        "never tell I am got" --> "never till I am got"
- p.30, line 7         opening paren in roman, but closing in italic type
- p.35, line 7         opening paren in roman, but closing in italic type
- p.36, line 16        "cousequences" -> "consequeneces", compositor confused u and n
- p.45, line 2 of fn   "Scarpio" -> "Scorpio"
- p.45, line 7 of fn   "seclestissima" --> "scelestissima"
- p.46, line 8         first letter of line has slipped down
- p.46, line 15        two digits missing before "83" -- apparently 14?
- p.56, line 12        opening paren in roman, but closing in italic type
- p.56, line 17        "Epistasis" --> "Epitasis" -- Sterne's error? (correct on p.57)
- p.56, line 18        first letter of line has slipped down
- p.67, line 4 of Ode  "move-/-ment" has an extra hyphen
- p.73, line 3         "facy" --> "fancy"
- p.80, line 1         opening paren in roman, but closing in italic type
- p.94, line 4         "anew" --> "enow" ? or "enew" as in Vol. I. ?
- p.96, line 14        "?" --> "!"  (maybe...)
- p.107, line 19       "I perceive shall" --> "I perceive I shall"
- p.118, line 21       closing paren is italic font
- p.139, line 1        Footnote asterisk (apparently) missing from text
- p.143, line 5        first letter of line has slipped down
- p.175, line 10       "its accord" -> "its own accord"
- p.201, line 1        "said" --> "sad" (maybe?, also the catch word)
- p.203, line 11       "to'ther" --> "t'other"
- p.208, line 19       opening paren is in italic font

### Vol. V - 1762 Becket

- p.33, line 2      Missing closing paren after "suspicions."
- p.33, line 5      Missing "it" after "may"
- p.70, line 16     "Tristra-pœdia" --> "Tristra-pædia", compositor confused oe and ae ligatures
- p.70, catch-word  Unwanted space in "le scence."
- p.73, line 10     opening paren in roman, but closing in italic type
- p.79, line 10     opening paren in italic, but closing in roman type
- p.106, line 10    no matching closing paren
- p.109, line 15    opening paren in roman, but closing in italic type
- p.109, line 21    "πρώτισα" --> "πρώτιστα" (possibly Sterne's mistake)
- p.112, line 16    opening paren in roman, but closing in italic type
- p.117, line 15    "it's" --> "its"
- p.127, line 1,2   "Jerico" --> "Jericho"
- p.139, line 17    "Tristra-pœdia" --> "Tristra-pædia", compositor confused oe and ae ligatures
- p.146, line 7     "Yo do?" --> "You do?"

### Vol. VI - 1762 Becket

- p.8, line 10   "anodines" --> "anodynes" (maybe ?)
- p.15, line 8    opening paren in roman, but closing in italic type
- p.19, line 15  "neither" --> "either" (sense is positive)
- p.38, line 5   "Derdermond" --> "Dendermond"
- p.47, line 20  "knowlege" --> "knowledge" 
- p.49, line 20  "knowlege" --> "knowledge" (setter is consistent at least!)
- p.152, line 3  "vegitable" --> "vegetable"

### Vol. VII - 1765 Becket

The scanned edition used includes a list of Errata at the start, discussed below.

- Titlepage      "Dehont" --> "Dehondt" ???
- p.5, line 6    Missing opening paren before "holding"
- p.14, line 6   "it’s" --> "its"
- p.14, line 16  "it’s" --> "its"

- p.33, last line  - This is the first erratum in the edition, which says: delete "and".
                   But that does not really help!  Better to change "e’er" --> "ere"

- p.71, line 3  - This is the second erratum -- "striking" --> "sticking"

- p.83, line 1  "Andouillets" --> "Andoüillets" 
- p.85, line 7  "Andouillets" --> "Andoüillets" 
- p.85, line 9  "then" -->"than"
- p.86, line 14  "Andouillets" --> "Andoüillets"  

  That these three are all in signature "G" (pp 81--96) perhaps suggests
  that the typesetter did not have (or ignored) the diacritic ü character 
  when "G" was being composed.

- p.94, line 1   "it’s" --> "its"
- p.105 line 9   "Andoüillet’s" --> "Andoüillets’s" ??
- p.110 line 13  "Jesuists" --> "Jesuits"
- p.116 line 19  quotation marks from line 12 never closed
- p.123 line 14  "Andoüillet’s" --> "Andoüillets’s" ??
- p.125 line 1   Chapter number jumps from XXXII to XXXIV
- p.127 line 2   "Avignion" --> "Avignon"
- p.132 line 15  "Avignion" --> "Avignon"
- p.142, line 1  "it’s" --> "its"
- p.145 line 3   "Avignion" --> "Avignon"
- p.146 thrice   "Avignion" --> "Avignon"
- p.147 line 4   "Avignion" --> "Avignon"
- p.151 line 16  repeated "of" at end of line 15

  The seven uses of "Avignion" outnumber the three uses of "Avignon".

### Vol. VIII - 1765 Becket

- Titlepage     "Dehont" --> "Dehondt" ???
- p.11 line 5   "so see" --> "to see"
- p.18 last line "run-ing" --> "run-ning"  doubled "n" lost at page break
- p.34 line 13  "inflamgatory" --> "inflammatory" -- This is the third 
  erratum from the list at the start of Vol. VII

- p.35 line 5    second line is indented instead of flush to LH margin
- p.47, line 8   "it’s" --> "its"
- p.48, line 16   "it’s" --> "its"
- p.51, last line  "it’s" --> "its"
- p.83, line 17  "it’s" --> "its"
- p.85, line 11  "its" --> "it’s"  (this one is the other way round!) 
- p.113, line 1  "--there" --> "--There" (to match the catch word)
- p.117, line 5   "fefell" --> "befell"
- p.131, line 5   final "the" repeated on next line
- p.143, line 15  "it’s" --> "its"
- p.156, line 6  "it’s" --> "its"

The "it's" (which are never correct) are mainly in Vol VII and VIII

    Vol   its  it's
    ---------------
    I      13     0
    II     24     0
    III    22     0
    IV     24     0
    V      15     1
    VI     19     0
    VII    16     4
    VIII   13     6
    IX     13     0


### Vol. IX - 1767 Becket

- 2nd page of Dedication, line 1  "riori" --> "ori" -- extra "ri" carried over in page break
- p.17, after flourish  Missing catch-word "A"
- p.59, line 3          final "e" in the line has slipped
- p.90, line 14         "been" --> "had been" (word dropped at line break)
- p.99, line 14         "Garagantna" --> "Garagantua" (compositor confused u and n)
- p.100, last line      Missing catch-word ? "The" in Gothic type?

