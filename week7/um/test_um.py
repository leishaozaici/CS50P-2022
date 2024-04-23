from um import count


def test_count():
    assert count("Um") == 1
    assert count("um") == 1
    assert count("UMAB UM") == 1
    assert count("Um, thanks, um...") == 2
