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
