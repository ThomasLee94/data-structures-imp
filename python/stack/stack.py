class Stack(object):
    """
        Stack implementation with list. The top of
        the stack is the end of the list, the bottom 
        of the stack is the beginning.

        push - prepend, O(1)
        pop - change pointer of head, O(1)
        peek - O(1)
    """

    def __init__(self, iterable=None):
        self.stack = list()
        self.size = 0

        if iterable:
            for data in iterable:
                self.push(data)

    def is_empty(self):
        return self.size == 0

    def push(self, item):
        self.stack.append(item)
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise ValueError('Linked list length is 0')

        self.size -= 1
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]


obj = Stack([1, 5, 8])
obj.push(11)
res = obj.pop()
print(obj.peek())


