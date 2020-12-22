import dataclasses
import re
import typing as t
from collections import Counter
from jerome import k
from jerome.keeper import KeepCase

WORD_CASE = KeepCase["WORD"]


@dataclasses.dataclass
class WordBuilder:
    text: str = None
    counter: t.Optional[Counter] = None

    def __post_init__(self):
        if self.counter is None:
            if self.text is not None:
                words = re.findall(r"\w+", self.text)
                self.counter = Counter(words)
            else:
                self.counter = Counter()

    def ingest(self, s: str):
        words = re.findall(r"\w+", s)
        new = Counter(words)
        self.counter.update(new)

    def top(self, n: int = 10):
        return self.counter.most_common(n)

    def __getitem__(self, word):
        return self.counter[word]

    def replacement_dict(self, min_cost=5):
        result = dict()
        for word in self.counter:
            if len(word) > 1 and (len(word) * self.counter[word]) >= min_cost:
                symbol = next(k)
                result[word] = symbol
                k.keep(symbol, WORD_CASE)
        return result
