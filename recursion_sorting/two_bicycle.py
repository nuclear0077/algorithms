# https://contest.yandex.ru/contest/24734/problems/L/

def binary_search_descending(arr, price, left, right):
    if right <= left:
        return -1
    mid = (left + right) // 2
    if arr[mid] >= price and (arr[mid - 1] < price or mid == 0):
        return mid + 1
    elif arr[mid] >= price:
        return binary_search_descending(arr, price, left, mid)
    else:
        return binary_search_descending(arr, price, mid + 1, right)


def get_input():
    n = int(input())
    arr = list(map(int, input().split()))
    price = int(input())
    return n, arr, price


if __name__ == '__main__':
    n, arr, price = get_input()
    print(binary_search_descending(arr, price, left=0, right=len(arr)), end=' ')
    print(binary_search_descending(arr, price * 2, left=0, right=len(arr)), end=' ')
