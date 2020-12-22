import pytest
from jerome import k
from jerome.keeper import KeepCase


def test_keeper(printable):
    s = next(k)
    assert s not in printable


def test_keep():
    s = next(k)
    word_case = KeepCase['WORD']
    k.keep(s, keep_case=word_case)
    assert k[s].symbol == s
    assert k[s].symbol in k.filter_kept(word_case)
    assert k[s].keep_case == word_case
    k.release(s)
    with pytest.raises(KeyError):
        k[s]


def test_printable(printable):
    reconstructed = set(k.PRINTABLE + k.MARK)
    for ch in printable:
        assert ch in reconstructed


def test_numbers(numbers):
    n = k.NUMBERS
    for d in numbers:
        assert d in n


def test_size():
    s = next(k)
    k.keep(s, KeepCase['WORD'])
    size = k[s].size
    assert (50 <= size <= 76)


def test_repr():
    s = next(k)
    k.keep(s, KeepCase['WORD'])
    repr(k[s])
