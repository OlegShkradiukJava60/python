from sortedcontainers import SortedKeyList
# used for lists/arrays with  frequent add/remove operaions

# method add has complexity O[LogN]
sortedList: SortedKeyList[str] = SortedKeyList(key=str.casefold)
sortedList.add("AbCd")
sortedList.add("aBc")
sortedList.add("abcd")
sortedList.add("ac")


print(sortedList)
