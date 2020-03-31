def find_subarray(arr, sum):
    local_sum = 0
    start = 0
    i = 0

    while i < len(arr) + 1:

        while local_sum > sum and start < i:
            local_sum -= arr[start]
            start += 1

        if local_sum == sum:
            return arr[start:i]

        if i < len(arr):
            local_sum += arr[i]
        i += 1

    return []


print(find_subarray([1, 4, 20, 3, 10, 5], 33))