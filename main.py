
def bSearchSortedList(lst: list[int], num: int) -> int:
    # takes sorted list and a number
    # returns index of the number if exists, otherwise -1
    left: int = 0
    right: int = len(lst) - 1
    middle: int = (left + right) // 2
    while left <= right and lst[middle] != num:
        if num < lst[middle]:
            right = middle - 1
        else:
            left = middle + 1
        middle = (right + left) // 2
    return middle if left <= right else -1


numbers: list[int] = [1, 5, 20, 20, 20, 20, 20, 30, 100]
print(bSearchSortedList(numbers, 4))
