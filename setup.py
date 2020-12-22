# from Cython.Build import cythonize

import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="jerome",
    version="0.0.1",
    author="Patrick Shechet",
    author_email="patrick.shechet@gmail.com",
    description=("String Processing Tools"),
    license="BSD",
    packages=find_packages(),
    include_package_data=True,
    long_description=read("README"),
    install_requires=["msgpack", "click", "typer"],
    entry_points={
        "console_scripts": ["nce=jerome.__main__"],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Text Editors :: Word Processors",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
    ],
)
