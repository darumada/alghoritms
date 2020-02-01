class DoublyLinkedList:
    class _Node:
        def __init__(self, element, next=None, prev=None):
            self.element = element
            self.next = next
            self.prev = prev

    def __init__(self):
        self._size = 0
        self.header = self._Node(None, None, None)
        self.trailer = self._Node(None, None, None)

        self.header.next = self.trailer
        self.trailer.prev = self.header

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def add_first(self, e):
        return self.insert_between(e, self.header.next, self.header)

    def add_last(self, e):
        return self.insert_between(e, self.trailer, self.trailer.prev)

    def insert_between(self, e, next, prev):
        new_node = self._Node(e, next, prev)

        next.prev = new_node
        prev.next = new_node

        self._size += 1

        return new_node

    def delete_node(self, node):
        prev = node.prev
        next = node.next

        element = node.element

        prev.next = next
        next.prev = prev

        node.prev = node.next = node.element = None

        self._size -= 1

        return element


if __name__ == "__main__":

    list = DoublyLinkedList()

    list.add_first(1)
    list.add_first(2)
    list.add_first(3)
    list.add_first(4)
    list.add_last(5)
    list.add_last(6)
    list.add_last(7)
    list.add_last(8)


    def traversal(list):
        head = list.header.next
        while head is not list.trailer:
            print(head.element)
            head = head.next

    traversal(list)