https://contest.yandex.ru/contest/23389/problems/K/
def main() -> None:
    n = int(input())
    x = str(input()).replace(' ', '')
    k = int(input())
    x_k = list(str(int(x) + k))
    print(*x_k)


if __name__ == '__main__':
    main()
