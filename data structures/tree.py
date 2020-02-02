class Tree:
    class _Node:
        def __init__(self, e, parent=None):
            self.element = e
            self.parent = parent
            self.children = []

    def __init__(self):
        self.root = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def add_root(self, e):
        if self.root is not None:
            raise ValueError('Root exists')

        self.root = self._Node(e)
        self._size += 1

    def append_child(self, node, e):
        node.append(self._Node(e, node))
        self._size += 1

    def num_children(self, node):
        return len(node.children)

