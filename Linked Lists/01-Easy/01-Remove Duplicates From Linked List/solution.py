# Problem Description:

"""
                                            # Remove Duplicates From Linked List

You're given the head of a Singly Linked List whose nodes are in sorted order with respect to their values. Write a function that returns a modified version of the Linked List that doesn't contain any nodes with duplicate values. The Linked List should be modified in place (i.e., you shouldn't create a brand new list), and the modified Linked List should still have its nodes sorted with respect to their values.

Each `LinkedList` node has an integer `value` as well as a `next` node pointing to the next node in the list or to `None` / `null` if it's the tail of the list.


## Sample Input:
```
linked_list = {
    "head": "1",
    "nodes": [
        {"id": "1", "next": "1-2", "value": 1},
        {"id": "1-2", "next": "1-3", "value": 1},
        {"id": "1-3", "next": "2", "value": 1},
        {"id": "2", "next": "3", "value": 3},
        {"id": "3", "next": "3-2", "value": 4},
        {"id": "3-2", "next": "3-3", "value": 4},
        {"id": "3-3", "next": "4", "value": 4},
        {"id": "4", "next": "5", "value": 5},
        {"id": "5", "next": "5-2", "value": 6},
        {"id": "5-2", "next": None, "value": 6},
    ],
}

The List Looks Like: [1] -> [1] -> [3] -> [4] -> [4] -> [4] -> [5] -> [6] -> [6] -> None // the head node with value 1
```

## Sample Output:
```
1 -> 3 -> 4 -> 5 -> 6 -> None // the head node with value 1
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
# O(n) time | O(1) space
def remove_duplicates_from_linked_list(linked_list):
    """Removes consecutive duplicate values from a sorted linked list in-place.

    Args:
        linked_list: The head node of the linked list to process

    Returns:
        The head node of the modified linked list
    """
    current_node = linked_list
    while current_node is not None:
        # Find the next node with a different value
        next_distinct_node = current_node.next
        while (
            next_distinct_node is not None
            and next_distinct_node.value == current_node.value
        ):
            next_distinct_node = next_distinct_node.next

        # Skip over all duplicates and point to the next distinct node
        current_node.next = next_distinct_node

        # Move to the next distinct node for next iteration
        current_node = next_distinct_node

    return linked_list  # Return the head of the modified list


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
linked_list_dict = {
    "head": "1",
    "nodes": [
        {"id": "1", "next": "1-2", "value": 1},
        {"id": "1-2", "next": "1-3", "value": 1},
        {"id": "1-3", "next": "2", "value": 1},
        {"id": "2", "next": "3", "value": 3},
        {"id": "3", "next": "3-2", "value": 4},
        {"id": "3-2", "next": "3-3", "value": 4},
        {"id": "3-3", "next": "4", "value": 4},
        {"id": "4", "next": "5", "value": 5},
        {"id": "5", "next": "5-2", "value": 6},
        {"id": "5-2", "next": None, "value": 6},
    ],
}

# Test Case:

# Build the linked list from dictionary
linked_list = build_linked_list(linked_list_dict)

# Remove duplicates
result = remove_duplicates_from_linked_list(linked_list)

print_linked_list(result)
# Output: 1 -> 3 -> 4 -> 5 -> 6 -> None

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

Let's analyze the time and space complexity of the `remove_duplicates_from_linked_list` function.

### Time Complexity:

The function processes each node in the linked list exactly once in the outer while loop. For each node, it may also
traverse some subsequent nodes in the inner while loop to skip duplicates. 

In the worst case (when all nodes are unique), the inner loop doesn't do any work (just one comparison per node),
resulting in O(n) time. 

In the case where there are many duplicates, each node is still only processed once by either the outer or inner loop. 
For example, if all nodes are the same value, the inner loop will traverse all nodes once, and the outer loop will only run once.

Thus, the time complexity is **O(n)**, where n is the number of nodes in the linked list.

### Space Complexity:

The function uses a constant amount of additional space (only a few pointers like `current_node` and `next_distinct_node` are used).
It modifies the linked list in-place without using any additional data structures that grow with input size.

Thus, the space complexity is **O(1)** (constant space).

### Summary:
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

"""
