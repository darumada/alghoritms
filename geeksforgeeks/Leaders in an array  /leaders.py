import math


def leaders(arr):
    max_right = arr[-1]
    res = [max_right]

    for i in range(len(arr) - 2, -1, -1):
        if arr[i] > max_right:
            max_right = arr[i]
            res.append(arr[i])

    return res


arr = [16, 17, 4, 3, 5, 2]

print(leaders(arr))

