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
        self.value = value
        self.next = None


def build_linked_list(data):
    if not data:
        return None

    nodes = {}
    for node_data in data["nodes"]:
        node = LinkedList(node_data["value"])
        nodes[node_data["id"]] = node

    for node_data in data["nodes"]:
        if node_data["next"] is not None:
            nodes[node_data["id"]].next = nodes[node_data["next"]]

    return nodes[data["head"]]


def zip_linkedList(linked_list):
    if linked_list.next is None or linked_list.next.next is None:
        return linked_list

    first_half_head = linked_list
    second_half_head = split_linkedList(linked_list)

    reversed_second_half_head = reverse_linkedList(second_half_head)
    return interweave_linkedLists(first_half_head, reversed_second_half_head)


def split_linkedList(linked_list):
    slow_iterator = linked_list
    fast_iterator = linked_list

    while fast_iterator is not None and fast_iterator.next is not None:
        slow_iterator = slow_iterator.next
        fast_iterator = fast_iterator.next.next

    second_half_head = slow_iterator.next
    slow_iterator.next = None

    return second_half_head


def interweave_linkedLists(linked_list_1, linked_list_2):
    linked_list_1_iterator = linked_list_1
    linked_list_2_iterator = linked_list_2

    while linked_list_1_iterator is not None and linked_list_2_iterator is not None:
        # Save next pointers
        linked_list_1_next = linked_list_1_iterator.next
        linked_list_2_next = linked_list_2_iterator.next

        # Link current nodes
        linked_list_1_iterator.next = linked_list_2_iterator
        if linked_list_1_next is not None:
            linked_list_2_iterator.next = linked_list_1_next

        # Move to next nodes
        linked_list_1_iterator = linked_list_1_next
        linked_list_2_iterator = linked_list_2_next

    return linked_list_1


def reverse_linkedList(linked_list):
    previous_node, current_node = None, linked_list

    while current_node is not None:
        next_node = current_node.next
        current_node.next = previous_node

        previous_node = current_node
        current_node = next_node

    return previous_node


def print_linked_list(linked_list):
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

linked_list = build_linked_list(linked_list_dict)

result = zip_linkedList(linked_list)

print_linked_list(result)
# Output: 1 -> 6 -> 2 -> 5 -> 3 -> 4 -> None
