function bubbleSort(array) {
  for (let i = 0; i < array.length; i++) {
    for (let j = array.length; j > i; j--) {
      if (array[j] < array[j - 1]) {
        swapItemsInList(array, j, j - 1);
      }
    }
  }
}

function swapItemsInList(list, indexA, indexB) {
  let temp = list[indexA];
  list[indexA] = list[indexB];
  list[indexB] = temp;
}

const arr = [9, 20, 3, 1, 8, 10, 11, 5];

bubbleSort(arr);

console.log(arr);
