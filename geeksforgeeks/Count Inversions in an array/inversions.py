def merge_sort(arr, left, right):

    inv_count = 0

    if right > left:
        middle = (left + right) // 2
        inv_count += merge_sort(arr, left, middle)
        inv_count += merge_sort(arr, middle + 1, right)
        inv_count += merge(arr, left, middle, right)

    return inv_count


def merge(array, left, middle, right):

    inv_count = 0

    left_array = array[left:middle + 1]
    right_array = array[middle + 1:right + 1]

    i = j = 0
    k = left

    while i < len(left_array) and j < len(right_array):
        if left_array[i] <= right_array[j]:
            array[k] = left_array[i]
            i += 1
        else:
            array[k] = right_array[j]
            j += 1
            inv_count += (middle - i + 1)
        k += 1

    while i < len(left_array):
        array[k] = left_array[i]
        i += 1
        k += 1

    while j < len(right_array):
        array[k] = right_array[j]
        j += 1
        k += 1

    return inv_count



def count(arr):
    return merge_sort(arr, 0, len(arr))


arr = [8, 4, 2, 1]

print(count(arr))