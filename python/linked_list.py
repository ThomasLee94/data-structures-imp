# ALMOST WORKING

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    
class LinkedList:
    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        self.size = 0

        if iterable:
            for item in iterable:
                self.append(item)
    
    def is_empty(self):
        return self.head is None
    
    def items(self):
        items = []

        node = self.head

        while node is not None:
            items.append(node.val)
            node = node.next 
        
        return items
    
    def append(self, val):
        node = Node(val)

        # if ll is empty
        if self.is_empty():
            self.head = node
        else:
            self.tail.next = node
        
        self.tail = node
        self.size += 1

    def prepend(self, val):
        node = Node(val)

        if self.is_empty():
            self.head = node
        else:
            node.next = self.head

        self.head = node
        self.size += 1

    def find(self, val):
        node = self.head

        while node is not None:
            if val == node.val: return node
            node = node.next
        
        return -1 # Not found

    def replace(self, old_val, new_val):
        node = self.head

        while node is not None:
            if node.val == old_val:
                node.val = new_val
                return
            
            node = node.next
        
        return -1 # old_val was not found

    def delete(self, val):
        node = self.head
        found = False
        prev = None

        while node.next is not None:
            if node.val == val: break
            prev = node
            node = node.next 
        
        prev.next = node.next
        node.next = None

    def reverse(self):
        prev, node = None, self.head

        while node is not None:
            node.next = prev # reversal

            # reassign prev & node
            prev = node
            node = node.next 
        
        self.head = prev
        self.tail = self.get_last_node()

    def get_last_node(self):
        node = self.head

        while node is not None:
            node = node.next
        
        return node
if __name__ == "__main__":
    ll = LinkedList(["a", "b", "c", "d"])

    res1 = ll.items()
    ll.reverse()
    res2 = ll.items()
    # print(res2)
    print(ll.head.val)

     

