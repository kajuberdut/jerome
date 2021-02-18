import string

import pytest
from jerome.bw.burrowswheeler import forward_bw
from jerome.glosser import degloss
from jerome.keeper import SymbolKeeper
from jerome.runlength import rle


def pytest_addoption(parser):
    parser.addoption(
        "--runslow", action="store_true", default=False, help="run slow tests"
    )


def pytest_configure(config):
    config.addinivalue_line("markers", "slow: mark test as slow to run")


def pytest_collection_modifyitems(config, items):
    if config.getoption("--runslow"):
        # --runslow given in cli: do not skip slow tests
        return
    skip_slow = pytest.mark.skip(reason="need --runslow option to run")
    for item in items:
        if "slow" in item.keywords:
            item.add_marker(skip_slow)


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
def forward_bwjabber(jabber):
    return forward_bw(jabber)


@pytest.fixture(scope="session")
def runforward_bwjabber(forward_bwjabber):
    return rle(forward_bwjabber)


@pytest.fixture(scope="session")
def numbers():
    return string.digits


@pytest.fixture(scope="session")
def glossy():
    return "Hi Ca$hMoney"


@pytest.fixture(scope="session")
def deglossed(glossy, glossmark):
    deglossed, glossfile = degloss(glossy, glossmark)
    return (deglossed, glossfile)


@pytest.fixture(scope="session")
def printable():
    return string.printable

@pytest.fixture(scope="session")
def k(printable):
    return SymbolKeeper(reserved=printable)
