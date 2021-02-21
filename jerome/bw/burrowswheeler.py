
def forward_bw(text: str, mark: str = "\003") -> str:
    """Returns the Burrows Wheeler transform of text.
    Mark is by convention $
    Mark must be the lowest sort order character in text.
    """
    if mark in text:
        raise ValueError(f"The mark '{mark}' exists in text.")
    matrix = [text + mark]
    [matrix.append(matrix[-1][1:] + matrix[-1][:1]) for i in text if i != mark]
    return "".join([i[-1] for i in sorted(matrix)])


def reverse_bw(text: str, mark: str = None) -> str:
    """Returns the Burrows Wheeler reverse transform of text."""
    result = ""
    p = sorted((t, i) for i, t in enumerate(text))
    mark = p[0][0] if mark is None else mark
    k = text.index(mark)
    for _ in text:
        t, k = p[k]
        result += t
    return result.strip(mark)


# python -m nuitka --module burrowswheeler.py
