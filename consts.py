# consts.py
# part of asciipa2
# supports Python 3.7+
# Maria Szegedy, 2022
# no rights reserved

import re
from collections import OrderedDict

def re_string_from_keys(d):
    return '|'.join(re.escape(x) for x in d.keys())


# first pass

MAIN_DICT = OrderedDict((
    ('ph',   'ɸ'),
    ('bh',   'ϐ'),
    ('mm',   'ɱ'),
    ('vv',   'ⱱ'),
    ('v*',   'ʋ'),
    ('4',    'ɾ'),
    ('th',   'ϑ'),
    ('dh',   'ð'),
    ('&',    'ɬ'),
    ('lZ',   'ɮ'),
    ('r*',   'ɹ'),
    ('S',    'ʃ'),
    ('Z',    'ʒ'),
    ('t;',   'ʈ'),
    ('d;',   'ɖ'),
    ('n;',   'ɳ'),
    ('4;',   'ɽ'),
    ('s;',   'ʂ'),
    ('z;',   'ʐ'),
    ('r;',   'ɻ'),
    ('l;',   'ɭ'),
    ('d^',   'ɟ'),
    ('n^',   'ɲ'),
    ('s^',   'ç'),
    ('z^',   'ʝ'),
    ('l^',   'ʎ'),
    ('ng',   'ŋ'),
    ('gh',   'ɣ'),
    ('u*',   'ɰ'),
    ('L',    'ʟ'),
    ('G',    'ɢ'),
    ('N',    'ɴ'),
    ('R',    'ʀ'),
    ('X',    'χ'),
    ('Gh',   'ʁ'),
    ('hh',   'ħ'),
    ('3',    'ʕ'),
    ('h*',   'ɦ'),
    ('00',   'ʘ'),
    ('--',   'ǀ'),
    ('!',    'ǃ'),
    ('++',   'ǂ'),
    ('==',   'ǁ'),
    ('K',    'ʞ'),
    ('b?',   'ɓ'),
    ('d?',   'ɗ'),
    ('d^?',  'ʄ'),
    ('g?',   'ɠ'),
    ('G?',   'ʛ'),
    ('pph',  'p͡ɸ'),
    ('bbh',  'b͡β'),
    ('ts',   't͡s'),
    ('dz',   'd͡z'),
    ('tS',   't͡ʃ'),
    ('dZ',   'd͡ʒ'),
    ('tsh',  't͡ɕ'),
    ('dzh',  'd͡ʑ'),
    ('cs^',  'c͡ç'),
    ('dz^',  'ɟ͡ʝ'),
    ('t&',   't͡ɬ'),
    ('dlZ',  'd͡ɮ'),
    ('kx',   'k͡x'),
    ('ggh',  'g͡ɣ'),
    ('qX',   'q͡χ'),
    ('GGh',  'ɢ͡ʁ'),
    ('%',    'ø'),
    ('E',    'ɛ'),
    ('oe',   'œ'),
    ('ae',   'æ'),
    ('OE',   'ɶ'),
    ('I',    'ɪ'),
    ('Y',    'ʏ'),
    ('i@',   'ɨ'),
    ('u@',   'ʉ'),
    ('e@',   'ɘ'),
    ('o@',   'ɵ'),
    ('@',    'ə'),
    ('@e',   'ɜ'),
    ('@o',   'ʚ'),
    ('9',    'ɐ'),
    ('uu',   'ɯ'),
    ('6',    'ɤ'),
    ('7',    'ʌ'),
    ('O',    'ɔ'),
    ('aa',   'ɑ'),
    ('ao',   'ɒ'),
    ('wh',   'ʍ'),
    ('yy',   'ɥ'),
    ('H',    'ʜ'),
    ('33',   'ʢ'),
    ('??',   'ʡ'),
    ('sh',   'ɕ'),
    ('zh',   'ʑ'),
    ('44',   'ɺ'),
    ('SJH',  'ɧ'),
    ('()',   '∅'),
    ('(^)',  '͡'),
    ('(_)',  '͜'),
    ('1',    'ˈ'),
    ('2',    'ˌ'),
    ('.:.',  '|'),
    ('.::.', '‖'),
    (':',    'ː'),
    (',,',   'ˑ'),
    ('..',   'ʼ'),
    ('(-+)', '˔'),
    ('(+-)', '˕'),
    ('__',   '_'),
    ('0',    '̥'),
    ('=',    '̩'),
    ('<',    '̯'),
    ('~',    '̃'),
    ('>',    '̚'),
    ('-+',   '̝'),
    ('+-',   '̞'),
    ('^_',   '↘︎'),
    ('_^',   '↗︎'),
    ('<<',   'ꜛ'),
    ('>>',   'ꜜ'),
))
MAIN_RE_STRING = re_string_from_keys(MAIN_DICT)

TONE_LETTER_DICT = OrderedDict((
    ('1', '˩'),
    ('2', '˨'),
    ('3', '˧'),
    ('4', '˦'),
    ('5', '˥'),
))
TONE_LETTER_RE_STRING = re_string_from_keys(TONE_LETTER_DICT)

