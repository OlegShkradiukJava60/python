from dataclasses import dataclass, field
from sortedcontainers import SortedSet, SortedKeyList


@dataclass(order=True, unsafe_hash=True)
class Person:
    id: int
    age: int = field(compare=False)


prs1: Person = Person(123, 25)
prs2: Person = Person(100, 40)
prs3: Person = Person(50, 40)
print(f"prs1 > prs2 is {prs1 > prs2}")
print(f"{prs3} == Person(50, None) is {prs3 == Person(50, None)}")


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


club: Club = Club()
club.addPerson(prs1)
club.addPerson(prs2)
club.addPerson(prs3)
print("sorted by id -> ", club.getAllSortedId())
print("sorted by age, id -> ", club.getAllSortedAgeId())
print("age in [30, 40] -> ", club.getPersonsByAge(30, 40))


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
        res = []
        for w in self.__words[left:right]:
            if w.lower().startswith(pref):
                res.append(w)
        return res


d = Dictionary()
for w in ["Apple", "application", "app", "Ban", "banana", "Band", "АПП", "аппарат"]:
    d.addWord(w)
print("prefix 'app' ->", d.getWordsByPrefix("app"))
print("prefix 'BAN' ->", d.getWordsByPrefix("BAN"))
print("prefix 'ап' ->", d.getWordsByPrefix("ап"))
print("prefix '' ->", d.getWordsByPrefix(""))
