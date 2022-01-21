import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.corpus import wordnet as wn
import string


def textTransformer(text):
    """    
    This function modifies a block of text by replacing all nouns
    with an animal.

    Parameters
    ----------
    text: str
        text to be transformed.

   Returns
    -------
    str
        a string containing the transformed text.

    Example
    --------
    >>> text = "The silly chicken walked across the road"
    >>> textTransformer(text)
    "The silly duck walked across the duck"
    """

    #animal = animalClassifier(text)   # use this once animalClassfier is working

    animal = "Duck"   #temporary paceholder

    text_list = text.split()
    revised_text_list = text_list

    for i in range(0, len(text_list)):
        if text_list[i] in nouns:
            revised_text_list[i] = animal

    output = ' '.join(revised_text_list)
        
    return output