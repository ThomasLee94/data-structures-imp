from singly_linked_list import SinglyLinkedList

class Queue(object):
    """
        Queue will be implemented with a linked list as the start
        of the queue as the head, and the end of the queue as the tail.
        This way, enqueue's and dequeue's are O(1).

        Enqueue is appending from the tail, dequeueing is reassigning
        the pointer of the head to None.
    """
    def __init__(self, iterable=None):
        self.queue = SinglyLinkedList()
        if iterable:
            for data in iterable:
                self.enqueue(data)

    def is_empty(self):
        if self.queue.size < 1:
            return True
        return False

    def front(self):
        if self.is_empty():
            return None
        return self.head.data

    def append(self, data):
        new_node = Node(data)

        node = self.head
        while node.next is not None:
            node = node.next

        node.next = new_node
        self.length += 1

    def enqueue(self, data):
        self.tail.append(data)

    def dequeue(self):
        next_node = self.head.next

        self.head.next = None
        self.head = next_node
        self.length -= 1
