def left_rotate(arr, k):
    for i in range(k):
        temp = arr[0]
        for j in range(1, len(arr)):
            arr[j - 1] = arr[j]

        arr[len(arr) - 1] = temp


def right_rotate(arr, k):
    for i in range(k):
        temp = arr[len(arr) - 1]
        for j in range(len(arr) - 2, -1, -1):
            arr[j + 1] = arr[j]

        arr[0] = temp


arr = [1, 2, 3, 4, 5, 6, 7]
right_rotate(arr, 3)
print(arr)
