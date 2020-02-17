import random

"""

Chaining Hash map with MAD (Multiply-Add-and-Divide) hash function

[(ai+b) mod p] mod N

where N is the size of the bucket array, p is a prime number larger than N, and a and b are integers chosen at random from the interval [0, p − 1], with a > 0.

"""


class ChainingHashMap:
    class _Node:
        def __init__(self, key, value, next=None):
            self.key = key
            self.value = value
            self.next = next

    def __init__(self):
        self._capacity = 11
        self._p = 1046527
        self._a = random.randint(0, self._p - 1)
        self._b = random.randint(0, self._p - 1)
        self._table = [None] * self._capacity
        # all elements stored in _table
        self._size = 0
        # elements stored in indexes in _table
        self._n = 0

    def __len__(self):
        return self._size

    def _hash_func(self, key):
        return (hash(key) * self._a + self._b) % self._p % self._capacity

    def __setitem__(self, key, value):
        index = self._hash_func(key)
        if self._table[index] is None:
            self._table[index] = self._Node(key, value)
            self._n += 1
            self._size += 1
        else:
            walk = self._table[index]
            while walk is not None:
                if walk.key == key:
                    walk.value = value
                    break
                walk = walk.next

            if walk is None:
                self._table[index] = self._Node(key, value, self._table[index])
                self._size += 1

        if self._n > len(self._table) * 0.75:
            self._resize(self._capacity * 2 - 1)

    def __getitem__(self, key):
        index = self._hash_func(key)
        walk = self._table[index]
        while walk is not None:
            if walk.key == key:
                return walk.value
            walk = walk.next

        raise KeyError()

    def __delitem__(self, key):
        index = self._hash_func(key)
        if self._table[index] is not None:
            if self._table[index].key == key:
                self._table[index] = self._table[index].next
                self._size -= 1

                if self._table[index] is None:
                    self._n -= 1

                return
            else:
                slow = self._table[index]
                fast = self._table[index].next

                while fast is not None:
                    if fast.key == key:
                        slow.next = fast.next
                        self._size -= 1
                        return

                    slow = slow.next
                    fast = fast.next

        raise KeyError()

    def __iter__(self):
        for node in self._table:
            walk = node
            while walk is not None:
                yield walk.key, walk.value
                walk = walk.next

    def _resize(self, new_capacity):
        self._capacity = new_capacity
        old_table = self._table
        self._table = [None] * self._capacity
        self._n = 0
        self._size = 0

        # rehashing old values
        for node in old_table:
            walk = node
            while walk is not None:
                self[walk.key] = walk.value
                walk = walk.next

