from jerome import NumberCruncher, UnCruncher, k


def rle(s: str) -> str:
    s = NumberCruncher.process(s)
    result = ""
    current: str = s[0]
    count: int = 0
    for char in s:
        if char == current:
            count += 1
        else:
            if count > 1:
                result = result + str(count)
            result = result + current
            current = char
            count = 1
    if count > 1:
        result = result + str(count)
    result = result + current
    return result


def unrle(s: str) -> str:
    result = ""
    num: str = ""
    for char in s:
        if char in k.NUMBERS:
            num += char
        else:
            if num:
                result = result + char * int(num)
                num = ""
            else:
                result = result + char
    return UnCruncher.process(result)
