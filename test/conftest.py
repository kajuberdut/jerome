import string

import pytest
from jerome import NumberCruncher, UnCruncher, k
from jerome.burrowswheeler import bwt
from jerome.glosser import degloss
from jerome.runlength import rle


@pytest.fixture(scope="session")
def jabber():
    text = """’Twas brillig, and the slithy toves
      Did gyre and gimble in the wabe:
All mimsy were the borogoves,
      And the mome raths outgrabe.

“Beware the Jabberwock, my son!
      The jaws that bite, the claws that catch!
Beware the Jubjub bird, and shun
      The frumious Bandersnatch!”

He took his vorpal sword in hand;
      Long time the manxome foe he sought—
So rested he by the Tumtum tree
      And stood awhile in thought.

And, as in uffish thought he stood,
      The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
      And burbled as it came!

One, two! One, two! And through and through
      The vorpal blade went snicker-snack!
He left it dead, and with its head
      He went galumphing back.

“And hast thou slain the Jabberwock?
      Come to my arms, my beamish boy!
O frabjous day! Callooh! Callay!”
      He chortled in his joy.

’Twas brillig, and the slithy toves
      Did gyre and gimble in the wabe:
All mimsy were the borogoves,
      And the mome raths outgrabe."""
    return text


@pytest.fixture(scope="session")
def bwtjabber(jabber):
    return bwt(jabber)


@pytest.fixture(scope="session")
def runbwtjabber(bwtjabber):
    return rle(bwtjabber)


@pytest.fixture(scope="session")
def number_replacer():
    return NumberCruncher


@pytest.fixture(scope="session")
def number_restorer():
    return UnCruncher


@pytest.fixture(scope="session")
def numbers():
    return string.digits


@pytest.fixture(scope="session")
def normal_use():
    return k.PRINTABLE


@pytest.fixture(scope="session")
def glossy():
    return "Hi Ca$hMoney"


@pytest.fixture(scope="session")
def deglossed(glossy):
    deglossed, glossfile = degloss(glossy)
    return (deglossed, glossfile)


@pytest.fixture(scope="session")
def printable():
    return string.printable
