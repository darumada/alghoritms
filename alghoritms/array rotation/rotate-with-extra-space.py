def left_rotate(arr, k):
    k %= len(arr)
    arr = arr[k:] + arr[:k]
    return arr


def left_rotate_in_place(arr, k):
    temp = []
    for i in range(k):
        temp.append(arr.pop(0))

    for i in range(k):
        arr.append(temp[i])


def right_rotate(arr, k):
    arr = arr[-k:] + arr[:-k]
    return arr


def right_rotate_in_place(arr, k):
    temp = []
    for i in range(k):
        temp.append(arr.pop())

    for i in range(k):
        arr.insert(i, temp[k - i - 1])


arr = [1, 2, 3, 4, 5, 6, 7]

print(left_rotate(arr, 3))
print(right_rotate(arr, 3))
# left_rotate_in_place(arr, 3)
right_rotate_in_place(arr, 3)
print(arr)
