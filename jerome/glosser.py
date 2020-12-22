import typing as t  # noqa: E902

from jerome import k
from jerome.keeper import KeepCase

PRINTABLE = k.PRINTABLE
MARK_CASE = KeepCase['GLOSS']


def get_gloss_mark() -> str:
    if (mark := k.filter_kept(MARK_CASE)):
        return list(mark.keys())[0]
    else:
        mark = next(k)
        k.keep(mark, MARK_CASE)
        return mark


def degloss(s: str) -> t.Tuple[str, str]:
    mark = get_gloss_mark()
    g = mark
    o = ""
    for c in s:
        if c in PRINTABLE:
            o += c
        else:
            g += c
            o += mark
    return (o, g)


def gloss(s: str, gloss: str) -> str:
    g = gloss[0]
    i = 1
    o = ""
    for c in s:
        if c == g:
            o += gloss[i]
            i += 1
        else:
            o += c
    return o
