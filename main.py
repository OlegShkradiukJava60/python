from dataclasses import dataclass, field
from sortedcontainers import SortedSet, SortedKeyList
import unittest


@dataclass(order=True, unsafe_hash=True)
class Person:
    id: int
    age: int = field(compare=False)


class Club:
    def __init__(self):
        self.__sortedSet = SortedSet()
        self.__sortedKeyList = SortedKeyList(key=lambda p: (p.age, p.id))

    def addPerson(self, person: Person):
        if person in self.__sortedSet:
            raise ValueError(f"person with id {person.id} already exists")
        self.__sortedSet.add(person)
        self.__sortedKeyList.add(person)

    def getAllSortedId(self) -> list[Person]:
        return list(self.__sortedSet)

    def getAllSortedAgeId(self) -> list[Person]:
        return list(self.__sortedKeyList)

    def getPersonsByAge(self, minAge: int, maxAge: int) -> list[Person]:
        if minAge > maxAge:
            return []
        MIN_ID = -10**18
        MAX_ID = 10**18
        left = self.__sortedKeyList.bisect_key_left((minAge, MIN_ID))
        right = self.__sortedKeyList.bisect_key_right((maxAge, MAX_ID))
        return list(self.__sortedKeyList[left:right])


class Dictionary:
    def __init__(self):
        self.__words = SortedKeyList(key=lambda w: w.lower())
        self.__lower_set = set()

    def addWord(self, word: str):
        low = word.lower()
        if low in self.__lower_set:
            raise ValueError(
                f'word "{word}" already exists (case-insensitive)')
        self.__lower_set.add(low)
        self.__words.add(word)

    def getWordsByPrefix(self, prefix: str) -> list[str]:
        if prefix == "":
            return list(self.__words)
        pref = prefix.lower()
        upper_pref = pref + chr(0x10FFFF)
        left = self.__words.bisect_left(pref)
        right = self.__words.bisect_right(upper_pref)
        result = []
        for w in self.__words[left:right]:
            if w.lower().startswith(pref):
                result.append(w)
        return result


if __name__ == "__main__":
    prs1: Person = Person(123, 25)
    prs2: Person = Person(100, 40)
    prs3: Person = Person(50, 40)
    print(f"prs1 > prs2 is {prs1 > prs2}")
    print(f"{prs3} == Person(50, None) is {prs3 == Person(50, None)}")
    club: Club = Club()
    club.addPerson(prs1)
    club.addPerson(prs2)
    club.addPerson(prs3)
    print("sorted by id -> ", club.getAllSortedId())
    print("sorted by age, id -> ", club.getAllSortedAgeId())
    print("age in [30, 40] -> ", club.getPersonsByAge(30, 40))


class TestClub(unittest.TestCase):
    def setUp(self):
        self.club = Club()
        self.p1 = Person(3, 20)
        self.p2 = Person(1, 30)
        self.p3 = Person(2, 30)
        self.p4 = Person(5, 40)
        self.p5 = Person(4, 40)
        for p in [self.p1, self.p2, self.p3, self.p4, self.p5]:
            self.club.addPerson(p)

    def test_addPerson_unique(self):
        with self.assertRaises(ValueError):
            self.club.addPerson(Person(3, 99))

    def test_getAllSortedId(self):
        ids = [p.id for p in self.club.getAllSortedId()]
        self.assertEqual(ids, [1, 2, 3, 4, 5])

    def test_getAllSortedAgeId(self):
        pairs = [(p.age, p.id) for p in self.club.getAllSortedAgeId()]
        self.assertEqual(pairs, [(20, 3), (30, 1), (30, 2), (40, 4), (40, 5)])

    def test_getPersonsByAge_middle_range(self):
        result = self.club.getPersonsByAge(25, 35)
        self.assertEqual([(p.age, p.id) for p in result], [(30, 1), (30, 2)])

    def test_getPersonsByAge_edges_inclusive(self):
        result = self.club.getPersonsByAge(20, 40)
        self.assertEqual([(p.age, p.id) for p in result],
                         [(20, 3), (30, 1), (30, 2), (40, 4), (40, 5)])

    def test_getPersonsByAge_no_results(self):
        result = self.club.getPersonsByAge(41, 50)
        self.assertEqual(result, [])

    def test_getPersonsByAge_min_greater_than_max(self):
        result = self.club.getPersonsByAge(50, 40)
        self.assertEqual(result, [])


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
        words = self.d.getWordsByPrefix("app")
        self.assertEqual(words, ["app", "Apple", "application"])

    def test_getWordsByPrefix_case_insensitive(self):
        words = self.d.getWordsByPrefix("BAN")
        self.assertEqual(words, ["Ban", "banana", "Band"])

    def test_getWordsByPrefix_non_latin(self):
        words = self.d.getWordsByPrefix("ап")
        self.assertEqual(words, ["АПП", "аппарат"])

    def test_getWordsByPrefix_empty_returns_all(self):
        words = self.d.getWordsByPrefix("")
        self.assertEqual(
            words,
            ["app", "Apple", "application", "Ban",
                "banana", "Band", "АПП", "аппарат"]
        )
