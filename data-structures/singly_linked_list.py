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
                self.append(node(data))

    def insert_at_index():
        pass

    def prepend():
        pass

    def append():
        pass

    def delete():
        pass
