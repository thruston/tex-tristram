# tex-tristram

This project is an attempt to produce an accurate and useable unannotated
text of Laurence Sterne's "Tristram Shandy" for general reading or study.

Part of the joy of the original work is that each of the nine volumes is a
work of art in itself, and that the pagination, the decorations, and even in
some cases the hyphenation of the lines are all meaningful.  

This project therefore presents the text in nine separate PDF files,
designed to be read in a PDF viewer that allows you to see two pages at
once, like an open book.  Each page break faithfully follows the page breaks
in the originals, and the text includes all the dashes, asterisks, blanks, and
catch-words.

The spelling and punctuation is all Sterne's (as far as human proof-reading
can be sure), but the medial long-s characters are replaced with modern
ones.  The font used is Linux Libertine, with historical swash ligatures
for ct and st.

The text is derived from the Project Gutenberg source for Sterne's work,
carefully corrected by hand using scanned copies of the real first edition
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

I have not attempted to mark every variation of spelling -- only those where
the mis-spelled word is obviously wrong -- one source to check these is
Johnson's Dictionary (available online) which came out in 1755.  I've also
ignored the more or less random variation between -ic and -ick suffixes, and
the "grocer's apostrophes" that abound -- with the exception of "it's" which
occurs exclusively (but not consistently) in Vol. VII and Vol. VIII

### Vol. I - 1760 Dodsley

- p.16, last line  "ate very" --> "at every"
- p.20, lines 7,8  "left it, seems," --> "left, it seems,"
- p.27, at the bottom -- catch-word "form," has unwanted comma ","
- p.65, 2nd from bottom   "enew" --> "enow" ?
- p.151, lines 1,2  "irresistable" --> "irresistible" ? 

### Vol. II - 1760 Dodsley

- Nothing obviously wrong in this volume.

### Vol. III - 1761 Dodsley

- p.9, first letter of catch-word has slipped
- p.19, third para.    "-- Brother Toby, quoth my uncle," --> "my father"
- p.28, line 5         "swiming" --> "swimming"
- p.86, line 3         "Agalastes" --> "Agelastes" which means "Unsmiling"
- p.110, lines 7,8     "elegant" --> "eloquent" ?
- p.117, line 10       "fitst" --> "first"
- p.123, line 11       "would laid down" --> "would have laid down"
- p.138, second para.  "brothet" --> "brother"
- p.138, catch word    Catch has "CHAP," instead of "CHAP."
- p.144, line 15       "or" --> "nor" (maybe?)
- p.160, line 10       "chattles" --> "chattels" (as elsewhere)
- p.168, lines 11,12   "unraval" --> "unravel" (as elsewhere)
- p.171, line 3        closing quote is single ’ instead of double ”
- p.171, line 5        "analitical" --> "analytical" (maybe?)
- p.190, line 9        "swiming" --> "swimming"
- p.191, line 5        closing paren is in italic font

### Vol. IV - 1761 Dodsley

- p.21, line 17        "never tell I am got" --> "never till I am got"
- p.36, line 16        The first "n" in "consequences" is inverted
- p.45, line 7 of fn   "seclestissima" --> "scelestissima"
- p.46, line 8         first letter of line has slipped down
- p.46, line 15        two digits missing before "83" -- apparently 14?
- p.56, line 18        first letter of line has slipped down
- p.67, line 4 of Ode  "move-/-ment" has an extra hyphen
- p.73, line 3         "facy" --> "fancy"
- p.94, line 4         "anew" --> "enow" ? compare to Vol. I.
- p.107, line 19       "I perceive shall" --> "I perceive I shall"
- p.113, line 13       "favorite" --> "favourite" (as elsewhere)
- p.118, line 21       closing paren is italic font
- p.143, line 5        first letter of line has slipped down
- p.201, line 1        "said" --> "sad" (maybe??, also the catch word)
- p.203, line 11       "to'ther" --> "t'other"
- p.208, line 19       opening paren is in italic font

### Vol. V - 1762 Becket

- p.33, line 2      Missing closing paren after "suspicions."
- p.33, line 5      Missing "it" after "may"
- p.70, catch-word  Unwanted space in "le scence."
- p.109, line 21    "πρώτισα" --> "πρώτιστα"
- p.117, line 15    "it's" --> "its"
- p.127, line 1,2   "Jerico" --> "Jericho"
- p.146, line 7     "Yo do?" --> "You do?"

### Vol. VI - 1762 Becket

- p.8, line 10   "anodines" --> "anodynes" (maybe ?)
- p.19, line 15  "neither" --> "either" (sense is positive)
- p.38, line 5   "Derdermond" --> "Dendermond"
- p.152, line 3  "vegitable" --> "vegetable"

### Vol. VII - 1765 Becket

The scanned edition used includes a list of Errata at the start, discussed below.

- Titlepage     "Dehont" --> "Dehondt" ???
- p.14, lines 6 and 16  "it’s" --> "its"
- p.19, line 18    "enterance" --> "entrance"

- p.33, last line  - This is the first erratum in the edition, which says: delete "and".
                   But that does not really help!  Better to change "e’er" --> "ere"

- p.65, line 1    diarrhaea --> diarrhoea (wrong ligature type chosen)

- p.71, line 3  - This is the second erratum -- "striking" --> "sticking"

- p.83, line 1  "Andouillets" --> "Andoüillets" 
- p.85, line 7  "Andouillets" --> "Andoüillets" 
- p.86, line 14  "Andouillets" --> "Andoüillets"  

  That these three are all in signature "G" (pp 81--96) perhaps suggests
  that the typesetter did not have (or ignored) the diacritic ü character 
  when "G" was being composed.

- p.94, line 1   "it’s" --> "its"
- p.104 line 10  "Cotê" --> "Côte"
- p.105 line 9   "Andoüillet’s" --> "Andoüillets’s" ??
- p.110 line 13  "Jesuists" --> "Jesuits"
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
- p.18 last line "run-"  --> "runn-" -- doubled "n" lost at page break

- p.34 line 13  "inflamgatory" --> "inflammatory" -- This is the third 
  erratum from the list at the start of Vol. VII

- p.47, line 8   "it’s" --> "its"
- p.48, line 16   "it’s" --> "its"
- p.51, last line  "it’s" --> "its"
- p.83, line 17  "it’s" --> "its"
- p.112, catch-word  "--There" --> "--there" (or possibly line 1 of p.113 should be "--There")
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
- p.99, line 14         The "u" in "Garagantua" has been inverted
- p.100, last line      Missing catch-word ?

