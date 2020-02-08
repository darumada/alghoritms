class Tree:

    def __init__(self):
        self.root = None

    def add_root(self, val):
        self.root = Node(val)


class Node:
    def __init__(self, val):
        self.val = val
        self.children = []


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

    T.root.children.append(Node(2))
    T.root.children.append(Node(3))
    T.root.children[0].children.append(Node(4))
    T.root.children[0].children.append(Node(5))
    T.root.children[1].children.append(Node(7))
    T.root.children[1].children.append(Node(8))
    T.root.children[0].children[0].children.append(Node(6))

    #      1
    #    2   3
    #   4 5 7 8
    #  6

    print('pre order')


    def preorder(root):
        print(root.val)

        for child in root.children:
            preorder(child)


    preorder(T.root)  # 1 2 4 6 5 3 7 8

    print('post order')


    def postorder(root):

        for child in root.children:
            postorder(child)

        print(root.val)


    postorder(T.root)  # 6 4 5 2 7 8 3 1

    print('breadth first')

    def breadthfirst(root):

        queue = Queue()

        queue.enqueue(root)

        while not queue.is_empty():
            node = queue.dequeue()

            for child in node.children:
                queue.enqueue(child)

            print(node.val)


    breadthfirst(T.root)  # 1 2 3 4 5 7 8 6
