# Problem Description:

"""
                                            Zip Linked List

You're given the head of a Singly Linked List of arbitrary length `k`. Write a function that zips the Linked List in place (i.e.,
doesn't create a brand new list) and returns its head.

A Linked List is zipped if its nodes are in the following order, where `k` is the length of the Linked List:

```
1st node -> kth node -> 2nd node -> (k - 1)th node -> 3rd node -> (k - 2)th node -> ...
```

Each `LinkedList` node has an integer `value` as well as a `next` node pointing to the next node in the list or to `None` if it's
the tail of the list.

You can assume that the input Linked List will always have at least one node; in other words, the head will never be `None`.


## Sample Input:
```
linked_list = 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None

// The head node with value 1
```

## Sample Output:
```
1 -> 6 -> 2 -> 5 -> 3 -> 4 -> None

// The head node with value 1
```

## Optimal Time & Space Complexity:
```
O(n) time | O(1) space - where `n` is the length of the input Linked List.
```

"""

# =========================================================================================================================== #

# Solution:


class LinkedList:
    def __init__(self, value):
        self.value = value  # Store the value of this node
        self.next = None  # Pointer to the next node (initially None)


def build_linked_list(data):
    """Builds a linked list from dictionary representation.

    Args:
        data: Dictionary containing 'head' id and 'nodes' list with each node's
              id, value, and next node id.

    Returns:
        The head node of the constructed linked list.
    """
    if not data:
        return None

    # First create all nodes and store them in a dictionary by id
    nodes = {}
    for node_data in data["nodes"]:
        node = LinkedList(node_data["value"])
        nodes[node_data["id"]] = node

    # Then connect the nodes by setting next pointers
    for node_data in data["nodes"]:
        if node_data["next"] is not None:
            nodes[node_data["id"]].next = nodes[node_data["next"]]

    return nodes[data["head"]]


# O(n) time | O(1) space
def zip_linkedList(linked_list):
    """Zips a linked list in place by interleaving first half with reversed second half.

    Example: 1->2->3->4->5->6 becomes 1->6->2->5->3->4

    Args:
        linked_list: Head node of the linked list to zip.

    Returns:
        The head of the zipped linked list.
    """
    # Base case: list is too short to zip
    if linked_list.next is None or linked_list.next.next is None:
        return linked_list

    # Split the list into two halves
    first_half_head = linked_list
    second_half_head = split_linkedList(linked_list)

    # Reverse the second half
    reversed_second_half_head = reverse_linkedList(second_half_head)

    # Interweave the two halves
    return interweave_linkedLists(first_half_head, reversed_second_half_head)


def split_linkedList(linked_list):
    """Splits a linked list into two halves using slow/fast pointer technique.

    Args:
        linked_list: Head node of the linked list to split.

    Returns:
        The head node of the second half.
    """
    slow_iterator = linked_list
    fast_iterator = linked_list

    # Fast pointer moves twice as fast as slow pointer
    while fast_iterator is not None and fast_iterator.next is not None:
        slow_iterator = slow_iterator.next
        fast_iterator = fast_iterator.next.next

    # When fast reaches end, slow is at midpoint
    second_half_head = slow_iterator.next
    slow_iterator.next = None  # Terminate first half

    return second_half_head


def interweave_linkedLists(linked_list_1, linked_list_2):
    """Interweaves two linked lists by alternating nodes from each list.

    Args:
        linked_list_1: Head node of first linked list.
        linked_list_2: Head node of second linked list.

    Returns:
        The head node of the interwoven list (linked_list_1 will be first node).
    """
    linked_list_1_iterator = linked_list_1
    linked_list_2_iterator = linked_list_2

    while linked_list_1_iterator is not None and linked_list_2_iterator is not None:
        # Save next pointers before we overwrite them
        linked_list_1_next = linked_list_1_iterator.next
        linked_list_2_next = linked_list_2_iterator.next

        # Link current node from first list to current node of second list
        linked_list_1_iterator.next = linked_list_2_iterator

        # Only link second list node to next first list node if it exists
        if linked_list_1_next is not None:
            linked_list_2_iterator.next = linked_list_1_next

        # Move to next nodes in each list
        linked_list_1_iterator = linked_list_1_next
        linked_list_2_iterator = linked_list_2_next

    return linked_list_1


def reverse_linkedList(linked_list):
    """Reverses a linked list in place.

    Args:
        linked_list: Head node of the linked list to reverse.

    Returns:
        The new head node of the reversed list.
    """
    previous_node, current_node = None, linked_list

    while current_node is not None:
        next_node = current_node.next  # Save next node before overwriting
        current_node.next = previous_node  # Reverse the link

        # Move pointers forward
        previous_node = current_node
        current_node = next_node

    return previous_node  # New head of reversed list


def print_linked_list(linked_list):
    """Prints a linked list in arrow format.

    Args:
        linked_list: Head node of the linked list to print.
    """
    current = linked_list
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")


