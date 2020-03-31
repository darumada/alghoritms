import math

'''

Kadane's algorithm для поиска подмассива с максимальной суммой

@:param array: лист элементов

@:return: максимальная сумма подмассива array

'''


def find_max_sub_array_sum(array):
    local_max = 0
    global_max = -math.inf

    for i in range(len(array)):
        local_max += array[i]

        if local_max > global_max:
            global_max = local_max

        if local_max < 0:
            local_max = 0

    return global_max


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

print(find_max_sub_array_sum(arr))
