import dataclasses
import json
import typing as t

import msgpack
import typer

from jerome.burrowswheeler import bwt, ibwt
from jerome.glosser import degloss, gloss
from jerome.loader import file_to_bytes, file_to_str, loader
from jerome.pathlike import Path, ensure_path  # Dropped union type to make typer happy
from jerome.replacer import StringReplacer
from jerome.runlength import rle, unrle
from jerome.wordbuilder import WordBuilder

app = typer.Typer()


def _compress(text: str, chunk_size: int = 1024) -> bytes:
    # Setup our return dict
    r = {"c": list(), "l": len(text)}

    # Gloss out any characters we don't support
    glossed, glossfile = degloss(text)
    if glossfile:
        r["g"] = glossfile

    # Find common words and replace them
    words = WordBuilder(glossed)
    r["w"] = words.replacement_dict()
    rep = StringReplacer(r["w"])
    wordless = rep.process(glossed)

    # Now we slice this into c and for each
    # Burrows-Wheeler transform
    # Runlength encode
    # Add to our list of c
    [r["c"].append(rle(bwt(chunk))) for chunk in loader(wordless, chunk_size)]

    # Finally msgpack and return
    return msgpack.packb(r)


def _decompress(b: bytes) -> str:
    # Load the package
    package = msgpack.unpackb(b)

    # Now for each chunk
    # Unencode runs
    # ibwt burrows wheeler transform
    # and append to our working text
    text = "".join([ibwt(unrle(chunk)) for chunk in package["c"]])

    # Restore words
    if "w" in package:
        rep = StringReplacer({v: k for k, v in package["w"].items()})
        text = rep.process(text)

    # If gloss exists gloss back in those characters
    if "g" in package:
        text = gloss(text, gloss=package["g"])

    # Finally, return text
    return text


@app.command()
def compress(file_path: Path, output_path: Path) -> None:
    """Given a path compresses the text found in that file outputing to output_path."""
    file_path = ensure_path(file_path)
    output_path = ensure_path(output_path)
    result = _compress(text=file_to_str(file_path))
    with open(output_path, "wb") as fh:
        fh.write(result)


@app.command()
def decompress(file_path: Path, output_path: Path) -> None:
    """Decompresses .nce file outputing to output_path."""
    file_path = ensure_path(file_path)
    output_path = ensure_path(output_path)
    result = _decompress(b=file_to_bytes(file_path))
    with open(output_path, "w", encoding="utf-8") as fh:
        fh.write(result)


@app.command()
def expand(source: Path, max_text: int = -1):
    """Expand contents of a .nce file."""
    source = ensure_path(source)

    # Load the package
    package = msgpack.unpackb(file_to_bytes(source))

    stem = source.stem
    target_dir = source.parent / stem
    target_dir.mkdir(exist_ok=True)
    gloss_path = target_dir / "gloss.txt"
    word_path = target_dir / "words.json"
    text_dir = target_dir / "texts"
    text_dir.mkdir(exist_ok=True)

    with open(word_path, "w") as p:
        json.dump(obj=package["w"], fp=p)

    with open(gloss_path, "w", encoding="utf-8") as g:
        g.write(package["g"])

    if max_text > -1:
        for i, ch in enumerate(package["c"]):
            if i <= max_text:
                fh = text_dir / (str(i) + ".txt")
                with open(fh, "w", encoding="utf-8") as h:
                    h.write(ch)


if __name__ == "__main__":
    app()
