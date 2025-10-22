from typing import Generic, TypeVar
T = TypeVar("T")


class MyArray(Generic[T]):
    def __init__(self, length: int):
        if length < 1:
            raise ValueError("amount of items cannot be less than 1")
        self.allValue: T = None
        self.indexValue: dict[int, T] = {}
        self.length: int = length

    def __checkIndex(self, index: int):
        if (index < 0 or index >= self.length):
            raise IndexError(index)

    def setAll(self, value: T):
        self.allValue = value
        self.indexValue = {}

    def set(self, value: T, index: int):
        self.__checkIndex(index)
        self.indexValue[index] = value

    def get(self, index: int):
        self.__checkIndex(index)
        return self.indexValue.get(index, self.allValue)
