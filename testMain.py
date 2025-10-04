import unittest
from main import Person, Club, Dictionary


class TestClub(unittest.TestCase):
    def setUp(self):
        self.club = Club()
        for p in [Person(3, 20), Person(1, 30), Person(2, 30), Person(5, 40), Person(4, 40)]:
            self.club.addPerson(p)

    def test_addPerson_unique(self):
        with self.assertRaises(ValueError):
            self.club.addPerson(Person(3, 99))

    def test_getAllSortedId(self):
        self.assertEqual(
            [p.id for p in self.club.getAllSortedId()], [1, 2, 3, 4, 5])

    def test_getAllSortedAgeId(self):
        self.assertEqual([(p.age, p.id) for p in self.club.getAllSortedAgeId()],
                         [(20, 3), (30, 1), (30, 2), (40, 4), (40, 5)])

    def test_getPersonsByAge_middle(self):
        self.assertEqual([(p.age, p.id) for p in self.club.getPersonsByAge(25, 35)],
                         [(30, 1), (30, 2)])

    def test_getPersonsByAge_edges(self):
        self.assertEqual([(p.age, p.id) for p in self.club.getPersonsByAge(20, 40)],
                         [(20, 3), (30, 1), (30, 2), (40, 4), (40, 5)])

    def test_getPersonsByAge_none(self):
        self.assertEqual(self.club.getPersonsByAge(41, 50), [])

    def test_getPersonsByAge_min_gt_max(self):
        self.assertEqual(self.club.getPersonsByAge(50, 40), [])


class TestDictionary(unittest.TestCase):
    def setUp(self):
        self.d = Dictionary()
        for w in ["Apple", "application", "app", "Ban", "banana", "Band", "АПП", "аппарат"]:
            self.d.addWord(w)

    def test_addWord_duplicates_case_insensitive(self):
        with self.assertRaises(ValueError):
            self.d.addWord("APP")
        with self.assertRaises(ValueError):
            self.d.addWord("banana")

    def test_getWordsByPrefix_basic(self):
        self.assertEqual(self.d.getWordsByPrefix("app"),
                         ["app", "Apple", "application"])

    def test_getWordsByPrefix_case_insensitive(self):
        self.assertEqual(self.d.getWordsByPrefix(
            "BAN"), ["Ban", "banana", "Band"])

    def test_getWordsByPrefix_non_latin(self):
        self.assertEqual(self.d.getWordsByPrefix("ап"), ["АПП", "аппарат"])

    def test_getWordsByPrefix_empty_returns_all(self):
        self.assertEqual(
            self.d.getWordsByPrefix(""),
            ["app", "Apple", "application", "Ban",
                "banana", "Band", "АПП", "аппарат"]
        )


if __name__ == "__main__":
    unittest.main()
