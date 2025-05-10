# Problem Description:

"""
                                            Middle Node

You're given a Linked List with at least one node. Write a function that returns the middle node of the Linked List. If there are
two middle nodes (i.e. an even length list), your function should return the second of these nodes.

Each `LinkedList` node has an integer `value` as well as a `next` node pointing to the next node in the list or to `None` if it's
the tail of the list.

## Sample Input:
```
linked_list = 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> None
```

## Sample Output:
```
5 -> 6 -> 7 -> 8 -> 9 -> None
```

## Optimal Time & Space Complexity:
```
O(n) time | O(1) space - where `n` is the number of nodes in the linked list.
```

"""

# =========================================================================================================================== #

# Solution:


# Linked List Class
class LinkedList:
    def __init__(self, value):
        self.value = value  # Store the value of this node
        self.next = None  # Pointer to the next node (initially None)


# Helper function to convert dictionary to LinkedList
def build_linked_list(data):
    """Builds a linked list from a dictionary representation.

    Args:
        data: Dictionary containing 'head' (id of head node) and 'nodes' (list of node dictionaries)

    Returns:
        The head node of the constructed linked list
    """
    if not data:
        return None

    # Create all nodes first and store them in a dictionary by their IDs
    nodes = {}
    for node_data in data["nodes"]:
        node = LinkedList(node_data["value"])
        nodes[node_data["id"]] = node

    # Connect the nodes by setting the next pointers based on the 'next' IDs
    for node_data in data["nodes"]:
        if node_data["next"] is not None:
            nodes[node_data["id"]].next = nodes[node_data["next"]]

    # Return the head node (the starting point of the linked list)
    return nodes[data["head"]]


# Function to find the middle node
# O(n) time | O(1) space
def middle_node(linked_list):
    # Initialize two pointers, both starting at the head of the linked list
    slow = linked_list
    fast = linked_list

    # Traverse the list with 'fast' moving twice as fast as 'slow'
    # When 'fast' reaches the end, 'slow' will be at the middle
    while fast is not None and fast.next is not None:
        slow = slow.next  # Move slow pointer one step forward
        fast = fast.next.next  # Move fast pointer two steps forward

    # Return the middle node (slow pointer's position)
    return slow


# Function to print the linked list (for verification)
def print_linked_list(linked_list):
    """Prints the linked list in a readable format.

    Args:
        linked_list: The head node of the linked list to print
    """
    current = linked_list

    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")


# Input data
linked_list_dict = {
    "head": "1",
    "nodes": [
        {"id": "1", "next": "2", "value": 1},
        {"id": "2", "next": "3", "value": 2},
        {"id": "3", "next": "4", "value": 3},
        {"id": "4", "next": "5", "value": 4},
        {"id": "5", "next": "6", "value": 5},
        {"id": "6", "next": "7", "value": 6},
        {"id": "7", "next": "8", "value": 7},
        {"id": "8", "next": "9", "value": 8},
        {"id": "9", "next": None, "value": 9},
    ],
}

# Test Case:

# Build the linked list from dictionary
linked_list = build_linked_list(linked_list_dict)

# Remove duplicates
result = middle_node(linked_list)

print_linked_list(result)
# Output: 5 -> 6 -> 7 -> 8 -> 9 -> None

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

Let's analyze the time and space complexity of the `middle_node` function.

### Time Complexity:

The function uses the "tortoise and hare" approach to find the middle node of a linked list.
Here's how it works:

1. `slow` pointer moves one node at a time.
2. `fast` pointer moves two nodes at a time.
3. When `fast` reaches the end of the list (or goes beyond it), `slow` will be at the middle node.

- In the worst case, `fast` will traverse the entire list (or nearly the entire list), which takes `O(n)` time, where `n`
is the number of nodes in the linked list.
- Therefore, the **time complexity is `O(n)`**.

### Space Complexity:

The function only uses two pointers (`slow` and `fast`) and does not use any additional data structures or recursive calls
that grow with the input size.
- Thus, the **space complexity is `O(1)` (constant space)**.

### Summary:
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
Let's break down the code step by step and explain **how it works**, what **each part does**, and why the **final output is correct**.

---

## ✅ 1. **`LinkedList` Class**

```
class LinkedList:
    def __init__(self, value):
        self.value = value  # Store the value of this node
        self.next = None    # Pointer to the next node (initially None)
```

### ✔ Purpose:

This defines a **single node** in a **singly linked list**. Each node stores:

