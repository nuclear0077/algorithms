# https://contest.yandex.ru/contest/23758/problems/L/
def fibonacci_module(n, k):
    if n <= 1:
        return 1
    n1, n2 = 1, 1
    for _ in range(int(n) - 1):
        n1, n2 = n2, (n2 + n1) % 10 ** k    
    return n2


if __name__ == '__main__':
    n, k = map(int, input().split())
    print(fibonacci_module(n, k))
