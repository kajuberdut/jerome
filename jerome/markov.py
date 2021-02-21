# type: ignore
import bz2
import dataclasses
import json
import random
import typing as t
from collections import defaultdict
from functools import partial, singledispatchmethod
from importlib import resources

SEED_PATHS = {
    "Pride and Prejudice": resources.path("jerome.seeds", "pride.seed"),
    "Black Gate Speech": resources.path("jerome.seeds", "blackgate.seed"),
    "Lorem Ipsum": resources.path("jerome.seeds", "loremipsum.seed"),
}


def sample_text(source_name="Lorem Ipsum") -> "Markov":
    with SEED_PATHS[source_name] as f:
        m = Markov.from_seedfile(f)
    return m


STX = "\002"
ETX = "\003"

wcounter = partial(defaultdict, int)
datadict = partial(defaultdict, wcounter)


@dataclasses.dataclass
class Markov:
    _words: t.List[str] = dataclasses.field(default_factory=list)
    _data: t.DefaultDict[int, t.DefaultDict[int, int]] = dataclasses.field(
        default_factory=datadict
    )

    @staticmethod
    def formatdata(data: t.Dict) -> t.Dict:
        d = datadict()
        for k, p in data.items():
            d[int(k)] = wcounter({int(k): v for k, v in p.items()})
        return d

    @classmethod
    def from_corpus(cls, corpus: str) -> "Markov":
        return cls.from_sentences(sentences=corpus.splitlines())

    @classmethod
    def from_sentences(cls, sentences: t.List[str]) -> "Markov":
        m = cls()
        [m.ingest_sentence(s) for s in sentences]
        return m

    @classmethod
    def from_seed(cls, seed: t.Dict) -> "Markov":
        return cls(_words=seed["_words"], _data=cls.formatdata(seed["_data"]))

    @classmethod
    def from_seedfile(cls, path: str) -> "Markov":
        with bz2.open(path, "rb") as f:
            return cls.from_seed(json.loads(f.read()))

    def __post_init__(self):
        self.add_word(STX)
        self.add_word(ETX)

    @property
    def key(self) -> int:
        self._key += 1
        return self._key

    @property
    def words(self):
        return set(self._words)

    @singledispatchmethod
    def add_word(self, w: str) -> None:
        if w not in self._words:
            self._words.append(w)

    @add_word.register
    def _(self, w: list) -> None:
        new = set(w).difference(self.words)
        [self.add_word(w) for w in new]

    @singledispatchmethod
    def _get(self, k: int) -> str:
        return self._words[k]

    @_get.register
    def _(self, k: str) -> int:
        return self._words.index(k)

    @property
    def start(self) -> int:
        return self._get(STX)

    @property
    def end(self) -> int:
        return self._get(ETX)

    def ingest_bigram(self, b: t.Tuple[str, str]) -> None:
        x, y = self._get(b[0]), self._get(b[1])
        self._data[x][y] += 1

    @singledispatchmethod
    def ingest_sentence(self, s: t.List[str]) -> None:
        self.add_word(s)
        s.append(ETX)
        [self.ingest_bigram(b) for b in zip([STX] + s, s)]

    @ingest_sentence.register
    def _(self, s: str) -> None:
        self.ingest_sentence(s.split())

    @singledispatchmethod
    def follows(self, leads: int) -> int:
        p, w = zip(*self._data[leads].items())
        return random.choices(population=p, weights=w)[0]

    @follows.register
    def _(self, leads: str):
        return self.follows(self._get(leads))

    def sentence(self, state: str = None):
        if state is None:
            state = self.start
        result = []
        while state != self.end:
            result.append((state := self.follows(state)))
        return result

    def translate(self, s: t.List[int]) -> str:
        return " ".join([self._get(i) for i in s])

    def get_text(self, sentences: int) -> str:
        return "\n".join([self.translate(self.sentence()) for i in range(sentences)])

    @property
    def seed(self):
        return {"_words": self._words, "_data": self._data}

    def save(self, path):
        with bz2.open(path, "wb") as f:
            f.write(json.dumps(self.seed).encode("utf-8"))
