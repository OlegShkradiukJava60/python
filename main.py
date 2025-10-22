from array import array


class MyStackInt:
    def __init__(self):
        self._data = array('i')
        self._max_idx = array('i')

    def __len__(self) -> int:
        return len(self._data)

    def _index_of_max(self):
        if not self._max_idx:
            raise IndexError("max from empty stack")
        return self._max_idx[-1]

    def push(self, val: int):
        self._data.append(val)
        i = len(self._data) - 1
        if not self._max_idx:
            self._max_idx.append(i)
            return
        current_max_index = self._max_idx[-1]
        if val >= self._data[current_max_index]:
            self._max_idx.append(i)

    def pop(self):
        if not self._data:
            raise IndexError("pop from empty stack")
        i = len(self._data) - 1
        result = self._data.pop()
        if self._max_idx and self._max_idx[-1] == i:
            self._max_idx.pop()
        return result

    def max(self):
        return self._data[self._index_of_max()]

    def peek(self):
        if not self._data:
            raise IndexError("peek from empty stack")
        return self._data[-1]
