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
    list_length = 1
    list_tail = head

    while list_tail.next is not None:
        list_tail = list_tail.next
        list_length += 1

    offset = abs(k) % list_length
    if offset == 0:
        return head

    new_tail_position = list_length - offset if k > 0 else offset
    new_tail = head

    for _ in range(1, new_tail_position):
        new_tail = new_tail.next

    new_head = new_tail.next
    new_tail.next = None

    list_tail.next = head
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
