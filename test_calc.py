from calc import add, get_num


def test_get_num():
    res = get_num(42)
    assert res == 42


def test_add():
    res = add(41, 1)
    assert res == 42


if __name__ == "__main__":
    test_get_num()
    test_add()
