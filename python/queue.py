# Creating a queue is O(n)
# Assuming the head is front of the queue & tail is back of queue
    # enqueue & dequeue are O(1)

from linked_list import LinkedList

class Queue:
    def __init__(self, iterable=None):
        self.queue = LinkedList()

        if iterable:
            for item in iterable:
                self.enqueue(item)

    def peek(self):
        return self.queue.head.val
    
    def is_empty(self):
        return self.queue.is_empty()
    
    def enqueue(self, val):
        self.queue.append(val)

    def dequeue(self):
        val = self.peek()

        if val is not None:
            self.queue.delete(val)
        
        return val
