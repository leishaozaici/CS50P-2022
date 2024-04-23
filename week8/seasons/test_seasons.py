from seasons import convert


def test_main():
    assert (
        convert("2022-11-17")
        == "Five hundred twenty-five thousand, six hundred minutes"
    )
