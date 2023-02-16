# 82407868
# https://contest.yandex.ru/contest/23759/problems/B/
from typing import List, Union, Any

OPERATIONS = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '/': lambda x, y: x // y,
    '//': lambda x, y: x // y,
    '*': lambda x, y: x * y,
    }


class StackIndexError(IndexError):
    pass


class Stack:
    def __init__(self) -> None:
        self.__items: List[Any] = []

    def push(self, item: Union[int, float]) -> None:
        self.__items.append(item)

    def pop(self) -> Union[int, float]:
        try:
            return self.__items.pop()
        except IndexError:
            raise StackIndexError('pop from empty stack')


def input_data() -> List[Any]:
    return input().split()


def calculator(stack: Stack, expression):
    for item in expression:
        if item in OPERATIONS:
            x, y = stack.pop(), stack.pop()
            stack.push(OPERATIONS.get(item)(y, x))
        else:
            stack.push(int(item))
    return stack.pop()


def main():
    stack = Stack()
    expression = input_data()
    print(calculator(stack=stack, expression=expression))


if __name__ == '__main__':
    main()
