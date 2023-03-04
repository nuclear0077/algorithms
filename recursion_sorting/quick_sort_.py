def quick_sort(array):
    if len(array) < 1:
        return array
    pivot = array[0]
    left = list(filter(lambda x: x < pivot, array))
    middle = [elem for elem in array if elem == pivot]
    right = list(filter(lambda x: x > pivot, array))
    return quick_sort(left) + middle + quick_sort(right)


array = [7, 6, 10, 5, 9, 8, 10, 3, 4]

print(quick_sort(array))