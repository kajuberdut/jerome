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
    <img src="https://raw.githubusercontent.com/kajuberdut/jerome/main/images/Logo.svg" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Jerome</h3>

  <p align="center">
    A collection of string functions that may or may not be useful for compression.
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

Jerome is a library of string functions written in pure Python -- With parallel implimentations in Nim and JavaScript.

* 100% of functionality available in pure Python
* No external dependencies
* 100% test coverage


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
from random import choice

from jerome import (
    SymbolKeeper,
    common,
    forward_bw,
    replacer,
    reverse_bw,
    runlength_decode,
    runlength_encode,
)

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
```

### Example compression of randomized text:

  |step|result|
  |----|------|
  |Original Text length:| 64,819|
  |With words replaced:| 23,328|
  |Burrows Wheeler Transformed and run length encoded:| 11,668|
  |Reasonable dict representation length:| 966|
  |Dict + Processed Text:| 12,634|
  |Compressed size:| 19%|
  |Total time:|  458.293 ms|

  **NOTE 1:** *This is a very artificial text, real results will vary.*  
  **NOTE 2:** *Time was taken on a Ryzen 3600x @ 3.9Ghz.*
  
### Additional Documentation
* [Burrows Wheeler Transform ](https://github.com/kajuberdut/Jerome/blob/main/jerome/bw/burrowswheeler.md)


<!-- ROADMAP -->
## Roadmap

* [In place BWT](https://www.sciencedirect.com/science/article/pii/S1570866715000052)
* Nim versions of all functions
* js versions of all functions
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

Distributed under the BSD Two-clause License. See `LICENSE` for more information.



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
[license-shield]: https://img.shields.io/badge/License-BSD%202--Clause-orange.svg?style=for-the-badge
[license-url]: https://github.com/kajuberdut/Jerome/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/patrick-shechet