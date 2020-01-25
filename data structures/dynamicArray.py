from ctypes import *


class DArray:

    def __init__(self):
        self._n = 0
        self._capacity = 1;
        self._A = self._make_array(self._capacity)

    def __getitem__(self, index):
        if 0 <= index < len(self._A):
            return self._A[index]
        else:
            raise IndexError('test')

    def __len__(self):
        return self._n

    def append(self, item):
        if self._n == self._capacity:
            self._resize(self._capacity * 2)

        self._A[self._n] = item

        self._n += 1

    def _resize(self, capacity):
        B = self._make_array(capacity)
        for i in range(len(self._A)):
            B[i] = self._A[i]

        self._capacity = capacity

        self._A = B

    def _make_array(self, capacity):
        return (capacity * py_object)()
