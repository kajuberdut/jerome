""" Find commonly occuring words in a text """
import typing as t
from collections import Counter
from collections.abc import Iterable
from functools import singledispatch


@singledispatch
def common(text: Iterable, min_length=2, min_weight=4, top=100) -> t.List[str]:
    c = Counter(text)

    return [
        word
        for word, count in c.most_common(top)
        if (length := len(word)) >= min_length and (length * count) >= min_weight
    ]


@common.register
def _(text: str, min_length=2, min_weight=4) -> t.List[str]:
    return common(text.split(), min_length=min_length, min_weight=min_weight)


if __name__ == "__main__":
    print(common("this is some words words words", min_length=5))