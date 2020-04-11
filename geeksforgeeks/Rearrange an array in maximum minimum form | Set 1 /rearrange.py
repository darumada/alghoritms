def rearrange(arr):
    left = 0
    right = len(arr) - 1
    temp = [None] * len(arr)

    flag = True

    for i in range(len(arr)):
        if flag:
            temp[i] = arr[right]
            right -= 1
        else:
            temp[i] = arr[left]
            left += 1

        flag = not flag

    return temp

def rearrangeWithoutExtraSpace(arr):
    end = len(arr) - 1
    start = 0
    for i in range(len(arr)):
        if i % 2 == 0:
            if i <= end:
                arr[i] = arr[i], arr[end]
            else:
                arr[i] = arr[i], arr[end][0]
            end -= 1
        else:
            arr[i] = arr[i], arr[start][0]
            start += 1

    for i in range(len(arr)):
        arr[i] = arr[i][1]


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
rearrangeWithoutExtraSpace(arr)
print(arr)
