class BinaryTree:
    class _Node:
        def __init__(self, e, parent=None):
            self.element = e
            self.parent = parent
            self.left = None
            self.right = None

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

    def append_left(self, node, e):
        node.left = self._Node(e, node)
        self._size += 1

    def append_right(self, node, e):
        node.right = self._Node(e, node)
        self._size += 1

    def num_children(self, node):
        count = 0

        if node.left is not None:
            count += 1

        if node.rigth is not None:
            count += 1

        return count

    def delete(self, node):
        if self.num_children(node) == 2:
            raise ValueError('node has two children')

        child = node.left if node.left else node.right

        if child is not None:
            child.parent = node.parent

        if node is self.root:
            self.root = child
        else:
            parent = node.parent
            if node is parent.left:
                parent.left = child
            else:
                parent.right = child

            self.size -= 1

            return node.element
