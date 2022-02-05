from animalsgonewild.animalsgonewild import wordCloud

text_wordcloud = "https://www.canada.ca/en.html"
text_wordcloud1 = "http://www.calendar.ubc.ca/"
text_wordcloud2 = "https://en.wikipedia.org/wiki/Outside_(magazine)"
text_wordcloud3 = "https://www.britannica.com/place/Japan"

def test_duckshapedwordcloud():
    expected = 'duck'
    actual = wordCloud(text_wordcloud)
    assert actual == expected, "WordCloud failed to output duck!"

def test_monkeyshapedwordcloud():
    expected = 'monkey'
    actual = wordCloud(text_wordcloud1)
    assert actual == expected, "WordCloud failed to output monkey!"

def test_giraffeshapedwordcloud():
    expected = 'giraffe'
    actual = wordCloud(text_wordcloud2)
    assert actual == expected, "WordCloud failed to output giraffe!"

def test_whaleshapedwordcloud():
    expected = 'whale'
    actual = wordCloud(text_wordcloud3)
    assert actual == expected, "WordCloud failed to output whale!"

def test_input_error_wordcloud():
    """Check TypeError raised when the input is not string"""
    with pytest.raises(TypeError):
        number = 111
        wordCloud(number)