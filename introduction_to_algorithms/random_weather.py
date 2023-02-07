#  если числа первое, то проверяем следующие, если первое число больше второго
# то считаем, что это хаотичность
# если последнее число больше предыдущего, то считаем, что это хаотичность
# обработаем сначала len(1) return 1
# далее певую итерацию и последнюю
# остальные берем curr_itter -1 and curr_itter + 1 и проверяем условие
def get_randomness(n, list_of_measurements):
    if n == 1:
        return 1
    randomness = 0
    max_iter = n - 1
    for i in range(0, n):
        if i == 0:
            if list_of_measurements[i] > list_of_measurements[i + 1]:
                randomness += 1
            continue
        if i == max_iter:
            if list_of_measurements[i] > list_of_measurements[i - 1]:
                randomness += 1
            continue
        current_value = list_of_measurements[i]
        next_value = list_of_measurements[i + 1]
        prev_value = list_of_measurements[i - 1]
        if current_value > next_value and current_value > prev_value:
            randomness += 1
    return randomness


if __name__ == '__main__':
    n = int(input())
    list_of_measurements = list(map(int, input().split()))
    print(get_randomness(n, list_of_measurements))
