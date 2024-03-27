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

The spelling and punctuation is all Sterne's (as far as my
proof-reading can be sure), but the medial long-s characters are
replaced with modern ones.  The font used is Linux Libertine, with
historical swash ligatures enabled for "ct" and "st", and with the
(horrible) "Th" ligature suppressed.  Libertine looks reasonably
modern, but (apart from the italics) is not too far from the Caslon
typefaces used by Dodsley and Becket.  It has the advantage also of
being free for use.

For the occasional bits of Greek, I have used the Greek Font Society's
version of "Porson" is used.  This font dates from the early 19th 
century, so the characters are more contemporary than those Sterne's 
printers used, and (in my opinion) much much easier to read. 
I have not corrected any of the bad grammar, nor the more-or-less 
random use of accents and breathing marks.  But  I have fixed the
occasional terminal sigma in the middle of a word, and I have rendered 
the archaic letter forms some times used for  "γ", "τ", "π", into the
more usual equivalents.  Note also that the 18th century printers used 
various ligatures (for "ου" etc) that  are not available in GFS Porson.
Other than these alterations, the Greek follows the scanned first
editions as closely as possible.  So for example, on the title page
of Vol. I. the second line of the motto is given correctly as "ἀλλὰ"
but in Vol II. the same word is missing both breathing mark and
accent in the scan of the original, so I have it as "αλλα". 

