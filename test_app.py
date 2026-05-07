from calc import get_num, add


def test_app():
    a = get_num(1)
    b = get_num(41)
    res = add(a, b)
    assert res == 42


if __name__ == "__main__":
    test_app()
