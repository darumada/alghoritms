class BinarySearchTree:
    class _Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def _insert(self, root, data):
        if root.data < data:
            if root.right is None:
                root.right = self._Node(data)
            else:
                self._insert(root.right, data)
        else:
            if root.left is None:
                root.left = self._Node(data)
            else:
                self._insert(root.left, data)

    def _search(self, root, item):
        if root is None:
            return None

        if root.data == item:
            return root
        elif root.data < item:
            return self._search(root.right, item)
        else:
            return self._search(root.left, item)

    def _min(self, root):
        if root.left is None:
            return root
        else:
            return self._min(root.left)

    def _max(self, root):
        if root.right is None:
            return root
        else:
            return self._min(root.right)

    def _delete(self, root, item):
        if root is None:
            return root

        if root.data > item:
            root.left = self._delete(root.left, item)
        elif root.data < item:
            root.right = self._delete(root.right, item)

        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self._min(root.right)

            root.data = temp.data

            root.right = self._delete(root.right, temp.data)

        return root

    def append(self, data):
        if self.root is None:
            self.root = self._Node(data)
        else:
            self._insert(self.root, data)

    def search(self, item):
        return self._search(self.root, item)

    def min(self):
        return self._min(self.root)

    def max(self):
        return self.max(self.root)

    def delete(self, item):
        self._delete(self.root, item)


