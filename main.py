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
        # adds person
        # raises ValueError if person already exists
        if person in self.__sortedSet:
            raise ValueError(f"person with id {person.id} already exists")
        self.__sortedSet.add(person)
        self.__sortedKeyList.add(person)

    def getAllSortedId(self) -> list[Person]:
        return list(self.__sortedSet)

    def getAllSortedAgeId(self) -> list[Person]:
        return list(self.__sortedKeyList)


club: Club = Club()
club.addPerson(prs1)
club.addPerson(prs2)
club.addPerson(prs3)
print("sorted by id -> ", club.getAllSortedId())
print("sorted by age, id -> ", club.getAllSortedAgeId())
