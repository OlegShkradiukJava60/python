

from typing import Callable, Iterator


class NumberBox:
    def __init__(self):
        self.__data: list[int] = []

    def addNumber(self, num: int) -> None:
        self.__data.append(num)

    def removeNumber(self, num: int) -> int:
        for i, v in enumerate(self.__data):
            if v == num:
                self.__data.pop(i)
                return num
        return None  # type: ignore

    def removeNumbersPredicate(self, pred: Callable[[int], bool]) -> int:
        new_data: list[int] = []
        removed = 0
        for x in self.__data:
            if pred(x):
                removed += 1
            else:
                new_data.append(x)
        self.__data = new_data
        return removed

    def removeNumbersRange(self, min: int, max: int) -> int:
        return self.removeNumbersPredicate(lambda x: min <= x <= max)

    def __iter__(self) -> Iterator[int]:
        return iter(self.__data)

    def distinct(self) -> int:
        seen: set[int] = set()
        new_data: list[int] = []
        removed = 0
        for x in self.__data:
            if x in seen:
                removed += 1
            else:
                seen.add(x)
                new_data.append(x)
        self.__data = new_data
        return removed
