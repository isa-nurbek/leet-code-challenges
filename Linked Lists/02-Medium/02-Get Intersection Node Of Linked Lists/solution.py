# Problem Description:

"""
                                            Get Intersection Node Of Linked Lists

You're given two Linked Lists of potentially unequal length. These Linked Lists potentially merge at a shared intersection node.
Write a function that returns the intersection node or returns `None` if there is no intersection.

Each `LinkedList` node has an integer `value` as well as a `next` node pointing to the next node in the list or to `None` if it's
the tail of the list.

> Note: Your function should return an existing node. It should not modify either Linked List, and it should not create any new
Linked Lists.


## Sample Input:
```
linkedList_one = 2 -> 3 -> 1 -> 4 -> None
linkedList_two = 8 -> 7 -> 1 -> 4 -> None
```

## Sample Output:
```
1 -> 4 -> None

// The lists intersect at the node with value 1
```

## Optimal Time & Space Complexity:
```
O(n + m) time | O(1) space - where `n` is the length of the first Linked List and `m` is the length of the second Linked List.
```

"""

# =========================================================================================================================== #

# Solution:


class LinkedList:
    def __init__(self, value):
        self.value = value  # Stores the value of the node
        self.next = None  # Pointer to the next node (initially None)


# Helper function to convert dictionary to LinkedList
def build_intersected_linked_lists(list_one_data, list_two_data):
    """Builds two linked lists that may intersect, ensuring shared nodes are the same object.

    Args:
        list_one_data: Dictionary containing head ID and node data for first list
        list_two_data: Dictionary containing head ID and node data for second list

    Returns:
        Tuple of (head_of_list_one, head_of_list_two)
    """
    if not list_one_data or not list_two_data:
        return None, None

    # Dictionary to store all nodes by their IDs to ensure shared nodes are same objects
    all_nodes = {}

    # Process list_one_data - create nodes if they don't exist
    for node_data in list_one_data["nodes"]:
        if node_data["id"] not in all_nodes:
            all_nodes[node_data["id"]] = LinkedList(node_data["value"])

    # Process list_two_data - reuse nodes if IDs overlap with list_one
    for node_data in list_two_data["nodes"]:
        if node_data["id"] not in all_nodes:
            all_nodes[node_data["id"]] = LinkedList(node_data["value"])

    # Connect nodes for list_one using the 'next' pointers
    for node_data in list_one_data["nodes"]:
        if node_data["next"] is not None:
            all_nodes[node_data["id"]].next = all_nodes[node_data["next"]]

    # Connect nodes for list_two using the 'next' pointers
    for node_data in list_two_data["nodes"]:
        if node_data["next"] is not None:
            all_nodes[node_data["id"]].next = all_nodes[node_data["next"]]

    # Return the head nodes of both lists
    return all_nodes[list_one_data["head"]], all_nodes[list_two_data["head"]]


# O(n + m) time | O(1) space
def merging_linked_lists(linked_list_one, linked_list_two):
    """Finds the intersection point of two linked lists.

    Args:
        linked_list_one: Head node of first linked list
        linked_list_two: Head node of second linked list

    Returns:
        The first intersecting node if found, None otherwise
    """

    def get_length(head):
        """Helper function to get length of a linked list."""
        length = 0
        while head:
            length += 1
            head = head.next
        return length

    # Get lengths of both lists
    len_one = get_length(linked_list_one)
    len_two = get_length(linked_list_two)

    current_one = linked_list_one
    current_two = linked_list_two

    # Move the longer list's pointer forward to align starting points
    if len_one > len_two:
        for _ in range(len_one - len_two):
            current_one = current_one.next
    else:
        for _ in range(len_two - len_one):
            current_two = current_two.next

    # Traverse both lists in parallel until intersection is found
    while current_one and current_two:
        if current_one == current_two:  # If nodes are the same object
            return current_one
        current_one = current_one.next
        current_two = current_two.next

    return None  # No intersection found


# Function to print the linked list (for verification)
def print_linked_list(linked_list):
    """Prints the linked list values in order."""
    current = linked_list
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")


# Input data for first test case
linkedList_one_data = {
    "head": "1",
    "nodes": [
        {"id": "1", "next": "2", "value": 1},  # Node 1 -> Node 2
        {"id": "2", "next": "3", "value": 2},  # Node 2 -> Node 3
        {"id": "3", "next": None, "value": 3},  # Node 3 -> None
    ],
}

