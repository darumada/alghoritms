# coding=utf-8
arr = [1, 2, 100, 99, 44, 23]

target1 = 2

target2 = 120

'''

Алгоритм линейного поиска

@:param array: лист элементов
@:param target: значение, индекс, которого будет искаться в array

@:return индекс target в array или None, если target отсутствует в array

'''


def linear_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
            
    return None


print(linear_search(arr, target1))  # 1

print(linear_search(arr, target2))  # None


# Наилучший исход - O(1)
# Наихудший исход - O(n)