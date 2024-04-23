from plates import is_valid


def test_length():
    assert is_valid("AAA2222") == False
    assert is_valid("A") == False


def test_true():
    assert is_valid("CS50") == True


def test_leastletter():
    assert is_valid("A123") == False


def test_nospace():
    assert is_valid("A. 123") == False


def test_zero():
    assert is_valid("CS05") == False


def test_middlenumber():
    assert is_valid("CS50P") == False


def test_alphanumeric():
    assert is_valid("OP..") == False
