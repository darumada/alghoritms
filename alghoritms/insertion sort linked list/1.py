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


class PositionalList(DoublyLinkedList):
    class Position:
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node.element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            return not (self == other)

    def validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node.next is None:
            raise ValueError('p is no longer valid')

        return p._node

    def make_position(self, node):
        if node is self.header or node is self.trailer:
            return None
        else:
            return self.Position(self, node)

    def first(self):
        return self.make_position(self.header.next)

    def last(self):
        return self.make_position(self.trailer.prev)

    def before(self, p):
        node = self.validate(p)
        return self.make_position(node.prev)

    def after(self, p):
        node = self.validate(p)
        return self.make_position(node.next)

    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    def insert_between(self, e, next, prev):
        node = super().insert_between(e, next, prev)
        return self.make_position(node)

    def add_before(self, p, e):
        node = self.validate(p)
        return self.insert_between(e, node, node.prev)

    def add_after(self, p, e):
        node = self.validate(p)
        return self.insert_between(e, node.next, node)

    def delete(self, p):
        node = self.validate(p)
        return self.delete_node(node)

    def replace(self, p, e):
        node = self.validate(p)
        old_value = node.element
        node.element = e
        return old_value


def insertion_sort(linked_list):
    marker = linked_list.first()

    while marker != linked_list.last():
        pivot = linked_list.after(marker)
        value = pivot.element()

        if value > marker.element():
            marker = pivot
        else:
            walk = marker
            while walk != linked_list.first() and linked_list.before(walk).element() > value:
                walk = linked_list.before(walk)

            linked_list.delete(pivot)
            linked_list.add_before(walk, value)

