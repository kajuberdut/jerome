def bwt(s: str, mark: str = "$") -> str:
    def rotate(s: str, n: int = 1):
        return s[n:] + s[:n]

    s = s + mark
    l = len(s)
    p = list()
    [p.append(rotate(s, i)) for i in range(l)]
    p.sort()

    return "".join([i[-1] for i in p])


def ibwt(s: str, mark: str = "$"):
    result = ""
    k = s.index(mark)
    p = sorted((t, i) for i, t in enumerate(s))
    for _ in s:
        t, k = p[k]
        result += t

    return result.strip(mark)
