# 82247719
# https://contest.yandex.ru/contest/23759/problems/B/
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


def input_data():
    return input().split()


def main():
    stack = Stack()
    polish_notation = input_data()
    operations = '*/-+'
    for values in polish_notation:
        if values not in operations:
            stack.push(int(values))
            continue
        if values == '-':
            num_second = stack.pop()
            num_first = stack.pop()
            result = num_first - num_second
            stack.push(result)
            continue
        if values == '+':
            num_second = stack.pop()
            num_first = stack.pop()
            result = num_first + num_second
            stack.push(result)
            continue
        if values == '*':
            num_second = stack.pop()
            num_first = stack.pop()
            result = num_first * num_second
            stack.push(result)
            continue
        if values == '/':
            num_second = stack.pop()
            num_first = stack.pop()
            result = num_first // num_second
            stack.push(result)
            continue
    print(stack.pop())


if __name__ == '__main__':
    main()
