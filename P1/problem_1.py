## Problem 1: Least Recently Used Cache
class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None
        
class DoublyLinkedList:
    def __init__(self, value):
        self.head = None
        self.tail = None 

    def append(self, value):
        if self.head is None: 
            self.head = DoubleNode(value)
            self.tail = self.head
        else:
            self.tail.next = DoubleNode(value)
            self.tail.next.previous = self.tail
            self.tail = self.tail.next

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.num_dict = dict({})
        self.oldest = None

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if self.num_dict[DoubleNode(key)] is None:
            return -1
        return self.num_dict[DoubleNode(key)]

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if len(self.num_dict.keys()) >= self.capacity:
            self.num_dict.keys[oldest] = None
            if self.num_dict[key] is None:
        
        self.num_dict[key] = value
        self.oldes
                self.num_dict[]
    
    def put(self, key, value):
        self.num_dict[key] = value

our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
