## i want the user to be able to provide an expected language to search for
## so here is the list of available ones that tesseract can be installed with:
#( https://github.com/tesseract-ocr/tesseract/blob/master/doc/tesseract.1.asc )
def get_languages_help_text():
    return "afr (Afrikaans) \n \
amh (Amharic) \n \
ara (Arabic) \n \
asm (Assamese) \n \
aze (Azerbaijani) \n \
aze_cyrl (Azerbaijani - Cyrilic) \n \
bel (Belarusian) \n \
ben (Bengali) \n \
bod (Tibetan) \n \
bos (Bosnian) \n \
bre (Breton) \n \
bul (Bulgarian) \n \
cat (Catalan; Valencian) \n \
ceb (Cebuano) \n \
ces (Czech) \n \
chi_sim (Chinese - Simplified) \n \
chi_tra (Chinese - Traditional) \n \
chr (Cherokee) \n \
cym (Welsh) \n \
dan (Danish) \n \
deu (German) \n \
dzo (Dzongkha) \n \
ell (Greek \n \
Modern (1453-)) \n \
eng (English) \n \
enm (English \n \
Middle (1100-1500)) \n \
epo (Esperanto) \n \
equ (Math / equation detection module) \n \
est (Estonian) \n \
eus (Basque) \n \
fas (Persian) \n \
fin (Finnish) \n \
fra (French) \n \
frk (Frankish) \n \
frm (French \n \
Middle (ca.1400-1600)) \n \
gle (Irish) \n \
glg (Galician) \n \
grc (Greek \n \
Ancient (to 1453)) \n \
guj (Gujarati) \n \
hat (Haitian; Haitian Creole) \n \
heb (Hebrew) \n \
hin (Hindi) \n \
hrv (Croatian) \n \
hun (Hungarian) \n \
iku (Inuktitut) ind (Indonesian) \n \
isl (Icelandic) \n \
ita (Italian) \n \
ita_old (Italian - Old) \n \
jav (Javanese) \n \
jpn (Japanese) \n \
kan (Kannada) \n \
kat (Georgian) \n \
kat_old (Georgian - Old) \n \
kaz (Kazakh) \n \
khm (Central Khmer) \n \
kir (Kirghiz; Kyrgyz) \n \
kor (Korean) \n \
kor_vert (Korean (vertical)) \n \
kur (Kurdish) \n \
kur_ara (Kurdish (Arabic)) \n \
lao (Lao) \n \
lat (Latin) \n \
lav (Latvian) \n \
lit (Lithuanian) \n \
ltz (Luxembourgish) \n \
mal (Malayalam) \n \
mar (Marathi) \n \
mkd (Macedonian) \n \
mlt (Maltese) \n \
mon (Mongolian) \n \
mri (Maori) \n \
msa (Malay) \n \
mya (Burmese) \n \
nep (Nepali) \n \
nld (Dutch; Flemish) \n \
nor (Norwegian) \n \
oci (Occitan (post 1500)) \n \
ori (Oriya) \n \
osd (Orientation and script detection module) \n \
pan (Panjabi; Punjabi) \n \
pol (Polish) \n \
por (Portuguese) \n \
pus (Pushto; Pashto) \n \
que (Quechua) \n \
ron (Romanian; Moldavian; Moldovan) \n \
rus (Russian) \n \
san (Sanskrit) \n \
sin (Sinhala; Sinhalese) \n \
slk (Slovak) \n \
slv (Slovenian) \n \
snd (Sindhi) \n \
spa (Spanish; Castilian) \n \
spa_old (Spanish; Castilian - Old) \n \
sqi (Albanian) \n \
srp (Serbian) \n \
srp_latn (Serbian - Latin) \n \
sun (Sundanese) \n \
swa (Swahili) \n \
swe (Swedish) \n \
syr (Syriac) \n \
tam (Tamil) \n \
tat (Tatar) \n \
tel (Telugu) \n \
tgk (Tajik) \n \
tgl (Tagalog) \n \
tha (Thai) \n \
tir (Tigrinya) \n \
ton (Tonga) \n \
tur (Turkish) \n \
uig (Uighur; Uyghur) \n \
ukr (Ukrainian) \n \
urd (Urdu) \n \
uzb (Uzbek) \n \
uzb_cyrl (Uzbek - Cyrilic) \n \
vie (Vietnamese) \n \
yid (Yiddish) \n \
yor (Yoruba)"
