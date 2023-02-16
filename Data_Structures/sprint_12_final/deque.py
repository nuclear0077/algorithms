# 82340964
# https://contest.yandex.ru/contest/23759/problems/A/
from typing import List


class EmptyDequeError(Exception):
    pass


class FullDequeError(Exception):
    pass


class Deque:
    def __init__(self, max_size: int) -> None:
        self.__deque: List = [None] * max_size
        self.__max_size: int = max_size
        self.__head: int = 0
        self.__tail: int = 0
        self.__size: int = 0

    def __inc_index(self, value: int) -> int:
        return (value + 1) % self.__max_size

    def __dec_index(self, value: int) -> int:
        return (value - 1) % self.__max_size

    def is_empty(self) -> bool:
        return self.__size == 0

    def is_full(self) -> bool:
        return self.__size == self.__max_size

    def push_back(self, item) -> None:
        if self.is_full():
            raise FullDequeError('Стек переполнен')
        self.__deque[self.__tail] = item
        self.__tail = self.__inc_index(self.__tail)
        self.__size += 1

    def push_front(self, item) -> None:
        if self.is_full():
            raise FullDequeError('Стек переполнен')
        self.__deque[self.__dec_index(self.__head)] = item
        self.__head -= 1
        self.__size += 1

    def pop_front(self):
        if self.is_empty():
            raise EmptyDequeError('Стек пустой')
        item = self.__deque[self.__head]
        self.__deque[self.__head] = None
        self.__head = self.__inc_index(self.__head)
        self.__size -= 1
        return item

    def pop_back(self):
        if self.is_empty():
            raise EmptyDequeError('Стек пустой')
        item = self.__deque[self.__dec_index(self.__tail)]
        self.__deque[self.__dec_index(self.__tail)] = None
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


def main():
    command_amount: int = int(input())
    max_size_deque: int = int(input())
    deque = Deque(max_size_deque)
    for _ in range(command_amount):
        input_command = get_command()
        try:
            run_deque_method(deque, input_command)
        except (EmptyDequeError, FullDequeError):
            print('error')


if __name__ == '__main__':
    main()
