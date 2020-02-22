class SortedMap:
    class _Item:
        def __init__(self, key, value):
            self.key = key
            self.value = value

    def _find_item(self, key):
        def binary_search(low, high):
            if low > high:
                return high + 1

            mid = (low + high) // 2

            if self._table[mid].key == key:
                return mid

            if self._table[mid].key > key:
                return binary_search(low, mid - 1)

            if self._table[mid].key < key:
                return binary_search(mid + 1, high)

        return binary_search(0, len(self._table) - 1)

    def __init__(self):
        self._table = []

    def __setitem__(self, key, value):
        index = self._find_item(key)

        if index < len(self._table) and self._table[index].key == key:
            self._table[index].value = value
        else:
            self._table.insert(index, self._Item(key, value))

    def __getitem__(self, key):
        index = self._find_item(key)

        if index == len(self._table) or self._table[index].key != key:
            raise KeyError()

        return self._table[index]

    def __delitem__(self, key):
        index = self._find_item(key)

        if index == len(self._table) or self._table[index].key != key:
            raise KeyError()

        self._table.pop(index)

    def __len__(self):
        return len(self._table)

    def __iter__(self):
        for item in self._table:
            yield item.key, item.value

