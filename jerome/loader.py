from io import FileIO, StringIO
from pathlib import Path
from typing import Generator


def loader(
    s: str, size: int = -1, allow_bytes: bool = False
) -> Generator[str, None, None]:
    p = Path(s)
    if p.is_file():
        io_handle = FileIO(p)
    else:
        io_handle = StringIO(s)

    while True:
        chunk = io_handle.read(size)

        if len(chunk) > 0:
            if isinstance(chunk, bytes) and allow_bytes is False:
                chunk = chunk.decode("utf-8")
            yield chunk
        else:
            io_handle.close()
            break


def file_to_str(source: Path) -> str:
    return next(loader(source, allow_bytes=False))


def file_to_bytes(source: Path) -> bytes:
    return next(loader(source, allow_bytes=True))