from pickle import TRUE
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
    if not isinstance(text, str):
        raise TypeError("Text input should be of type 'str'")
    
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