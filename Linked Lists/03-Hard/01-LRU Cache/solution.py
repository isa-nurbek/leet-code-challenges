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
        # Initialize the cache as a dictionary to store key-node pairs
        self.cache = {}
        # Ensure maxSize is at least 1 (minimum cache size)
        self.maxSize = max(1, maxSize)
        # Doubly linked list to maintain usage order (most recent at head)
        self.listOfMostRecent = DoublyLinkedList()

    def insertKeyValuePair(self, key, value):
        # If key already exists in cache
        if key in self.cache:
            # Just replace the value and update usage
            self._replace_value(key, value)
        else:
            # If cache is full, evict least recently used item
            if len(self.cache) == self.maxSize:
                self._evict_least_recent()
            # Create new node and add to cache
            self.cache[key] = DoublyLinkedListNode(key, value)
        # Update usage (move to front of LRU list)
        self._update_most_recent(self.cache[key])

    def getValueFromKey(self, key):
        # Return None if key doesn't exist
        if key not in self.cache:
            return None
        # Update usage since this key was recently accessed
        self._update_most_recent(self.cache[key])
        return self.cache[key].value

    def getMostRecentKey(self):
        # Return the key of the most recently used item (head of list)
        return self.listOfMostRecent.head.key if self.listOfMostRecent.head else None

    def _evict_least_recent(self):
        # Remove the tail node (least recently used) from both list and cache
        key_to_remove = self.listOfMostRecent.tail.key
        self.listOfMostRecent.remove_tail()
        del self.cache[key_to_remove]

    def _update_most_recent(self, node):
        # Move the accessed node to the head of the list (most recent position)
        self.listOfMostRecent.set_head_to(node)

    def _replace_value(self, key, value):
        # Simply update the value of an existing key
        self.cache[key].value = value

    def __str__(self):
        # Helper method to print cache contents in order (most to least recent)
        keys = []
        current = self.listOfMostRecent.head
        while current:
            keys.append(current.key)
            current = current.next
        return f"LRUCache({keys})"


class DoublyLinkedList:
    def __init__(self):
        # Initialize empty doubly linked list
        self.head = None  # Most recently used
        self.tail = None  # Least recently used

    def set_head_to(self, node):
        # If node is already head, no action needed
        if self.head == node:
            return
        # If list is empty, set both head and tail to node
        if self.head is None:
            self.head = node
            self.tail = node
            return
        # If node is currently tail, remove it from tail position first
        if self.tail == node:
            self.remove_tail()
        # Remove node from its current position in list (if any)
        node.remove_bindings()
        # Insert node at head
        self.head.prev = node
        node.next = self.head
        self.head = node

    def remove_tail(self):
        # If list is empty, do nothing
        if self.tail is None:
            return
        # Special case: only one node in list
        if self.tail == self.head:
            self.head = None
            self.tail = None
            return
        # Move tail pointer to previous node and clear next pointer
        self.tail = self.tail.prev
        self.tail.next = None


class DoublyLinkedListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None  # Pointer to previous node
        self.next = None  # Pointer to next node

    def remove_bindings(self):
        # Remove this node from its current position by updating neighbors' pointers
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
        # Clear this node's pointers
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

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### Time Complexity Analysis

1. **`insertKeyValuePair(key, value)`**:
   - **Checking if key exists in cache**: O(1) average time (hash table lookup).
   - **Replacing value (if key exists)**: O(1) (updating the value in the node).
   - **Evicting least recent (if cache is full)**:
     - Removing the tail from the doubly linked list: O(1).
     - Deleting the key from the hash table: O(1).
   - **Inserting new key-value pair**:
     - Creating a new node: O(1).
     - Adding to the hash table: O(1) average time.
   - **Updating most recent**:
     - Moving the node to the head of the doubly linked list: O(1) (since `set_head_to` and `remove_bindings` are O(1)).
   - **Total**: O(1) average time per operation.

2. **`getValueFromKey(key)`**:
   - **Checking if key exists in cache**: O(1) average time.
   - **Updating most recent**:
     - Moving the node to the head of the doubly linked list: O(1).
   - **Total**: O(1) average time per operation.

3. **`getMostRecentKey()`**:
   - Accessing the head of the doubly linked list: O(1).
   - **Total**: O(1).

4. **Helper Methods**:
   - `_evict_least_recent()`: O(1) (removing tail and hash table deletion).
   - `_update_most_recent(node)`: O(1) (moving node to head).
   - `_replace_value(key, value)`: O(1) (updating node value).

