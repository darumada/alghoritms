class Deque:
    def __init__(self):
        self._n = 0
        self._header = Node(None, None, None)
        self._trailer = Node(None, None, None)

        self._header.next = self._trailer
        self._trailer.prev = self._header

    def __len__(self):
        return self._n

    def is_empty(self):
        return self._n == 0

    def append_left(self, e):
        self.insert_between(e, self._header.next, self._header)

    def append_right(self, e):
        self.insert_between(e, self._trailer, self._trailer.prev)

    def insert_between(self, e, next, prev):
        node = Node(e, next, prev)
        next.prev = node
        prev.next = node

        self._n += 1

    def pop_left(self):
        if self.is_empty():
            raise Error()

        return self.delete_node(self._header.next)

    def pop_right(self):
        if self.is_empty():
            raise Error()

        return self.delete_node(self._trailer.prev)

    def delete_node(self, node):
        prev = node.prev
        next = node.next

        element = node.element

        prev.next = next
        next.prev = prev

        node.prev = node.next = node.element = None

        self._n -= 1

        return element



class Node:
    def __init__(self, element, next=None, prev=None):
        self.element = element
        self.next = next
        self.prev = prev


class Error(Exception):
    pass


if __name__ == "__main__":
    d = Deque()

    d.append_left(10)
    d.append_left(2)
    d.append_left(10)
    d.append_left(8)
    d.append_right(20)
    d.append_right(21)

    print(d.pop_right())
    print(d.pop_left())
    print(len(d))