linkedList_two_data = {
    "head": "4",
    "nodes": [
        {"id": "4", "next": "5", "value": 4},  # Node 4 -> Node 5
        {"id": "5", "next": "3", "value": 5},  # Node 5 -> Node 3 (shared with list one)
        {"id": "3", "next": None, "value": 3},  # Node 3 -> None (shared)
    ],
}

# Input data for second test case
linkedList_three_data = {
    "head": "2",
    "nodes": [
        {"id": "2", "next": "3", "value": 2},  # Node 2 -> Node 3
        {"id": "3", "next": "1", "value": 3},  # Node 3 -> Node 1
        {"id": "1", "next": "4", "value": 1},  # Node 1 -> Node 4
        {"id": "4", "next": None, "value": 4},  # Node 4 -> None
    ],
}

linkedList_four_data = {
    "head": "8",
    "nodes": [
        {"id": "8", "next": "7", "value": 8},  # Node 8 -> Node 7
        {
            "id": "7",
            "next": "1",
            "value": 7,
        },  # Node 7 -> Node 1 (shared with list three)
        {"id": "1", "next": "4", "value": 1},  # Node 1 -> Node 4 (shared)
        {"id": "4", "next": None, "value": 4},  # Node 4 -> None (shared)
    ],
}

# Build the linked lists with shared nodes
ll1, ll2 = build_intersected_linked_lists(linkedList_one_data, linkedList_two_data)
ll3, ll4 = build_intersected_linked_lists(linkedList_three_data, linkedList_four_data)

# Test case 1
print("Original test case:")
result1 = merging_linked_lists(ll1, ll2)
if result1:
    print(f"Intersection at node with value: {result1.value}")
    print("Intersected list:")
    print_linked_list(result1)
else:
    print("No intersection found")

# Test case 2
print("\nNew test case (2->3->1->4 and 8->7->1->4):")
result2 = merging_linked_lists(ll3, ll4)
if result2:
    print(f"Intersection at node with value: {result2.value}")
    print("Intersected list:")
    print_linked_list(result2)
else:
    print("No intersection found")

# Output:

"""
Original test case:
Intersection at node with value: 3
Intersected list:
3 -> None

New test case (2->3->1->4 and 8->7->1->4):
Intersection at node with value: 1
Intersected list:
1 -> 4 -> None

"""

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

Let's analyze the time and space complexity of the `merging_linked_lists` function.

### Time Complexity:

1. **Calculating Lengths**: 
   - `get_length(linked_list_one)` traverses the entire first list, taking O(n) time where n is the length of the first list.
   - `get_length(linked_list_two)` traverses the entire second list, taking O(m) time where m is the length of the second list.
   - Total for this part: O(n + m).

2. **Advancing the Pointer of the Longer List**:
   - The loop runs `abs(len_one - len_two)` times, which is O(|n - m|).
   - This is also bounded by O(n + m) in the worst case.

3. **Parallel Traversal**:
   - The while loop runs until the end of the shorter list (after alignment), which is O(min(n, m)).
   - In the worst case, this is O(n + m) (when one list is much longer than the other, but the merge happens at the end).

Overall, the time complexity is **O(n + m)**, where n and m are the lengths of the two linked lists. This is because all steps
are linear and additive.

### Space Complexity:

1. The function only uses a constant amount of extra space (variables like `len_one`, `len_two`, `current_one`, `current_two`, etc.).
2. No additional data structures are used that grow with the input size.

Thus, the space complexity is **O(1)** (constant space).

### Summary:
- **Time Complexity**: O(n + m)
- **Space Complexity**: O(1)

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
This code is a Python implementation that builds two linked lists which **may share nodes (i.e., intersect)** and detects the
intersection point if it exists. Let’s go through each part of the code in detail to understand how it works.

---

## ✅ Classes and Helpers

### `class LinkedList`

```
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
```

This defines a basic singly linked list node. Each node contains:

