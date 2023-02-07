# ID 81849212
from typing import List, Tuple

INFINITY = float('inf')
MAX_SEQ_ZEROS = 10000

def nearest_zero(lenght: int, number_street: List[int]) -> List[int]:
    exit_function: bool = False
    zeros: List[int] = [idx for idx, num in enumerate(number_street) if num == 0]
    distance: List[int] = [0] * lenght

    if not zeros:
        return number_street

    if (len(zeros) == len(number_street) - 1
            and len(number_street) > MAX_SEQ_ZEROS):
        for idx, num in enumerate(number_street):
            if num == 0:
                exit_function = True
            distance[idx] = num

    if len(zeros) >= 2:
        first_zero: int = zeros[0]
        next_zero: int = zeros[1]
        if len(zeros) == len(number_street):
            exit_function = True
    else:
        first_zero = zeros[0]
        next_zero = INFINITY

    if exit_function:
        return distance

    for idx, num in enumerate(number_street):
        dist_first: int = abs(first_zero - idx)
        dist_second: int = abs(next_zero - idx)
        if dist_first <= dist_second:
            distance[idx] = dist_first
        else:
            distance[idx] = dist_second
            if num == 0:
                zeros.pop(0)
                first_zero = next_zero
                if len(zeros) >= 2:
                    next_zero = zeros[1]
                else:
                    next_zero = INFINITY
    return distance


def get_input() -> Tuple[int, List[int]]:
    lenght: int = int(input())
    number_street: List[int] = [int(num) for num in input().split()]
    return lenght, number_street


def main() -> None:
    lenght, number_street = get_input()
    distance = nearest_zero(lenght=lenght, number_street=number_street)
    print(*distance)


if __name__ == "__main__":
    main()
