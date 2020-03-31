# using XOR


def missing_number(nums):
    ans = len(nums)

    for i in range(len(nums)):
        ans ^= nums[i] ^ i

    return ans


# 3 ^ 1 ^ 0 = 2
# 11 ^ 01 ^ 00 = 10

# 2 ^ 3 ^ 1 = 0
# 10 ^ 11 ^ 01 = 0

# 0 ^ 0 ^ 2 = 2
# 00 ^ 00 ^ 10 = 10


print(missing_number([1, 3, 0]))
