# coding=utf-8
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

'''

Алгоритм бинарного поиска

@:param array: лист элементов
@:param left: начальный индекс поиска
@:param right: конечный индекс поиска
@:param target: значение, индекс, которого будет искаться в array

@:return индекс target в array или None, если target отсутствует в array

'''


def binary_search(array, left, right, target):
    if left > right:
        return None

    middle = (right + left) // 2

    if array[middle] == target:
        return middle
    elif array[middle] > target:
        return binary_search(array, left, middle - 1, target)
    else:
        return binary_search(array, middle + 1, right, target)


print(binary_search(arr, 0, len(arr) - 1, 4))  # 3
print(binary_search(arr, 0, len(arr) - 1, -2))  # None
