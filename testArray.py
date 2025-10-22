

import unittest as ut
from main import MyStackInt


class TestMyStackInt(ut.TestCase):
    def setUp(self) -> None:
        self.stack = MyStackInt()
        self.stack.push(2)
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(4)
        self.empty = MyStackInt()

    def test_pop_order(self) -> None:
        self.assertEqual(self.stack.pop(), 4)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)
        self.assertEqual(self.stack.pop(), 2)
        self.assertRaises(IndexError, self.stack.pop)

    def test_max_basic(self) -> None:
        self.assertEqual(self.stack.max(), 4)

    def test_max_raises_when_empty(self) -> None:
        self.assertRaises(IndexError, self.empty.max)

    def test_push_of_bigger_value_updates_max(self) -> None:
        self.stack.push(100)
        self.assertEqual(self.stack.max(), 100)

    def test_push_of_smaller_value_keeps_max(self) -> None:
        self.stack.push(1)
        self.stack.push(-100)
        self.assertEqual(self.stack.max(), 4)

    def test_pop_of_current_max_moves_to_prev(self) -> None:
        self.assertEqual(self.stack.pop(), 4)
        self.assertEqual(self.stack.max(), 2)

    def test_duplicate_max_handling(self) -> None:
        s = MyStackInt()
        for x in [5, 3, 5]:
            s.push(x)
        self.assertEqual(s.max(), 5)
        s.pop()
        self.assertEqual(s.max(), 5)
        s.pop()
        self.assertEqual(s.max(), 5)
        s.pop()
        self.assertRaises(IndexError, s.max)

    def test_negative_and_zero(self) -> None:
        s = MyStackInt()
        for x in [0, -1, -1, -5]:
            s.push(x)
        self.assertEqual(s.max(), 0)
        s.pop()
        s.pop()
        self.assertEqual(s.max(), 0)

    def test_peek_and_peek_raises(self) -> None:
        self.assertEqual(self.stack.peek(), 4)
        self.assertEqual(self.stack.pop(), 4)
        self.assertEqual(self.stack.peek(), 2)
        self.assertRaises(IndexError, self.empty.peek)


if __name__ == "__main__":
    ut.main(verbosity=2)
