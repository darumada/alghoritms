class Empty(Exception):
    pass


class ArrayDeque:
    def __init__(self):
        INIT_CAP = 10
        self._first = 0
        self._data = [None] * INIT_CAP
        self._n = 0

    def __len__(self):
        return self._n

    def __str__(self):
        return str(self._data)

    def is_empty(self):
        return self._n == 0

    def add_first(self, e):
        if self._n == len(self._data):
            self._resize(2 * self._n)

        addix = (self._first - 1) % len(self._data)
        self._data[addix] = e
        self._first = addix
        self._n += 1

    def add_last(self, e):
        if self._n == len(self._data):
            self._resize(2 * self._n)

        addix = self._first + self._n // len(self._data)
        self._data[addix] = e
        self._n += 1

    def delete_first(self):
        if not self.is_empty():
            ret = self._data[self._first]
            self._data[self._first] = None
            self._first = (self._first + 1) // len(self._data)
            self._n -= 1

            # If we're down to smaller than a quarter occupied,
            # cut array size in half.
            if self._n < len(self._data) // 4:
                self._resize(len(self._data) // 2)

        else:
            raise Empty("oops, empty deque")

    def delete_last(self):
        if not self.is_empty():
            getix = (self._first + self._n - 1) // len(self._data)
            ret = self._data[getix]
            self._data[getix] = None
            self._n -= 1

            # If we're down to smaller than a quarter occupied,
            # cut array size in half.
            if self._n < len(self._data) // 4:
                self._resize(len(self._data) // 2)

        else:
            raise Empty("oops, empty deque")

    def _resize(self, newcap):

        old = self._data
        self._data = [None] * newcap
        walk = self._first

        # Need to pay close attention here:
        # range over each of the n elements
        for k in range(self._n):
            self._data[k] = old[walk]
            # Increment walk after the update, not before
            walk += 1
            walk %= len(old)

        self._first = 0


if __name__ == "__main__":
    d = ArrayDeque()
    for i, c in enumerate("ABCDEFGHIJKLMNOP"):
        d.add_first(c)
        print(d)

    for j in range(100):
        try:
            d.delete_first()
            print(d)
        except Empty:
            pass

    print("Length of d: {0}".format(len(d)))

    for i, c in enumerate("12345"):
        d.add_last(c)
        print(d)

    for j in range(4):
        d.delete_last()
        print(d)

    print("final:")
    print(d)
