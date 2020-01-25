# coding=utf-8
array = [5, 3, 1, 14, 2];


'''

Алгоритм сортировки вставками в DESC порядке

@:param list: лист элементов

'''


def insertion_sort(list):
    for i in range(1, len(list)):
        current = list[i]
        position = i

        while position > 0 and list[position - 1] < current:
            list[position] = list[position - 1]
            position -= 1

        list[position] = current


insertion_sort(array)

print(array)  # [14, 5, 3, 2, 1]
