# animalsgonewild

[![codecov](https://codecov.io/gh/UBC-MDS/animalsgonewild/branch/main/graph/badge.svg?token=tGLNiVr2OZ)](https://codecov.io/gh/UBC-MDS/animalsgonewild) [![ci-cd](https://github.com/UBC-MDS/animalsgonewild/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/UBC-MDS/animalsgonewild/actions/workflows/ci-cd.yml) [![Docs](https://readthedocs.org/projects/animalsgonewild/badge/?version=latest)](https://animalsgonewild.readthedocs.io/en/latest/index.html)

This package is designed to demonstrate how basic features of text analysis can be utilized to analyze and represent a text file or string while applying a humorous lens (because what is data science without a dash of humor!). It counts the number of words from a text, calculates the average word length of that text, and returns an animal image corresponding to the average word length. It subsequently transforms the text into a wordcloud in the shape of the animal. We have included a bonus fourth function for fun, inspired by the popular childhood game - MadLibs.

# Contributors

Kyle Maj, Nagraj Rao, Morgan Rosenberg, Junrong Zhu

## Installation

```bash
pip install git+https://github.com/UBC-MDS/animalsgonewild
```

## Usage

This package can be used in conjunction with any code to read in multiple text files to analyze and compare whole corpuses (your software must call the Animals Gone Wild functions for each text variable).

### Function 1: animalClassifier

This function takes a sequence of text(str), counts the words in the string, and then returns an animal type (str).

### Function 2: animalType

This function takes a sequence of text(str)  and a species (str), determines the average word length (proxy for language complexity), and returns an smart looking animal image (jpg) corresponding to the average word length.

### Function 3: wordcloud

This function takes a sequence of text(str) and an animal image (jpg), and returns a wordcloud in the shape of the species comprised of the sequence of text (jpg).

### Function 4: textTransformer

This function takes a sequence of text(str) and a species(str), and returns a new text sequence where all proper nouns are replaced with the species.

### Fit within the Python ecosystem

While other fun packages with animal images exist, most are very basic. For example, the animal-cuties script (<https://pypi.org/project/animal-cuties/#description>) generates animal images (e.g. animal-cuties cat). However, we were unable to find any interactive, multidimensional comedic relief package, where users can input information, and receive dynamic humorous feedback in the form of cute and/or hilarious animals. Given how much time we all are spending in front of a computer screen during the pandemic, this package is an essential addition to the ecosystem promoting mental wellness through humor. By offering it as a package rather than a script, we also empower other developers to integrate this is as a fun injection to their coding projecs.

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`animalsgonewild` was created by DSCI 524 - Team 16:
Nagraj Rao, Junrong Zhu, Kyle Maj, Morgan Rosenberg

It is licensed under the terms of the MIT license.

## Credits

`animalsgonewild` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).

# Easter egg #1

Did you know the name of our package was almost called "whattheduck"?

# Easter egg #2

Got any carrots?

# Easter egg #3

Aren't we pretty?
