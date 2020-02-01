class Stack:

    def __init__(self):
        self._n = 0
        self._head = None

    def __len__(self):
        return self._n

    def is_empty(self):
        return self._n == 0

    def append(self, data):
        self._head = Node(data, self._head)
        self._n += 1

    def pop(self):
        if self.is_empty():
            raise Error()

        ret = self._head.element
        self._head = self._head.next
        self._n -= 1

        return ret

    def top(self):
        if self.is_empty():
            raise Error()

        return self._head.element


class Node:
    def __init__(self, element, next):
        self.element = element
        self.next = next


class Error(Exception):
    pass
