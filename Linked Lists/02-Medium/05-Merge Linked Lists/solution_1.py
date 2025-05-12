# Problem Description:

"""
                                            Merge Linked Lists

Write a function that takes in the heads of two Singly Linked Lists that are in `sorted order`, respectively. The function should
merge the lists in place (i.e., it shouldn't create a brand new list) and return the head of the merged list; the merged list
should be in `sorted order`.

Each `LinkedList` node has an integer `value` as well as a `next` node pointing to the next node in the list or to `None` if it's
the tail of the list.

You can assume that the input linked lists will always have at least one node; in other words, the heads will never be `None`.


## Sample Input:
```
head_one = 2 -> 6 -> 7 -> 8 -> None              // the head node with value 2
head_two = 1 -> 3 -> 4 -> 5 -> 9 -> 10 -> None   // the head node with value 1
```

## Sample Output:
```
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> None  // the new head node with value 1
```

## Optimal Time & Space Complexity:
```
O(n + m) time | O(1) space - where `n` is the number of nodes in the first Linked List and
`m` is the number of nodes in the second Linked List.

```

"""

# =========================================================================================================================== #

# Solution:


class LinkedList:
    """Node class for a singly linked list."""

    def __init__(self, value):
        self.value = value  # Value stored in the node
        self.next = None  # Pointer to the next node (initially None)


def build_linked_list(data):
    """Builds a linked list from a dictionary representation.

    Args:
        data: Dictionary with 'head' (id of head node) and 'nodes' (list of node dicts).

    Returns:
        The head node of the constructed linked list, or None if data is empty.
    """
    if not data:
        return None

    # Create all nodes and store them in a dictionary by ID
    nodes = {}
    for node_data in data["nodes"]:
        node = LinkedList(node_data["value"])
        nodes[node_data["id"]] = node

    # Connect nodes using 'next' pointers
    for node_data in data["nodes"]:
        if node_data["next"] is not None:
            nodes[node_data["id"]].next = nodes[node_data["next"]]

    return nodes[data["head"]]  # Return the head node


def merge_linked_lists(head_one, head_two):
    """Merges two sorted linked lists into a single sorted list in-place.

    Args:
        head_one: Head node of the first sorted linked list.
        head_two: Head node of the second sorted linked list.

    Returns:
        The head node of the merged linked list.
    """
    # Edge case: If one list is empty, return the other
    if head_one is None:
        return head_two
    if head_two is None:
        return head_one

    # Initialize pointers
    p1 = head_one  # Pointer for the first list
    p2 = head_two  # Pointer for the second list
    merged_head = head_one if head_one.value < head_two.value else head_two

    # Traverse both lists and merge them
    prev = None  # Tracks the last node in the merged list
    while p1 is not None and p2 is not None:
        if p1.value < p2.value:
            if prev is not None:
                prev.next = p1
            prev = p1
            p1 = p1.next
        else:
            if prev is not None:
                prev.next = p2
            prev = p2
            p2 = p2.next

    # Attach remaining nodes (if any)
    if p1 is not None:
        prev.next = p1
    else:
        prev.next = p2

    return merged_head


def print_linked_list(head):
    """Prints the linked list in a readable format.

    Args:
        head: The head node of the linked list to print.
    """
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")


# Test Case 1: Two non-empty sorted lists
linked_list_dict_one = {
    "head": "2",
    "nodes": [
        {"id": "2", "next": "6", "value": 2},
        {"id": "6", "next": "7", "value": 6},
        {"id": "7", "next": "8", "value": 7},
        {"id": "8", "next": None, "value": 8},
    ],
}

linked_list_dict_two = {
    "head": "1",
    "nodes": [
        {"id": "1", "next": "3", "value": 1},
        {"id": "3", "next": "4", "value": 3},
        {"id": "4", "next": "5", "value": 4},
        {"id": "5", "next": "9", "value": 5},
        {"id": "9", "next": "10", "value": 9},
        {"id": "10", "next": None, "value": 10},
    ],
}

# Build and merge the lists
list_one = build_linked_list(linked_list_dict_one)
list_two = build_linked_list(linked_list_dict_two)
merged_list = merge_linked_lists(list_one, list_two)