# Test case
linked_list_dict = {
    "head": "1",
    "nodes": [
        {"id": "1", "next": "2", "value": 1},
        {"id": "2", "next": "3", "value": 2},
        {"id": "3", "next": "4", "value": 3},
        {"id": "4", "next": "5", "value": 4},
        {"id": "5", "next": "6", "value": 5},
        {"id": "6", "next": None, "value": 6},
    ],
}

# Build, zip, and print the linked list
linked_list = build_linked_list(linked_list_dict)

result = zip_linkedList(linked_list)

print_linked_list(result)
# Output: 1 -> 6 -> 2 -> 5 -> 3 -> 4 -> None

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

Let's analyze the time and space complexity of each function and then the overall `zip_linkedList` function.

### 1. `split_linkedList(linked_list)`
- **Time Complexity**: O(n)
  - The slow and fast pointer approach traverses the list once. The fast pointer moves two steps at a time, so the loop runs
  approximately n/2 times, which is O(n).
- **Space Complexity**: O(1)
  - Only a constant amount of extra space is used for the pointers (`slow_iterator` and `fast_iterator`).

### 2. `reverse_linkedList(linked_list)`
- **Time Complexity**: O(n)
  - The function traverses the entire list once, reversing the links as it goes.
- **Space Complexity**: O(1)
  - Only a constant amount of extra space is used for the pointers (`previous_node`, `current_node`, and `next_node`).

### 3. `interweave_linkedLists(linked_list_1, linked_list_2)`
- **Time Complexity**: O(n)
  - The function traverses both lists once, interweaving the nodes. Since the second half is reversed and roughly half the
  length of the original list, the total number of operations is proportional to n.
- **Space Complexity**: O(1)
  - Only a constant amount of extra space is used for the pointers (`linked_list_1_iterator`, `linked_list_2_iterator`,
  `linked_list_1_next`, and `linked_list_2_next`).

### 4. `zip_linkedList(linked_list)`
- **Time Complexity**: O(n)
  - `split_linkedList`: O(n)
  - `reverse_linkedList`: O(n/2) ≈ O(n) (since it reverses the second half)
  - `interweave_linkedLists`: O(n)
  - The total time complexity is O(n) + O(n) + O(n) = O(n).
- **Space Complexity**: O(1)
  - All operations are done in-place with only a constant amount of extra space used across all helper functions.

### Summary:
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)

The algorithm efficiently zips the linked list in linear time with constant space by splitting the list, reversing the
second half, and then interweaving the two halves.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
Let's walk through the entire code step-by-step to understand what it does and how it works.

## 🎯 **Goal of the Program**

The code takes a **singly linked list** and rearranges it in a **zip** fashion:

> **Original:** `1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None`
> **Zipped:** `1 -> 6 -> 2 -> 5 -> 3 -> 4 -> None`

This is commonly called **zipping a linked list**, where nodes from the **start** and **end** are interleaved.

---

## 📦 1. `class LinkedList`

```
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
```

Defines a node in the singly linked list:

* `value`: holds data (e.g. 1, 2, ...).
* `next`: points to the next node in the list.

---

## 🏗️ 2. `build_linked_list(data)`

This helper function converts a **dictionary representation** of a linked list into actual `LinkedList` objects.

```
def build_linked_list(data):
    if not data:
        return None

    nodes = {}
    for node_data in data["nodes"]:
        node = LinkedList(node_data["value"])
        nodes[node_data["id"]] = node

    for node_data in data["nodes"]:
        if node_data["next"] is not None:
            nodes[node_data["id"]].next = nodes[node_data["next"]]

    return nodes[data["head"]]
```

### 🔍 What it does:

* Step 1: Create all `LinkedList` nodes and map them by their `"id"`.
* Step 2: Link them according to the `"next"` field.
* Step 3: Return the head of the linked list.

✅ This gives us a proper `LinkedList` object we can work with.

---

## 🔄 3. `zip_linkedList(linked_list)`

This is the **main function** that performs the zipping.

```
def zip_linkedList(linked_list):
    if linked_list.next is None or linked_list.next.next is None:
        return linked_list  # Too short to zip

    first_half_head = linked_list
    second_half_head = split_linkedList(linked_list)

    reversed_second_half_head = reverse_linkedList(second_half_head)
    return interweave_linkedLists(first_half_head, reversed_second_half_head)
```

### 🔍 Breakdown:

* If the list has 1 or 2 elements, return it directly.
* Otherwise:

  1. Split the list into two halves.
  2. Reverse the second half.
  3. Interleave the two halves (zip them).

---

## ✂️ 4. `split_linkedList(linked_list)`

This splits the list into two halves using the **slow and fast pointer** approach.

