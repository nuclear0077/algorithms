# https://contest.yandex.ru/contest/24734/problems/J/
def bubles_sort(array):
    sort = False
    for i in range(len(array)-1):
        was_changed = False
        for j in range(len(array)-1-i):
            if array[j] > array[j + 1]:
                array[j + 1], array[j] = array[j], array[j + 1]
                was_changed = True
                sort = True
        if was_changed:
            print(*array)
        was_changed = False
    if not sort:
        print(*array)


if __name__ == '__main__':
    n = input()
    string = list(map(int, input().split()))
    bubles_sort(string)
