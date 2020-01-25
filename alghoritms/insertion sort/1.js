const array = [5, 3, 1, 14, 2]

function insertionSort(list) {
    for (let i = 1; i < list.length; i++) {
      const current = list[i];
      let position = i;

      while (position > 0 && list[position - 1] > current) {
        list[position] = list[position - 1];
        position--;
      }

      list[position] = current;
    }
}

insertionSort(array)

console.log(array);