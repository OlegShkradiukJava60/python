
from typing import Generic, TypeVar

T = TypeVar("T")


class MyArray(Generic[T]):
    def __init__(self, length: int) -> None:
        if length < 1:
            raise ValueError("amount of items cannot be less than 1")
        self.length: int = length
        self.allValue: T | None = None
        self.indexValue: dict[int, T] = {}

    def __checkIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            raise IndexError(index)

    def setAll(self, value: T) -> None:
        self.allValue = value
        self.indexValue = {}  # O(1)

    def set(self, value: T, index: int) -> None:
        self.__checkIndex(index)
        self.indexValue[index] = value  # O(1)

    def get(self, index: int) -> T | None:
        self.__checkIndex(index)
        return self.indexValue.get(index, self.allValue)  # O(1)
