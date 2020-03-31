def find_subarray(arr, sum):
    local_sum = 0
    ans = []

    for i in range(len(arr)):
        if arr[i] > sum:
            continue

        local_sum += arr[i]
        ans.append(arr[i])

        while local_sum > sum:
            local_sum -= ans.pop(0)

        if local_sum == sum:
            break

    return ans


print(find_subarray([1, 4, 20, 3, 10, 5], 33))