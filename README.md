<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
***
***
***
*** To avoid retyping too much info. Do a search and replace for the following:
*** kajuberdut, Jerome, twitter_handle, patrick.shechet@gmail.com, Jerome, String functions in pure Python
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/kajuberdut/Jerome">
    <img src="https://raw.githubusercontent.com/kajuberdut/jerome/main/images/Logo.svg" alt="Logo" width="160" height="160">
  </a>

  <h3 align="center">Jerome</h3>

  <p align="center">
    A collection of functions that illustrate several techniques useful in text compression.
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
    <li><a href="#usage">Usage</a>
      <ul>
        <li><a href="#additional-documentation">Additional Documentation</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Jerome is a library of string functions written in pure Python. The library's name is taken from St. Jerome of Stridon who is considered the patron saint of archivists.

* Zero dependencies[^1]
* 100% test coverage

[^1]: Examples use augustine_text to generate material to compress

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Installing with pip

  ```sh
  pip install jerome
  ```

For information about cloning and dev setup see: [Contributing](#Contributing)


<!-- USAGE EXAMPLES -->
## Usage
Here is an example showing basic usage.

```python
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
| Compressed size % | {round(((rlen+dlen)/text_length)*100, 2)} |
"""
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

```

### Example compression of randomized text:

| step | result |
| ---- | ------ |
| Original Text length | 402270 |
| With words replaced | 198228 |
| Encoded | 74160 |
| Reasonable length | 5724 |
| Compressed size % | 19.86 |
| Compression time |  1045 ms |
| Decompression time |  172 ms |
| Total time |  1217 ms |  
  
**NOTE** *Time was taken on a Ryzen 3600x @ 3.9Ghz.*

This is only an example of how the text functions in Jerome work.
Python's built in bz2 is both many times faster and many time better at compressing than the above example.

### Additional Documentation
* [Burrows Wheeler Transform ](https://github.com/kajuberdut/Jerome/blob/main/jerome/bw/burrowswheeler.md)


<!-- ROADMAP -->
## Roadmap

* [In place BWT](https://www.sciencedirect.com/science/article/pii/S1570866715000052)
* Huffman Coding
* Additional examples

See the [open issues](https://github.com/kajuberdut/Jerome/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Add tests, we aim for 100% test coverage [Using Coverage](https://coverage.readthedocs.io/en/coverage-5.3.1/#using-coverage-py)
4. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
5. Push to the Branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request

### Cloning / Development setup
1. Clone the repo and install
    ```sh
    git clone https://github.com/kajuberdut/Jerome.git
    cd Jerome
    pipenv install --dev
    ```
2. Run tests
    ```sh
    pipenv shell
    py.test
    ```
  For more about pipenv see: [Pipenv Github](https://github.com/pypa/pipenv)



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Patrick Shechet - patrick.shechet@gmail.com

Project Link: [https://github.com/kajuberdut/Jerome](https://github.com/kajuberdut/Jerome)




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/kajuberdut/Jerome.svg?style=for-the-badge
[contributors-url]: https://github.com/kajuberdut/Jerome/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/kajuberdut/Jerome.svg?style=for-the-badge
[forks-url]: https://github.com/kajuberdut/Jerome/network/members
[stars-shield]: https://img.shields.io/github/stars/kajuberdut/Jerome.svg?style=for-the-badge
[stars-url]: https://github.com/kajuberdut/Jerome/stargazers
[issues-shield]: https://img.shields.io/github/issues/kajuberdut/Jerome.svg?style=for-the-badge
[issues-url]: https://github.com/kajuberdut/Jerome/issues
[license-shield]: https://img.shields.io/badge/License-MIT-orange.svg?style=for-the-badge
[license-url]: https://github.com/kajuberdut/Jerome/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/patrick-shechet
