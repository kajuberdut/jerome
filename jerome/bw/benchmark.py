from datetime import datetime

from jerome.bw.burrowswheeler import bwt, ibwt

import nbw  # type: ignore


s = "banana" * 10000

start = datetime.now()
presult1 = bwt(s)
end = datetime.now()
print(f"Python Forward BWT time: {(end-start).total_seconds() * 1000.0} ms")


start = datetime.now()
presult2 = ibwt(presult1)
end = datetime.now()
print(f"Python Reverse BWT time: {(end-start).total_seconds() * 1000.0} ms")

assert presult2 == s

start = datetime.now()
nresult1 = nbw.bwt(s)
end = datetime.now()
print(f"Nim Forward BWT time: {(end-start).total_seconds() * 1000.0} ms")

assert nresult1 == presult1

start = datetime.now()
nresult2 = nbw.ibwt(nresult1)
end = datetime.now()
print(f"Nim Reverse BWT time: {(end-start).total_seconds() * 1000.0} ms")

assert nresult2 == s
