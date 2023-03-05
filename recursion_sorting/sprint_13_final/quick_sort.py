# 83408385

from typing import List, Tuple, Any


class Participant:
    def __init__(self, name: str, solved: str, errors: str) -> None:
        self.name: str = name
        self.solved: int = -int(solved)
        self.errors: int = int(errors)

    def __lt__(self, obj):
        return(
            (self.solved, self.errors, self.name) <
            (obj.solved, obj.errors, obj.name)
        )

    def __str__(self) -> str:
        return f"{self.name}"


def partition(data: List[Participant], left: int, right: int) -> Tuple[List[Participant], int]:
    pivot = data[(left + right) // 2]

    while left <= right:

        while data[left] < pivot:
            left += 1

        while data[right] > pivot:
            right -= 1

        if left >= right:
            break

        data[left], data[right] = data[right], data[left]
        left += 1
        right -= 1

    return data, right


def quick_sort(data: List[Participant], left: int, right: int):
    if left < right:
        data, pivot = partition(data, left, right)
        data = quick_sort(data, left, pivot)
        data = quick_sort(data, pivot + 1, right)
    return data


def main() -> None:
    amount: int = int(input())
    data: List[Participant] = [Participant(*input().split()) for _ in range(amount)]
    quick_sort(data, 0, amount - 1)
    print(*data, sep="\n")


if __name__ == '__main__':
    main()