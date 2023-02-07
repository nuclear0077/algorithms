# n - число которое надо перевести
# b - итоговая строка в двоичной системе
# 1 - получаем остаток  и добавляем его в начало строки и приклеиваем другая часть
# 2 - n // 2 и перезаписываем число n
# цикл работает пока n != 0

def binarization(num):
    if num == 0:
        return 0
    b = ''
    while num != 0:
        b = str(num % 2) + b
        num = num // 2
    return b


if __name__ == '__main__':
    num = int(input())
    print(binarization(num))
