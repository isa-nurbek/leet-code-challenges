# Problem Description:

"""
                                            Node Swap

Write a function that takes in the head of a Singly Linked List, swaps every pair of adjacent nodes in place (i.e., doesn't create
a brand new list), and returns its new head.

If the input Linked List has an odd number of nodes, its final node should remain the same.

Each `LinkedList` node has an integer `value` as well as a `next` node pointing to the next node in the list or to `None` if it's
the tail of the list.

You can assume that the input Linked List will always have at least one node; in other words, the head will never be `None`.


## Sample Input:
```
head = 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> None

// The head node with value 0
```

## Sample Output:
```
1 -> 0 -> 3 -> 2 -> 5 -> 4 -> None

// The new head node with value 1
```

## Optimal Time & Space Complexity:
```
O(n) time | O(1) space - where `n` is the number of nodes in the Linked List.
```

"""

# =========================================================================================================================== #

# Solution:


class LinkedList:
    def __init__(self, value):
        self.value = value  # Store the value of this node
        self.next = None  # Pointer to the next node (initially None)


# Helper function to convert dictionary to LinkedList
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
def node_swap(head):
    # Create a dummy node to serve as the new head's predecessor.
    # This helps handle edge cases where the original head is swapped.
    dummy = LinkedList(0)
    dummy.next = head
    prev = dummy  # 'prev' will track the node before the current pair

    while prev.next and prev.next.next:
        # There are at least two nodes left to swap
        first = prev.next  # First node in the pair to swap
        second = prev.next.next  # Second node in the pair to swap

        # Perform the swap:
        # 1. Connect previous node to the second node
        prev.next = second
        # 2. Connect first node to what comes after the second node
        first.next = second.next
        # 3. Connect second node back to the first node
        second.next = first

        # Move 'prev' forward to be before the next pair
        # (which is now the first node, since we just swapped)
        prev = first

    # Return the new head (what comes after dummy)
    return dummy.next


# Function to print the linked list (for verification)
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

# Build and print the linked list
linked_list = build_linked_list(linked_list_dict)

result = node_swap(linked_list)

print_linked_list(result)
# Output: 1 -> 0 -> 3 -> 2 -> 5 -> 4 -> None

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

Let's analyze the time and space complexity of the `node_swap` function, which swaps every two adjacent nodes in a linked list.

### Time Complexity:

- The function iterates through the linked list once, processing nodes in pairs.
- For each pair of nodes, it performs a constant number of operations (pointer updates).
- If the linked list has `n` nodes, the loop runs approximately `n/2` times (since we process two nodes at a time).
- Thus, the time complexity is **O(n)**, where `n` is the number of nodes in the linked list.

### Space Complexity:

- The function uses a constant amount of extra space (`dummy`, `prev`, `first`, and `second` pointers), regardless of the input size.
- No additional data structures or recursive calls are used.
- Thus, the space complexity is **O(1)** (constant space).

### Summary:
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

This is an efficient in-place algorithm for swapping adjacent nodes in a linked list.

"""
