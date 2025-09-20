
def bSearchSortedList(lst: list[int], num: int) -> int:

    left: int = 0
    right: int = len(lst) - 1
    defp: int = len(lst)

    while left <= right:
        middle: int = (left + right) // 2
        if num <= lst[middle]:
            defp = middle
            right = middle - 1
        else:
            left = middle + 1
    if defp < len(lst) and lst[defp] == num:
        return defp
    else:
        return -(defp) - 1


numbers1: list[int] = [1, 5, 20, 20, 20, 20, 20, 30, 100]
print(bSearchSortedList(numbers1, 4))  # -2

numbers2: list[int] = [20, 20, 20, 20, 20, 20]
print(bSearchSortedList(numbers2, 20))  # 0

numbers3: list[int] = [20, 30, 40, 50, 60]
print(bSearchSortedList(numbers3, 45))  # -4
