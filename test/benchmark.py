from datetime import datetime

from jerome.bw.burrowswheeler import forward_bw, reverse_bw

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
