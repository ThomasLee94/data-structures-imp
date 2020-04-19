class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:

    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        self.size = 0

        if iterable:
            for data in iterable:
                self.append(Node(data))

    def prepend(node):
        pass

    def append():
        pass

    def insert_at_index():
        pass

    def delete():
        pass
