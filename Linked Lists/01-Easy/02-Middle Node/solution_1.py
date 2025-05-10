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
    count = 0
    current_node = linked_list

    while current_node is not None:
        count += 1
        current_node = current_node.next

    middle_node = linked_list

    for _ in range(count // 2):
        middle_node = middle_node.next

    return middle_node


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
