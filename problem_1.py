# Your job is to use an appropriate data structure(s) to implement the cache.
# In case of a cache hit, your get() operation should return the appropriate value.
# In case of a cache miss, your get() should return -1.
# While putting an element in the cache, your put() / set() operation must insert the element.
# If the cache is full,
# you must write code that removes the least recently used entry first and then insert the element.
from collections import OrderedDict

class LRU_Cache(object):

    def __init__(self, capacity=5):
        # Initialize class variables
        self.capacity=5
        self.cache= OrderedDict()
        self.num_elements=0
        pass

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.cache:
            x=self.cache[key]
            del self.cache[key]
            self.cache[key]=x
            return x
        else:
            return -1
        pass

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if self.num_elements<5:
            self.cache[key]=value
            self.num_elements+=1
        else:
            self.cache.popitem(last=False)
            self.cache[key]=value
        pass

our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


assert(our_cache.get(1)==1)    # returns 1
assert(our_cache.get(2)==2)      # returns 2
assert(our_cache.get(9)==-1)     # returns -1 because 9 is not present in the cache
our_cache.set(5, 5)
our_cache.set(6, 6)
assert(our_cache.get(3)==-1)     # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
