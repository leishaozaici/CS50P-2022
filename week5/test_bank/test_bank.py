from bank import value


def test_hello():
    assert value("hello world") == 0


def test_startsh():
    assert value("haaa") == 20


def test_extra():
    assert value("aabb") == 100


def test_nocase():
    assert value("aabBB") == 100
    assert value("Hello") == 0
