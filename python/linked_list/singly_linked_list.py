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

    def items(self):
        node = self.head
        output = list()

        for _ in range(self.size):
            output.append(node.data)
            node = node.next

        return output

    def length(self):
        return self.size

    def replace(self, old, new):
        node = self.head

        for _ in range(self.size):
            if node.data == old:
                node.data = new
                return
            node = node.next
        raise ValueError("item does not exist")

    def prepend(self, item):
        new_node = Node(item)

        if self.is_empty():
            self.tail = new_node
            self.size += 1
        else:
            new_node.next = self.head
            self.size += 1
        self.head = new_node

    def append(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
            self.size += 1
        else:
            self.tail.next = new_node
            self.size += 1
        self.tail = new_node

    def find(self, quality):
        node = self.head
        while node is not None:
            if quality(node.data):
                return node.data
            node = node.next
        return None

    def get_at_index(self, index):
        if not (0 <= index < self.size):
            raise ValueError('List index out of range: {}'.format(index))

        node = self.head

        for _ in range(index):
            node = node.next
        return node.data


    def node_at_index(self, index):
        if not (0 <= index < self.size):
            raise ValueError('List index out of range: {}'.format(index))

        node = self.head

        for _ in range(index):
            node = node.next
        return node

    def insert_at_index(self, index, item):
        if not (0 <= index <= self.size):
            raise ValueError('List index out of range')

        if index == 0:
            self.prepend(item)
            return

        if index == self.size:
            self.append(item)
            return

        else:
            new_node = Node(item)
            previous_node = self.node_at_index(index - 1)
            index_node = self.node_at_index(index)

            new_node.next = index_node
            previous_node.next = new_node

            self.size += 1

    def delete(self, item):

        node = self.head
        previous = None
        found = False

        while not found and node is not None:
            if node.data == item:
                found = True
            else:
                previous = node
                node = node.next

        if found:
            if node is not self.head and node is not self.tail:
                previous.next = node.next
                node.next = None
                self.size -= 1

            if node is self.head:
                self.head = node.next
                node.next = None
                self.size -= 1

            if node is self.tail:
                if previous is not None:
                    previous.next = None
                    self.size -= 1
                self.tail = previous
        else:
            raise ValueError('Item not found: {}'.format(item))


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
