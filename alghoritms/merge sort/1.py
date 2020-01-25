# coding=utf-8

"""

Алгоритм сортировки слиянием

@:param array: лист элементов
@:param left: индекс начального элементе
@:param right: индекс конечного элементе

"""


def merge_sort(array, left, right):
    if left < right:
        middle = (left + right) // 2

        merge_sort(array, left, middle)
        merge_sort(array, middle + 1, right)

        merge(array, left, middle, right)


def merge(array, left, middle, right):
    n1 = middle - left + 1
    n2 = right - middle

    left_array = [0] * n1
    right_array = [0] * n2

    for i in range(n1):
        left_array[i] = array[left + i]

    for j in range(n2):
        right_array[j] = array[middle + j + 1]

    i = j = 0
    k = left

    while i < n1 and j < n2:
        if left_array[i] <= right_array[j]:
            array[k] = left_array[i]
            i += 1
        else:
            array[k] = right_array[j]
            j += 1
        k += 1

    while i < n1:
        array[k] = left_array[i]
        i += 1
        k += 1

    while j < n2:
        array[k] = right_array[j]
        j += 1
        k += 1


arr = [9, 20, 3, 1, 8, 10, 11, 5]

merge_sort(arr, 0, len(arr) - 1)

print(arr)
