class MaxStack:
    class _Node:
        def __init__(self, value, next=None):
            self.val = value
            self.next = next

    def __init__(self):
        self._max = None
        self.head = None

    def push(self, val):

        if self.head is None:
            self.head = self._Node(val)
            self._max = val
            return

        if val > self._max:
            temp = self._max
            self._max = val
            val = val * 2 + temp

        self.head = self._Node(val, self.head)

    def pop(self):
        val = self.head.val

        if val > self._max:
            temp = self._max
            self._max = val - self._max * 2
            val = temp

        self.head = self.head.next

        return val

    def top(self):
        if self.head is None:
            return None

        val = self.head.val

        if val > self._max:
            val = self._max

        return val

    def get_max(self):
        return self._max