* `value`: the data the node holds.
* `next`: a pointer to the next node (or `None` if it's the last node).

---

## 🔧 Function: `build_intersected_linked_lists`

This function **builds two linked lists** from the input data structures. If nodes in the two lists share the same ID, they are
**treated as the same object (i.e., same memory reference)** — this allows the lists to **intersect**.

```
def build_intersected_linked_lists(list_one_data, list_two_data):
```

### Key variables:

* `all_nodes`: dictionary that maps `id` strings to actual `LinkedList` node objects.

### Step-by-step:

1. **Create nodes for `list_one_data`** using `LinkedList(node_data["value"])`.

   * Store them in `all_nodes` using `node_data["id"]` as the key.

2. **Do the same for `list_two_data`**, but **reuse any existing nodes** if their ID is already in `all_nodes`.

3. **Connect nodes** for both lists based on their `next` pointers (which refer to other node IDs).

4. Return the **head nodes** of both lists using their IDs.

> ✅ This enables **node sharing** — if both lists refer to a node with the same ID, they **literally point to the same object**,
allowing true intersections.

---

## 🔍 Function: `merging_linked_lists`

This function **detects the intersection node** (if any) between two linked lists.

```
def merging_linked_lists(linked_list_one, linked_list_two):
```

### Step-by-step:

1. Compute the **length** of each list using the helper `get_length`.

2. **Align the start positions** of both lists:

   * Advance the pointer of the longer list by the difference in lengths so both are equidistant from the end.

3. **Traverse both lists in parallel**:

   * At each step, compare `current_one == current_two` (i.e., same object in memory).
   * If they point to the **same node**, return it as the **intersection point**.
   * Otherwise, continue traversing.

4. If no match is found, return `None`.

> 🧠 **Key Insight**: Because intersecting lists share nodes by reference, comparing the **object identity** is enough.

---

## 🖨️ Function: `print_linked_list`

This is a simple printer for linked lists:

```
def print_linked_list(linked_list):
```

It walks through the list and prints values in a readable `a -> b -> ... -> None` format.

---

## 🧪 Input Data & Test Cases

### Original Test Case:

```
linkedList_one_data = {
    "head": "1",
    "nodes": [
        {"id": "1", "next": "2", "value": 1},
        {"id": "2", "next": "3", "value": 2},
        {"id": "3", "next": None, "value": 3},
    ],
}

linkedList_two_data = {
    "head": "4",
    "nodes": [
        {"id": "4", "next": "5", "value": 4},
        {"id": "5", "next": "3", "value": 5},  # points to same "3"
        {"id": "3", "next": None, "value": 3},  # same node as above
    ],
}
```

* `list_one`: 1 → 2 → 3
* `list_two`: 4 → 5 → 3 (intersects at node `3`)

### New Test Case:

```
linkedList_three_data = {
    "head": "2",
    "nodes": [
        {"id": "2", "next": "3", "value": 2},
        {"id": "3", "next": "1", "value": 3},
        {"id": "1", "next": "4", "value": 1},
        {"id": "4", "next": None, "value": 4},
    ],
}

linkedList_four_data = {
    "head": "8",
    "nodes": [
        {"id": "8", "next": "7", "value": 8},
        {"id": "7", "next": "1", "value": 7},
        {"id": "1", "next": "4", "value": 1},
        {"id": "4", "next": None, "value": 4},
    ],
}
```

* `list_three`: 2 → 3 → 1 → 4
* `list_four`: 8 → 7 → 1 → 4 (intersects at node `1`)

---

## ✅ Output Explanation

### For Test Case 1:

```
Intersection at node with value: 3
Intersected list:
3 -> None
```

### For Test Case 2:

```
Intersection at node with value: 1
Intersected list:
1 -> 4 -> None
```

In both cases, the function correctly identifies the first intersecting node and prints the rest of the list from that point.

---

## 🔚 Summary

* **Shared nodes by ID** are reused to simulate realistic intersections.
* **Intersection detection** is efficient: O(n + m) time and O(1) space.
* **Real-life analogy**: Think of two roads merging at a junction — this detects where they meet **based on reference**, not value.

---

Here's an **ASCII visualization** of the two test cases showing how the linked lists intersect.

---

### 🔹 Test Case 1:

**List One:** `1 → 2 → 3`
**List Two:** `4 → 5 ↘`
         `↘ 3`

```
List One:   1 → 2 → 3
                     ↑
List Two:   4 → 5 ───┘
```

**Intersection Point:** Node with value `3`

---

### 🔹 Test Case 2:

**List Three:** `2 → 3 → 1 → 4`
**List Four:** `8 → 7 ↘`
               `↘ 1 → 4`

```
List Three: 2 → 3 → 1 → 4
                        ↑
List Four:  8 → 7 ──────┘
```

**Intersection Point:** Node with value `1`

---

These diagrams clearly show how the lists **merge into a shared tail**, which is exactly what your `merging_linked_lists`
function detects.

"""
