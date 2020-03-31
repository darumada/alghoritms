# using Gauss' Formula (n * (n+1) / 2)


def missing_number(nums):
    given_sum = sum(nums)
    expected_sum = len(nums) * (len(nums) + 1) // 2

    return expected_sum - given_sum


print(missing_number([1, 3, 0]))
