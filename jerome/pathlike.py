import typing as t
from pathlib import Path

PathLike = t.Union[str, Path]


def ensure_path(p: PathLike) -> Path:
    """Takes a pathlike object and returns a Path"""
    if not isinstance(p, Path):
        p = Path(p)
    return p