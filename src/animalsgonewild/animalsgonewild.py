import string
import numpy as np

def animalClassifier(text):
    """    
    Count proportion of unique words in the input text and returns an corresponding animal type. 
    
    Parameters
    ----------
    text: str
        text to be analyzed

    Returns
    -------
    str
        the corresponding animal species
    
    Example
    --------
    >>> animalClassifier("what do you think?") 
    "duck"
    """
    animal_list = ["Duck", "Monkey", "Giraffe", "Whale"]
    cleaned_text = text.translate(str.maketrans('', '', string.punctuation))
    total_words = len(str.split(cleaned_text))
    unique_words = np.unique(str.split(cleaned_text))
    uni_counts = len(unique_words)


    if uni_counts/total_words <= 0.4:
        output = animal_list[0]
    elif uni_counts/total_words <= 0.6:
        output = animal_list[1]
    elif uni_counts/total_words <= 0.8:
        output = animal_list[2]
    else:
        output = animal_list[3]

    return output

def animalType(species, text):
    """    
    Analyzes text based on average word length and returns an animal picture representing language complexity. 
    
    Parameters
    ----------
    species: str
        name of the species determined from animalClassifier.py or user determined
    text: str
        text to be analyzed
    Returns
    -------
    jpg
        an image representative of the species and the complexity of the text (more complex text will have 'wiser' looking animals)
    
    Example
    --------
    >>> animal_rep = animalType(animalClassifier(text), text) 
    >>> animal_rep = animalType("duck", text) 
    >>> animal_rep(species, text)
    reallySmartDuck.jpg
    """

def wordcloud(image, text):
    """
    Inputs a text and animal picture to return a wordcloud in the shape of the animal created using the text.

    Parameters
    ----------
    image: jpg
        an image representative of the species based on the complexity of the text from animalType.py
    text: str
        text to be inserted

    Returns
    -------
    jpg
        a wordcloud image in the shape of the species inputed.

    Example
    --------
    >>> word_cloud = wordcloud(image, text) 
    wordcloud_image.jpg
    """

def textTransformer(text):
    """    
    This function modifies a block of text by replacing all pronouns
    with a complexity category and all nouns with an animal.

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
    "The smart duck walked across the duck"
    """