from collections import OrderedDict
from dataclasses import dataclass, field
from typing import Generic, Hashable, TypeVar
from sortedcontainers import SortedSet

K = TypeVar('K', bound=Hashable)
V = TypeVar("V")


@dataclass(order=True, frozen=True)
class Entry(Generic[K, V]):
    key: K
    value: V = field(compare=False, hash=False)

    def __str__(self):
        return f"'{self.key}': {self.value}"


class MyDict(Generic[K, V]):
    def __init__(self):
        self.__entries: set[Entry[K, V]] = set()

    def __getitem__(self, key: K) -> V:
        entry: Entry[K, V] | None = self.__getEntryByKey(key)
        if not entry:
            raise KeyError(key)
        return entry.value

    def __setitem__(self, key: K, value: V):
        probe: Entry[K, V] = Entry(key, value)
        self.__entries.discard(probe)
        self.__entries.add(probe)

    def __getEntryByKey(self, key: K) -> Entry[K, V] | None:
        res: Entry[K, V] | None = None
        probe: Entry[K, V] = Entry(key, None)
        if probe in self.__entries:
            res = next((e for e in self.__entries if e == probe))
        return res

    def __str__(self):
        return '{' + ", ".join([str(e) for e in self.__entries]) + '}'

    def __len__(self):
        return len(self.__entries)

    def setdefault(self, key: K, default: V = None):
        entry = self.__getEntryByKey(key)
        if entry:
            return entry.value
        self[key] = default
        return default

    def get(self, key: K, default: V = None):
        entry = self.__getEntryByKey(key)
        return entry.value if entry else default

    def items(self) -> list[tuple[K,  V]]:
        return [(e.key, e.value) for e in self.__entries]

    def keys(self) -> list[K]:
        return [e.key for e in self.__entries]

    def values(self) -> list[V]:
        return [e.value for e in self.__entries]

    def update(self, key: K, value: V):
        self[key] = value

    _sentinel = object()

    def pop(self, key: K, default=_sentinel) -> V:
        probe: Entry[K, V] = Entry(key, None)
        if probe in self.__entries:
            entry = next(e for e in self.__entries if e == probe)
            self.__entries.remove(entry)
            return entry.value
        if default is self._sentinel:
            raise KeyError(key)
        return default


class MySortedDict(Generic[K, V]):
    def __init__(self):
        self.__entries: SortedSet[Entry[K, V]] = SortedSet()

    def __getitem__(self, key: K) -> V:
        probe: Entry[K, V] = Entry(key, None)
        i = self.__entries.bisect_left(probe)
        if i == len(self.__entries) or self.__entries[i] != probe:
            raise KeyError(key)
        return self.__entries[i].value

    def __setitem__(self, key: K, value: V):
        probe: Entry[K, V] = Entry(key, None)
        self.__entries.discard(probe)
        self.__entries.add(Entry(key, value))

    def __str__(self):
        return '{' + ", ".join([str(e) for e in self.__entries]) + '}'

    def __len__(self):
        return len(self.__entries)

    def setdefault(self, key: K, default: V = None):
        probe: Entry[K, V] = Entry(key, None)
        i = self.__entries.bisect_left(probe)
        if i != len(self.__entries) and self.__entries[i] == probe:
            return self.__entries[i].value
        self.__entries.add(Entry(key, default))
        return default

    def get(self, key: K, default: V = None):
        probe: Entry[K, V] = Entry(key, None)
        i = self.__entries.bisect_left(probe)
        if i != len(self.__entries) and self.__entries[i] == probe:
            return self.__entries[i].value
        return default

    def items(self) -> list[tuple[K,  V]]:
        return [(e.key, e.value) for e in self.__entries]

    def keys(self) -> list[K]:
        return [e.key for e in self.__entries]

    def values(self) -> list[V]:
        return [e.value for e in self.__entries]

    def update(self, key: K, value: V):
        self[key] = value

    _sentinel = object()

    def pop(self, key: K, default=_sentinel) -> V:
        probe: Entry[K, V] = Entry(key, None)
        i = self.__entries.bisect_left(probe)
        if i != len(self.__entries) and self.__entries[i] == probe:
            entry = self.__entries[i]
            self.__entries.discard(probe)
            return entry.value
        if default is self._sentinel:
            raise KeyError(key)
        return default

    def bisect_left(self, key: K) -> int:

        return self.__entries.bisect_left(Entry(key, None))

    def bisect_right(self, key: K) -> int:

        return self.__entries.bisect_right(Entry(key, None))

    def peekitem(self, ind: int) -> tuple[K, V]:
        n = len(self.__entries)
        j = ind if ind >= 0 else n + ind
        if j < 0 or j >= n:
            raise IndexError("index out of range")
        e = self.__entries[j]
        return (e.key, e.value)


class DictCache(OrderedDict[K, V]):
    def __init__(self, maxsize=128):
        super().__init__()
        self.maxsize = maxsize

    def __getitem__(self, key):
        val = super().__getitem__(key)
        self.move_to_end(key)
        return val

    def __setitem__(self, key, value):
        if key in self:
            super().__setitem__(key, value)
            self.move_to_end(key)
            return
        if len(self) >= self.maxsize:
            self.popitem(last=False)
        super().__setitem__(key, value)
