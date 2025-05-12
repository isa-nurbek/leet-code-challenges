# Problem Description:

"""
                                            Find Loop

Write a function that takes in the head of a Singly Linked List that contains a loop (in other words, the list's tail node points
to some node in the list instead of `None`). The function should return the node (the actual node, not just its value) from which
the loop originates in constant space.

Each `LinkedList` node has an integer `value` as well as a `next` node pointing to the next node in the list.


## Sample Input:
```
// The head node with value 0

head = 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6
                           ^         v
                           9 <- 8 <- 7
```

## Sample Output:
```
4 -> 5 -> 6
^         v
9 <- 8 <- 7

// The node with value 4
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
def find_loop(head):
    """Finds the starting node of a loop in a linked list using Floyd's algorithm.

    Args:
        head: The head node of the linked list

    Returns:
        The node where the loop starts, or None if there is no loop
    """
    if not head or not head.next:
        return None

    # Initialize two pointers
    slow = head.next
    fast = head.next.next

    # Find the meeting point
    while slow != fast:
        if not fast or not fast.next:
            return None  # No loop
        slow = slow.next
        fast = fast.next.next

    # Reset slow to head and find the start of the loop
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow


def print_linked_list_with_loop(head, loop_start):
    """Prints the linked list up to the loop start and then the loop once.

    Args:
        head: The head node of the linked list
        loop_start: The node where the loop starts
    """
    current = head
    loop_detected = False
    visited = set()

    # Print the list until the loop starts
    while current and current != loop_start:
        print(current.value, end=" -> ")
        current = current.next

    if not current:
        print("None")
        return

    # Now print the loop once
    print(f"{current.value} -> ", end="")
    current = current.next
    while current != loop_start:
        print(f"{current.value} -> ", end="")
        current = current.next
    print(f"{loop_start.value} (loop starts here)")


# Input data
linked_list_dict = {
    "head": "0",
    "nodes": [
        {"id": "0", "next": "1", "value": 0},
        {"id": "1", "next": "2", "value": 1},
        {"id": "2", "next": "3", "value": 2},
        {"id": "3", "next": "4", "value": 3},
        {"id": "4", "next": "5", "value": 4},
        {"id": "5", "next": "6", "value": 5},
        {"id": "6", "next": "7", "value": 6},
        {"id": "7", "next": "8", "value": 7},
        {"id": "8", "next": "9", "value": 8},
        {"id": "9", "next": "4", "value": 9},
    ],
}

# Build the linked list from dictionary
linked_list = build_linked_list(linked_list_dict)

# Find the loop
loop_start = find_loop(linked_list)

if loop_start:
    print_linked_list_with_loop(linked_list, loop_start)
else:
    print("No loop detected")

# Output: 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 4 (loop starts here)

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### Time Complexity Analysis:

1. **Detecting the Loop (First While Loop):**
   - The `slow` pointer moves one step at a time (`slow = slow.next`).
   - The `fast` pointer moves two steps at a time (`fast = fast.next.next`).
   - In the worst case (when there is a loop), the `fast` pointer will eventually catch up to the `slow` pointer after `O(n)` iterations, where `n` is the number of nodes in the linked list. This is because the `fast` pointer closes the gap between
   itself and the `slow` pointer by 1 node in each iteration.

2. **Finding the Start of the Loop (Second While Loop):**
   - After resetting `slow` to `head`, both `slow` and `fast` move one step at a time until they meet.
   - The distance from the head to the start of the loop is `k`, and the distance from the meeting point to the start of the loop
   is also `k` (this is a property of Floyd's algorithm). Thus, this loop runs in `O(k)` time, which is `O(n)` in the worst case.

Combining both parts, the total time complexity is `O(n) + O(n) = O(n)`.

### Space Complexity Analysis:

- The algorithm uses only two pointers (`slow` and `fast`) and no additional data structures, so the space complexity is `O(1)`
(constant space).

### Summary:
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

### Correctness:
The algorithm is correct and follows Floyd's Tortoise and Hare algorithm for cycle detection in linked lists. It first detects
whether a loop exists and then finds the starting node of the loop. The logic is sound, and the time and space complexity analysis
is accurate.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
This code defines a complete workflow for:

1. **Building a linked list** from a dictionary-like structure.
2. **Detecting if there's a loop** in the list using **Floyd’s Cycle Detection Algorithm**.
3. **Printing the list with loop awareness**, showing where the cycle starts.

Let’s walk through each part in detail:

---

### 🧱 1. `LinkedList` Class

```
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
```

This defines a node in the linked list. Each node has:

* `value`: the data the node stores.
* `next`: a pointer to the next node in the list.

---

### 🏗️ 2. `build_linked_list(data)`

This function constructs a linked list from a dictionary input.

```
linked_list_dict = {
    "head": "0",
    "nodes": [
        {"id": "0", "next": "1", "value": 0},
        ...
        {"id": "9", "next": "4", "value": 9},  # creates a loop here
    ]
}
```

**Step-by-step:**

#### a. Create all nodes:

```
nodes = {}
for node_data in data["nodes"]:
    node = LinkedList(node_data["value"])
    nodes[node_data["id"]] = node
```

* Loop through each dictionary entry.
* Create a `LinkedList` node using the `value`.
* Store it in a dictionary `nodes`, using the string `id` as the key.

#### b. Set up `.next` pointers:

```
for node_data in data["nodes"]:
    if node_data["next"] is not None:
        nodes[node_data["id"]].next = nodes[node_data["next"]]
```

* For each node, if it has a `next` field, set its `.next` pointer to the corresponding node using the ID.

#### c. Return head node:

```
return nodes[data["head"]]
```

* This gives you the head of the linked list.

---

### 🔁 3. `find_loop(head)`

This function detects a loop using **Floyd’s Tortoise and Hare algorithm**.

**Floyd's Algorithm Key Idea**:

* Use two pointers: one moves slow (`slow`), another fast (`fast`).
* If there's a loop, they will meet inside the loop.

#### a. Initialization:

```
slow = head.next
fast = head.next.next
```

#### b. Detection loop:

```
while slow != fast:
    if not fast or not fast.next:
        return None  # No loop
    slow = slow.next
    fast = fast.next.next
```

* Both pointers move (slow by 1 step, fast by 2).
* If `fast` reaches the end → no loop.
* If `slow` and `fast` meet → loop exists.

#### c. Finding the start of the loop:

```
slow = head
while slow != fast:
    slow = slow.next
    fast = fast.next
```

Once they meet, reset `slow` to the head. Move both one step at a time. They will meet **at the loop's starting point**.

---

### 📋 4. `print_linked_list_with_loop(head, loop_start)`

This function prints the list, stopping and highlighting the loop correctly.

**Key points:**

#### a. Print non-loop part:

```
while current and current != loop_start:
    print(current.value, end=" -> ")
    current = current.next
```

#### b. Print loop part:

```
print(f"{current.value} -> ", end="")
current = current.next
while current != loop_start:
    print(f"{current.value} -> ", end="")
    current = current.next
print(f"{loop_start.value} (loop starts here)")
```

Prints from the loop start node until it loops back.

---

### 🧪 Running Example:

Given:

```
{"id": "9", "next": "4", "value": 9}
```

* Node 9 points back to node 4 → forms a cycle: `4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 4 -> ...`

So:

```
0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 4 (loop starts here)
```

---

### ✅ Summary

| Part                          | Purpose                                    |
| ----------------------------- | ------------------------------------------ |
| `LinkedList`                  | Defines node structure                     |
| `build_linked_list`           | Constructs list from dictionary            |
| `find_loop`                   | Detects and returns start of loop          |
| `print_linked_list_with_loop` | Prints the list, visually showing the loop |

---

Here's an **ASCII diagram** that visualizes how the linked list and the loop work, especially with respect to Floyd's Tortoise
and Hare algorithm:

---

### 🔗 Linked List with a Loop

```
          ┌────────────────────────────────────────────────────────────────────┐
          ↓                                                                    │
[0] -> [1] -> [2] -> [3] -> [4] -> [5] -> [6] -> [7] -> [8] -> [9]
                                              ↑                              │
                                              └──────────────────────────────┘
```

* Each `[n]` is a node with value `n`.
* The arrow `->` shows the `.next` pointer.
* Node `[9]` connects back to node `[4]`, forming a **loop**:
  `[4] → [5] → [6] → [7] → [8] → [9] → [4] → ...`

---

### 🐢🐇 Floyd's Cycle Detection (Tortoise and Hare)

Initially:

```
slow = head.next          # points to node [1]
fast = head.next.next     # points to node [2]
```

Then:

| Step | Slow Points To | Fast Points To    |
| ---- | -------------- | ----------------- |
| 1    | 2              | 4                 |
| 2    | 3              | 6                 |
| 3    | 4              | 8                 |
| 4    | 5              | 4                 |
| 5    | 6              | 6 ✅ (They meet)  |

They **meet inside the loop** at node `[6]`.

Now reset `slow = head` and move both one step at a time:

| Step | Slow  | Fast    |
| ---- | ----- | ------- |
| 1    | 0     | 7       |
| 2    | 1     | 8       |
| 3    | 2     | 9       |
| 4    | 3     | 4       |
| 5    | 4 ✅  | 4 ✅   |

Now they meet at the **start of the loop**: node `[4]`.

"""
