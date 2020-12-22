import typing as t  # noqa: E902
import urllib.request
from pathlib import Path


def download_text(uri: str, output_path: t.Union[str, Path]):
    if not output_path.is_file():
        urllib.request.urlretrieve(uri, output_path)


if __name__ == "__main__":

    # Test on War and Peace
    wp_url = "https://raw.githubusercontent.com/mmcky/nyu-econ-370/master/notebooks/data/book-war-and-peace.txt"

    t = Path("C:\\Code\\jerome\\jerome\\docs\\wp.txt")
    download_text(wp_url, t)
