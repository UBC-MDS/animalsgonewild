from animalsgonewild.animalsgonewild import textTransformer
from animalsgonewild.animalsgonewild import animalClassifier
import pytest

text = "one, one, one"
text1 = "test tests test for test"
text2 = "Before we can use pytest to run our test for us we need to add it as a development dependency of our package using the command poetry add --dev. A development dependency is a package that is not required by a user to use your package but is required for development purposes (like testing)"
text3 = "we can see that our test passed! We could add more tests for our package."
text4 = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
text5 = "one two three"
text6 = "should be the same"

def test_no_nouns():
    expected = "should be the same"
    actual = textTransformer(text6)
    assert actual == expected, "Transformer changed text that did not contain nouns"
    
def test_long_text():
    expected = "Lorem Ipsum is simply Giraffe Giraffe of the Giraffe and typesetting industry. Lorem Ipsum has been the industry's Giraffe Giraffe Giraffe ever since the 1500s, when an Giraffe Giraffe took Giraffe Giraffe of Giraffe and scrambled it to make Giraffe Giraffe Giraffe book. It has survived not only Giraffe centuries, but also the Giraffe into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the Giraffe of Letraset sheets containing Lorem Ipsum passages, and Giraffe recently with Giraffe publishing Giraffe Giraffe Aldus PageMaker including versions of Lorem Ipsum."
    actual = textTransformer(text4)
    assert actual == expected, "Transformer did not correctly transform long text"
    
def test_short_text():
    expected = 'Whale Whale Whale'
    actual = textTransformer(text5)
    assert actual == expected, "Transformer did not correctly transform short text"
    
def test_length():
    expected = 54
    actual = textTransformer(text2)
    assert len(actual.split()) == expected, "Transformer changed the text wordcount"
    
def test_input_error():
"""Check TypeError raised when the input is not string"""
with pytest.raises(TypeError):
    try_num = 111
    textTransformer(try_num)