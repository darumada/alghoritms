class PriorityQueue:
    class _Node:
        def __init__(self, key, val, next=None):
            self.key = key
            self.val = val
            self.next = next

    def __init__(self):
        self.head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def enqueue(self, key, val):
        node = self._Node(key, val)
        if self.is_empty():
            self.head = node
        else:
            if self.head.key > key:
                node.next = self.head
                self.head = node
            else:
                prev = self.head
                current = self.head.next
                while current and current.key < key:
                    current = current.next
                    prev = prev.next

                prev.next = node
                node.next = current

        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise Error()

        val = self.head.val
        self.head = self.head.next

        self._size -= 1
        return val


class Error(Exception):
    pass


if __name__ == '__main__':
    P = PriorityQueue()

    P.enqueue(1, 200)
    P.enqueue(4, 2)
    P.enqueue(2, 20)
    P.enqueue(-1, 1)

    print(P.dequeue())  # 1
    print(P.dequeue())  # 200
    print(P.dequeue())  # 20
    print(P.dequeue())  # 2
