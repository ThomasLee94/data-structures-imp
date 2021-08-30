# LRU Cache
# The LRU Cache will have a queue (Doubley Linked List) & a dictionary.
# We need to use a queue (dll) to reorder accessed keys
# We need a dictionary to map keys to values for O(1) Get & Put functions

# It needs to be a doubly linked list because if it was a singly linked list, deleting would be O(n)

# The cache has a max capacity
# get(key) function, return the value of a key if it exists, else -1
# insert(key, val) function, update the key with value if key exists, otherwise add key-val pair to cache. If the number exceeds the capacity, 
    # evict the least recently used key

# new items get added to the beginning of our queue
# begginning of the queue (head) represents most used item, end of queue (tail) represents least used.

# space heavy - O(2n) because it stores a queue (dll) & dictionary, but constant lookups & removals. 

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val

        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
    
    def insert(self, node):
        if self.head is None:
            self.head = node
        else:
            node.prev = self.tail
            self.tail.next = node
        
        self.tail = node

    def remove(self, node):
        node.prev.next = node.next 
        node.next.prev = node.prev

class LRU_Cache:
    def __init__(self, capacity, iterable=None):
        self.capacity = capacity
        self.queue = DoublyLinkedList()
        self.seen = {}

        if iterable:
            for item in iterable:
                self.insert(item)

    def get(self, key):
        if key in self.seen:
            node = self.seen[key]
            # remove then insert to maintain used ordering
            self.remove(node.key)
            self.queue.remove(node)
            self.insert(node.key, node.val)
            self.queue.insert(node)

            return node.val
        
        return -1 # error, key does not exist 
    
    def insert(self, key, val):
        if len(self.seen) > self.capacity:
            self.queue.remove(self.queue.tail)
            self.remove(self.queue.tail.key)
            
        node = Node(key, val)
        self.queue.insert(node)

    def remove(self, key):
        del self.seen[key]

def test_lru():
    cache = LRU_Cache(2)

    cache.insert(1,1)
    assert cache.items() == {1:1}

    cache.insert(2,2)
    assert cache.items() == {1:1, 2:2}

    assert cache.get(1) == 1

    cache.insert(3,3)
    assert cache.items() == {1:1, 3:3}

    assert cache.get(2) == -1

    cache.insert(4,4)
    assert cache.items() == {4:4, 3:3}

    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4


if __name__ == "__main__":
    test_lru()

