from datetime import datetime

from jerome import (
    SymbolKeeper,
    common,
    forward_bw,
    replacer,
    reverse_bw,
    runlength_decode,
    runlength_encode,
    sample_text,
)

MARK = "\003"  # Mark must be the lowest sorting character in a text
start = datetime.now()

# Let's take 100 sentences of procedurally generated text
# from each of the bundles Markov seeds.
text = " ".join(
    [
        sample_text(t).get_text(75)
        for t in ["Pride and Prejudice", "Black Gate Speech", "Lorem Ipsum"]
    ]
)
text_length = len(text)

# SymbolKeeper is used to portion out un-used symbols
k = SymbolKeeper(
    reserved=set(list(text) + list("0123456789$" + MARK))
)  # These appear in our text so we don't want to use them as placeholders

# common is a utility function for finding commonly occuring words
# We're using k from above to create a dictionary where each key is a word
#  and the value is a single symbol replacement for that word
replacements = {word: next(k) for word in common(text, min_length=4)}
# We want to use a single space in our burrows wheeler transform
replacements[MARK] = next(k)
# {'dolore': '\x00', 'elit,': '\x02', 'labore': '\x03', ...

replaced = replacer(text, replacements)
transformed = forward_bw(replaced, mark=MARK)

runcoded = runlength_encode(transformed)
print(
    f"""Original Text length: {text_length}
With words replaced: {len(replaced)}
Burrows Wheeler Transformed and run length encoded: {(rlen := len(runcoded))}
Reasonable dict representation length: {(dlen := len(str([(k,v) for k,v in replacements.items()])))}
Compressed size %: {(rlen+dlen)/text_length}
"""
)

# Reverse the whole thing
assert (unruncoded := runlength_decode(runcoded)) == transformed
assert (untransformed := reverse_bw(unruncoded, mark=MARK)) == replaced
assert replacer(untransformed, replacements, reverse=True) == text
print(f"Total time:  {(datetime.now()-start).total_seconds() * 1000.0} ms")
