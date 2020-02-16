class MaxHeap:

    def __init__(self):
        self._data = []

    def __str__(self):
        return self._data.__str__()

    def __repr__(self):
        return self._data.__repr__()

    def __len__(self):
        return len(self._data)

    def _parent(self, i):
        return (i - 1) // 2

    def _left(self, i):
        return i * 2 + 1

    def _right(self, i):
        return i * 2 + 2

    def _has_left(self, i):
        return self._left(i) < len(self._data)

    def _has_right(self, i):
        return self._right(i) < len(self._data)

    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, i):
        parent = self._parent(i)
        if i > 0 and self._data[parent] < self._data[i]:
            self._swap(parent, i)
            self._upheap(parent)

    def _downheap(self, i):
        if self._has_left(i):
            left = self._left(i)
            max_child = left

            if self._has_right(i):
                right = self._right(i)

                if self._data[right] > self._data[left]:
                    max_child = right

            if self._data[i] < self._data[max_child]:
                self._swap(i, max_child)
                self._downheap(max_child)

    def push(self, value):
        self._data.append(value)
        self._upheap(len(self._data) - 1)

    def pop(self):
        if len(self._data) > 0:
            self._swap(0, len(self._data) - 1)

            ret = self._data.pop()

            self._downheap(0)

            return ret


if __name__ == '__main__':
    M = MaxHeap()

    M.push(10)       #     20
    M.push(5)        #   8   13
    M.push(13)       # 5  3  1 10
    M.push(8)
    M.push(3)
    M.push(1)
    M.push(20)

    print(M.pop())
    print(M.pop())
    print(M.pop())

    print(M)