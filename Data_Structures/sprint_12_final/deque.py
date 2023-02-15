# 82340964
# https://contest.yandex.ru/contest/23759/problems/A/
from typing import List


class EmptyStackError(Exception):
    pass


class FullStackError(Exception):
    pass


class Deque:
    def __init__(self, max_size: int) -> None:
        self.__deque: List = [None] * max_size
        self.__max_size: int = max_size
        self.__head: int = 0
        self.__tail: int = 0
        self.__size: int = 0

    def is_empty(self) -> bool:
        return self.__size == 0

    def is_full(self) -> bool:
        return self.__size == self.__max_size

    def push_back(self, item) -> None:
        if self.is_full():
            raise EmptyStackError('Стек переполнен')
        self.__deque[self.__tail] = item
        self.__tail = (self.__tail + 1) % self.__max_size
        self.__size += 1

    def push_front(self, item) -> None:
        if self.is_full():
            raise EmptyStackError('Стек переполнен')
        self.__deque[self.__head - 1] = item
        self.__head -= 1
        self.__size += 1

    def pop_front(self):
        if self.is_empty():
            raise EmptyStackError('Стек пустой')
        item = self.__deque[self.__head]
        self.__deque[self.__head] = None
        self.__head = (self.__head + 1) % self.__max_size
        self.__size -= 1
        return item

    def pop_back(self):
        if self.is_empty():
            raise EmptyStackError('Стек пустой')
        item = self.__deque[self.__tail - 1]
        self.__deque[self.__tail - 1] = None
        self.__size -= 1
        self.__tail -= 1
        return item


def get_command() -> List:
    return input().split()


def run_deque_method(deque: Deque, command: List):
    run_command = getattr(deque, command[0])
    if 'push' not in command[0]:
        print(run_command())
    else:
        run_command(command[1])


def run_command(command_amount: int, max_size_deque: int):
    deque = Deque(max_size_deque)
    for _ in range(command_amount):
        try:
            run_deque_method(deque, get_command())
        except (EmptyStackError, FullStackError):
            print('error')


def main():
    command_amount: int = int(input())
    max_size_deque: int = int(input())
    try:
        run_command(command_amount, max_size_deque)
    except (EmptyStackError, FullStackError):
        print('error')


if __name__ == '__main__':
    main()
