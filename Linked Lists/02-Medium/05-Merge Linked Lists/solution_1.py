# Problem Description:

"""
                                            Merge Linked Lists

Write a function that takes in the heads of two Singly Linked Lists that are in `sorted order`, respectively. The function should
merge the lists in place (i.e., it shouldn't create a brand new list) and return the head of the merged list; the merged list
should be in `sorted order`.

Each `LinkedList` node has an integer `value` as well as a `next` node pointing to the next node in the list or to `None` if it's
the tail of the list.

You can assume that the input linked lists will always have at least one node; in other words, the heads will never be `None`.


## Sample Input:
```
head_one = 2 -> 6 -> 7 -> 8 -> None              // the head node with value 2
head_two = 1 -> 3 -> 4 -> 5 -> 9 -> 10 -> None   // the head node with value 1
```

## Sample Output:
```
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> None  // the new head node with value 1
```

## Optimal Time & Space Complexity:
```
O(n + m) time | O(1) space - where `n` is the number of nodes in the first Linked List and
`m` is the number of nodes in the second Linked List.

```

"""

# =========================================================================================================================== #

# Solution:


class LinkedList:
    """Node class for a singly linked list."""

    def __init__(self, value):
        self.value = value  # Value stored in the node
        self.next = None  # Pointer to the next node (initially None)


def build_linked_list(data):
    """Builds a linked list from a dictionary representation.

    Args:
        data: Dictionary with 'head' (id of head node) and 'nodes' (list of node dicts).

    Returns:
        The head node of the constructed linked list, or None if data is empty.
    """
    if not data:
        return None

    # Create all nodes and store them in a dictionary by ID
    nodes = {}
    for node_data in data["nodes"]:
        node = LinkedList(node_data["value"])
        nodes[node_data["id"]] = node

    # Connect nodes using 'next' pointers
    for node_data in data["nodes"]:
        if node_data["next"] is not None:
            nodes[node_data["id"]].next = nodes[node_data["next"]]

    return nodes[data["head"]]  # Return the head node


def merge_linked_lists(head_one, head_two):
    """Merges two sorted linked lists into a single sorted list in-place.

    Args:
        head_one: Head node of the first sorted linked list.
        head_two: Head node of the second sorted linked list.

    Returns:
        The head node of the merged linked list.
    """
    # Edge case: If one list is empty, return the other
    if head_one is None:
        return head_two
    if head_two is None:
        return head_one

    # Initialize pointers
    p1 = head_one  # Pointer for the first list
    p2 = head_two  # Pointer for the second list
    merged_head = head_one if head_one.value < head_two.value else head_two

    # Traverse both lists and merge them
    prev = None  # Tracks the last node in the merged list
    while p1 is not None and p2 is not None:
        if p1.value < p2.value:
            if prev is not None:
                prev.next = p1
            prev = p1
            p1 = p1.next
        else:
            if prev is not None:
                prev.next = p2
            prev = p2
            p2 = p2.next

    # Attach remaining nodes (if any)
    if p1 is not None:
        prev.next = p1
    else:
        prev.next = p2

    return merged_head


def print_linked_list(head):
    """Prints the linked list in a readable format.

    Args:
        head: The head node of the linked list to print.
    """
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")


# Test Case 1: Two non-empty sorted lists
linked_list_dict_one = {
    "head": "2",
    "nodes": [
        {"id": "2", "next": "6", "value": 2},
        {"id": "6", "next": "7", "value": 6},
        {"id": "7", "next": "8", "value": 7},
        {"id": "8", "next": None, "value": 8},
    ],
}

linked_list_dict_two = {
    "head": "1",
    "nodes": [
        {"id": "1", "next": "3", "value": 1},
        {"id": "3", "next": "4", "value": 3},
        {"id": "4", "next": "5", "value": 4},
        {"id": "5", "next": "9", "value": 5},
        {"id": "9", "next": "10", "value": 9},
        {"id": "10", "next": None, "value": 10},
    ],
}

# Build and merge the lists
list_one = build_linked_list(linked_list_dict_one)
list_two = build_linked_list(linked_list_dict_two)
merged_list = merge_linked_lists(list_one, list_two)

print("Merged List:")
print_linked_list(merged_list)
# Merged List: 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 → 10 → None

# Test Case 2: One list is empty
empty_list = None
merged_with_empty = merge_linked_lists(empty_list, list_two)

print("\nMerged with Empty List:")
print_linked_list(merged_with_empty)
# Merged with Empty List: 1 → 3 → 4 → 5 → 9 → 10 → None
