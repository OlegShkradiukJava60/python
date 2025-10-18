
from main import NumberBox


def test_add_and_iter():
    nb = NumberBox()
    nb.addNumber(5)
    nb.addNumber(1)
    nb.addNumber(5)
    assert list(nb) == [5, 1, 5]


def test_removeNumber_found_and_missing():
    nb = NumberBox()
    nb.addNumber(2)
    nb.addNumber(3)
    nb.addNumber(2)
    assert nb.removeNumber(2) == 2
    assert list(nb) == [3, 2]
    assert nb.removeNumber(10) is None
    assert list(nb) == [3, 2]


def test_removeNumbersPredicate():
    nb = NumberBox()
    for x in [1, 2, 3, 4, 5, 6]:
        nb.addNumber(x)
    removed = nb.removeNumbersPredicate(lambda x: x % 2 == 0)
    assert removed == 3
    assert list(nb) == [1, 3, 5]


def test_removeNumbersRange():
    nb = NumberBox()
    for x in [10, 5, 7, 12, 5, 8]:
        nb.addNumber(x)
    removed = nb.removeNumbersRange(6, 10)
    assert removed == 3
    assert list(nb) == [5, 12, 5]


def test_distinct():
    nb = NumberBox()
    for x in [1, 2, 1, 3, 2, 2, 4, 4, 4]:
        nb.addNumber(x)
    removed = nb.distinct()
    assert list(nb) == [1, 2, 3, 4]
    assert removed == 5


if __name__ == "__main__":
    test_add_and_iter()
    test_removeNumber_found_and_missing()
    test_removeNumbersPredicate()
    test_removeNumbersRange()
    test_distinct()
    print("All tests passed!")
