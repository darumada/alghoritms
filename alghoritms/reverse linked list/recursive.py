class List:
    class _Node:
        def __init__(self, val, next=None):
            self.val = val
            self.next = next

    def __init__(self):
        self.head = None

    def reverse_util(self, curr, prev):
        if curr.next is None:
            curr.next = prev
            self.head = curr
            return

        next = curr.next
        curr.next = prev

        self.reverse_util(next, curr)

    def reverse(self):
        if self.head is None:
            return

        self.reverse_util(self.head, None)



