# coding=utf-8
"""

Написать имплементации 3х выученныйх алгоритмов (insertion sort, selection sort, linear search)

"""


def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return None


def insertion_sort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        index = i

        while index > 0 and arr[index - 1] > current:
            arr[index] = arr[index - 1]
            index -= 1

        arr[index] = current


def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_index = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]


my_arr = [10, 2, 3, 5]

selection_sort(my_arr)

print my_arr
