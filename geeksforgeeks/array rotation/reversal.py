def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def right_rotate(arr, k):
    k %= len(arr)
    reverse(arr, 0, len(arr) - 1)
    reverse(arr, 0, k - 1)
    reverse(arr, k, len(arr) - 1)


def left_rotate(arr, k):
    k %= len(arr)
    reverse(arr, 0, k - 1)
    reverse(arr, k, len(arr) - 1)
    reverse(arr, 0, len(arr) - 1)


arr = [1, 2, 3, 4, 5, 6, 7]

left_rotate(arr, 3)

print(arr)
