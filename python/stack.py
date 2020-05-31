from singly_linked_list import SinglyLinkedList

class Stack(object):
    """
        Stack implementation with linkedlist. The top of
        the stack is the head, the bottom of the stack is the tail.

        push - prepend, O(1)
        pop - change pointer of head, O(1)
        peek - O(1)
    """

    def __init__(self, iterable=None):
        self.stack = SinglyLinkedList()

        if iterable:
            for data in iterable:
                self.stack.prepend(data)

    def is_empty(self):
        if self.stack.size < 1:
            return True
        return False

    def length(self):
        return self.stack.size

    def push(self, item):
        self.stack.prepend(item)

    def pop(self):
        if self.stack.length() == 0:
            raise ValueError('Linked list length is 0')

        if self.stack.is_empty():
            raise ValueError("Node is empty")

        item = self.stack.head.data
        self.stack.delete(item)
        return item

    def peek(self):
        if self.stack.is_empty():
            return None
        return self.stack.head.data
