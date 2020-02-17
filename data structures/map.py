class Map:
    class _Item:
        def __init__(self, key, value):
            self.key = key
            self.value = value

    def __init__(self):
        self._table = []

    def __getitem__(self, key):
        for item in self._table:
            if item.key == key:
                return item.value

        raise KeyError()

    def __setitem__(self, key, value):
        for item in self._table:
            if item.key == key:
                item.value = value
                return

        self._table.append(self._Item(key, value))

    def __delitem__(self, key):
        for i in range(self._table):
            if self._table[i].key == key:
                self._table.pop(i)
                return

        raise KeyError()

    def __len__(self):
        return len(self._table)

    def __iter__(self):
        for item in self._table:
            yield item.key, item.value
