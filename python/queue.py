class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    """
        Queue will be implemented with a linked list as the start
        of the queue as the tail, and the end of the queue as the head.
        This way, enqueue's and dequeue's are O(1).

        Enqueue is appending from the tail, dequeueing is reassigning
        the pointer of the head to None.
    """
    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        self.size = 0

        if iterable:
            for data in iterable:
                self.append(data)

    def append(self, data):
        new_node = Node(data)

        node = self.head
        while node.next is not None:
            node = node.next

        node.next = new_node

    def enqueue(self, data):
        node = self.tail

        node.append(data)

    def dequeue(self):
        next_node = self.head.next

        self.head.next = None
        self.head = next_node
