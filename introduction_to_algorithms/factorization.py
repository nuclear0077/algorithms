# https://contest.yandex.ru/contest/23389/problems/J/
def factorize(n):
    divisor = 2
    result = []
    while divisor ** 2 <= n:
        if n % divisor == 0:
            n //= divisor
            result.append(divisor)
        else:
            divisor += 1
    if n != 1:
        result.append(n)
        return result
    result.append(n)
    return result


if __name__ == '__main__':
    n = int(input())
    print(*factorize(n))
