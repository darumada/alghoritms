# coding=utf-8
arr = [5, 3, 1, 10, 11, 4];

'''

Алгоритм сортировки выбором

@:param list: лист элементов

'''


def selection_sort(array):
    for i in range(len(array) - 1):
        min_index = i

        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j

        array[i], array[min_index] = array[min_index], array[i]


selection_sort(arr)

print(arr)  # [1, 3, 4, 5, 10, 11]

# Наилучший исход - O(n^2)
# Наихудший исход - O(n^2)
