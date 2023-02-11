# https://contest.yandex.ru/contest/23389/problems/I/
# num вход число которое проверяем входит оно в степень 4х или нет
# pow = 1 - текущая степень
# curr_number = число которое получилось после возведения в степень 4 ** n
# каждую итерацию pow += 1 
# цикл работает пока curr_number < num


def check_number(n):
    if n == 1:
        return True
    pow = 1
    curr_number = 4
    while curr_number < n:
        curr_number = 4 ** pow
        pow += 1
    return n == curr_number


if __name__ == '__main__':
    n = int(input())
    print(check_number(n))