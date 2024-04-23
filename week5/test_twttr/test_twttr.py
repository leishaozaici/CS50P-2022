from twttr import shorten


def test_vowel():
    assert shorten("aeid") == "d"
    assert shorten("aeId") == "d"
    assert shorten("aEid") == "d"


def test_number():
    assert shorten("123ai") == "123"


def test_punctuation():
    assert shorten(".;aei") == ".;"
