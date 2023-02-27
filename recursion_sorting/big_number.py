# https://contest.yandex.ru/contest/24734/problems/H/
def compare(num_1, num_2):
    return num_1 > num_2


def insertion_sort_by_comparator(array, less):
    for i in range(0, len(array)):
        item_to_insert = array[i]
        j = i
        while j > 0 and less(int(item_to_insert + array[j-1]), int(array[j-1] + item_to_insert)):
            array[j] = array[j-1]
            j -= 1
        array[j] = item_to_insert
    return ''.join(array)


if __name__ == '__main__':
    n = input()
    array = list(map(str, input().split()))
    print(insertion_sort_by_comparator(array, compare))