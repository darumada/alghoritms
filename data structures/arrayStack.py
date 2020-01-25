class ArrayStack:

    def __init__(self):
        self._list = []

    def __len__(self):
        return len(self._list)

    def is_empty(self):
        return len(self._list) == 0

    def last(self):
        if self.is_empty():
            raise EmptyError('stack is empty')
        return self._list[-1]

    def append(self, item):
        self._list.append(item)

    def pop(self):
        if self.is_empty():
            raise EmptyError('stack is empty')
        return self._list.pop()


class EmptyError(Exception):
    pass


stack = ArrayStack()

stack.append(10)

print(stack.last())

print(stack.pop())
