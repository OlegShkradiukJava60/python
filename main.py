from typing import List

def isSumTwo(numbers: List[int], target: int) -> bool:
    seen: set[int] = set()
    result: bool = False

    for num in numbers:
        other: int = target - num
        if other in seen:
            result = True
            break
        seen.add(num)

    return result


def maxNegativeRepr(numbers: List[int]) -> int:
    numbers_set: set[int] = set(numbers)
    max_value: int = -1

    for num in numbers:
        if num > 0 and -num in numbers_set:
            if num > max_value:
                max_value = num

    return max_value


if __name__ == "__main__":
    print(isSumTwo([1, 2, 3, 4], 4))   # True
    print(isSumTwo([1, 2, 3, 4], 2))   # False

    print(maxNegativeRepr([100, 4, 1, -1, -4, -100]))      # 100
    print(maxNegativeRepr([100, 4, 1, 1, 4, 100, -1]))     # 1
    print(maxNegativeRepr([100, 4, 1, 1, 4, 100, 1, -2]))  # -1
