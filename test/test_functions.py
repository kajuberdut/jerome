from sys import getsizeof  # noqa: E902

import pytest
from jerome.bw.burrowswheeler import bwt, ibwt
from jerome.glosser import degloss, gloss
from jerome.runlength import rle, unrle


@pytest.fixture(scope="session")
def glossmark(k):
    return next(k)


def test_bwt(jabber):
    rolled = bwt(jabber)
    assert (len(rolled) - 1) == len(jabber)


def test_ibwt(jabber, bwtjabber):
    ibwted = ibwt(bwtjabber, mark="$")
    assert ibwted == jabber


def test_runlength_encoding(jabber):
    run = rle(jabber)
    jsize = getsizeof(jabber)
    rsize = getsizeof(run)
    assert jsize > rsize
    jlen = len(jabber)
    rlen = len(run)
    assert jlen > rlen


def test_runlength_restore(bwtjabber, runbwtjabber):
    restored = unrle(runbwtjabber)
    assert bwtjabber == restored


def test_deglosser(glossy, printable, glossmark):
    deglossed, glossfile = degloss(glossy, mark=glossmark, allowed=printable)
    assert len(glossy) == len(deglossed)
    for c in deglossed:
        if c != glossmark:
            assert c in printable


def test_glosser(deglossed, glossy):
    assert glossy == gloss(*deglossed)
