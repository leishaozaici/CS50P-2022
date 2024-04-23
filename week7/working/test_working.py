from working import convert
from pytest import raises


def test_con1():
    assert convert("11 AM to 9 PM") == "11:00 to 21:00"
    with raises(ValueError):
        convert("9:00 AM 5:00 PM")
    with raises(ValueError):
        convert("9:70 AM to 6:60 PM")
