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
