from numb3rs import validate


def test_val():
    assert validate("256.127.12.127") == False
    assert validate("127.256.12.127") == False
    assert validate("12.127.256.127") == False
    assert validate("127.127.12.256") == False
    assert validate("127.127.12.255.222") == False
