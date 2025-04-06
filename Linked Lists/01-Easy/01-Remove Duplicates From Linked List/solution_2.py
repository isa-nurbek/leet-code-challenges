# Problem Description:

"""
                                            # Remove Duplicates From Linked List

You're given the head of a Singly Linked List whose nodes are in sorted/unsorted order with respect to their values. Write a
function that returns a modified version of the Linked List that doesn't contain any nodes with duplicate values. The Linked List
should be modified in place (i.e., you shouldn't create a brand new list), and the modified Linked List should still have its
nodes sorted/unsorted with respect to their values.

Each `LinkedList` node has an integer `value` as well as a `next` node pointing to the next node in the list or to `None` / `null`
if it's the tail of the list.


## Sample Input Unsorted Linked List:
```
unsorted_linked_list_dict = {
    "head": "a",
    "nodes": [
        {"id": "a", "next": "b", "value": 3},
        {"id": "b", "next": "c", "value": 1},
        {"id": "c", "next": "d", "value": 4},
        {"id": "d", "next": "e", "value": 1},
        {"id": "e", "next": "f", "value": 5},
        {"id": "f", "next": "g", "value": 3},
        {"id": "g", "next": None, "value": 2},
    ],
}


The List Looks Like: [3] → [1] → [4] → [1] → [5] → [3] → [2] → None  // the head node with value 3
```

## Sample Output Unsorted Linked List:
```
3 -> 1 -> 4 -> 5 -> 2 -> None  // the head node with value 3
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


# Function to remove duplicates
# O(n) time | O(n) space
def remove_duplicates_unsorted(linked_list):
    # Initialize a set to keep track of seen values
    seen = set()

    # Initialize pointers:
    # - current: starts at head of linked list, will traverse through nodes
    # - prev: will always point to the node before current
    current = linked_list
    prev = None

    # Traverse through the entire linked list
    while current:
        # Check if current node's value has been seen before
        if current.value in seen:
            # Duplicate found - skip/remove this node by:
            # 1. Linking prev.next to current.next (bypassing current node)
            # 2. Not updating prev (since we removed current)
            prev.next = current.next
        else:
            # New unique value found:
            # 1. Add value to seen set for future reference
            # 2. Update prev to current (since we're keeping this node)
            seen.add(current.value)
            prev = current

        # Move to next node in the list
        current = current.next

    # Return the modified linked list (with duplicates removed)
    return linked_list


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


# Your input data
unsorted_linked_list_dict = {
    "head": "a",
    "nodes": [
        {"id": "a", "next": "b", "value": 3},
        {"id": "b", "next": "c", "value": 1},
        {"id": "c", "next": "d", "value": 4},
        {"id": "d", "next": "e", "value": 1},
        {"id": "e", "next": "f", "value": 5},
        {"id": "f", "next": "g", "value": 3},
        {"id": "g", "next": None, "value": 2},
    ],
}

# Test Case:

# Build the linked list from dictionary
unsorted_linked_list = build_linked_list(unsorted_linked_list_dict)

# Remove duplicates
deduped_unsorted_list = remove_duplicates_unsorted(unsorted_linked_list)

# Print the result
print_linked_list(deduped_unsorted_list)
# Output: 3 -> 1 -> 4 -> 5 -> 2 -> None

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

Let's analyze the time and space complexity of the `remove_duplicates_unsorted` function for an unsorted linked list.

### Time Complexity:
- The function iterates through each node of the linked list exactly once. If the linked list has `n` nodes,
this is an `O(n)` operation.
- For each node, it checks if the value exists in a set (`seen`). Set operations (`in` check and `add`) are
average-case `O(1)` in Python (due to hashing).

- Therefore, the total time complexity is **`O(n)`** (linear time).

### Space Complexity:
- The function uses a set (`seen`) to keep track of unique values encountered.
- In the worst case, if all values in the linked list are unique, the set will store all `n` values.

- Thus, the space complexity is **`O(n)`** (linear space).

### Summary:
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

This is optimal for an unsorted linked list since you need to track seen values to detect duplicates efficiently. If you were
allowed to sort the list first, you could reduce the space complexity to `O(1)` (using an in-place algorithm), but that would
require modifying the original list's order.

"""