### Space Complexity Analysis
- **Hash Table (`self.cache`)**: O(n) where n is the number of key-value pairs (up to `maxSize`).
- **Doubly Linked List (`self.listOfMostRecent`)**: O(n) (stores the same nodes as the hash table, just in order).
- **Nodes in Doubly Linked List**: Each node stores `key`, `value`, `prev`, and `next`, but this is still O(1) per node.
- **Total Space**: O(n) where n is the maximum capacity (`maxSize`) of the cache.

### Summary
- **Time Complexity**: All operations (insert, get, update) are O(1) average time.
- **Space Complexity**: O(n) where n is the maximum size of the cache (`maxSize`).

This implementation efficiently maintains the LRU property using a hash table for O(1) access and a doubly linked list
for O(1) order updates.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
This implementation is a **Least Recently Used (LRU) Cache** using a combination of:

1. **A hash map (`dict`)** for fast lookups (`O(1)`).
2. **A doubly linked list** to keep track of the usage order (`O(1)` insertions/deletions from head/tail).

---

## 🔁 What is an LRU Cache?

An LRU cache evicts the **least recently used** item when it reaches its maximum size.

* Recently accessed or inserted items are moved to the **front** (head) of the list.
* The **least recently used** item sits at the **back** (tail), and will be evicted when the cache is full.

---

## 🔩 Components of the Code

### ✅ Class: `LRUCache`

```
class LRUCache:
```

This class manages the cache logic with methods to:

* Insert or update values (`insertKeyValuePair`)
* Retrieve values (`getValueFromKey`)
* Track the most recently used key (`getMostRecentKey`)

### 🔧 `__init__`

```
def __init__(self, maxSize):
    self.cache = {}  # Dictionary: key → node
    self.maxSize = max(1, maxSize)  # Avoid 0 size cache
    self.listOfMostRecent = DoublyLinkedList()  # Order tracker
```

* `self.cache` stores key → node mappings.
* `self.listOfMostRecent` keeps track of usage order.

---

### 🚀 `insertKeyValuePair`

```
def insertKeyValuePair(self, key, value):
```

* If the key exists: updates value via `_replace_value()`.
* If key is new and cache is full: evicts LRU item via `_evict_least_recent()`.
* Adds key-node mapping and moves node to head (most recent).

---

### 🔍 `getValueFromKey`

```
def getValueFromKey(self, key):
```

* If key doesn't exist → returns `None`.
* If found → moves node to head (mark as recently used) and returns value.

---

### 🔝 `getMostRecentKey`

```
def getMostRecentKey(self):
```

Returns the key of the **head** node (most recently used).

---

### 💣 `_evict_least_recent`

```
def _evict_least_recent(self):
    key_to_remove = self.listOfMostRecent.tail.key
    self.listOfMostRecent.remove_tail()
    del self.cache[key_to_remove]
```

Removes the tail node (least recently used) and deletes its entry in the dictionary.

---

### 🔁 `_update_most_recent`

```
def _update_most_recent(self, node):
    self.listOfMostRecent.set_head_to(node)
```

Moves a node to the head of the linked list.

---

### ✏️ `_replace_value`

```
def _replace_value(self, key, value):
    self.cache[key].value = value
```

Updates the value in the existing node.

---

## 🔗 Class: `DoublyLinkedList`

This class manages the order of keys.

### `set_head_to`

```
def set_head_to(self, node):
```

* If the node is already head → do nothing.
* If list is empty → make node both head and tail.
* If node is tail → remove it from tail.
* Remove node from current position (if exists), then insert at head.

### `remove_tail`

```
def remove_tail(self):
```

Removes the tail node and updates pointers.

---

## 🔘 Class: `DoublyLinkedListNode`

Represents a node with:

```
key, value, prev, next
```

Used in both dictionary and linked list.

### `remove_bindings`

```
def remove_bindings(self):
```

Disconnects the node from neighbors (helps in re-insertion elsewhere).

---

## 🔍 Example Execution Walkthrough

```
cache = LRUCache(3)
```

**Insertions:**

```
cache.insertKeyValuePair("a", 1)  # a
cache.insertKeyValuePair("b", 2)  # b → a
cache.insertKeyValuePair("c", 3)  # c → b → a
```

```
print(cache.getMostRecentKey())  # c
```

Accessing `"a"`:

```
cache.getValueFromKey("a")  # Moves a to front
# a → c → b
```

Insert `"d"` (capacity full):

```
cache.insertKeyValuePair("d", 4)
# Evicts least recent (b), inserts d → a → c
```

