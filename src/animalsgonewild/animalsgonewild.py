
def animalClassifier(text):
    """    
    Count total characters in the input text and returns an animal type. 
    
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
    output = ''
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