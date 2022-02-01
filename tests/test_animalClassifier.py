from animalsgonewild.animalsgonewild import animalClassifier
import pytest

text = "one, one, one"
text1 = "test tests test for test"
text2 = "Before we can use pytest to run our test for us we need to add it as a development dependency of our package using the command poetry add --dev. A development dependency is a package that is not required by a user to use your package but is required for development purposes (like testing)"
text3 = "we can see that our test passed! We could add more tests for our package."

def test_duck():
    expected = 'Duck'
    actual = animalClassifier(text)
    assert actual == expected, "Classifier failed to output Duck!"

def test_monkey():
    expected = 'Monkey'
    actual = animalClassifier(text1)
    assert actual == expected, "Classifier failed to output Monkey!"

def test_giraffe():
    expected = 'Giraffe'
    actual = animalClassifier(text2)
    assert actual == expected, "Classifier failed to output Giraffe!"

def test_whale():
    expected = 'Whale'
    actual = animalClassifier(text3)
    assert actual == expected, "Classifier failed to output Whale!"

def test_input_error():
    """Check TypeError raised when the input is not string"""
    with pytest.raises(TypeError):
        try_num = 111
        animalClassifier(try_num)