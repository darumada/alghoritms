# find 2 indexes of elements in array that give a sum

def two_sum(arr, target):
    map = {}
    for i in range(len(arr)):
        if arr[i] in map:
            return map[arr[i]], i
        else:
            map[target - arr[i]] = i


arr = [11, 15, 6, 8, 9, 10]
target = 16

print(two_sum(arr, target))