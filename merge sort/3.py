# coding=utf-8

"""

Алгоритм сортировки слиянием

@:param array: лист элементов

"""


def merge_sort(array):
    if len(array) > 1:
        middle = len(array) / 2

        left_array = array[:middle]
        right_array = array[middle:]

        merge_sort(left_array)
        merge_sort(right_array)

        i = j = k = 0

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

merge_sort(arr)

print arr
