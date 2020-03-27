def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def quick_sort(arr):
    def _quick_sort(arr, low, high):
        if low < high:
            p = partition(arr, low, high)

            _quick_sort(arr, low, p - 1)
            _quick_sort(arr, p + 1, high)

        return arr

    return _quick_sort(arr, 0, len(arr) - 1)


print(quick_sort([10, 5, 7, 4, 6]))
