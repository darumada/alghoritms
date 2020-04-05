def countWays(arr):
    max_val = max(arr)
    freq = [0 for i in range(max_val + 1)]
    ans = 0

    for i in range(len(arr)):
        freq[arr[i]] += 1

    # case 1 (0, 0, 0)
    ans += freq[0] * (freq[0] - 1) * (freq[0] - 2) // 6

    # case 2 (0, x, x)
    for i in range(1, max_val + 1):
        ans += freq[0] * freq[i] * (freq[i] - 1) // 2

    # case 3 (x, x, 2x)
    for i in range(1, (max_val + 1) // 2):
        ans += freq[i] * (freq[i] - 1) // 2 * freq[i * 2]

    # case 4 (x, y, x+y)
    for i in range(1, max_val + 1):
        for j in range(i + 1, max_val - i + 1):
            ans += freq[i] * freq[j] * freq[i + j]

    return ans


# Driver code
arr = [1, 1, 1, 2, 2]
print(countWays(arr))
