def find_missing_number(arr):
    n = len(arr) + 1
    real_sum = sum(arr)
    expected_sum = n * (n + 1) // 2

    return expected_sum - real_sum


arr = [1, 2, 4, 6, 3, 7, 8]

print(find_missing_number(arr))