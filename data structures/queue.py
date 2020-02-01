class Queue:

    def __init__(self):
        self._n = 0
        self._head = None
        self._tail = None

    def __len__(self):
        return self._n

    def is_empty(self):
        return self._n == 0

    def enqueue(self, data):
        newest = Node(data, None)

        if self.is_empty():
            self._head = newest
        else:
            self._tail.next = newest

        self._tail = newest
        self._n += 1

    def dequeue(self):
        if self.is_empty():
            raise Error()

        ret = self._head.element
        self._head = self._head.next
        self._n -= 1

        return ret


class Node:
    def __init__(self, element, next):
        self.element = element
        self.next = next


class Error(Exception):
    pass


if __name__ == '__main__':
    q = Queue()

    q.enqueue(123)
    q.enqueue(5)
    q.enqueue(7)

    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())