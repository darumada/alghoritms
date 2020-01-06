function mergeSort(array) {
  if (array.length < 2) {
    return array;
  }

  const middle = Math.floor(array.length / 2);

  const leftArray = array.slice(0, middle);
  const rightArray = array.slice(middle);

  return merge(mergeSort(leftArray), mergeSort(rightArray));
}

function merge(leftArray, rightArray) {
  const sortedArr = [];

  while (leftArray.length && rightArray.length) {
    if (leftArray[0] <= rightArray[0]) {
      sortedArr.push(leftArray.shift());
    } else {
      sortedArr.push(rightArray.shift());
    }
  }

  return [...sortedArr, ...leftArray, ...rightArray];
}


const arr = [9, 20, 3, 1, 8, 10, 11, 5];

console.log(mergeSort(arr));