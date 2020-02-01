class LinkedList:
    class _Node:
        def __init__(self, element, next=None):
            self.element = element
            self.next = next

    def __init__(self):
        self._size = 0
        self.head = None
        self.tail = None

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def add_first(self, e):
        self.head = self._Node(e, self.head)

        if self.is_empty():
            self.tail = self.head

        self._size += 1

    def add_last(self, e):
        node = self._Node(e)

        if self.is_empty():
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

        self._size += 1

    def remove_first(self):

        if self.is_empty():
            raise Error()

        element = self.head.element

        self.head = self.head.next

        self._size -= 1

        return element


class Error(Exception):
    pass

if __name__ == "__main__":

    list = LinkedList()

    list.add_first(1)
    list.add_first(2)
    list.add_first(3)
    list.add_first(4)
    list.add_last(5)
    list.add_last(6)
    list.add_last(7)
    list.add_last(8)

    list.remove_first()

    def traversal(list):
        head = list.head
        while head is not None:
            print(head.element)
            head = head.next


    traversal(list)


