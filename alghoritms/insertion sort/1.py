# coding=utf-8
array = [5, 3, 1];

'''

Алгоритм сортировки вставками

@:param list: лист элементов

цифра возле комментария, количество вызовов строки для переданного array

'''


def insertion_sort(list):
    for i in range(1, len(list)):  # 3
        current = list[i]  # 2
        position = i  # 2

        while position > 0 and list[position - 1] > current:  # 5
            list[position] = list[position - 1]  # 3
            position -= 1  # 3

        list[position] = current  # 2


insertion_sort(array)

print(array)  # [1, 3, 5]

# Наилучший исход - O(n)
# Наихудший исход - O(n^2)
