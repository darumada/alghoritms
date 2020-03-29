def rearrange(arr):
    for i in range(len(arr)):
        if arr[i] != i and arr[i] > -1:
            arr[arr[i]], arr[i] = arr[i], arr[arr[i]]


arr = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]

rearrange(arr)
print(arr)
