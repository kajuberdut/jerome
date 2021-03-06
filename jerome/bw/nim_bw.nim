import nimpy
import algorithm
 
const
  Etx = '\3'


proc forward_bw(text: string): string {.exportpy.} =
    ## Apply Burrows–Wheeler transform to input string.
    doAssert(Etx notin text, "Input string cannot contain ETX character")

    var m : seq[string] = @[text & $Etx]
    for i in 1 .. text.len: 
        m.add(m[^1][^1] & m[^1][0 .. ^2])
    m.sort()
    for i in m: 
        result.add(i[^1])

proc reverse_bw(text: string): string {.exportpy.} =
    var 
        m : seq[(char, int)]
        k = text.find(Etx)
        t : char
    for i in 0 .. text.len-1:
        m.add((text[i], i))
    m.sort()
    for _ in 1 .. text.len-1:
        (t, k) = m[k]
        result.add(t)

# nim c --app:lib -d:release --opt:speed --tlsEmulation:off --out:.\jerome\bw\nim_bw.pyd .\jerome\bw\nim_bw.nim
