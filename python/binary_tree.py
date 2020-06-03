class BinaryTreeNode(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def is_leaf(self):
        return self.left is None and self.right is None

    def is_branch(self):
        return self.left is not None or self.right is not None

    def height(self):
        if self.left is not None:
            left = self.left.height()
        else:
            left = -1

        if self.right is not None:
            right = self.right.height()
        else:
            right = -1

        return max(left, right) + 1

class BinarySearchTree(object):
    def __init__(self, iterable=None):
        self.root = None
        self.size = 0

        if iterable:
            for data in iterable:
                self.insert(data)

    def is_empty(self):
        if self.size == 0:
            return None

    def find_parent_node(self, item, node, parent=None):
        if node is None:
            return parent

        if item is node.data:
            return parent
        elif item < node.data:
            return self.find_parent_node(item, node.left, node)
        elif item > node.data:
            return self.find_parent_node(item, node.right, node)

        return parent


    def insert(self, data):
        if self.is_empty():
            self.root = BinaryTreeNode(data)
            self.size += 1

        parent = self.find_parent_node(data, self.root)

        if data < parent.data:
            parent.left = BinaryTreeNode(data)
        if data > parent.data:
            parent.right = BinaryTreeNode(data)
        self.size += 1

    def delete(self, data):
        parent = self.find_parent_node(data, self.root)

        if parent.left == data:
            parent.left = None
        elif parent.right == data:
            parent.right = None
        else:
            raise ValueError("data does not exist")

    def traverse(self, node, visit):
        """
            pre order traversal.
        """
        if node is None:
            node = self.root

        visit(node.data)
        self.traverse(node.left, visit)
        self.traverse(node.right, visit)

    def search(self, data, node=None):
        if node is None:
            node = self.root

        if node.data == data:
            return node

        if data < node.data:
            self.search(data, node.left)
        if data > node.data:
            self.search(data, node.right)
