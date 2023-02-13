# ID 81781529
# https://contest.yandex.ru/contest/23390/problems/B/
from collections import Counter
from typing import Tuple


def sleight_of_hand(max_possible_clicks: int, matrix: str) -> int:
    score = 0
    c_num = Counter(matrix)
    max_possible_clicks *= 2
    for time in range(0, 10):
        curr_value = c_num.get(str(time))
        if not curr_value:
            continue
        if curr_value <= max_possible_clicks:
            score += 1
    return score


def get_input() -> Tuple[int, str]:
    max_possible_clicks: int = int(input())
    matrix = ''.join([input() for _ in range(4)])
    return max_possible_clicks, matrix


def main() -> None:
    max_possible_clicks, matrix = get_input()
    score = sleight_of_hand(max_possible_clicks=max_possible_clicks,
                            matrix=matrix)
    print(score)


if __name__ == "__main__":
    main()
