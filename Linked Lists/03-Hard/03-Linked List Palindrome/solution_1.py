# Problem Description:

"""
                                            Linked List Palindrome

Write a function that takes in the head of a Singly Linked List and returns a `boolean` representing whether the linked list's
nodes form a palindrome. Your function shouldn't make use of any auxiliary data structure.

A palindrome is usually defined as a string that's written the same `forward` and `backward`. For a linked list's nodes to form
a palindrome, their values must be the same when read from left to right and from right to left.
> Note that single-character strings are palindromes, which means that single-node linked lists form palindromes.

Each `LinkedList` node has an integer `value` as well as a `next` node pointing to the next node in the list or to `None` if it's
the tail of the list.

You can assume that the input linked list will always have at least one node; in other words, the head will never be `None`.


## Sample Input:
```
head = 0 -> 1 -> 2 -> 2 -> 1 -> 0 -> None

// The head node with value 0
```

## Sample Output:
```
True
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


# O(n) time | O(n) space
def linkedList_palindrome(head):
    is_palindrome_results = is_palindrome(head, head)
    return is_palindrome_results.outer_nodes_are_equal


def is_palindrome(left_node, right_node):
    if right_node is None:
        return LinkedListInfo(True, left_node)

    recursive_call_results = is_palindrome(left_node, right_node.next)
    left_node_to_compare = recursive_call_results.left_node_to_compare
    outer_nodes_are_equal = recursive_call_results.outer_nodes_are_equal

    recursive_is_equal = (
        outer_nodes_are_equal and left_node_to_compare.value == right_node.value
    )
    next_left_node_to_compare = left_node_to_compare.next

    return LinkedListInfo(recursive_is_equal, next_left_node_to_compare)


class LinkedListInfo:
    def __init__(self, outer_nodes_are_equal, left_node_to_compare):
        self.outer_nodes_are_equal = outer_nodes_are_equal
        self.left_node_to_compare = left_node_to_compare


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
        {"id": "2", "next": "2-2", "value": 2},
        {"id": "2-2", "next": "1-2", "value": 2},
        {"id": "1-2", "next": "0-2", "value": 1},
        {"id": "0-2", "next": None, "value": 0},
    ],
}

# Test Case:

# Build and print the linked list
linked_list = build_linked_list(linked_list_dict)

print("Linked list:")
print_linked_list(linked_list)

# Check if palindrome
is_palindrome = linkedList_palindrome(linked_list)
print("\nIs palindrome?", is_palindrome)

# Output:

"""
Linked list:
0 -> 1 -> 2 -> 2 -> 1 -> 0 -> None

Is palindrome? True

"""
