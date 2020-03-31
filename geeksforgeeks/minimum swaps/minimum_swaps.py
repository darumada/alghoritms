def minimum_swaps(arr, k):
    count = 0
    bad = 0

    for item in arr:
        if item <= k:
            count += 1

    for i in range(count):
        if arr[i] > k:
            bad += 1

    ans = bad
    j = count

    for i in range(len(arr)):

        if j == len(arr):
            break

        if arr[i] > k:
            bad -= 1

        if arr[j] > k:
            bad += 1

        j += 1
        ans = min(ans, bad)

    return ans


arr = [2, 1, 5, 6, 3]

print(minimum_swaps(arr, 3))
