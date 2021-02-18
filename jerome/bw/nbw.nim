import nimpy
import algorithm

proc bwt(text: string): string {.exportpy.} =
    var m : seq[string] = @[text & "$"]
    for i in 1 .. text.len: 
        m.add(m[^1][^1] & m[^1][0 .. ^2])
    m.sort()
    for i in m: 
        result.add(i[^1])

proc ibwt(text: string): string {.exportpy.} =
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

# nim c --app:lib -d:release --opt:speed --tlsEmulation:off --out:nbw.pyd nbw
