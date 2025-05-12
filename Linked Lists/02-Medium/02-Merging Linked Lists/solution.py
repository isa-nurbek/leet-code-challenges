# Problem Description:

"""
                                            Merging Linked Lists

You're given two Linked Lists of potentially unequal length. These Linked Lists potentially merge at a shared intersection node.
Write a function that returns the intersection node or returns `None` if there is no intersection.

Each `LinkedList` node has an integer `value` as well as a `next` node pointing to the next node in the list or to `None` if it's
the tail of the list.

> Note: Your function should return an existing node. It should not modify either Linked List, and it should not create any new
Linked Lists.


## Sample Input:
```
linkedList_one = 2 -> 3 -> 1 -> 4 -> None
linkedList_two = 8 -> 7 -> 1 -> 4 -> None
```

## Sample Output:
```
1 -> 4 -> None

// The lists intersect at the node with value 1
```

## Optimal Time & Space Complexity:
```
O(n + m) time | O(1) space - where `n` is the length of the first Linked List and `m` is the length of the second Linked List.
```

"""

# =========================================================================================================================== #

# Solution:


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def build_intersected_linked_lists(list_one_data, list_two_data):
    """Builds two linked lists that may intersect, ensuring shared nodes are the same object."""
    if not list_one_data or not list_two_data:
        return None, None

    all_nodes = {}

    # Process list_one_data
    for node_data in list_one_data["nodes"]:
        if node_data["id"] not in all_nodes:
            all_nodes[node_data["id"]] = LinkedList(node_data["value"])

    # Process list_two_data (reuse nodes if IDs overlap)
    for node_data in list_two_data["nodes"]:
        if node_data["id"] not in all_nodes:
            all_nodes[node_data["id"]] = LinkedList(node_data["value"])

    # Connect nodes for list_one
    for node_data in list_one_data["nodes"]:
        if node_data["next"] is not None:
            all_nodes[node_data["id"]].next = all_nodes[node_data["next"]]

    # Connect nodes for list_two
    for node_data in list_two_data["nodes"]:
        if node_data["next"] is not None:
            all_nodes[node_data["id"]].next = all_nodes[node_data["next"]]

    return all_nodes[list_one_data["head"]], all_nodes[list_two_data["head"]]


def merging_linked_lists(linked_list_one, linked_list_two):
    def get_length(head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length

    len_one = get_length(linked_list_one)
    len_two = get_length(linked_list_two)

    current_one = linked_list_one
    current_two = linked_list_two

    # Move the longer list's pointer forward
    if len_one > len_two:
        for _ in range(len_one - len_two):
            current_one = current_one.next
    else:
        for _ in range(len_two - len_one):
            current_two = current_two.next

    # Traverse both lists in parallel
    while current_one and current_two:
        if current_one == current_two:
            return current_one
        current_one = current_one.next
        current_two = current_two.next

    return None


def print_linked_list(linked_list):
    current = linked_list
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")


# Input data
linkedList_one_data = {
    "head": "1",
    "nodes": [
        {"id": "1", "next": "2", "value": 1},
        {"id": "2", "next": "3", "value": 2},
        {"id": "3", "next": None, "value": 3},
    ],
}

linkedList_two_data = {
    "head": "4",
    "nodes": [
        {"id": "4", "next": "5", "value": 4},
        {"id": "5", "next": "3", "value": 5},
        {"id": "3", "next": None, "value": 3},
    ],
}

# New test case: 2->3->1->4 and 8->7->1->4 (intersect at 1->4)
linkedList_three_data = {
    "head": "2",
    "nodes": [
        {"id": "2", "next": "3", "value": 2},
        {"id": "3", "next": "1", "value": 3},
        {"id": "1", "next": "4", "value": 1},
        {"id": "4", "next": None, "value": 4},
    ],
}

linkedList_four_data = {
    "head": "8",
    "nodes": [
        {"id": "8", "next": "7", "value": 8},
        {"id": "7", "next": "1", "value": 7},
        {"id": "1", "next": "4", "value": 1},
        {"id": "4", "next": None, "value": 4},
    ],
}

# Build the linked lists with shared nodes
ll1, ll2 = build_intersected_linked_lists(linkedList_one_data, linkedList_two_data)
ll3, ll4 = build_intersected_linked_lists(linkedList_three_data, linkedList_four_data)

# Test case 1
print("Original test case:")
result1 = merging_linked_lists(ll1, ll2)
if result1:
    print(f"Intersection at node with value: {result1.value}")
    print("Intersected list:")
    print_linked_list(result1)
else:
    print("No intersection found")

# Test case 2
print("\nNew test case (2->3->1->4 and 8->7->1->4):")
result2 = merging_linked_lists(ll3, ll4)
if result2:
    print(f"Intersection at node with value: {result2.value}")
    print("Intersected list:")
    print_linked_list(result2)
else:
    print("No intersection found")

# Output:

"""
Original test case:
Intersection at node with value: 3
Intersected list:
3 -> None

New test case (2->3->1->4 and 8->7->1->4):
Intersection at node with value: 1
Intersected list:
1 -> 4 -> None

"""
