# Problem Description:

"""
                                            Shift Linked List

Write a function that takes in the head of a Singly Linked List and an integer `k`, shifts the list in place (i.e., doesn't create
a brand new list) by `k` positions, and returns its new head.

Shifting a Linked List means moving its nodes forward or backward and wrapping them around the list where appropriate. For example,
shifting a Linked List forward by one position would make its tail become the new head of the linked list.

Whether nodes are moved forward or backward is determined by whether `k` is positive or negative.

Each `LinkedList` node has an integer `value` as well as a `next` node pointing to the next node in the list or to `None` if it's
the tail of the list.

You can assume that the input Linked List will always have at least one node; in other words, the head will never be `None`.


## Sample Input:
```
head = 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> None
k = 2

// The head node with value 0
```

## Sample Output:
```
4 -> 5 -> 0 -> 1 -> 2 -> 3 -> None

// The new head node with value 4
```

## Optimal Time & Space Complexity:
```
O(n) time | O(1) space - where `n` is the number of nodes in the Linked List.
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


# O(n) time | O(1) space
def shift_linkedList(head, k):
    # Calculate the length of the linked list and find the tail node
    list_length = 1  # starts at 1 since we're counting the head
    list_tail = head  # we'll use this to traverse to the end

    # Traverse to the end of the list to find tail and get length
    while list_tail.next is not None:
        list_tail = list_tail.next
        list_length += 1

    # Calculate the effective offset (handle cases where k > list length)
    offset = abs(k) % list_length  # absolute value for negative k
    # If no effective shift needed, return original list
    if offset == 0:
        return head

    # Determine the position of the new tail node:
    # - For positive k: move list_length - offset nodes from start
    # - For negative k: move offset nodes from start
    new_tail_position = list_length - offset if k > 0 else offset

    # Find the new tail node
    new_tail = head
    for _ in range(1, new_tail_position):  # starts at 1 since head is node 0
        new_tail = new_tail.next

    # The node after new tail becomes the new head
    new_head = new_tail.next
    # Break the list at new tail
    new_tail.next = None
    # Connect original tail to original head to make it circular
    list_tail.next = head

    # Return the new head of the shifted list
    return new_head


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
    "head": "0",
    "nodes": [
        {"id": "0", "next": "1", "value": 0},
        {"id": "1", "next": "2", "value": 1},
        {"id": "2", "next": "3", "value": 2},
        {"id": "3", "next": "4", "value": 3},
        {"id": "4", "next": "5", "value": 4},
        {"id": "5", "next": None, "value": 5},
    ],
}

k = 2

# Test Case:

# Build the linked list from dictionary
linked_list = build_linked_list(linked_list_dict)

# Remove duplicates
result = shift_linkedList(linked_list, 2)

print_linked_list(result)
# Output: 4 -> 5 -> 0 -> 1 -> 2 -> 3 -> None

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

Let's analyze the time and space complexity of the `shift_linkedList` function.

### Time Complexity:

1. **Finding the Tail and Length**:  
   The first `while` loop traverses the entire linked list to find the tail and compute the length. This takes **O(n)** time,
   where `n` is the number of nodes in the linked list.

2. **Calculating the Offset**:  
   The `offset` is computed using `abs(k) % list_length`, which is an **O(1)** operation.

3. **Finding the New Tail and New Head**:  
   The `for` loop runs for `new_tail_position - 1` iterations, where `new_tail_position` is at most `n - 1`.
   In the worst case, this is **O(n)**.

4. **Adjusting Pointers**:  
   The operations `new_tail.next = None` and `list_tail.next = head` are **O(1)**.

**Total Time Complexity**:  
Since all steps are either **O(n)** or **O(1)**, the overall time complexity is:  
**O(n)** (linear time).

### Space Complexity:

1. **Variables Used**:  
   The function uses a constant number of variables (`list_length`, `list_tail`, `offset`, `new_tail_position`, `new_tail`,
   `new_head`), regardless of the input size. No additional data structures (like arrays or hash tables) are used.

**Total Space Complexity**:  
**O(1)** (constant space).

### Summary:
- **Time Complexity**: **O(n)**  
- **Space Complexity**: **O(1)**  

This is optimal for this problem since you must traverse the entire list at least once to determine its length and tail.
The space usage is minimal since only a few pointers are modified in place.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
Let's go through the entire code step by step to understand how it works and how it produces the final output.

---

## 🔧 1. Class Definition: `LinkedList`

```
class LinkedList:
    def __init__(self, value):
        self.value = value  # Stores the value of the node
        self.next = None    # Points to the next node (initially None)
```

This class represents a **single node** in a singly linked list. Each node has:

* `value`: the data it holds.
* `next`: a reference to the next node in the list (or `None` if it’s the last node).

---

## 🏗️ 2. Building the Linked List: `build_linked_list`

```
def build_linked_list(data):
    ...
```

This function builds a linked list from a **dictionary input** format.

### Example Input:

```
linked_list_dict = {
    "head": "0",
    "nodes": [
        {"id": "0", "next": "1", "value": 0},
        {"id": "1", "next": "2", "value": 1},
        {"id": "2", "next": "3", "value": 2},
        {"id": "3", "next": "4", "value": 3},
        {"id": "4", "next": "5", "value": 4},
        {"id": "5", "next": None, "value": 5},
    ],
}
```

### Breakdown:

1. **Step 1 – Create Nodes**: All nodes are created and stored in a dictionary:

   ```
   nodes[node_data["id"]] = node
   ```

   So, for example:

   * `"0"` → Node with value `0`
   * `"1"` → Node with value `1`
   * etc.

2. **Step 2 – Link Nodes**:
   Based on the `next` field, each node's `next` pointer is assigned.

3. **Step 3 – Return Head**:
   The node with ID `"0"` is returned as the head node (start of the list).

---

## 🔁 3. Shifting the Linked List: `shift_linkedList`

```
def shift_linkedList(head, k):
    ...
```

### Purpose:

This function "shifts" the linked list by `k` positions:

* If `k > 0`: shift the list **right** (move tail nodes to front).
* If `k < 0`: shift the list **left** (move head nodes to back).

### Step-by-Step Breakdown:

#### ✅ Step 1 – Get Length and Tail

```
list_length = 1
list_tail = head

while list_tail.next is not None:
    list_tail = list_tail.next
    list_length += 1
```

* Traverse the list to find the last node (`list_tail`) and calculate its length.

For the input list: `0 -> 1 -> 2 -> 3 -> 4 -> 5 -> None`

* `list_length = 6`
* `list_tail = node with value 5`

---

#### ✅ Step 2 – Compute Offset

```
offset = abs(k) % list_length
if offset == 0:
    return head
```

* `offset = abs(2) % 6 = 2`
* If `offset == 0`, no shift is needed.

---

#### ✅ Step 3 – Find New Tail and Head

```
new_tail_position = list_length - offset if k > 0 else offset
new_tail = head
for i in range(1, new_tail_position):
    new_tail = new_tail.next
```

* For `k = 2`, we want to move 2 nodes from the end to the front.
* So, new tail is at position `6 - 2 = 4` (0-indexed).

Node positions:

* `0 -> 1 -> 2 -> 3 -> 4 -> 5`
* New tail is node with value `3`
* New head is node with value `4`

---

#### ✅ Step 4 – Cut and Reconnect

```
new_head = new_tail.next     # Node with value 4
new_tail.next = None         # Break the link
list_tail.next = head        # Connect old tail to old head
return new_head              # Return new head
```

After this:

* `4 -> 5 -> 0 -> 1 -> 2 -> 3 -> None`

---

## 🖨️ 4. Printing the Linked List: `print_linked_list`

```
def print_linked_list(linked_list):
    ...
```

A simple traversal of the list to print each node's value followed by `" -> "`, ending with `"None"`.

---

## ✅ Output for Test Case

Input List:
`0 -> 1 -> 2 -> 3 -> 4 -> 5 -> None`
`k = 2` → shift right by 2

Output:
`4 -> 5 -> 0 -> 1 -> 2 -> 3 -> None`

---

## 📌 Summary

| Function            | Responsibility                                   |
| ------------------- | ------------------------------------------------ |
| `LinkedList`        | Defines a node in a singly linked list           |
| `build_linked_list` | Converts a dict structure into a linked list     |
| `shift_linkedList`  | Shifts list nodes left or right by `k` positions |
| `print_linked_list` | Prints linked list elements in readable format   |

"""