```
def split_linkedList(linked_list):
    slow_iterator = linked_list
    fast_iterator = linked_list

    while fast_iterator is not None and fast_iterator.next is not None:
        slow_iterator = slow_iterator.next
        fast_iterator = fast_iterator.next.next

    second_half_head = slow_iterator.next
    slow_iterator.next = None  # Break the list

    return second_half_head
```

### 🔍 Purpose:

* Use two pointers:

  * `slow` moves one step.
  * `fast` moves two steps.
* When `fast` reaches the end, `slow` is in the middle.
* Cut the list after `slow`.

**Example:**
From `1 -> 2 -> 3 -> 4 -> 5 -> 6`, we get:

* First half: `1 -> 2 -> 3`
* Second half: `4 -> 5 -> 6`

---

## 🔁 5. `reverse_linkedList(linked_list)`

Reverses a singly linked list.

```
def reverse_linkedList(linked_list):
    previous_node, current_node = None, linked_list

    while current_node is not None:
        next_node = current_node.next
        current_node.next = previous_node

        previous_node = current_node
        current_node = next_node

    return previous_node
```

**Example:**
Turns `4 -> 5 -> 6 -> None` into `6 -> 5 -> 4 -> None`.

---

## 🔗 6. `interweave_linkedLists(linked_list_1, linked_list_2)`

This interleaves (zips) two lists together.

```
def interweave_linkedLists(linked_list_1, linked_list_2):
    linked_list_1_iterator = linked_list_1
    linked_list_2_iterator = linked_list_2

    while linked_list_1_iterator is not None and linked_list_2_iterator is not None:
        # Save next pointers
        linked_list_1_next = linked_list_1_iterator.next
        linked_list_2_next = linked_list_2_iterator.next

        # Link current nodes
        linked_list_1_iterator.next = linked_list_2_iterator
        if linked_list_1_next is not None:
            linked_list_2_iterator.next = linked_list_1_next

        # Move to next nodes
        linked_list_1_iterator = linked_list_1_next
        linked_list_2_iterator = linked_list_2_next

    return linked_list_1
```

**Example:**
Interweaving `1 -> 2 -> 3` and `6 -> 5 -> 4` gives:

```
1 -> 6 -> 2 -> 5 -> 3 -> 4 -> None
```

It does so by alternating nodes between the two lists.

---

## 📤 7. `print_linked_list(linked_list)`

Simply prints the linked list in readable format:

```
1 -> 6 -> 2 -> 5 -> 3 -> 4 -> None
```

---

## ✅ Test Case

```
linked_list_dict = {
    "head": "1",
    "nodes": [
        {"id": "1", "next": "2", "value": 1},
        {"id": "2", "next": "3", "value": 2},
        {"id": "3", "next": "4", "value": 3},
        {"id": "4", "next": "5", "value": 4},
        {"id": "5", "next": "6", "value": 5},
        {"id": "6", "next": None, "value": 6},
    ],
}
```

This builds the list:

```
1 -> 2 -> 3 -> 4 -> 5 -> 6
```

After zipping:

```
1 -> 6 -> 2 -> 5 -> 3 -> 4
```

---

## 🔚 Summary

The entire flow:

1. **Build** a linked list from a dictionary.
2. **Split** it in two halves.
3. **Reverse** the second half.
4. **Interleave** the two halves to zip them.
5. **Print** the result.

---

Let's walk through the **zipping process** visually using **ASCII diagrams** step-by-step:

### 📋 **Original Linked List**

We start with:

```
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
```

---

### ✂️ **Step 1: Split into Two Halves**

Use **slow and fast pointers** to find the middle.

```
First Half:     1 -> 2 -> 3 -> None
Second Half:                     4 -> 5 -> 6 -> None
```

---

### 🔁 **Step 2: Reverse the Second Half**

We reverse `4 -> 5 -> 6`:

```
Reversed Second Half:  6 -> 5 -> 4 -> None
```

---

### 🔗 **Step 3: Interleave (Zip) the Two Lists**

Now we interleave:

* From first half: `1 -> 2 -> 3`
* From reversed second half: `6 -> 5 -> 4`

We do this **one node at a time**:

#### ✅ Iteration 1:

```
Take 1 from First
Take 6 from Second

Result so far:  1 -> 6
```

#### ✅ Iteration 2:

```
Take 2 from First
Take 5 from Second

Result so far:  1 -> 6 -> 2 -> 5
```

#### ✅ Iteration 3:

```
Take 3 from First
Take 4 from Second

Final Result:   1 -> 6 -> 2 -> 5 -> 3 -> 4 -> None
```

---

### 🎉 **Final Zipped Linked List**

```
1 -> 6 -> 2 -> 5 -> 3 -> 4 -> None
```

---

### 🧠 Summary of Steps Visually:

```
Original:        1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
Split:           1 -> 2 -> 3       and       4 -> 5 -> 6
Reversed 2nd:                       6 -> 5 -> 4
Zipped:          1 -> 6 -> 2 -> 5 -> 3 -> 4 -> None
```

"""
