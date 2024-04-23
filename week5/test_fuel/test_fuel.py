from fuel import convert
from fuel import gauge
from pytest import raises


def test_con():
    assert convert("5/10") == 50
    assert convert("0/10") == 0
    with raises(ValueError):
        convert("a/b")
        convert("5/4")
        convert("2.5/4")
    with raises(ZeroDivisionError):
        convert("1/0")


def test_gau():
    assert gauge(50) == "50%"
    assert gauge(0) == "E"
    assert gauge(99) == "F"
    assert gauge(1) == "E"
