from newspaper import Article
from wordcloud import STOPWORDS
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

def wordCloud(link):
    """
    Inputs URL of a website to return the name and a wordcloud in the shape of the animal created using the text.

    Parameters
    ----------
    link: str
        URL of the webpage from which the animal shaped wordcloud is to be created

    Returns
    -------
    jpg
        a wordcloud image in the shape of the animal based on number of words in the article obtained from the URL.
    txt
        name of the animal associated with the jpg output.

    Example
    --------
    >>> wordCloud('https://www.britannica.com/place/Japan') 
    whale
    ![image]('animalsgonewild/images/whale.jpg')
    """
    if not isinstance(link, str):
        raise TypeError("Text input should be of type 'str' and a URL")

    article = Article(link)
    article.download()
    article.parse()
    article_length = len(article.text)
    
    if article_length < 300:
        mask = np.array(Image.open('animalsgonewild/images/duck.jpg'))
        wc = WordCloud(stopwords=STOPWORDS, mask=mask, background_color="white", max_words=2000, max_font_size=256, random_state=42, width=mask.shape[0], height=mask.shape[0])
        wc.generate(article.text)
        plt.imshow(wc, interpolation="bilinear")
        plt.axis('off')
        animal = 'duck'
    elif article_length < 2000:
        mask = np.array(Image.open('animalsgonewild/images/monkey.jpg'))
        wc = WordCloud(stopwords=STOPWORDS, mask=mask, background_color="white", max_words=2000, max_font_size=256, random_state=42, width=mask.shape[0], height=mask.shape[0])
        wc.generate(article.text)
        plt.imshow(wc, interpolation="bilinear")
        plt.axis('off')
        animal = 'monkey'
    elif article_length < 3000:
        mask = np.array(Image.open('animalsgonewild/images/giraffe.jpg'))
        wc = WordCloud(stopwords=STOPWORDS, mask=mask, background_color="white", max_words=2000, max_font_size=256, random_state=42, width=mask.shape[0], height=mask.shape[0])
        wc.generate(article.text)
        plt.imshow(wc, interpolation="bilinear")
        plt.axis('off')
        animal = 'giraffe'
    else:
        mask = np.array(Image.open('animalsgonewild/images/whale.jpg'))
        wc = WordCloud(stopwords=STOPWORDS, mask=mask, background_color="white", max_words=2000, max_font_size=256, random_state=42, width=mask.shape[0], height=mask.shape[0])
        wc.generate(article.text)
        plt.imshow(wc, interpolation="bilinear")
        plt.axis('off')
        animal = 'whale'
    return animal