print("Merged List:")
print_linked_list(merged_list)
# Merged List: 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 → 10 → None

# Test Case 2: One list is empty
empty_list = None
merged_with_empty = merge_linked_lists(empty_list, list_two)

print("\nMerged with Empty List:")
print_linked_list(merged_with_empty)
# Merged with Empty List: 1 → 3 → 4 → 5 → 9 → 10 → None

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

Let's analyze the time and space complexity of the `mergeLinkedLists` function.

### Time Complexity:

The function iterates through both linked lists (`head_one` and `head_two`) exactly once. At each step, it compares the values
of the current nodes and appends the smaller one to the merged list. 

- If `head_one` has `n` nodes and `head_two` has `m` nodes, the while loop runs for at most `n + m` iterations (since in each
iteration, either `p1` or `p2` advances).
- The remaining nodes (if any) are attached in constant time (`O(1)`).

Thus, the **time complexity is `O(n + m)`**, where `n` and `m` are the lengths of the two input linked lists.

### Space Complexity:

The function uses a constant amount of extra space:
- Pointers `p1`, `p2`, `prev`, and `merged_head` are used, but no additional data structures are created that scale with the
input size.
- The merging is done in-place by rearranging the `next` pointers of the existing nodes.

Thus, the **space complexity is `O(1)` (constant space)**.

### Summary:
- **Time Complexity:** `O(n + m)`
- **Space Complexity:** `O(1)` (in-place merge)

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
This code is a full implementation for **merging two sorted singly linked lists** using Python. Let’s break it down and explain
how each part works step-by-step:

---

### **1. Class Definition**

```
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
```

This defines a node in a **singly linked list**:

* `value`: Stores the value/data in the node.
* `next`: Pointer to the **next node** in the list. Initially set to `None`.

---

### **2. `build_linked_list(data)`**

This function builds a linked list from a **dictionary format** (like from JSON). It returns the head of the constructed linked list.

```
def build_linked_list(data):
    if not data:
        return None
```

* If the input `data` is `None` or empty, return `None`.

```
nodes = {}
for node_data in data["nodes"]:
    node = LinkedList(node_data["value"])
    nodes[node_data["id"]] = node
```

* Creates a mapping from node `id` to the `LinkedList` object.
* Example: if a node has id `"2"` and value `2`, then `nodes["2"] = LinkedList(2)`.

```
for node_data in data["nodes"]:
    if node_data["next"] is not None:
        nodes[node_data["id"]].next = nodes[node_data["next"]]
```

* This loop links each node to its next node using the ID-based mapping.

```
return nodes[data["head"]]
```

* Finally, return the node corresponding to the head ID as the head of the list.

---

### **3. `merge_linked_lists(head_one, head_two)`**

This merges two **sorted singly linked lists** into one, **in-place**, without creating new nodes.

```
if head_one is None:
    return head_two
if head_two is None:
    return head_one
```

* If either list is empty, return the other one.

```
p1 = head_one
p2 = head_two
merged_head = head_one if head_one.value < head_two.value else head_two
```

* Use `p1` and `p2` as pointers to traverse the two lists.
* `merged_head` will point to the **smaller of the two starting nodes**.

```
prev = None
while p1 is not None and p2 is not None:
    if p1.value < p2.value:
        if prev is not None:
            prev.next = p1
        prev = p1
        p1 = p1.next
    else:
        if prev is not None:
            prev.next = p2
        prev = p2
        p2 = p2.next
```

* In each iteration:

  * Compare `p1.value` and `p2.value`.
  * Attach the smaller one to the `prev.next`.
  * Move the pointer (`p1` or `p2`) ahead.
  * `prev` always points to the **last node in the merged list**.

```
if p1 is not None:
    prev.next = p1
else:
    prev.next = p2
```

* After the loop, attach any **remaining nodes** in `p1` or `p2`.

```
return merged_head
```

* Return the merged list’s head node.

---

### **4. `print_linked_list(head)`**

```
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")
```

* Walks through the list from the head and prints each node's value followed by `->`.
* Ends with `"None"` to indicate the end of the list.

---

### **5. Test Case 1: Two Non-Empty Sorted Lists**

```
linked_list_dict_one = { ... }
linked_list_dict_two = { ... }
```

These are dictionary representations of two sorted linked lists:

* `linked_list_dict_one` has nodes: 2 → 6 → 7 → 8
* `linked_list_dict_two` has nodes: 1 → 3 → 4 → 5 → 9 → 10

They are built and then merged using:

```
list_one = build_linked_list(linked_list_dict_one)
list_two = build_linked_list(linked_list_dict_two)
merged_list = merge_linked_lists(list_one, list_two)
```

The output printed by `print_linked_list(merged_list)` will be:

```
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> None
```

---

### **6. Test Case 2: One List is Empty**

```
empty_list = None
merged_with_empty = merge_linked_lists(empty_list, list_two)
print_linked_list(merged_with_empty)
```

* Merges `None` and a valid list (`list_two`).
* Output: `1 -> 3 -> 4 -> 5 -> 9 -> 10 -> None`

---

### ✅ Summary

* **build_linked_list**: Converts a JSON-like structure into a linked list.
* **merge_linked_lists**: Merges two sorted linked lists in-place.
* **print_linked_list**: Prints a linked list in readable format.

---

Here's a step-by-step **ASCII visualization** of how the `merge_linked_lists` function works for the first test case:

### **Initial Linked Lists**

#### List One (`list_one`)

```
2 -> 6 -> 7 -> 8 -> None
```

#### List Two (`list_two`)

```
1 -> 3 -> 4 -> 5 -> 9 -> 10 -> None
```

---

### **Step-by-Step Merge Process**

We'll walk through the comparison and merging by tracking `p1`, `p2`, and `prev`.

---

#### **Step 1**:

Compare `p1=2`, `p2=1`
`1 < 2`, so `merged_head = 1`, and `prev = 1`, advance `p2`.

```
Merged so far: 1 ->
Remaining:
  p1: 2 -> 6 -> 7 -> 8
  p2: 3 -> 4 -> 5 -> 9 -> 10
```

---

#### **Step 2**:

Compare `p1=2`, `p2=3`
`2 < 3`, so `prev.next = 2`, `prev = 2`, advance `p1`.

```
Merged so far: 1 -> 2 ->
Remaining:
  p1: 6 -> 7 -> 8
  p2: 3 -> 4 -> 5 -> 9 -> 10
```

---

#### **Step 3**:

Compare `p1=6`, `p2=3`
`3 < 6`, so `prev.next = 3`, `prev = 3`, advance `p2`.

```
Merged so far: 1 -> 2 -> 3 ->
Remaining:
  p1: 6 -> 7 -> 8
  p2: 4 -> 5 -> 9 -> 10
```

---

#### **Step 4**:

Compare `p1=6`, `p2=4`
`4 < 6`, so `prev.next = 4`, `prev = 4`, advance `p2`.

```
Merged so far: 1 -> 2 -> 3 -> 4 ->
Remaining:
  p1: 6 -> 7 -> 8
  p2: 5 -> 9 -> 10
```

---

#### **Step 5**:

Compare `p1=6`, `p2=5`
`5 < 6`, so `prev.next = 5`, `prev = 5`, advance `p2`.

```
Merged so far: 1 -> 2 -> 3 -> 4 -> 5 ->
Remaining:
  p1: 6 -> 7 -> 8
  p2: 9 -> 10
```

---

#### **Step 6**:

Compare `p1=6`, `p2=9`
`6 < 9`, so `prev.next = 6`, `prev = 6`, advance `p1`.

```
Merged so far: 1 -> 2 -> 3 -> 4 -> 5 -> 6 ->
Remaining:
  p1: 7 -> 8
  p2: 9 -> 10
```

---

#### **Step 7**:

Compare `p1=7`, `p2=9`
`7 < 9`, so `prev.next = 7`, `prev = 7`, advance `p1`.

```
Merged so far: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 ->
Remaining:
  p1: 8
  p2: 9 -> 10
```

---

#### **Step 8**:

Compare `p1=8`, `p2=9`
`8 < 9`, so `prev.next = 8`, `prev = 8`, advance `p1`.

```
Merged so far: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 ->
Remaining:
  p1: None
  p2: 9 -> 10
```

---

#### **Step 9**:

`p1` is now `None`, so attach remaining `p2` list to merged list.

```
Final Merged: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> None
```

"""
