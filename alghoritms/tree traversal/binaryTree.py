class Tree:

    def __init__(self):
        self.root = None

    def add_root(self, val):
        self.root = Node(val)


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Queue:
    class _Node:
        def __init__(self, val, next=None):
            self.val = val
            self.next = next

    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def enqueue(self, v):
        node = self._Node(v)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self._size += 1

    def dequeue(self):
        if not self.is_empty():
            val = self.head.val
            self.head = self.head.next
            self._size -= 1

            return val


if __name__ == '__main__':
    T = Tree()

    T.add_root(1)

    T.root.left = Node(2)
    T.root.right = Node(3)
    T.root.left.left = Node(4)
    T.root.left.right = Node(5)
    T.root.left.left.left = Node(6)
    T.root.right.left = Node(7)
    T.root.right.right = Node(8)


    #      1
    #    2   3
    #   4 5 7 8
    #  6

    print('pre order')

    def preorder(root):

        if root:
            print(root.val)
            preorder(root.left)
            preorder(root.right)


    preorder(T.root)  # 1 2 4 6 5 3

    print('post order')

    def postorder(root):

        if root:
            preorder(root.left)
            preorder(root.right)
            print(root.val)


    postorder(T.root)  # 6 4 5 2 7 8 3 1

    print('in order')

    def inorder(root):

        if root:
            inorder(root.left)
            print(root.val)
            inorder(root.right)


    inorder(T.root)  # 6 4 2 5 1 7 3 8 1

    print('breadth first')

    def breadthfirst(root):

        queue = Queue()

        queue.enqueue(root)

        while not queue.is_empty():
            node = queue.dequeue()

            if node:
                queue.enqueue(node.left)
                queue.enqueue(node.right)

                print(node.val)


    breadthfirst(T.root)  # 1 2 3 4 5 7 8 6
