class Stack(object):
    """
        Stack implementation with list. The top of
        the stack is the end of the list, the bottom of the stack is the beginning.

        push - prepend, O(1)
        pop - change pointer of head, O(1)
        peek - O(1)
    """

    def __init__(self, iterable=None):
        self.stack = list()

        if iterable:
            for data in iterable:
                self.stack.append(data)

    def is_empty(self):
        if len(self.stack) < 1:
            return True
        return False

    def length(self):
        return len(self.stack)

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            raise ValueError('Linked list length is 0')

        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]
