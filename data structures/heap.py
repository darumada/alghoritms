class MinHeap:
    def __init__(self):
        self._data = []

    def __str__(self):
        return self._data.__str__()

    def __repr__(self):
        return self._data.__repr__()

    def __len__(self):
        return len(self._data)

    def _left(self, i):
        return 2 * i + 1

    def _right(self, i):
        return 2 * i + 2

    def _parent(self, i):
        return (i - 1) // 2

    def _has_left(self, i):
        return self._left(i) < len(self._data)

    def _has_right(self, i):
        return self._right(i) < len(self._data)

    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, i):
        parent = self._parent(i)

        if i > 0 and self._data[parent] > self._data[i]:
            self._swap(parent, i)
            self._upheap(parent)

    def _downheap(self, i):
        if self._has_left(i):
            left = self._left(i)
            smallest = left

            if self._has_right(i):
                right = self._right(i)
                if self._data[right] < self._data[left]:
                    smallest = right

            if self._data[i] > self._data[smallest]:
                self._swap(i, smallest)
                self._downheap(smallest)


    def is_empty(self):
        return len(self._data) == 0

    def push(self, v):
        self._data.append(v)
        self._upheap(len(self._data) - 1)

    def pop(self):
        if not self.is_empty():
            self._swap(0, len(self._data) - 1)

            ret = self._data.pop()

            self._downheap(0)

            return ret


if __name__ == '__main__':
    M = MinHeap()

    M.push(10)
    M.push(5)
    M.push(13)
    M.push(8)
    M.push(3)
    M.push(1)
    M.push(20)

    print(M.pop())
    print(M.pop())
    print(M.pop())

    print(M)

