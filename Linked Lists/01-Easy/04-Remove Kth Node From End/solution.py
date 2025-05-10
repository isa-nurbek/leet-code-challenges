# Problem Description:

"""
                                            Remove `K`th Node From End

Write a function that takes in the head of a `Singly Linked List` and an integer `k` and removes the kth node from the end of
the list.

The removal should be done in place, meaning that the original data structure should be mutated (no new structure should be created).

Furthermore, the input head of the linked list should remain the head of the linked list after the removal is done, even if the head
is the node that's supposed to be removed. In other words, if the head is the node that's supposed to be removed, your function
should simply mutate its `value` and `next` pointer.

> Note that your function doesn't need to return anything.

You can assume that the input Linked List will always have at least two nodes and, more specifically, at least k nodes.

Each `LinkedList` node has an integer `value` as well as a `next` node pointing to the next node in the list or to `None` if it's
the tail of the list.

## Sample Input:
```
head = 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> None
k = 4
```

## Sample Output:
```
// No output required
// The 4th node from the end of the list (the node with value 6) is removed.

0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 7 -> 8 -> 9 -> None
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


# Function to remove kth node from end
# O(n) time | O(1) space
def remove_kth_node_from_end(head, k):
    # Initialize two pointers, both starting at the head of the linked list
    counter = 1
    first = head  # This will eventually point to the node BEFORE the one to remove
    second = head  # This will be used to create the proper distance between pointers

    # Move the second pointer k nodes ahead of the first pointer
    while counter <= k:
        second = second.next
        counter += 1

    # If second has reached the end (None), this means we need to remove the head
    if second is None:
        # Copy the value from the next node to effectively remove the head
        head.value = head.next.value
        # Skip over the next node (which now has the head's original value)
        head.next = head.next.next
        return  # Early return since we've handled the special case

    # Move both pointers until second reaches the last node
    # This maintains the k node gap between them
    while second.next is not None:
        second = second.next
        first = first.next

    # Now first points to the node before the one to remove
    # Skip over the kth node from end by pointing first.next to first.next.next
    first.next = first.next.next


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

# Remove 4th node from end
remove_kth_node_from_end(linked_list, 4)  # This modifies the linked_list in place

# Print the modified linked list
print_linked_list(linked_list)
# Output: 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 7 -> 8 -> 9 -> None
