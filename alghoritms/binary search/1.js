const arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

function binarySearch(array, left, right, target) {

  if (left > right) {
    return null;
  }

  const middle = Math.floor((left + right) / 2);

  if (array[middle] === target) {
    return middle;
  } else if (array[middle] > target) {
    return binarySearch(array, left, middle - 1, target);
  } else {
    return binarySearch(array, middle + 1, right, target);
  }
}


console.log(binarySearch(arr, 0, arr.length - 1, 4)); // 3
console.log(binarySearch(arr, 0, arr.length - 1, -2)); // null