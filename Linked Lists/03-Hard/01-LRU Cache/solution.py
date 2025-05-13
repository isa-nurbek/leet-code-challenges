# Problem Description:

"""
                                            LRU Cache

Implement an `LRUCache` class for a Least Recently Used (LRU) cache. The class should support:

- Inserting key-value pairs with the `insertKeyValuePair` method.
- Retrieving a key's value with the `getValueFromKey` method.
- Retrieving the most recently used (the most recently inserted or retrieved) key with the `getMostRecentKey` method.

Each of these methods should run in constant time.

Additionally, the `LRUCache` class should store a `maxSize` property set to the size of the cache, which is passed in as an
argument during instantiation. This size represents the maximum number of key-value pairs that the cache can store at once. If
a key-value pair is inserted in the cache when it has reached maximum capacity, the least recently used key-value pair should be
evicted from the cache and no longer retrievable; the newly added key-value pair should effectively replace it.

Note that inserting a key-value pair with an already existing key should simply replace the key's value in the cache with the new
value and shouldn't evict a key-value pair if the cache is full. Lastly, attempting to retrieve a value from a key that isn't in
the cache should return `None`.


## Sample Usage:
```
// All operations below are performed sequentially.

LRUCache(3): -  // instantiate an LRUCache of size 3
insertKeyValuePair("b", 2): -
insertKeyValuePair("a", 1): -
insertKeyValuePair("c", 3): -
getMostRecentKey(): "c"  // "c" was the most recently inserted key
getValueFromKey("a"): 1
getMostRecentKey(): "a"  // "a" was the most recently retrieved key
insertKeyValuePair("d", 4): -  // the cache had 3 entries; the least recently used one is evicted
getValueFromKey("b"): None  // "b" was evicted in the previous operation
insertKeyValuePair("a", 5): -  // "a" already exists in the cache so its value just gets replaced
getValueFromKey("a"): 5
```

## Optimal Time & Space Complexity:
```
All 3 methods: `insertKeyValuePair`, `getValueFromKey`, `getMostRecentKey` - O(1) time | O(1) space.
```

"""

# =========================================================================================================================== #

# Solution:


class LRUCache:
    def __init__(self, maxSize):
        self.cache = {}
        self.maxSize = max(1, maxSize)  # Ensures maxSize is at least 1
        self.listOfMostRecent = DoublyLinkedList()

    def insertKeyValuePair(self, key, value):
        if key in self.cache:
            self._replace_value(key, value)
        else:
            if len(self.cache) == self.maxSize:
                self._evict_least_recent()
            self.cache[key] = DoublyLinkedListNode(key, value)
        self._update_most_recent(self.cache[key])

    def getValueFromKey(self, key):
        if key not in self.cache:
            return None
        self._update_most_recent(self.cache[key])
        return self.cache[key].value

    def getMostRecentKey(self):
        return self.listOfMostRecent.head.key if self.listOfMostRecent.head else None

    def _evict_least_recent(self):
        key_to_remove = self.listOfMostRecent.tail.key
        self.listOfMostRecent.remove_tail()
        del self.cache[key_to_remove]

    def _update_most_recent(self, node):
        self.listOfMostRecent.set_head_to(node)

    def _replace_value(self, key, value):
        self.cache[key].value = value

    def __str__(self):
        keys = []
        current = self.listOfMostRecent.head
        while current:
            keys.append(current.key)
            current = current.next
        return f"LRUCache({keys})"


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def set_head_to(self, node):
        if self.head == node:
            return
        if self.head is None:
            self.head = node
            self.tail = node
            return
        if self.tail == node:
            self.remove_tail()
        node.remove_bindings()  # This should come before modifying head's prev
        self.head.prev = node
        node.next = self.head
        self.head = node

    def remove_tail(self):
        if self.tail is None:
            return
        if self.tail == self.head:
            self.head = None
            self.tail = None
            return
        self.tail = self.tail.prev
        self.tail.next = None


class DoublyLinkedListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def remove_bindings(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
        self.prev = None
        self.next = None


# Initialize LRUCache with maxSize = 3
cache = LRUCache(3)

# Insert key-value pairs
cache.insertKeyValuePair("a", 1)
cache.insertKeyValuePair("b", 2)
cache.insertKeyValuePair("c", 3)

# Check the most recent key (should be "c")
print("Most recent key:", cache.getMostRecentKey())  # Output: "c"

# Get value for key "a" (updates its recent usage)
print("Value for 'a':", cache.getValueFromKey("a"))  # Output: 1

# Now the most recent key should be "a" (since we accessed it)
print("Most recent key after accessing 'a':", cache.getMostRecentKey())  # Output: "a"

# Insert a new key-value pair (evicts least recent key "b" since maxSize=3)
cache.insertKeyValuePair("d", 4)

# Try to get evicted key "b" (should return None)
print("Value for 'b' (evicted):", cache.getValueFromKey("b"))  # Output: None

# Current state of the cache: {"a": 1, "c": 3, "d": 4}
print("Most recent key after inserting 'd':", cache.getMostRecentKey())  # Output: "d"

# Output:

"""
Most recent key: c
Value for 'a': 1
Most recent key after accessing 'a': a
Value for 'b' (evicted): None
Most recent key after inserting 'd': d
"""
