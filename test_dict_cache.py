from main import MySortedDict, DictCache
import unittest
from main import MyDict


class TestMyDict(unittest.TestCase):
    def test_set_get_len(self):
        d = MyDict[str, int]()
        d['a'] = 1
        d['b'] = 2
        self.assertEqual(d['a'], 1)
        self.assertEqual(d['b'], 2)
        self.assertEqual(len(d), 2)

    def test_override_on_set(self):
        d = MyDict[str, int]()
        d['a'] = 1
        d['a'] = 5
        self.assertEqual(d['a'], 5)
        self.assertEqual(len(d), 1)

    def test_get_and_default(self):
        d = MyDict[str, int]()
        self.assertIsNone(d.get('x'))
        self.assertEqual(d.get('x', 10), 10)
        with self.assertRaises(KeyError):
            _ = d['x']

    def test_setdefault(self):
        d = MyDict[str, int]()
        self.assertEqual(d.setdefault('a', 7), 7)
        self.assertEqual(d.setdefault('a', 9), 7)
        self.assertEqual(d['a'], 7)

    def test_items_keys_values(self):
        d = MyDict[str, int]()
        d['a'] = 1
        d['b'] = 2
        self.assertEqual(set(d.items()), {('a', 1), ('b', 2)})
        self.assertEqual(set(d.keys()), {'a', 'b'})
        self.assertEqual(set(d.values()), {1, 2})

    def test_update_and_pop(self):
        d = MyDict[str, int]()
        d.update('a', 3)
        self.assertEqual(d['a'], 3)
        self.assertEqual(d.pop('a'), 3)
        self.assertEqual(len(d), 0)
        self.assertEqual(d.pop('x', 100), 100)
        with self.assertRaises(KeyError):
            d.pop('x')


if __name__ == "__main__":
    unittest.main()


class TestMySortedDict(unittest.TestCase):
    def test_set_get_sorted_and_len(self):
        d = MySortedDict[str, int]()
        d['b'] = 2
        d['a'] = 1
        d['c'] = 3
        self.assertEqual(d['a'], 1)
        self.assertEqual(d['b'], 2)
        self.assertEqual(d['c'], 3)
        self.assertEqual(d.items(), [('a', 1), ('b', 2), ('c', 3)])
        self.assertEqual(d.keys(), ['a', 'b', 'c'])
        self.assertEqual(d.values(), [1, 2, 3])
        self.assertEqual(len(d), 3)

    def test_override_update_pop(self):
        d = MySortedDict[str, int]()
        d['a'] = 1
        d['a'] = 5
        self.assertEqual(d['a'], 5)
        d.update('b', 2)
        self.assertEqual(d['b'], 2)
        self.assertEqual(d.pop('a'), 5)
        with self.assertRaises(KeyError):
            _ = d['a']
        self.assertEqual(d.pop('x', 100), 100)
        with self.assertRaises(KeyError):
            d.pop('x')

    def test_get_and_setdefault(self):
        d = MySortedDict[str, int]()
        self.assertIsNone(d.get('x'))
        self.assertEqual(d.get('x', 9), 9)
        self.assertEqual(d.setdefault('k', 7), 7)
        self.assertEqual(d.setdefault('k', 10), 7)
        self.assertEqual(d['k'], 7)

    def test_bisect_and_peekitem(self):
        d = MySortedDict[int, str]()
        for k in [10, 20, 30]:
            d[k] = str(k)
        self.assertEqual(d.bisect_left(5), 0)
        self.assertEqual(d.bisect_left(20), 1)
        self.assertEqual(d.bisect_right(20), 2)
        self.assertEqual(d.peekitem(0), (10, '10'))
        self.assertEqual(d.peekitem(1), (20, '20'))
        self.assertEqual(d.peekitem(-1), (30, '30'))
        with self.assertRaises(IndexError):
            d.peekitem(3)
        with self.assertRaises(IndexError):
            d.peekitem(-4)


class TestDictCacheProvided(unittest.TestCase):
    def setUp(self):
        self.dictCache: DictCache[str, int] = DictCache(2)
        self.dictCache['a'] = 1
        self.dictCache['b'] = 2

    def test_inserting_removes_eldest(self):
        self.dictCache['c'] = 30
        with self.assertRaises(KeyError):
            self.dictCache['a']
        self.assertEqual(2, self.dictCache['b'])
        self.assertEqual(30, self.dictCache['c'])

    def test_access_order(self):
        self.assertEqual(1, self.dictCache['a'])
        self.dictCache['c'] = 30
        with self.assertRaises(KeyError):
            self.dictCache['b']
        self.assertEqual(1, self.dictCache['a'])
        self.assertEqual(30, self.dictCache['c'])

    def test_update_order(self):
        self.dictCache['a'] = 10
        self.dictCache['c'] = 30
        with self.assertRaises(KeyError):
            self.dictCache['b']
        self.assertEqual(10, self.dictCache['a'])
        self.assertEqual(30, self.dictCache['c'])


if __name__ == "__main__":
    unittest.main()
