import time
from pathlib import Path

from jerome.main import compress_file, decompress_file, expand

title = "wp"

txt = Path(f"C:\\Code\\jerome\\jerome\\docs\\{title}.txt")
nc = Path(f"C:\\Code\\jerome\\jerome\\docs\\{title}.nce")
final = Path(f"C:\\Code\\jerome\\jerome\\docs\\{title}_restored.txt")

compress_start = time.time()
compress_file(file_path=txt, output_path=nc)
compress_end = time.time()
print(f"Compression time = {compress_end - compress_start}")

decompress_start = time.time()
decompress_file(file_path=nc, output_path=final)
decompress_end = time.time()
print(f"DeCompression time = {decompress_end - decompress_start}")

# Examining why spaces in some files are doubled.
# text = e.file_to_str(txt)
# with open(final, 'w', encoding='utf-8') as fh:
#     fh.write(text)
