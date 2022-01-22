from animalsgonewild.animalsgonewild import animalType
from pathlib import Path
from PIL import Image

big_words = "inscrutable or at least esoteric language."
small_words = "hi my name is john and I am simple."
formatted_text = open(Path("tests/bigwords.txt")).read()

def test_big_words():
    expected = Image.open("tests/smart_Duck.jpeg")
    actual = animalType("Duck", big_words)
    assert expected == actual, "Failed to return smart Duck"

def test_small_words():
    expected = Image.open("tests/dumb_Giraffe.jpeg")
    actual = animalType("Giraffe", small_words)
    assert expected == actual, "Failed to return dumb Giraffe"
        
def test_file_text():
    expected = Image.open("tests/smart_Whale.jpeg")
    actual = animalType("Whale", formatted_text)
    assert expected == actual, "Failed to return smart Whale"