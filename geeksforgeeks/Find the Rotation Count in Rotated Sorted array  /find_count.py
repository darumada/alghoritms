def find_count(arr):
    def binary_search(left, right):

        if right < left:
            return 0

        if left == right:
            return left

        middle = (left + right) // 2

        if middle < right and arr[middle + 1] < arr[middle]:
            return middle + 1

        if middle > left and arr[middle - 1] > arr[middle]:
            return middle

        if arr[right] > arr[middle]:
            return binary_search(left, middle - 1)

        return binary_search(middle + 1, right)

    return binary_search(0, len(arr) - 1)


arr = [15, 18, 22, 40, 50, 60, 70, 2, 3, 6, 12]

print(find_count(arr))