The text is derived from the Project Gutenberg source for Sterne's work,
extensively corrected by hand using scanned copies of the real first edition
volumes that are available through Google Books, and listed (as of June 2023)
at [Laurence Sterne in Cyberspace](https://www1.gifu-u.ac.jp/~masaru/Sterne_on_the_Net.html).

The text is marked up with LaTeX and compiled into PDFs using the
`lualatex` engine.   I have done the proof-reading by viewing these
PDFs one page at a time, with the scanned originals loaded in
another tab.  By carefully adjusting the zoom levels, I can flick
between the two tabs and spot differences more easily.

If you find this project entertaining or useful please consider supporting
[Shandy Hall](https://www.laurencesternetrust.org.uk/join-in/donations/)
which is run as a museum and study-center in Coxwold, North Yorkshire, by
the Laurence Sterne Trust.

## Typographical accidentals, &c.

Various errors and accidents of type-setting are marked with a
marginal Ace of Clubs ♣︎ (like the poor squashed nose).  I cannot
pretend that my marks are comprehensive or complete.  If you look at
a different edition, you may spot more of them; or you may think I
have wrongly called out some of those that I have marked.  The
originals I used are the scanned copies linked above.

I have not attempted to mark variations of spelling -- only those
where the mis-spelled word is "obviously" mis-printed.  I've also
ignored the more or less random variation between -ic and -ick
suffixes, and the "grocer's apostrophes" that abound -- with the
exception of "it's" which occurs once in Vol. V and at random
throughout Vol. VII and Vol. VIII.  

Quite often it is impossible to distinguish mistakes from Sterne's
wit; what are we to make (for example) of the word "assimulation" on
page nine of Vol IX?  It might be a mistake, but then it might also
be a happy accident.  Or more probably learned wit.  My Latin
dictionary suggests that there was some classical confusion between
the verbs "assimilare" and "assimulare".  And Sterne uses the phrase
"electrical assimilation" (spelled thus) on page nineteen of Vol II.

### Vol. I - 1760 Dodsley (first London edition)

- p.16, last line    "ate very" --> "at every"
- p.20, lines 7,8    "left it, seems," --> "left, it seems,"
- p.27, catch word   "form," --> "form" -- following page has "form and place" with no comma
- p.35, line 16      "uudoubtedly" --> "undoubtedly", compositor confused u and n
- p.56, catch word   "folly:" --> "folly;" -- following page has semi-colon
- p.124, catch word  "He," --> "He" -- following page has no comma
- p.144, line 8      opening paren in roman, but closing in italic type
- p.166, line 9      "ofter" --> "after", compositor confused o and a
- p.170, line 16     "his own" --> "their own", Sterne's revision error?

# Vol. II - 1760 Dodsley (first London edition)

- p.30, catch word   "crutch," --> "crutch" -- stray comma on catch word
- p.39, line 6       opening paren in roman, but closing in italic type
- p.50, catch word   "“Not" --> "––“Not" -- following page has leading dash
- p.64, line 15      opening paren in italic, but closing in roman type
- p.75, line 2       "aliks" --> "alike", compositor confused s and e
- p.78, line 5       "fifth" --> "second" - Sterne's revision error?
- p.103, line 15     "ours." --> "ours," - or perhaps just no stop?
- p.150, line 15     opening paren in roman, but closing in italic type
- p.154, line 15     "male-treat" --> "mal-treat" - corrected in later eds
- p.169, line 8      opening paren in roman, but closing in italic type
- p.177, line 7      "pref-" --> "pres-", compositor confused f and long-s (but might just be a mark on the scanned copy)
- p.182, line 7      "Alquise" --> "Alquife", compositor confused long-s and f

### Vol. III - 1761 Dodsley

- p.5, 2nd last line   "quoth" should not be in italics
- p.18, line 8         "Avison" --> "Avison's" - i.e. his edition
- p.19, third para.    "my uncle" --> "my father"
- p.39, catch word     "the" --> "“ the", leading quotation marks missing from catch
- p.46, line 1         closing paren should have been a comma
- p.51, line 5         opening paren in roman, but closing in italic type
- p.55, line 5         unwanted space in "Hamet"
- p.70, catch word     Catch is set to the right of the margin
- p.72, line 15        unwanted , before ; 
- p.81, line 15        unwanted space in "regions"
- p.86, line 3         "Agalastes" --> "Agelastes" - Sterne's error here?
- p.88, line 16        "these veral" --> "the several"
- p.94, line 10        "your" --> "you"
- p.99. line 14, 15    final "a" repeated on next line
- p.99. line 16, 17    final "the" repeated on next line
- p.100, line 20       "catchesing" --> "catching", apparently Sterne's error?
- p.110, lines 7,8     "elegant" --> "eloquent", Sterne's error?
- p.112, line 10       "his parlour" --> "the parlour", Sterne's error?
- p.117, line 10       "fitst" --> "first"
- p.123, line 11       "would laid down" --> "would have laid down"
- p.138, second para.  "brothet" --> "brother"
- p.138, catch word    Catch has "CHAP," instead of "CHAP."
- p.144, line 15       "or" --> "nor" (maybe?)
- p.157, line 9        unwanted space at beginning of line
- p.164, line 12       "Bruscumbilles" --> "Bruscambilles", comp confused italic a and u ? (or stall-man gets it wrong?)
- p.167, line 18       opening paren in italic, but closing in roman type
- p.171, line 1        "poenitet" --> "paenitet", comp confused ae and oe ligatures
- p.171, line 3        closing quote is single ’ instead of double ”
- p.171, line 4        "poeniteat" --> "paeniteat", comp confused ae and oe ligatures
- p.177, line 12       "dialectially" --> "dialectically", comp missed "c"
- p.191, line 5        closing paren is in italic font

### Vol. IV - 1761 Dodsley

- p.3, line 8          "entred" --> "entered" (as two lines later...)
- p.8, line 4          "titigimus" -> "tetigimus" 
- p.19, catch word     "’Tis" --> "There’s" -- catch matches 2nd para not first on p.21
- p.20, line 11        "perveneo" -> "pervenio" 
- p.21, line 17        "never tell I am got" --> "never till I am got"
- p.30, line 7         opening paren in roman, but closing in italic type
- p.35, line 7         opening paren in roman, but closing in italic type
- p.36, line 16        "cousequences" -> "consequeneces", compositor confused u and n
- p.45, line 2 of fn   "Scarpio" -> "Scorpio"
- p.45, line 7 of fn   "seclestissima" --> "scelestissima"
- p.46, line 8         first letter of line has slipped down
- p.46, line 15        two digits missing before "83" -- apparently 14?
- p.51, line 12        "cannot" -->  "can", Sterne's error? (sense requires positive) 
- p.56, line 12        opening paren in roman, but closing in italic type
- p.56, line 17        "Epistasis" --> "Epitasis" -- correct on next page
- p.56, line 18        first letter of line has slipped down
- p.67, line 4 of Ode  "move-/-ment" has an extra hyphen
- p.73, line 3         "facy" --> "fancy"
- p.80, line 1         opening paren in roman, but closing in italic type
- p.94, line 4         "anew" --> "enow" ? or "enew" as in Vol. I. ?
- p.96, line 14        "?" --> "!"  (maybe...)
- p.107, line 19       "I perceive shall" --> "I perceive I shall"
- p.118, line 21       closing paren is italic font
- p.128, catch word    "Or" --> "--Or", dash is missing in catch word
- p.139, line 1        Footnote asterisk (apparently) missing from text
- p.143, line 5        first letter of line has slipped down
- p.175, line 10       "its accord" -> "its own accord"
- p.201, line 1        "said" --> "sad" (maybe?, also the catch word)
- p.203, line 11       "to'ther" --> "t'other"
- p.208, line 19       opening paren is in italic font

### Vol. V - 1762 Becket

- p.30, line 10     opening paren in roman, but closing in italic type
- p.33, line 2      Missing closing paren after "suspicions."
- p.33, line 5      Missing "it" after "may"
- p.52, line 10     opening paren in italic, but closing in roman type
- p.63, line 5      opening paren in roman, but closing in italic type
- p.70, line 16     "Tristra-pœdia" --> "Tristra-pædia", compositor confused oe and ae ligatures
- p.70, catch-word  Unwanted space in "le scence."
- p.73, line 10     opening paren in roman, but closing in italic type
- p.79, line 10     opening paren in italic, but closing in roman type
- p.101, line 17    "Pharoah" --> "Pharaoh" -- Sterne's error?”
- p.106, line 10    no matching closing paren
- p.109, line 15    opening paren in roman, but closing in italic type    
- p.109, line 21    "πρώτισα" --> "πρώτιστα" (possibly Sterne's mistake)
- p.112, line 16    opening paren in roman, but closing in italic type
- p.117, line 15    "it's" --> "its"
- p.127, line 1,2   "Jerico" --> "Jericho"
- p.139, line 17    "Tristra-pœdia" --> "Tristra-pædia", compositor confused oe and ae ligatures
- p.146, line 7     "Yo do?" --> "You do?"

### Vol. VI - 1762 Becket

- p.6, line 4       "know-lege" --> "know-ledge" (apparently a typo in Vol VI)
- p.15, line 8      opening paren in roman, but closing in italic type
- p.19, line 15     "neither" --> "either" (sense is positive)
- p.20, catch word  catch word not aligned to margin
- p.38, line 5      "Derdermond" --> "Dendermond"
- p.45, line 15     "wishfully" --> "wistfully", comp confused "sh" and "st" ligatures ?
- p.47, line 20     "knowlege" --> "knowledge" 
- p.47, line 10     "know-lege" --> "know-ledge" 
- p.132, line 16    "diligentias" --> "diligentius", Sterne's error copying from Burton?

### Vol. VII - 1765 Becket

The scanned edition used includes a list of Errata at the start, discussed below.

- Titlepage      "Dehont" --> "Dehondt" ???
- p.5, line 6    Missing opening paren before "holding"
- p.14, line 6   "it’s" --> "its"
- p.14, line 16  "it’s" --> "its"

- p.33, last line  - This is the first erratum in the edition, which says: delete "and".
                   But that does not really help!  
                   Perhaps change "e’er" (ever) --> "ere" (meaning before)

- p.43, line 6   opening paren in italic, but closing in roman type
- p.71, line 3   This is the second erratum -- "striking" --> "sticking"

- p.83, line 1   "Andouillets" --> "Andoüillets"
- p.85, line 7   "Andouillets" --> "Andoüillets"
- p.85, line 9   "then" -->"than"
- p.86, line 14  "Andouillets" --> "Andoüillets"

  That these three are all in signature "G" (pp 81--96) perhaps suggests
  that the typesetter did not have (or ignored) the diacritic ü character 
  when "G" was being composed.

- p.94, line 1      "it’s" --> "its"
- p.104 line 10     "Cotê roti" --> Côte-Rôtie" (possibly Sterne? perhaps comic?)
- p.105 line 9      "Andoüillet’s" --> "Andoüillets’s" ??
- p.110 line 13     "Jesuists" --> "Jesuits"
- p.116 line 19     quotation marks from line 12 never closed
- p.123 line 14     "Andoüillet’s" --> "Andoüillets’s" ??
- p.125 line 1      Chapter number jumps from XXXII to XXXIV
- p.127 line 2      "Avignion" --> "Avignon"
- p.128 catch word  "And" --> "--And", leading dash is missing
- p.132 line 15     "Avignion" --> "Avignon"
- p.142, line 1     "it’s" --> "its"
- p.142, catch word  "For" should be in italics to match next page
- p.145 line 3      "Avignion" --> "Avignon"
- p.146 thrice      "Avignion" --> "Avignon"  (and once correctly on the same page)
- p.147 line 4      "Avignion" --> "Avignon"
- p.148 line 5      "the lord" --> "the Lord", probably, given the "He" on the next line.
- p.151 line 16     repeated "of" at end of line 15

  The seven uses of "Avignion" outnumber the three uses of "Avignon".

### Vol. VIII - 1765 Becket

- Titlepage        "Dehont" --> "Dehondt" ???
- p.11 line 5      "so see" --> "to see"
- p.12 last line   quotation marks never closed
- p.18 last line   "run-ing" --> "run-ning" doubled "n" lost at page break
- p.34 line 13     "inflamgatory" --> "inflammatory" -- This is the third
-                  erratum from the list at the start of Vol. VII
- p.35 line 5      second line is indented instead of flush to LH margin
- p.47, line 8     "it’s" --> "its"
- p.48, line 16    "it’s" --> "its"
- p.51, last line  "it’s" --> "its"
- p.83, line 17    "it’s" --> "its"
- p.85, line 11    "Its" --> "It’s" (this error is the other way round)
- p.111, line 16   "incidesset" --> "incidisset", Sterne's error copying from Burton?
- p.113, line 1    "--there" --> "--There" (to match the catch word)
- p.117, line 5    "fefell" --> "befell"
- p.131, line 5    final "the" repeated on next line
- p.143, line 15   "it’s" --> "its"
- p.156, line 6    "it’s" --> "its"

The "it's" (which are never correct) are mainly in Vol VII and VIII

    Vol    its  it's
    ----------------
    I       13     0   Dodsley 1760
    II      24     0   Dodsley 1760
    III     22     0   Dodsley 1761
    IV      24     0   Dodsley 1761
    V       15     1   Becket 1762
    VI      19     0   Becket 1762
    VII     16     4   Becket 1765
    VIII    13     6   Becket 1765
    IX      13     0   Becket 1767
    ----------------
    Total  159    11

Sterne's usual abbreviation for "it is" is "’tis" (400 occurrences).
Uncle Toby does once say (Vol VIII, p.85) "It's high time I should [hear Trim's story].
Unfortunately the setter has this as "Its high time I should", as noted above.


### Vol. IX - 1767 Becket

- 2nd page of Dedication, line 1  "riori" --> "ori" -- extra "ri" carried over in page break
- p.9, line 10          "assimulated" --> "assimilated", but possibly Sterne's choice of spelling here
- p.11, line 18         "Le Fevre's" --> "Le Fever's" -- perhaps? (to match in previous volumes)
- p.17, after flourish  Missing catch-word "A"
- p.22, line 3         "Le Fevre's" --> "Le Fever's" -- as above, the only occurrences in Vol. IX
- p.59, line 3          final "e" in the line has slipped
- p.90, line 14         "been" --> "had been" (word dropped at line break)
- p.99, line 14         "Garagantna" --> "Garagantua" (compositor confused u and n)
- p.100, last line      Missing catch-word -- "The", perhaps in Blackletter type?
- p.140, line 2         opening paren in roman, but closing in italic type