DELIMITED_DICT = OrderedDict((
    ('v',  '̬'),
    ('h',  'ʰ'),
    ('h*', 'ʱ'),
    ('o',  '̹'),
    ('e',  '̜'),
    ('+',  '̟'),
    ('-',  '̠'),
    ('++', '̘'),
    ('--', '̙'),
    (':',  '̈'),
    ('::', '̽'),
    ('r',  '˞'),
    ('_:', '̤'),
    ('~',  '̰'),
    ('mm', '̼'),
    ('w',  'ʷ'),
    ('j',  'ʲ'),
    ('b',  'ᵝ'),
    ('g',  'ˠ'),
    ('3',  'ˁ'),
    ('?',  'ˀ'),
    ('<',  '̪'),
    ('>',  '̺'),
    ('#',  '̻'),
    ('m',  'ᵐ'),
    ('n',  'ⁿ'),
    ('ng', 'ᵑ'),
    ('l',  'ˡ'),
    ('s',  'ˢ'),
    ('x',  'ˣ'),
    ('X',  'ᵡ'),
    ('HH', '̋'),
    ('H',  '́'),
    ('M',  '̄'),
    ('L',  '̀'),
    ('LL', '̏'),
    ('HL', '̂'),
    ('LH', '̌'),
    ('MH', '᷄'),
    ('LM', '᷅'),
    ('ML', '᷆'),
    ('HM', '᷇'),
    ('LHL', '᷈'),
    ('HLH', '᷉'),
))
DELIMITED_RE_STRING = re_string_from_keys(DELIMITED_DICT)

TOKEN_MATCHER = re.compile(
    r'\\(.)'
    r'|(' + MAIN_RE_STRING + r')'
    r'|\(((' + TONE_LETTER_RE_STRING + r')+)\)'
    r'|_(' + DELIMITED_RE_STRING + r')'
    r'|\(((' + DELIMITED_RE_STRING + r')+)\)'
    r'|(.)'
)


# second pass

REWRITE_DICT = OrderedDict((
    ('à', 'à'),
    ('á', 'á'),
    ('â', 'â'),
    ('ã', 'ã'),
    ('ä', 'ä'),
    ('è', 'è'),
    ('é', 'é'),
    ('ê', 'ê'),
    ('ë', 'ë'),
    ('ì', 'ì'),
    ('í', 'í'),
    ('î', 'î'),
    ('ï', 'ï'),
    ('ò', 'ò'),
    ('ó', 'ó'),
    ('ô', 'ô'),
    ('õ', 'õ'),
    ('ö', 'ö'),
    ('ù', 'ù'),
    ('ú', 'ú'),
    ('û', 'û'),
    ('ü', 'ü'),
    ('ý', 'ý'),
    ('ÿ', 'ÿ'),
    ('g̥', 'g̊'),
    ('j̥', 'j̊'),
    ('p̥', 'p̊'),
    ('q̥', 'q̊'),
    ('y̥', 'ẙ'),
    ('ɣ̥', 'ɣ̊'),
    ('χ̥', 'χ̊'),
    ('ɟ̥', 'ɟ̊'),
    ('ʝ̥', 'ʝ̊'),
    ('ɥ̥', 'ɥ̊'),
    ('ʞ̥', 'ʞ̊'),
    ('ʒ̥', 'ʒ̊'),
    ('ɰ̥', 'ɰ̊'),
    ('ɱ̥', 'ɱ̊'),
    ('ɲ̥', 'ɲ̊'),
    ('ɳ̥', 'ɳ̊'),
    ('ŋ̥', 'ŋ̊'),
    ('ɻ̥', 'ɻ̊'),
    ('ɽ̥', 'ɽ̊'),
    ('ʈ̥', 'ʈ̊'),
    ('ɭ̥', 'ɭ̊'),
    ('ç̥', 'ç̊'),
    ('g̥', 'g̊'),
    ('j̥', 'j̊'),
    ('p̥', 'p̊'),
    ('q̥', 'q̊'),
    ('y̥', 'ẙ'),
    ('ɣ̥', 'ɣ̊'),
    ('χ̥', 'χ̊'),
    ('ɟ̥', 'ɟ̊'),
    ('ʝ̥', 'ʝ̊'),
    ('ɥ̥', 'ɥ̊'),
    ('ʞ̥', 'ʞ̊'),
    ('ʒ̥', 'ʒ̊'),
    ('ɰ̥', 'ɰ̊'),
    ('ɱ̥', 'ɱ̊'),
    ('ɲ̥', 'ɲ̊'),
    ('ɳ̥', 'ɳ̊'),
    ('ŋ̥', 'ŋ̊'),
    ('ɻ̥', 'ɻ̊'),
    ('ɽ̥', 'ɽ̊'),
    ('ʈ̥', 'ʈ̊'),
    ('ɭ̥', 'ɭ̊'),
    ('ç̥', 'ç̊'),
    ('ə˞', 'ɚ'),
    ('ɜ˞', 'ɝ'),
))
REWRITE_MATCHER = re.compile(
    r'(' + re_string_from_keys(REWRITE_DICT) + r')')