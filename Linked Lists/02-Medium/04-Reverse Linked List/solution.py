# Problem Description:

"""
                                            Reverse Linked List

Write a function that takes in the head of a Singly Linked List, reverses the list in place (i.e., doesn't create a brand new list),
and returns its new head.

Each `LinkedList` node has an integer `value` as well as a `next` node pointing to the next node in the list or to `None` if it's
the tail of the list.

You can assume that the input Linked List will always have at least one node; in other words, the head will never be `None`.


## Sample Input:
```
// The head node with value 0

head = 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> None
```

## Sample Output:
```
5 -> 4 -> 3 -> 2 -> 1 -> 0 -> None

// The new head node with value 5
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
def reverse_linked_list(head):
    """Reverse a singly linked list.

    Args:
        head: The head node of the linked list to be reversed

    Returns:
        The new head node of the reversed linked list
    """

    # Initialize two pointers:
    # previous_node will track the node before current_node in the original list
    # current_node starts at the head of the original list
    previous_node, current_node = None, head

    # Traverse through the original list
    while current_node is not None:
        # Store the next node before we overwrite current_node.next
        next_node = current_node.next

        # Reverse the link by pointing current_node's next to the previous node
        current_node.next = previous_node

        # Move both pointers forward in their respective directions:
        # previous_node moves to current position
        # current_node moves to the next node we stored earlier
        previous_node = current_node
        current_node = next_node

    # When the loop ends, current_node is None and previous_node is the last node,
    # which is now the head of the reversed list
    return previous_node


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

# Test Case:

# Build the linked list from dictionary
linked_list = build_linked_list(linked_list_dict)

# Remove duplicates
result = reverse_linked_list(linked_list)

print_linked_list(result)
# Output: 5 -> 4 -> 3 -> 2 -> 1 -> 0 -> None

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

Let's analyze the time and space complexity of the given `reverse_linked_list` function.

### Time Complexity:

The function iterates through each node in the linked list exactly once. For each node, it performs a constant amount of
work (updating pointers). 

- If the linked list has `n` nodes, the time complexity is **O(n)**.

### Space Complexity:

The function uses a fixed number of additional variables (`previous_node`, `current_node`, `next_node`), regardless of the size of
the input linked list. No additional data structures or recursive calls are used.

- Thus, the space complexity is **O(1)** (constant space).

### Summary:
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
Here's a **detailed explanation** of the code you provided, breaking it down into its parts and describing how it all works together:

---

## 🔷 Part 1: The `LinkedList` Class

```
class LinkedList:
    def __init__(self, value):
        self.value = value  # Store the value of this node
        self.next = None    # Pointer to the next node (initially None)
```

* This class defines a **node** of a singly linked list.
* Each node contains:

  * `value`: the actual data stored in the node.
  * `next`: a reference (pointer) to the **next node** in the list, initially set to `None`.

---

## 🔷 Part 2: `build_linked_list(data)` Function

This function **builds a linked list** from a dictionary input.

### Input:

```
{
    "head": "0",
    "nodes": [
        {"id": "0", "next": "1", "value": 0},
        {"id": "1", "next": "2", "value": 1},
        ...
    ]
}
```

### Step-by-step:

```
if not data:
    return None
```

* Handles empty input by returning `None`.

```
nodes = {}
for node_data in data["nodes"]:
    node = LinkedList(node_data["value"])
    nodes[node_data["id"]] = node
```

* Creates `LinkedList` objects for each node in the input.
* Uses a dictionary (`nodes`) to map each node's `"id"` to its corresponding object.

```
for node_data in data["nodes"]:
    if node_data["next"] is not None:
        nodes[node_data["id"]].next = nodes[node_data["next"]]
```

* Iterates again to **connect nodes** by setting the `next` pointers using the `"next"` field in the input.

```
return nodes[data["head"]]
```

* Returns the **head node** (starting point) using the `"head"` ID.

---

## 🔷 Part 3: `reverse_linked_list(head)` Function

This function **reverses** the linked list **in-place**.

### Logic:

It uses three pointers:

* `previous_node` (starts as `None`)
* `current_node` (starts at the head of the list)
* `next_node` (temporarily holds the next node)

```
while current_node is not None:
    next_node = current_node.next         # Step 1: Store next node
    current_node.next = previous_node     # Step 2: Reverse the pointer
    previous_node = current_node          # Step 3: Move previous forward
    current_node = next_node              # Step 4: Move current forward
```

At each step, the current node’s `next` is redirected to the previous node, effectively reversing the link direction.

```
return previous_node
```

At the end, `previous_node` will point to the **new head** of the reversed list.

---

## 🔷 Part 4: `print_linked_list(linked_list)` Function

A helper function to **print the list** in human-readable format.

```
while current:
    print(current.value, end=" -> ")
    current = current.next
print("None")
```

---

## 🔷 Final Execution Flow

```
linked_list = build_linked_list(linked_list_dict)
result = reverse_linked_list(linked_list)
print_linked_list(result)
```

### What happens here:

1. The dictionary is used to **build a linked list**:
   `0 -> 1 -> 2 -> 3 -> 4 -> 5 -> None`

2. `reverse_linked_list()` is called to reverse the list.

3. The final list becomes:
   `5 -> 4 -> 3 -> 2 -> 1 -> 0 -> None`

---

## ✅ Summary

| Component               | Purpose                                                       |
| ----------------------- | ------------------------------------------------------------- |
| `LinkedList` class      | Defines a single node with `value` and `next`                 |
| `build_linked_list()`   | Constructs the entire linked list from a dictionary           |
| `reverse_linked_list()` | Reverses the linked list in-place in O(n) time and O(1) space |
| `print_linked_list()`   | Traverses and prints the linked list for visualization        |

"""
