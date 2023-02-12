# https://contest.yandex.ru/contest/23758/problems/J/
# get() — вывести элемент, находящийся в голове очереди, и удалить его.
#  Если очередь пуста, то вывести «error».
# put(x) — добавить число x в очередь
# size() — вывести текущий размер очереди

# Добавление.
# При первом добавлении в head записываем только что созданную ноду,
# далее в tail указываем head
# на следующей итерации в tail.next записываем новую ноду
# в tail записываем значение tail.next
# Получение.
# Получаем первое значение с голову head.value
# сохраняем следующую ноду и голове присваиваем ее

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def get(self):
        if self.is_empty():
            return 'error'
        value = self.head.value
        next_node = self.head.next
        self.head = next_node
        self.size -= 1
        return value

    def put(self, x):
        new_node = Node(x)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return True
        self.tail.next = new_node
        self.tail = self.tail.next
        self.size += 1
        return True


def input_data():
    return input().split()


def main():
    n = int(input())
    queue = Queue()
    answers = []
    for _ in range(0, n):
        data = input_data()
        if data[0] == 'get':
            answers.append(queue.get())
        if data[0] == 'size':
            answers.append(queue.size)
        if data[0] == 'put':
            queue.put(data[1])
    for answer in answers:
        print(answer)


if __name__ == '__main__':
    main()
