from datetime import datetime

from jerome.bw.burrowswheeler import forward_bw, reverse_bw
from jerome.bw import nim_bw

s = "banana" * 5000

start = datetime.now()
presult1 = forward_bw(s)
end = datetime.now()
print(f"Python Forward forward_bw time: {(end-start).total_seconds() * 1000.0} ms")


start = datetime.now()
presult2 = reverse_bw(presult1)
end = datetime.now()
print(f"Python Reverse forward_bw time: {(end-start).total_seconds() * 1000.0} ms")

assert presult2 == s

start = datetime.now()
nresult1 = nim_bw.forward_bw(s)
end = datetime.now()
print(f"Nim Forward forward_bw time: {(end-start).total_seconds() * 1000.0} ms")

assert nresult1 == presult1

start = datetime.now()
nresult2 = nim_bw.reverse_bw(nresult1)
end = datetime.now()
print(f"Nim Reverse forward_bw time: {(end-start).total_seconds() * 1000.0} ms")

assert nresult2 == s