* A `value` (the actual data, e.g., 1, 2, 3…)
* A `next` pointer that will reference the **next node** in the list (or `None` if it's the last node).

---

## ✅ 2. **`build_linked_list(data)` Function**

```
def build_linked_list(data):
    ...
```

### ✔ Purpose:

This function **constructs a linked list** from a dictionary. The dictionary includes:

* `"head"`: the ID of the head node.
* `"nodes"`: a list of node definitions, each having:

  * `id`: unique string ID of the node
  * `value`: the integer value of the node
  * `next`: the ID of the next node or `None` if it's the last

### ✔ Key Steps:

```
nodes = {}
for node_data in data["nodes"]:
    node = LinkedList(node_data["value"])
    nodes[node_data["id"]] = node
```

* It creates all nodes in memory **without connecting** them yet and stores them in a dictionary by their IDs.

```
for node_data in data["nodes"]:
    if node_data["next"] is not None:
        nodes[node_data["id"]].next = nodes[node_data["next"]]
```

* It then loops through again to **connect each node’s `.next` pointer** to the appropriate node (based on its ID).

```
return nodes[data["head"]]
```

* Finally, it returns the head of the list (using the `"head"` ID from the dictionary).

---

## ✅ 3. **`middle_node(linked_list)` Function**

```
def middle_node(linked_list):
    slow = linked_list
    fast = linked_list
    ...
    return slow
```

### ✔ Purpose:

Finds the **middle node** of a singly linked list in **O(n) time** and **O(1) space**.

### ✔ How It Works (Two Pointer Technique):

* You have two pointers: `slow` and `fast`.
* `slow` moves **one step** at a time.
* `fast` moves **two steps** at a time.

```
while fast is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next
```

* When `fast` reaches the **end of the list**, `slow` will be in the **middle**.

### 📌 Why does this work?

* Because `fast` moves twice as fast, by the time it gets to the end, `slow` will have covered **half the distance**.

---

## ✅ 4. **`print_linked_list(linked_list)` Function**

```
def print_linked_list(linked_list):
    current = linked_list
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")
```

### ✔ Purpose:

Prints all the nodes starting from the given node in a readable format.

---

## ✅ 5. **Test Input**

```
linked_list_dict = {
    "head": "1",
    "nodes": [
        {"id": "1", "next": "2", "value": 1},
        {"id": "2", "next": "3", "value": 2},
        {"id": "3", "next": "4", "value": 3},
        {"id": "4", "next": "5", "value": 4},
        {"id": "5", "next": "6", "value": 5},
        {"id": "6", "next": "7", "value": 6},
        {"id": "7", "next": "8", "value": 7},
        {"id": "8", "next": "9", "value": 8},
        {"id": "9", "next": None, "value": 9},
    ],
}
```

### ✔ What It Represents:

A linked list like this:

```
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> None
```

---

## ✅ 6. **Execution Flow**

```
linked_list = build_linked_list(linked_list_dict)
result = middle_node(linked_list)
print_linked_list(result)
```

### ✔ Step-by-step:

1. **`build_linked_list()`** converts the dictionary into a proper linked list.
2. **`middle_node()`** finds the node starting from the middle (`value = 5`).
3. **`print_linked_list()`** prints from that node to the end.

---

## ✅ Final Output:

```
5 -> 6 -> 7 -> 8 -> 9 -> None
```

This is correct because the middle of a 9-element list is the 5th node (1-based), which has the value `5`.

---

To return **two middle nodes** in case of an **even-length** linked list (e.g., 8 nodes → return nodes 4 and 5), we’ll need
to slightly modify the `middle_node()` function.

---

## ✅ Goal:

* For **odd number** of nodes → return the **single middle node**.
* For **even number** of nodes → return a **tuple of two middle nodes**.

---

## 🔁 Modified `middle_node()` Function:

```
def middle_node(linked_list):
    # Initialize pointers
    slow = linked_list
    fast = linked_list
    prev = None  # To keep track of node before 'slow'

    # Traverse the list
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    # If fast is None, the list has even length → return two middle nodes
    if fast is None:
        return (prev, slow)
    else:
        return (slow,)
```

---

## 🧪 Example Output:

Let’s say your list is:

```
1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → None
```

That’s 8 nodes (even), so this will return:

```
(4, 5)
```

If the list is:

```
1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 → None
```

That’s 9 nodes (odd), so it returns:

```
(5,)
```

---

## 🖨️ Updated Print Function (Optional for Debugging):

To print one or two nodes:

```
def print_middle_nodes(nodes):
    if len(nodes) == 1:
        print(f"Middle node: {nodes[0].value}")
    else:
        print(f"Middle nodes: {nodes[0].value}, {nodes[1].value}")
```

---

## ✅ Example Usage:

```
middle_nodes = middle_node(linked_list)
print_middle_nodes(middle_nodes)
```

"""
