# 82244590
# https://contest.yandex.ru/contest/23759/problems/A/


class Decue:
    def __init__(self, n):
        self.deque = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push_back(self, x):
        if self.size != self.max_n:
            self.deque[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
            return True
        return 'error'

    def push_front(self, x):
        if self.size != self.max_n:
            self.deque[self.head - 1] = x
            self.head -= 1
            self.size += 1
            return True
        return 'error'

    def pop_front(self):
        if self.is_empty():
            return 'error'
        x = self.deque[self.head]
        self.deque[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x

    def pop_back(self):
        if self.is_empty():
            return 'error'
        x = self.deque[self.tail - 1]
        self.deque[self.tail - 1] = None
        self.size -= 1
        self.tail -= 1
        return x


def input_data():
    return input().split()


def main():
    n = int(input())
    m = int(input())
    deque = Decue(m)
    answers = []
    for _ in range(0, n):
        data = input_data()
        if data[0] == 'push_front':
            answer = deque.push_front(int(data[1]))
            if answer == 'error':
                answers.append(answer)
        if data[0] == 'push_back':
            answer = deque.push_back(int(data[1]))
            if answer == 'error':
                answers.append(answer)
        if data[0] == 'pop_front':
            answers.append(deque.pop_front())
        if data[0] == 'pop_back':
            answers.append(deque.pop_back())
    for answer in answers:
        print(answer)


if __name__ == '__main__':
    main()
