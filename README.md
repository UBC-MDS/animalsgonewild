** TODO: replace function1 with function names once finalized. Validate function descriptions against function docstrings once created.
# animalsgonewild

This package is designed to demonstrate how basic features of text analysis can be utilized to analyze, sort, and represent a text file or string, while applying a humorous lens (because what is data science without the humor we see embedded throughout the R programming language and core packages). This package can analyze a text (stored as a string), sort based on number of words, and then represent the text via image (animal size will correspond to length) and wordcloud. We have included a bonus fourth function for fun, inspired by the popular childhood game MadLibs.

# Contributors
Kyle Maj, Nagraj Rao, Morgan Rosenberg, Junrong Zhu

## Installation

```bash
$ pip install animalsgonewild
```

## Usage

This package can be used in conjunction with any code to read in multiple text files to analyze and compare whole corpuses (your software must call the Animals Gone Wild functions for each text variable). 

Function 1: 
This function takes a sequence of text(str), counts the words in the string, and then returns an animal type as a string.

Function 2: 
This function takes a sequence of text(str)  and a species (str), determines the average word length (proxy for language complexity), and returns an appropriately smart looking animal image (jpg).

Function 3: 
This function takes a sequence of text(str) and a species (str), and returns a wordcloud in the shape of the species comprised of the sequence of text. 

Function 4:
This function takes a sequence of text(str) and a species(str), and returns a new text sequence where all proper nouns are replaced with the species.

Fit within the Python ecosystem:
While there are other fun packages working with animal images, most are more basic. For example, animal-cuties script (https://pypi.org/project/animal-cuties/#description) generates animal images (e.g. animal-cuties cat). However, we were unable to find any interactive, multidimensional comedic relief package, where users can input information, and receive dynamic humorous feedback in the form of cute and/or hillarious animals. Especially given how much time we all spend in front of a screen, this package seems like an essential addition to the ecosystem. By offerining it as a package rather than a script, we also empower other developers to integrate this is a fun injection to their coding projecs.![image](https://user-images.githubusercontent.com/20976116/149256760-ecf9fb02-bc08-45ce-a59c-2ef5ccb551bb.png)

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`animalsgonewild` was created by DSCI 524 - Team 16:
Nagraj Rao, Junrong Zhu, Kyle Maj, Morgan Rosenberg

It is licensed under the terms of the MIT license.

## Credits

`animalsgonewild` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
![image](https://user-images.githubusercontent.com/20976116/149257801-40094ce4-6695-4698-8d3a-c3191bd07ae9.png)
