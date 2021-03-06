# This file was generated by Nuitka and describes the types of the
# created shared library.

# At this time it lists only the imports made and can be used by the
# tools that bundle libraries, including Nuitka itself. For instance
# standalone mode usage of the created library will need it.

# In the future, this will also contain type information for values
# in the module, so IDEs will use this. Therefore please include it
# when you make software releases of the extension module that it
# describes.

import io
import typing

# This is not Python source even if it looks so. Make it clear for
# now. This was decided by PEP 484 designers.
__name__ = ...

import typing as t
from io import StringIO

STX = "\002"
ETX = "\003"
NEWLINE = "\n"

def split(
    text: t.Optional[str] = None,
    size: int = -1,
) -> t.Iterator[str]: ...
def forward_bw(
    text: str, mark: str = ETX, split_marker=STX, split_size=5000
) -> str: ...
def reverse_bw(text: str, mark: str = ETX, split_marker=STX) -> str: ...
