from datetime import datetime

from jerome.bw.burrowswheeler import forward_bw, reverse_bw
from jerome.bw import nim_bw

text = "banana " * 10000

start = datetime.now()
presult1 = forward_bw(text)
end = datetime.now()
print(f"Python Forward Burrows Wheeler: {(end-start).total_seconds() * 1000.0} ms")


start = datetime.now()
presult2 = reverse_bw(presult1)
end = datetime.now()
print(f"Python Reverse Burrows Wheeler: {(end-start).total_seconds() * 1000.0} ms")

assert presult2 == text

start = datetime.now()

nresult1 = nim_bw.forward_bw(text)
end = datetime.now()
print(f"Nim Forward Burrows Wheeler time: {(end-start).total_seconds() * 1000.0} ms")

# assert nresult1 == presult1

start = datetime.now()
nresult2 = nim_bw.reverse_bw(nresult1)
end = datetime.now()
print(f"Nim Reverse Burrows Wheeler time: {(end-start).total_seconds() * 1000.0} ms")

assert nresult2 == text
