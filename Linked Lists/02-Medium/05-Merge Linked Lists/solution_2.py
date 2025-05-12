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
    """
    Merges two sorted linked lists into one sorted linked list.

    Args:
        head_one: Head node of the first sorted linked list
        head_two: Head node of the second sorted linked list

    Returns:
        Head node of the merged sorted linked list
    """

    # Edge case: If one list is empty, return the other
    if head_one is None:
        return head_two
    if head_two is None:
        return head_one

    # Determine which head should be the new head (the smaller one)
    if head_one.value < head_two.value:
        # Merge with head_one as the starting node
        recursive_merge(head_one, head_two, None)
        return head_one
    else:
        # Merge with head_two as the starting node
        recursive_merge(head_two, head_one, None)
        return head_two


def recursive_merge(p1, p2, p1_prev):
    """
    Recursively merges two linked lists by rearranging their nodes in sorted order.

    Args:
        p1: Current node from the primary list (the list we're merging into)
        p2: Current node from the secondary list (the list we're merging from)
        p1_prev: Previous node from the primary list (used to rewire pointers)
    """

    # Base case: If we've reached end of primary list, attach rest of secondary list
    if p1 is None:
        p1_prev.next = p2
        return

    # Base case: If we've reached end of secondary list, we're done
    if p2 is None:
        return

    if p1.value < p2.value:
        # p1 is smaller, keep it and move forward in primary list
        recursive_merge(p1.next, p2, p1)
    else:
        # p2 is smaller, we need to insert it before p1

        # First save p2's next node before we overwrite it
        new_p2 = p2.next

        # If there was a previous node in primary list, rewire it to point to p2
        if p1_prev is not None:
            p1_prev.next = p2

        # Insert p2 before p1 in the merged list
        p2.next = p1

        # Continue merging with p1 in its new position and new_p2 as next in secondary list
        recursive_merge(p1, new_p2, p2)


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
