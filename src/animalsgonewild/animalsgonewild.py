import string
import numpy as np
import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')
from pathlib import Path
from PIL import Image
from nltk.corpus import wordnet as wn
from newspaper import Article
from wordcloud import STOPWORDS
from wordcloud import WordCloud
import matplotlib.pyplot as plt

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
    
def textTransformer(text):
    """    
    This function modifies a block of text by replacing all nouns with an animal.

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
    
    assert type(text) == str, "Input is not str datatype"
    
    nouns = {x.name().split('.', 1)[0] for x in wn.all_synsets('n')}
    animal = animalClassifier(text)

    text_list = text.split()
    revised_text_list = text_list

    for i in range(0, len(text_list)):
        if text_list[i] in nouns:
            revised_text_list[i] = animal

    output = ' '.join(revised_text_list)
    
    assert type(text) == str, "Output is not str datatype"
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
    jpeg
        an image representative of the species and the complexity of the words used (more complex words will have 'wiser' looking animals)
    
    Example
    --------
    >>> animal_rep = animalType(animalClassifier(text), text) 
    >>> animal_rep = animalType("duck", text) 
    >>> animal_rep(species, text)
    smart_Duck.jpeg
    """
    
    if not isinstance(text, str):
        raise TypeError("Text input should be of type 'str'")
        
    if not isinstance(species, str):
        raise TypeError("Species input should be of type 'str'")
    
    words = text.translate(str.maketrans('', '', string.punctuation)).split()
    average = sum(len(w) for w in words) / len(words)
    iq = ""
    
    if average < 5:
        iq = "dumb"
    else:
        iq = "smart"
    filename = "".join([iq, "_", species, ".jpeg"])    
    
    data_folder = Path("src/animalsgonewild/imgs/")

    file_to_open = data_folder / filename

    img = Image.open(file_to_open)

    return img


def wordCloud(link):
    """
    Inputs the URL of a website to return a wordcloud in the shape of the animal created and the animal name itself.
    Parameters
    ----------
    text: str
        text to be inserted
    Returns
    -------
    jpg
        a wordcloud image in the shape of the species inputed.
    Example
    --------
    >>> word_cloud = wordCloud('https://www.britannica.com/place/Japan') 
    whale
    """
    if not isinstance(link, str):
        raise TypeError("Text input should be of type 'str' and a URL")
    article = Article(link)
    article.download()
    article.parse()
    article_length = len(article.text)
    
    if article_length < 300:
        mask = np.array(Image.open(Path('src/animalsgonewild/images/duck.jpg')))
        wc = WordCloud(stopwords=STOPWORDS, mask=mask, background_color="white", max_words=2000, max_font_size=256, random_state=42,
                       width=mask.shape[0], height=mask.shape[0])
        wc.generate(article.text)
        plt.imshow(wc, interpolation="bilinear")
        plt.axis('off')
        animal = 'duck'
    elif article_length < 2000:
        mask = np.array(Image.open(Path('src/animalsgonewild/images/monkey.jpg')))
        wc = WordCloud(stopwords=STOPWORDS, mask=mask, background_color="white", max_words=2000, max_font_size=256, random_state=42,
                       width=mask.shape[0], height=mask.shape[0])
        wc.generate(article.text)
        plt.imshow(wc, interpolation="bilinear")
        plt.axis('off')
        animal = 'monkey'
    elif article_length < 3000:
        mask = np.array(Image.open(Path('src/animalsgonewild/images/giraffe.jpg')))
        wc = WordCloud(stopwords=STOPWORDS, mask=mask, background_color="white", max_words=2000, max_font_size=256, random_state=42,
                       width=mask.shape[0], height=mask.shape[0])
        wc.generate(article.text)
        plt.imshow(wc, interpolation="bilinear")
        plt.axis('off')
        animal = 'giraffe'
    else:
        mask = np.array(Image.open(Path('src/animalsgonewild/images/whale.jpg')))
        wc = WordCloud(stopwords=STOPWORDS, mask=mask, background_color="white", max_words=2000, max_font_size=256, random_state=42,
                       width=mask.shape[0], height=mask.shape[0])
        wc.generate(article.text)
        plt.imshow(wc, interpolation="bilinear")
        plt.axis('off')
        animal = 'whale'
    return animal
