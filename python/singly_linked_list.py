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

    def insert_at_index(self):
        pass

    def delete(self):
        pass

    def reverse(self):
        prev_node = None
        current_node = self.head
        next_node = None

        while current_node:
            next_node = current_node.next # temp var for next node

            current_node.next = prev_node # 1st iteration: tail points to None
            prev_node = current_node # set prev_node for next iteration
            current_node = next_node # set current_node for next iteration
        return prev_node
