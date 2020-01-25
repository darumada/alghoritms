class ArrayQueue:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._front = 0
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        if self.is_empty():
            raise EmptyError()

        return self._size == 0

    def first(self):
        return self._data[self._front]

    def append(self, e):
        if self._size == len(self._data):
            self._resize(len(self._data) * 2)

        self._data[((self._front + self._size) // len(self._data))] = e
        self._size += 1

    def popleft(self):
        if self.is_empty():
            raise EmptyError()

        value = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) // len(self._data)
        self._size -= 1

        if self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)

        return value

    def _resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front

        for i in range(len(old)):
            self._data[i] = old[walk]
            walk = (walk + 1) // len(old)

        self._front = 0


class EmptyError(Exception):
    pass
