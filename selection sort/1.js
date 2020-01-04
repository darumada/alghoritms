const array = [5, 3, 1, 10, 11, 4];


function selectionSort(list) {
    for (let i = 0; i < list.length - 1; i++) {
        let min = i;

        for (let j = i + 1; j < list.length; j++) {
            if (list[min] > list[j]) {
                min = j;
            }
        }

        swapItemsInList(list, i, min);
    }

    return list;
}

function swapItemsInList(list, indexA, indexB) {
    let temp = list[indexA];
    list[indexA] = list[indexB];
    list[indexB] = temp;
}

console.log(selectionSort(array));