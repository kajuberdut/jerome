import algorithm

proc bwt(text: string): string {.exportc.} =
    var m : seq[string] = @[text & "$"]
    for i in 1 .. text.len: 
        m.add(m[^1][^1] & m[^1][0 .. ^2])
    m.sort()
    for i in m: 
        result.add(i[^1])

proc ibwt(text: string): string {.exportc.} =
    var 
        m : seq[(char, int)]
        k = text.find('$')
        t : char
    for i in 0 .. text.len-1:
        m.add((text[i], i))
    m.sort()
    for _ in 1 .. text.len-1:
        (t, k) = m[k]
        result.add(t)


when isMainModule:
    let result = bwt("banana")
    echo result
    echo ibwt(result)

# nim js -d:release --opt:speed -o:jbw.js jbw.nim