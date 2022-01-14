def textTransformer(text, class_object):
    """    
    Based on the classifications determined by the functions `animalType() and 
    _____, This function modifys the original block of text by replacing all pronouns
    with a complexity category and all nouns with an animal. If classifiers have
    not been used "smart" and "duck" will be used respectively.

    Parameters
    ----------
    text: str
        text to be transformed.

   Returns
    -------
    str
        a string containing the transformed text.
    class_object
        a class object containing the outputs of the previous functions.

    Example
    --------
    >>> text = "The silly chicken walked across the road"
    >>> textTransformer(text)
    "The smart duck walked across the duck"
    """