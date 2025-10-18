

from main import MyStackInt


def test_push_and_pop():
    s = MyStackInt()
    s.push(10)
    s.push(5)
    s.push(20)
    assert s.pop() == 20
    assert s.pop() == 5
    assert s.pop() == 10


def test_pop_empty():
    s = MyStackInt()
    try:
        s.pop()
        assert False, "Expected IndexError"
    except IndexError:
        assert True


def test_max():
    s = MyStackInt()
    s.push(2)
    s.push(1)
    s.push(5)
    s.push(3)
    assert s.max() == 5
    s.pop()
    assert s.max() == 5
    s.pop()
    assert s.max() == 2


def test_max_empty():
    s = MyStackInt()
    try:
        s.max()
        assert False, "Expected IndexError"
    except IndexError:
        assert True


if __name__ == "__main__":
    test_push_and_pop()
    test_pop_empty()
    test_max()
    test_max_empty()
    print("All tests passed!")
