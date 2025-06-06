# Problem Description:

"""
                                            Sum of Linked Lists

You're given two Linked Lists of potentially unequal length. Each Linked List represents a `non-negative` integer, where each node
in the Linked List is a digit of that integer, and the first node in each Linked List always represents the least significant digit
of the integer. Write a function that returns the head of a new Linked List that represents the `sum` of the integers represented
by the two input Linked Lists.

Each `LinkedList` node has an integer `value` as well as a `next` node pointing to the next node in the list or to `None` if it's
the tail of the list. The `value` of each `LinkedList` node is always in the range of `0 - 9`.

> Note: your function must create and return a new Linked List, and you're not allowed to modify either of the input Linked Lists.


## Sample Input:
```
linkedList_one = 2 -> 4 -> 7 -> 1 -> None
linkedList_two = 9 -> 4 -> 5 -> None
```

## Sample Output:
```
1 -> 9 -> 2 -> 2 -> None

// linkedList_one represents: 1742
// linkedList_two represents: 549
// 1742 + 549 = 2291
```

## Optimal Time & Space Complexity:
```
O(max(n, m)) time | O(max(n, m)) space - where `n` is the length of the first Linked List and `m` is the length
of the second Linked List.
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


# Function to sum of 2 Linked Lists
# O(max(n, m)) time | O(max(n, m)) space
def sum_of_linked_lists(linkedList_one, linkedList_two):
    # Initialize a dummy head node for the new linked list (result list)
    # This helps simplify the code by providing a starting point
    new_linked_list_head_pointer = LinkedList(0)
    # Current node points to the last node in our new linked list
    current_node = new_linked_list_head_pointer
    # Carry stores the carry-over value when sum of digits >= 10
    carry = 0

    # Start with the head nodes of both input linked lists
    node_one = linkedList_one
    node_two = linkedList_two

    # Continue processing while:
    # 1. There are nodes remaining in either input list, OR
    # 2. There's a carry value that needs to be added
    while node_one is not None or node_two is not None or carry != 0:
        # Get the current digit from each list (0 if list is exhausted)
        value_one = node_one.value if node_one is not None else 0
        value_two = node_two.value if node_two is not None else 0

        # Calculate sum of current digits plus any carry from previous step
        sum_of_values = value_one + value_two + carry

        # The digit to store in new node is sum modulo 10
        new_value = sum_of_values % 10
        # Create new node with the calculated digit
        new_node = LinkedList(new_value)

        # Link the new node to our result list and move current pointer
        current_node.next = new_node
        current_node = new_node

        # Calculate carry for next iteration (sum divided by 10)
        carry = sum_of_values // 10

        # Move to next nodes in input lists (if they exist)
        node_one = node_one.next if node_one is not None else None
        node_two = node_two.next if node_two is not None else None

    # Return the head of the result list (skipping the dummy head node)
    return new_linked_list_head_pointer.next


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
linkedList_one_data = {
    "head": "2",
    "nodes": [
        {"id": "2", "next": "4", "value": 2},
        {"id": "4", "next": "7", "value": 4},
        {"id": "7", "next": "1", "value": 7},
        {"id": "1", "next": None, "value": 1},
    ],
}

linkedList_two_data = {
    "head": "9",
    "nodes": [
        {"id": "9", "next": "4", "value": 9},
        {"id": "4", "next": "5", "value": 4},
        {"id": "5", "next": None, "value": 5},
    ],
}

# Build the linked lists from dictionary
linked_list_one = build_linked_list(linkedList_one_data)
linked_list_two = build_linked_list(linkedList_two_data)

# Test Case 1: Sum linked_list_one and linked_list_two
result = sum_of_linked_lists(linked_list_one, linked_list_two)
print_linked_list(result)  # Output: 1 -> 9 -> 2 -> 2 -> None

# Test Case 2: Sum linked_list_one with itself (as in our original test)
result = sum_of_linked_lists(linked_list_one, linked_list_one)
print_linked_list(result)  # Output: 4 -> 8 -> 4 -> 2 -> None

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

Let's analyze the time and space complexity of the given `sum_of_linked_lists` function.

### Time Complexity:

The function iterates through both linked lists (`linkedList_one` and `linkedList_two`) simultaneously, processing one node
from each list in each iteration. The loop continues until:
1. Both `node_one` and `node_two` are `None`, and
2. There is no remaining `carry` to process.

- Let `n` be the length of `linkedList_one`.
- Let `m` be the length of `linkedList_two`.

The loop runs for a maximum of `max(n, m)` iterations (plus possibly one more iteration if there's a final carry). 

Since each iteration involves constant-time operations (arithmetic operations, creating a new node, pointer updates),
the overall time complexity is: **O(max(n, m))**

### Space Complexity:

The function constructs a new linked list to represent the sum. The size of the new linked list is at most `max(n, m) + 1`
(in the case of a final carry).

- The space used for the new linked list is proportional to the number of digits in the sum, which is **O(max(n, m))**.

The auxiliary space used (variables like `carry`, `current_node`, etc.) is constant, so it doesn't affect the overall space complexity.

Thus, the space complexity is:
- **O(max(n, m))**, due to the new linked list created.

### Summary:
- **Time Complexity:** O(max(n, m))
- **Space Complexity:** O(max(n, m)) (for the new linked list)

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
This code defines and manipulates **linked lists** to perform **addition of two numbers**, where each number is represented by
a linked list, with **digits stored in reverse order**. Here's a step-by-step breakdown of how the code works:

---

## ✅ 1. **LinkedList Class**

```
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
```

* Defines a single **node** in a singly linked list.
* Each node holds:

  * `value`: A digit (e.g., 2, 4, etc.).
  * `next`: A reference to the next node (or `None` if it’s the end).

---

## ✅ 2. **build_linked_list(data)**

This function **constructs a linked list** from a dictionary representation.

```
def build_linked_list(data):
    ...
```

### Input format (example for `linkedList_one_data`):

```
{
    "head": "2",
    "nodes": [
        {"id": "2", "next": "4", "value": 2},
        {"id": "4", "next": "7", "value": 4},
        {"id": "7", "next": "1", "value": 7},
        {"id": "1", "next": None, "value": 1},
    ]
}
```

### How it works:

1. Creates a dictionary of all nodes using their IDs.
2. Connects the nodes using their `"next"` references.
3. Returns the node that corresponds to the `"head"`.

🔁 This allows us to build any linked list from structured data (helpful for testing).

---

## ✅ 3. **sum_of_linked_lists(linkedList_one, linkedList_two)**

This is the **main function** that adds two numbers represented by linked lists.

### Analogy:

If we represent numbers in **reverse** (least significant digit first), then:

```
Number 1 = 1 -> 7 -> 4 -> 2  (represents 1742)
Number 2 = 5 -> 4 -> 9       (represents 945)
```

### Goal:

Add them:

```
   1742
+   945
-------
   2687
```

Then return as: `7 -> 8 -> 6 -> 2`

### Code breakdown:

```
new_linked_list_head_pointer = LinkedList(0)
```

* Dummy node to simplify logic; final result is `dummy.next`.

```
carry = 0
```

* Store carry from digit addition (just like column-wise addition).

```
while node_one is not None or node_two is not None or carry != 0:
```

* Loop as long as there's a digit to process or a leftover carry.

Inside the loop:

```
value_one = node_one.value if node_one is not None else 0
value_two = node_two.value if node_two is not None else 0
sum_of_values = value_one + value_two + carry
```

* Pull the digit from each list (or 0 if list has ended).
* Add the carry.
* Calculate `new_value = sum_of_values % 10` (ones digit).
* Update carry: `carry = sum_of_values // 10` (tens digit).
* Create a new node with `new_value`, attach it.

At the end:

```
return new_linked_list_head_pointer.next
```

* Return actual result, skipping the dummy head.

---

## ✅ 4. **print_linked_list(linked_list)**

Utility function to print list in human-readable form.

---

## ✅ 5. **Test Cases**

### 🔹Test Case 1:

Linked List One: `2 -> 4 -> 7 -> 1` (represents 1742)
Linked List Two: `9 -> 4 -> 5` (represents 549)

```
   1742
+   549
-------
   2291
```

Should be printed as: `1 -> 9 -> 2 -> 2` ✅

### 🔹Test Case 2:

Adding `linked_list_one` to itself:

```
   1742
+  1742
-------
   3484
```

Should be printed as: `4 -> 8 -> 4 -> 2` ✅

---

## ✅ Summary of Concepts Involved

| Concept              | Explanation                                    |
| -------------------- | ---------------------------------------------- |
| Linked List          | A chain of nodes pointing to the next          |
| Reverse Order Digits | Least significant digit is at the head         |
| Carry Handling       | Used when digit sum > 9                        |
| Dummy Node           | Simplifies list creation and return            |
| Edge Handling        | Continues addition even if one list ends early |

---

Here's an **ASCII visualization** of how the **linked list addition** works, using **Test Case 1** (1742 + 549):

### 🧮 Input Numbers (in reverse order):

```
Linked List One (represents 1742):
2 -> 4 -> 7 -> 1 -> None   # means 1,742 (read right to left)

Linked List Two (represents 549):
9 -> 4 -> 5 -> None        # means 549 (read right to left)
```

---

### ➕ Addition Step by Step:

We add digit-by-digit from head to tail (like manual addition), carrying over as needed.

```
     2       4       7       1       (digits from Linked List One)
+    9       4       5       -       (digits from Linked List Two, padded with 0)
-------------------------------------------------
    11      8      12       1        (raw sum)
     1      9       2       2        (digit placed in result)
  carry→1   0       1       0
```

---

### 🔢 Final Result Linked List:

```
1 -> 9 -> 2 -> 2 -> None   # represents 2,291
```

---

### 🧠 Summary in Visual Format:

```
  LL1:     2 ->   4 ->   7 ->   1 -> None
  LL2:     9 ->   4 ->   5 ->   - -> None
         -------------------------------
Sum:     (11)   (8)    (12)   (1)
Digit:    1 ->   9 ->   2 ->   2 -> None
Carry:    1      0      1      0
```

"""
