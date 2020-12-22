import dataclasses
import string
import typing as t
from sys import getsizeof
from enum import Enum


def get_symbols(
    min_cost: int = 0,
    max_cost: int = 50,
    min_ordinal: int = 0,
    max_ordinal: int = 1114111,
    test: t.Optional[t.Callable[[str], bool]] = lambda x: True,
) -> t.List[str]:
    return (
        chr(i)
        for i in range(min_ordinal, max_ordinal)
        if getsizeof(chr(i)) <= max_cost and test(i)
    )


class KeepCase(Enum):  # pragma: no cover
    NUMBER = 1
    MARK = 2
    GLOSS = 3
    WORD = 4
    UNKNOWN = 5


@dataclasses.dataclass
class KeptSymbol:
    symbol: str
    keeper: "SymbolKeeper" = None
    keep_case: KeepCase = KeepCase(5)

    def __repr__(self):
        return f"{self.symbol}, {self.keep_case.name}"

    @property
    def size(self):
        return getsizeof(self.symbol)


@dataclasses.dataclass
class SymbolKeeper:
    kept: t.Dict[str, KeptSymbol] = dataclasses.field(default_factory=dict)
    _PRINTABLE: str = string.printable
    NUMBER_MASK: str = "\x00\x01\x02\x03\x04\x05\x06\x07\x08\x0e"
    MARK: str = "$"

    def __post_init__(self):
        self.keep(self.MARK, KeepCase["MARK"])
        [self.keep(s, KeepCase["NUMBER"]) for s in self.NUMBER_MASK]
        self._symbol_generator = get_symbols(max_cost=76)

    @property
    def PRINTABLE(self):
        return self._PRINTABLE.replace(self.MARK, "")

    @property
    def NUMBERS(self):
        return string.digits

    @property
    def number_cypher(self):
        return {str(k): v for (k, v) in enumerate(self.NUMBER_MASK)}

    @property
    def reverse_number_cypher(self):
        return {v: k for (k, v) in self.number_cypher.items()}

    @property
    def reserved(self) -> set:
        r = set(self.NUMBER_MASK).union(self.PRINTABLE).union(self.MARK)
        return r

    def keep(self, symbol: str, keep_case: t.Optional[KeepCase] = None):
        for c in symbol:
            self.kept[c] = KeptSymbol(symbol=symbol, keeper=self, keep_case=keep_case)

    def release(self, s: str):
        for c in s:
            del self.kept[c]

    def filter_kept(self, keep_case: KeepCase):
        return {k: v for k, v in self.kept.items() if v.keep_case == keep_case}

    def __iter__(self):  # pragma: no cover
        return self

    def __next__(self):
        ch = None
        while ch is None:
            ch = next(
                ch
                for ch in self._symbol_generator
                if ch not in self.reserved and ch not in self.kept
            )
        return ch

    def __getitem__(self, character: str) -> KeptSymbol:
        return self.kept[character]
