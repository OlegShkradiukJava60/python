
class MyStackInt:
    def __init__(self):
        self.__stack: list[int] = []
        self.__max_stack: list[int] = []

    def push(self, num: int) -> None:
        self.__stack.append(num)
        if not self.__max_stack or num >= self.__max_stack[-1]:
            self.__max_stack.append(num)
        else:
            self.__max_stack.append(self.__max_stack[-1])

    def pop(self) -> int:
        if not self.__stack:
            raise IndexError("pop from empty stack")
        self.__max_stack.pop()
        return self.__stack.pop()

    def max(self) -> int:
        if not self.__stack:
            raise IndexError("max from empty stack")
        return self.__max_stack[-1]
