
from main import MyArray
from unittest import TestCase, main

LENGTH: int = 10000000000


class TestMyArray(TestCase):
    def setUp(self):
        array: MyArray[int] = MyArray(LENGTH)
        array.set(100, 0)
        array.set(-60, LENGTH // 2)
        array.set(80, LENGTH - 1)
        self.array = array

    def test_initial_setup(self):
        self.assertEqual(None, self.array.get(1))
        self.assertEqual(100, self.array.get(0))
        self.assertEqual(80, self.array.get(LENGTH - 1))
        self.assertEqual(-60, self.array.get(LENGTH // 2))

    def test_after_set_all(self):
        self.array.setAll(50)
        self.assertEqual(50, self.array.get(1))
        self.assertEqual(50, self.array.get(0))
        self.assertEqual(50, self.array.get(LENGTH - 1))
        self.assertEqual(50, self.array.get(LENGTH // 2))

    def test_index_error(self):
        self.assertRaises(IndexError, lambda: self.array.set(10, LENGTH))
        self.assertRaises(IndexError, lambda: self.array.get(-1))


if __name__ == "__main__":
    main()
