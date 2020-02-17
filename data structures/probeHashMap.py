import random

"""

Linear probe Hash map with MAD (Multiply-Add-and-Divide) hash function

[(ai+b) mod p] mod N

where N is the size of the bucket array, p is a prime number larger than N, and a and b are integers chosen at random from the interval [0, p − 1], with a > 0.

"""


class LinearProbeHashMap:
    _AVAIL = object()

    class _Item:
        def __init__(self, key, value):
            self.key = key
            self.value = value

    def __init__(self):
        self._capacity = 11
        self._p = 1046527
        self._a = random.randint(0, self._p - 1)
        self._b = random.randint(0, self._p - 1)
        self._table = [None] * self._capacity
        self._size = 0

    def __len__(self):
        return self._size

    def _hash_func(self, key):
        return (hash(key) * self._a + self._b) % self._p % self._capacity

    def _is_available(self, i):
        return self._table[i] is None or self._table[i] is LinearProbeHashMap._AVAIL

    def _find(self, key, i):
        first_avail = None
        while True:
            if self._is_available(i):
                if first_avail is None:
                    first_avail = i
                if self._table[i] is None:
                    return False, first_avail
            elif self._table[i].key == key:
                return True, i

            i = (i + 1) % self._capacity

    def __setitem__(self, key, value):
        index = self._hash_func(key)
        found, i = self._find(key, index)

        if not found:
            self._table[i] = self._Item(key, value)
            self._size += 1
        else:
            self._table[i].value = value

        if self._size > len(self._table) * 0.75:
            self._resize(self._capacity * 2 - 1)

    def __getitem__(self, key):
        index = self._hash_func(key)
        found, i = self._find(key, index)

        if found:
            return self._table[i].value

        raise KeyError()

    def __delitem__(self, key):
        index = self._hash_func(key)
        found, i = self._find(key, index)

        if found:
            self._table[i] = LinearProbeHashMap._AVAIL
            self._size -= 1
            return

        raise KeyError()

    def __iter__(self):
        for item in self._table:
            if item is not None:
                yield item.key, item.value

    def _resize(self, new_capacity):
        self._capacity = new_capacity
        old_table = self._table
        self._table = [None] * self._capacity
        self._size = 0

        # rehashing old values
        for item in old_table:
            if item is not None:
                self[item.key] = item.value
