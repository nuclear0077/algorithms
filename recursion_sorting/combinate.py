# https://contest.yandex.ru/contest/24734/problems/B/
# логика работы функции возвращаем список значений
# 1 - базовый случай когда string == 0
# 2 - записываем в значение набор букв на кнопке ( так как стек, первое значение будем использовать на возврате)
# 3 - запускаем цикл по функции и передаем срез строки (функция возращает список букв)

d = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}


def combinations(string):
    result = []
    if len(string) == 0:
        return ['']
    seq_letter = d[string[-1]]
    for num in combinations(string[:-1:]):
        for letter in seq_letter:
            result.append(num + letter)
    return result


if __name__ == '__main__':
    string = input()
    print(*combinations(string))