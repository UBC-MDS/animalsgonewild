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