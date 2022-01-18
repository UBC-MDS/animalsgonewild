import string


def animalClassifier(text):
    """
    Count total unique words in the input text and returns an animal type.
    
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
    unique_words = np.unique(np.array(str.split(cleaned_text)))
    counts = len(unique_words)

    if counts <= 20:
        output = animal_list[0]
    elif counts <= 80:
        output = animal_list[1]
    elif counts <= 160:
        output = animal_list[2]
    else:
        output = animal_list[3]

    return output