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

    left_array = array[left:middle + 1]
    right_array = array[middle + 1:right + 1]

    i = j = 0
    k = left

    while i < len(left_array) and j < len(right_array):
        if left_array[i] <= right_array[j]:
            array[k] = left_array[i]
            i += 1
        else:
            array[k] = right_array[j]
            j += 1
        k += 1

    while i < len(left_array):
        array[k] = left_array[i]
        i += 1
        k += 1

    while j < len(right_array):
        array[k] = right_array[j]
        j += 1
        k += 1


arr = [9, 20, 3, 1, 8, 10, 11, 5]

merge_sort(arr, 0, len(arr) - 1)

print(arr)
