from random import choice

from jerome.bw.burrowswheeler import bwt, ibwt
from jerome.common import common
from jerome.keeper import SymbolKeeper
from jerome.replacer import replace
from jerome.runlength import rle, unrle

WORD_COUNT = 10000
MARK = " "  # Mark must be the lowest sorting character

# Some good old Lorem Ipsum
lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
words = lorem.split()
text = " ".join([choice(words) for i in range(WORD_COUNT)])
text_length = len(text)

# SymbolKeeper is used to portion out un-used symbols
k = SymbolKeeper(
    reserved=set(list(lorem) + list("0123456789$" + MARK))
)  # These appear in our text so we don't want to use them as placeholders

# common is a utility function for finding commonly occuring words
# We're using k from above to create a dictionary where each key is a word
#  and the value is a single symbol replacement for that word
replacements = {word: next(k) for word in common(text, min_length=4)}
# We want to use a single space in our burrows wheeler transform
replacements[MARK] = next(k)
# {'dolore': '\x00', 'elit,': '\x02', 'labore': '\x03', ...

replaced = replace(text, replacements)
transformed = bwt(replaced, mark=MARK)

runcoded = rle(transformed)
print(f"""text length: {text_length}
Words replaced: {len(replaced)}
Run length encoded: {(rlen := len(runcoded))}
Reasonable dict representation length: {(dlen := len(str([(k,v) for k,v in replacements.items()])))}
Compressed size %: {(rlen+dlen)/text_length}
""")

# Reverse the whole thing
assert (unruncoded := unrle(runcoded)) == transformed
assert (untransformed := ibwt(unruncoded, mark=MARK)) == replaced
assert replace(untransformed, replacements, reverse=True) == text
