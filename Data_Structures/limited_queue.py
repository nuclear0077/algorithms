# https://contest.yandex.ru/contest/23758/problems/I/
# Создадим свой класс Queue. У объектов этого класса будут поля:
# head — индекс, по которому нужно извлекать элемент, если очередь не пустая;
# tail — индекс, по которому нужно добавлять элемент, если в очереди есть место;
# max_n — максимально возможное количество элементов в очереди;
# size — размер очереди.

# - `push(item)` — добавляет элемент в конец очереди;
# - `pop()` — берёт элемент из начала очереди и удаляет его;
# - `peek()` — берёт элемент из начала очереди без удаления;
# - `size()` — возвращает количество элементов в очереди.

class Queue:
    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_overloaded(self):
        return self.max_n == self.size

    def push(self, item):
        if self.is_overloaded():
            return 'error'
        self.queue[self.tail] = item
        self.tail = (self.tail + 1) % self.max_n
        self.size += 1
        return True

    def pop(self):
        if self.is_empty():
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[self.head]


def input_data():
    return input().split()


def main():
    n = int(input())
    max_long = int(input())
    queue = Queue(max_long)
    answers = []
    for _ in range(0, n):
        data = input_data()
        if data[0] == 'push':
            answer = queue.push(int(data[1]))
            if answer == 'error':
                answers.append(answer)
        if data[0] == 'peek':
            answers.append(queue.peek())
        if data[0] == 'pop':
            answers.append(queue.pop())
        if data[0] == 'size':
            answers.append(queue.size)
    for answer in answers:
        print(answer)


if __name__ == '__main__':
    main()
