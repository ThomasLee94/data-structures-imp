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
                self.append(data)

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        node = self.tail
        node.next = new_node
        self.tail = new_node

    def insert_at_index():
        pass

    def delete():
        pass
