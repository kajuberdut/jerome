from datetime import datetime

from jerome import (SymbolKeeper, common, forward_bw, replacer, reverse_bw,
                    runlength_decode, runlength_encode)
from augustine_text.sample_text import words


# 75K words of procedurally generated text
# This is about the length of novel.
text = words(75000)
text_length = len(text)

compression_start = datetime.now()
# SymbolKeeper is used to portion out un-used symbols
k = SymbolKeeper(
    reserved=set(list(text))
)  # These appear in our text so we don't want to use them as placeholders

# common is a utility function for finding commonly occuring words
# We're using k from above to create a dictionary where each key is a word
#  and the value is a single symbol replacement for that word
replacements = {word: next(k) for word in common(text, min_length=4)}
# {'dolore': '\x00', 'elit,': '\x02', 'labore': '\x03', ...

# Run replacements
replaced = replacer(text, replacements)
# Burrows Wheeler transform the text to improve runlength result
transformed = forward_bw(replaced)
# Runlength encode
runcoded = runlength_encode(transformed)

print(
    f"""| step | result |
| ---- | ------ |
| Original Text size | {text_length} |
| With words replaced | {len(replaced)} |
| Encoded | {(rlen := len(runcoded))} |
| Reasonable length | {(dlen := len(str([(k,v) for k,v in replacements.items()])))} |
| Compressed size % | {round(((rlen+dlen)/text_length)*100, 2)} |"""
)
compression_end = datetime.now()


# Reverse the whole thing
assert (unruncoded := runlength_decode(runcoded)) == transformed
assert (untransformed := reverse_bw(unruncoded)) == replaced
assert replacer(untransformed, replacements, reverse=True) == text
print(
    f"| Compression time |  {round((compression_end-compression_start).total_seconds() * 1000.0)} ms |"
)
print(
    f"| Decompression time |  {round((datetime.now()-compression_end).total_seconds() * 1000.0)} ms |"
)
print(
    f"| Total time |  {round((datetime.now()-compression_start).total_seconds() * 1000.0)} ms |"
)
