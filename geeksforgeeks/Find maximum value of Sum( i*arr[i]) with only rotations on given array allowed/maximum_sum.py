def find_max(arr):
    arrSum = 0
    currentSum = 0

    for i in range(len(arr)):
        arrSum += arr[i]
        currentSum += arr[i] * i

    maxVal = currentSum

    for j in range(1, len(arr)):
        print(arr[len(arr) - j])
        print(len(arr) * arr[len(arr) - j])
        currentSum += arrSum - len(arr) * arr[len(arr) - j]

        if currentSum > maxVal:
            maxVal = currentSum

    return maxVal


arr = [1, 20, 2, 10]

print(find_max(arr))