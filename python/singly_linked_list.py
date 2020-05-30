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

    def is_empty(self):
        return self.head is None

    def prepend(self, data):
        new_node = Node(item)

        if self.is_empty():
            # Assign tail to new node
            self.tail = new_node
            self.size += 1
        else:
            # Otherwise insert new node before head
            new_node.next = self.head
            self.size += 1
        self.head = new_node

    def append(self, data):
        new_node = Node(data)

        node = self.head
        while node.next is not None:
            node = node.next

        node.next = new_node

    def node_at_index(self, index):
        if not (0 <= index < self.size):
            raise ValueError("List index out of range")

        node = self.head
        for _ in range(index):
            node = node.next
        return node

    def insert_at_index(self, index, item):
        if not (0 <= index <= self.size):
            raise ValueError('List index out of range')

        if index == 0:
            self.prepend(item)

        if index == self.size:
            self.append(item)
        else:
            new_node = Node(item)
            index_node = self.node_at_index(index)
            previous_node = self.node_at_index(index - 1)

            new_node.next = index_node
            previous_node.next = new_node

            self.size += 1

    def delete(self, item):
        
        node = self.head
        previous_node = None
        next_node = None

        for _ in range(self.size):
            previous_node = node
            
            if node.data == item:
                break
            node = node.next



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
