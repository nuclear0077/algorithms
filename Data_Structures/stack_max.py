# https://contest.yandex.ru/contest/23758/problems/F/

# обрабатываем команды на пустых списках
# 1 - get_max -> None
# 2 - pop -> 'error'
# 3 - push если списки пустые, добавляем в item и max
# если списки не пустые, то в любом случае добавляем в items,
#  но в max проверяем, если новое значение >= текущего
# добавляем его
# 4 - pop, удаляем последнее значение,
# если значение == последнему в списке max, удаляем его тоже
# если списпики пустые, очищаем max
# 5 - get_max - возращаем последние значение


class Stack:
    def __init__(self):
        self.items = []
        self.max = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        if self.is_empty():
            self.items.append(item)
            self.max.append(item)
            return None
        self.items.append(item)
        if item >= self.max[-1]:
            self.max.append(item)
        return None

    def pop(self):
        if self.is_empty():
            return 'error'
        removed = self.items.pop()
        if self.max[-1] == removed:
            self.max.pop()
        if self.is_empty():
            self.max.clear()
        return None

    def get_max(self):
        if self.is_empty():
            return None
        return self.max[-1]


def input_data():
    return input().split()


def main():
    n = int(input())
    stack = Stack()
    answers = []
    for _ in range(0, n):
        data = input_data()
        if data[0] == 'push':
            stack.push(int(data[1]))
        elif data[0] == 'pop':
            answer = stack.pop()
            if answer == 'error':
                answers.append(answer)
        elif data[0] == 'get_max':
            answers.append(stack.get_max())
    for answer in answers:
        print(answer)


if __name__ == '__main__':
    main()
