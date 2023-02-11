# https://contest.yandex.ru/contest/23389/problems/H/
def main(num_first, num_second) -> None:
    diff_symb = len(num_first) - len(num_second)

    if diff_symb > 0:
        diff_symb *= '0'
        num_second = diff_symb + num_second
    else:
        diff_symb = abs(diff_symb) * '0'
        num_first = diff_symb + num_first
    result = ''
    remainder = 0
    for i in range(0, len(num_first)):
        discharge_first = num_first[-1]
        discharge_second = num_second[-1]
        num_first = num_first[:-1]
        num_second = num_second[:-1]
        add = int(discharge_first) + int(discharge_second)
        if add == 1 and remainder == 0:
            result = '1' + result
            continue
        if add == 1 and remainder > 0:
            result = '0' + result
            continue
        if add == 2 and remainder == 0:
            result = '0' + result
            remainder += 1
            continue
        if add == 2 and remainder == 1:
            result = '1' + result
            continue
        if add == 0 and remainder > 0:
            result = '1' + result
            remainder -= 1
            continue
        if add == 0 and remainder == 0:
            result = '0' + result
            continue

    if remainder > 0:
        result = '1' + result
    print(result)


if __name__ == '__main__':
    num_first = str(input())
    num_second = str(input())
    main(num_first, num_second)
