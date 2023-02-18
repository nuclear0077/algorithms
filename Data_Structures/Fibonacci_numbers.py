# https://contest.yandex.ru/contest/23758/problems/K/

def fib(x):
    if x == 0:
        return 1
    elif x == 1:
        return 1
    return fib(x - 1) + fib(x - 2)


if __name__ == '__main__':
    x = int(input())
    print(fib(x))
