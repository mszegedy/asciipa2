# __init__.py
# part of asciipa2
# supports Python 3.7+
# Maria Szegedy, 2022
# no rights reserved

import re
from . import consts

def compile(s):
    compiled = []
    for matches in consts.TOKEN_MATCHER.finditer(s):
        match = matches.group(1)
        if match:
            compiled.append(match)
            continue
        match = matches.group(2)
        if match:
            compiled.append(consts.MAIN_DICT[match])
            continue
        match = matches.group(3)
        if match:
            compiled.append(re.sub(
                r'(' + consts.TONE_LETTER_RE_STRING + r')',
                lambda mo: consts.TONE_LETTER_DICT[mo.group(1)],
                match
            ))
            continue
        match = matches.group(5)
        if match:
            compiled.append(consts.DELIMITED_DICT[match])
            continue
        match = matches.group(6)
        if match:
            compiled.append(re.sub(
                r'(' + consts.DELIMITED_RE_STRING + r')',
                lambda mo: consts.DELIMITED_DICT[mo.group(1)],
                match
            ))
            continue
        compiled.append(matches.group(8))
    return consts.REWRITE_MATCHER.sub(
        lambda mo: consts.REWRITE_DICT[mo.group(1)],
        ''.join(compiled))
