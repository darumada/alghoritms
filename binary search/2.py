# coding=utf-8
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

'''

Алгоритм бинарного поиска через while loop

@:param array: лист элементов
@:param target: значение, индекс, которого будет искаться в array

@:return индекс target в array или None, если target отсутствует в array

'''


def binary_search(array, target):
  
  left = 0
  right = len(array) - 1

  while left <= right:
    middle = (left + right) / 2

    if (arr[middle] == target):
      return middle
    
    if (arr[middle] < target):
      left = middle + 1
      continue
    
    if (arr[middle] > target):
      right = middle - 1
      continue

  return None
    


print binary_search(arr, 4)  # 3
print binary_search(arr, -2)  # None
