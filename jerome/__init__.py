from jerome.keeper import SymbolKeeper
from jerome.replacer import StringReplacer


k = SymbolKeeper()

NumberCruncher = StringReplacer(replacements=k.number_cypher)
UnCruncher = StringReplacer(replacements=k.reverse_number_cypher)
