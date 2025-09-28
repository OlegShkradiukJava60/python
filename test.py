import unittest
from main import isSumTwo, maxNegativeRepr

class TestWork(unittest.TestCase):
    def test_isSumTwo_case1(self):
        result: bool = isSumTwo([1, 2, 3, 4], 4)
        self.assertEqual(result, True)

    def test_isSumTwo_case2(self):
        result: bool = isSumTwo([1, 2, 3, 4], 2)
        self.assertEqual(result, False)

    def test_isSumTwo_case3(self):
        result: bool = isSumTwo([5, -1, 7, 2], 6)
        self.assertEqual(result, True)

    def test_isSumTwo_case4(self):
        result: bool = isSumTwo([], 5)
        self.assertEqual(result, False)

    def test_maxNegativeRepr_case1(self):
        result: int = maxNegativeRepr([100, 4, 1, -1, -4, -100])
        self.assertEqual(result, 100)

    def test_maxNegativeRepr_case2(self):
        result: int = maxNegativeRepr([100, 4, 1, 1, 4, 100, -1])
        self.assertEqual(result, 1)

    def test_maxNegativeRepr_case3(self):
        result: int = maxNegativeRepr([100, 4, 1, 1, 4, 100, 1, -2])
        self.assertEqual(result, -1)

    def test_maxNegativeRepr_case4(self):
        result: int = maxNegativeRepr([1, 2, 3])
        self.assertEqual(result, -1)

    def test_maxNegativeRepr_case5(self):
        result: int = maxNegativeRepr([-1, -2, -3])
        self.assertEqual(result, -1)


if __name__ == "__main__":
    unittest.main()
