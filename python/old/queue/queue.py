from singly_linked_list import SinglyLinkedList

class Queue:
    """
        Queue will be implemented with a linked list as the start
        of the queue as the tail, and the end of the queue as the head.
        This way, enqueue's and dequeue's are O(1).

        Enqueue is appending from the tail, dequeueing is reassigning
        the pointer of the head to None.
    """
    def __init__(self, iterable=None):
        self.queue = SinglyLinkedList()

        if iterable:
            for item in iterable:
                self.queue.append(item)

    def is_empty(self):
        return self.queue.is_empty()

    def length(self):
        return self.queue.size

    def front(self):
        if self.queue.is_empty():
            return None
        return self.queue.head.data

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.queue.size < 1:
            raise ValueError("queue is empty")

        output = self.front()

        self.queue.delete(output)

        return output
