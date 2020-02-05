class MinStack:
    class _Node:
        def __init__(self, value, next=None):
            self.val = value
            self.next = next

    def __init__(self):
        self._min = None
        self.head = None

    def push(self, val):

        if self.head is None:
            self.head = self._Node(val)
            self._min = val
            return

        if val < self._min:
            temp = self._min
            self._min = val
            val = val * 2 - temp

        self.head = self._Node(val, self.head)

    def pop(self):
        val = self.head.val

        if val < self._min:
            temp = self._min
            self._min = self._min * 2 - val
            val = temp

        self.head = self.head.next

        return val

    def top(self):
        if self.head is None:
            return None

        val = self.head.val

        if val < self._min:
            val = self._min

        return val

    def get_min(self):
        return self._min
