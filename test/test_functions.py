from sys import getsizeof  # noqa: E902

import pytest
from jerome.burrowswheeler import bwt, ibwt
from jerome.loader import loader
from jerome.glosser import degloss, gloss, get_gloss_mark
from jerome.runlength import rle, unrle


def test_bwt(jabber):
    rolled = bwt(jabber)
    assert (len(rolled) - 1) == len(jabber)


def test_ibwt(jabber, bwtjabber):
    ibwted = ibwt(bwtjabber)
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


def test_deglosser(glossy, normal_use):
    deglossed, glossfile = degloss(glossy)
    assert len(glossy) == len(deglossed)
    mark = get_gloss_mark()
    for c in deglossed:
        if c != mark:
            assert c in normal_use


def test_glosser(deglossed, glossy):
    assert glossy == gloss(*deglossed)


def test_gloss_mark():
    m1 = get_gloss_mark()
    m2 = get_gloss_mark()
    assert m1 == m2


def test_loader_small():
    result = list(loader("abc", 2))  # should return ['ab', 'c_']
    assert len(result) == 2
    assert len(result[0]) == 2
    assert result[0] == "ab"


def test_loader_file(tmpdir):
    p = tmpdir.join("hello.txt")
    p.write("content")
    r = next(loader(p, 10))
    assert r == "content"


def test_loader_large(jabber):
    wp = " ".join([jabber for i in range(100)])
    wp_chunk_generator = loader(wp, 25)
    for i in range(0, 2):
        chunk = next(wp_chunk_generator)
        assert len(chunk) == 25
