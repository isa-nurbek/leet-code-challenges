# Problem Description:

"""
                                            Zip Linked List

You're given the head of a Singly Linked List of arbitrary length `k`. Write a function that zips the Linked List in place (i.e.,
doesn't create a brand new list) and returns its head.

A Linked List is zipped if its nodes are in the following order, where `k` is the length of the Linked List:

```
1st node -> kth node -> 2nd node -> (k - 1)th node -> 3rd node -> (k - 2)th node -> ...
```

Each `LinkedList` node has an integer `value` as well as a `next` node pointing to the next node in the list or to `None` if it's
the tail of the list.

You can assume that the input Linked List will always have at least one node; in other words, the head will never be `None`.


## Sample Input:
```
linked_list = 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None

// The head node with value 1
```

## Sample Output:
```
1 -> 6 -> 2 -> 5 -> 3 -> 4 -> None

// The head node with value 1
```

## Optimal Time & Space Complexity:
```
O(n) time | O(1) space - where `n` is the length of the input Linked List.
```

"""

# =========================================================================================================================== #

# Solution:


class LinkedList:
    def __init__(self, value):
        self.value = value  # Store the value of this node
        self.next = None  # Pointer to the next node (initially None)


def build_linked_list(data):
    """Builds a linked list from dictionary representation.

    Args:
        data: Dictionary containing 'head' id and 'nodes' list with each node's
              id, value, and next node id.

    Returns:
        The head node of the constructed linked list.
    """
    if not data:
        return None

    # First create all nodes and store them in a dictionary by id
    nodes = {}
    for node_data in data["nodes"]:
        node = LinkedList(node_data["value"])
        nodes[node_data["id"]] = node

    # Then connect the nodes by setting next pointers
    for node_data in data["nodes"]:
        if node_data["next"] is not None:
            nodes[node_data["id"]].next = nodes[node_data["next"]]

    return nodes[data["head"]]


# O(n) time | O(1) space
def zip_linkedList(linked_list):
    """Zips a linked list in place by interleaving first half with reversed second half.

    Example: 1->2->3->4->5->6 becomes 1->6->2->5->3->4

    Args:
        linked_list: Head node of the linked list to zip.

    Returns:
        The head of the zipped linked list.
    """
    # Base case: list is too short to zip
    if linked_list.next is None or linked_list.next.next is None:
        return linked_list

    # Split the list into two halves
    first_half_head = linked_list
    second_half_head = split_linkedList(linked_list)

    # Reverse the second half
    reversed_second_half_head = reverse_linkedList(second_half_head)

    # Interweave the two halves
    return interweave_linkedLists(first_half_head, reversed_second_half_head)


def split_linkedList(linked_list):
    """Splits a linked list into two halves using slow/fast pointer technique.

    Args:
        linked_list: Head node of the linked list to split.

    Returns:
        The head node of the second half.
    """
    slow_iterator = linked_list
    fast_iterator = linked_list

    # Fast pointer moves twice as fast as slow pointer
    while fast_iterator is not None and fast_iterator.next is not None:
        slow_iterator = slow_iterator.next
        fast_iterator = fast_iterator.next.next

    # When fast reaches end, slow is at midpoint
    second_half_head = slow_iterator.next
    slow_iterator.next = None  # Terminate first half

    return second_half_head


def interweave_linkedLists(linked_list_1, linked_list_2):
    """Interweaves two linked lists by alternating nodes from each list.

    Args:
        linked_list_1: Head node of first linked list.
        linked_list_2: Head node of second linked list.

    Returns:
        The head node of the interwoven list (linked_list_1 will be first node).
    """
    linked_list_1_iterator = linked_list_1
    linked_list_2_iterator = linked_list_2

    while linked_list_1_iterator is not None and linked_list_2_iterator is not None:
        # Save next pointers before we overwrite them
        linked_list_1_next = linked_list_1_iterator.next
        linked_list_2_next = linked_list_2_iterator.next

        # Link current node from first list to current node of second list
        linked_list_1_iterator.next = linked_list_2_iterator

        # Only link second list node to next first list node if it exists
        if linked_list_1_next is not None:
            linked_list_2_iterator.next = linked_list_1_next

        # Move to next nodes in each list
        linked_list_1_iterator = linked_list_1_next
        linked_list_2_iterator = linked_list_2_next

    return linked_list_1


def reverse_linkedList(linked_list):
    """Reverses a linked list in place.

    Args:
        linked_list: Head node of the linked list to reverse.

    Returns:
        The new head node of the reversed list.
    """
    previous_node, current_node = None, linked_list

    while current_node is not None:
        next_node = current_node.next  # Save next node before overwriting
        current_node.next = previous_node  # Reverse the link

        # Move pointers forward
        previous_node = current_node
        current_node = next_node

    return previous_node  # New head of reversed list


def print_linked_list(linked_list):
    """Prints a linked list in arrow format.

    Args:
        linked_list: Head node of the linked list to print.
    """
    current = linked_list
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")


# Test case
linked_list_dict = {
    "head": "1",
    "nodes": [
        {"id": "1", "next": "2", "value": 1},
        {"id": "2", "next": "3", "value": 2},
        {"id": "3", "next": "4", "value": 3},
        {"id": "4", "next": "5", "value": 4},
        {"id": "5", "next": "6", "value": 5},
        {"id": "6", "next": None, "value": 6},
    ],
}

# Build, zip, and print the linked list
linked_list = build_linked_list(linked_list_dict)

result = zip_linkedList(linked_list)

print_linked_list(result)
# Correct output: 1 -> 6 -> 2 -> 5 -> 3 -> 4 -> None
