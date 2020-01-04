const arr = [1, 2, 100, 99, 44, 23]

const target1 = 2

const target2 = 120

function linearSearch(array, target) {
  for (let i = 0; i < array.length; i++) {
    if (array[i] === target) {
      return i;
    }
  }

  return null;
}

console.log(linearSearch(arr, target1))  // 1

console.log(linearSearch(arr, target2))  // None
