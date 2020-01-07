# coding=utf-8

"""

Алгоритм сортировки пузырьком

@:param array: лист элементов

"""


def bubble_sort(array):

    for i in range(len(array)):
        swapped = False
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                swapped = True
                array[j], array[j + 1] = array[j + 1], array[j]

        if not swapped:
            break


arr = [9, 20, 3, 1, 8, 10, 11, 5]

bubble_sort(arr)

print(arr)  # [1, 3, 5, 8, 9, 10, 11, 20]