Check evicted key:

```
print(cache.getValueFromKey("b"))  # None
```

---

## 🧠 Time and Space Complexity

| Operation            | Time |
| -------------------- | ---- |
| `insertKeyValuePair` | O(1) |
| `getValueFromKey`    | O(1) |
| `getMostRecentKey`   | O(1) |
| `Eviction`           | O(1) |

Space: O(N) for storing up to `maxSize` nodes.

---

## ✅ Summary

* Fast O(1) operations via `dict` + `doubly linked list`.
* Maintains correct usage order.
* Evicts least recently used when full.
* Nodes are reused and re-ordered efficiently.

---

Here's an **ASCII visualization** of how the **doubly linked list** (usage order) and the **cache dictionary** evolve as we
perform operations.

---

### ✅ Start: Initialize LRUCache(3)

```
cache = LRUCache(3)
```

Cache: `{}`
List: *(empty)*

---

### ➕ Insert ("a", 1)

```
cache.insertKeyValuePair("a", 1)
```

**Cache:**

```
{"a": Node("a", 1)}
```

**List (most recent on the left):**

```
[a]
```

---

### ➕ Insert ("b", 2)

```
cache.insertKeyValuePair("b", 2)
```

**Cache:**

```
{"a": Node("a", 1), "b": Node("b", 2)}
```

**List:**

```
[b] <-> [a]
```

---

### ➕ Insert ("c", 3)

```
cache.insertKeyValuePair("c", 3)
```

**Cache:**

```
{"a": Node("a", 1), "b": Node("b", 2), "c": Node("c", 3)}
```

**List:**

```
[c] <-> [b] <-> [a]
```

---

### 🔍 Access "a"

```
cache.getValueFromKey("a")
```

Move "a" to front.

**List:**

```
[a] <-> [c] <-> [b]
```

---

### ➕ Insert ("d", 4)

```
cache.insertKeyValuePair("d", 4)
```

* Cache full → evict least recent = "b"
* Insert "d" at front

**Cache:**

```
{"a": Node("a", 1), "c": Node("c", 3), "d": Node("d", 4)}
```

**List:**

```
[d] <-> [a] <-> [c]
```

---

### 🔍 Access "b"

```
cache.getValueFromKey("b")  # None (evicted)
```

---

### 🔚 Final state

**Cache:**

```
{"a": ..., "c": ..., "d": ...}
```

**List:**

```
[d] <-> [a] <-> [c]
```

---

### 🧭 Legend

* `[key]` is a node (value not shown for simplicity)
* Arrows `<->` show doubly linked connections
* Left = Most Recent
* Right = Least Recent

---

Here's a **step-by-step side-by-side table** of the cache and the doubly linked list (usage order) as operations are performed:

### 🗂️ Legend

| Term           | Meaning                                     |
| -------------- | ------------------------------------------- |
| `[key]`        | Node with `key` (value omitted for clarity) |
| Leftmost node  | Most recently used                          |
| Rightmost node | Least recently used                         |
| `<->`          | Doubly linked list connections              |

---

## 📋 Step-by-Step Table

| Step | Operation           | Cache Contents                                        | Doubly Linked List (MRU → LRU) |
| ---- | ------------------- | ----------------------------------------------------- | ------------------------------ |
| 0    | Init `LRUCache(3)`  | `{}`                                                  | *(empty)*                      |
| 1    | `insert("a", 1)`    | `{"a": [a]}`                                          | `[a]`                          |
| 2    | `insert("b", 2)`    | `{"a": [a], "b": [b]}`                                | `[b] <-> [a]`                  |
| 3    | `insert("c", 3)`    | `{"a": [a], "b": [b], "c": [c]}`                      | `[c] <-> [b] <-> [a]`          |
| 4    | `get("a")`          | `{"a": [a], "b": [b], "c": [c]}`                      | `[a] <-> [c] <-> [b]`          |
| 5    | `insert("d", 4)`    | `{"a": [a], "c": [c], "d": [d]}` <br> (*"b" evicted*) | `[d] <-> [a] <-> [c]`          |
| 6    | `get("b")` → `None` | `{"a": [a], "c": [c], "d": [d]}`                      | `[d] <-> [a] <-> [c]`          |

---

### ✅ Final State

| Component | State                            |
| --------- | -------------------------------- |
| **Cache** | `{"a": [a], "c": [c], "d": [d]}` |
| **List**  | `[d] <-> [a] <-> [c]`            |

"""
