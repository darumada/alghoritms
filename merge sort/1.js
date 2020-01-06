function mergeSort(array) {
  if (array.length > 1) {

    const middle = Math.floor(array.length / 2);

    const leftArray = array.slice(0, middle);
    const rightArray = array.slice(middle);

    mergeSort(leftArray);
    mergeSort(rightArray);


    let i = 0, j = 0, k = 0;

    while (i < leftArray.length && j < rightArray.length) {
      if (leftArray[i] <= rightArray[j]) {
        array[k] = leftArray[i];
        i++;
      } else {
        array[k] = rightArray[j];
        j++;
      }
      k++;
    }

    while(i < leftArray.length) {
      array[k] = leftArray[i];
      i++;
      k++;
    }

    while(j < rightArray.length) {
      array[k] = rightArray[j];
      j++;
      k++;
    }
    
  }
}


const arr = [9, 20, 3, 1, 8, 10, 11, 5];

mergeSort(arr);

console.log(arr);