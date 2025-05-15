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


# O(n) time | O(n) space
def node_swap(head):
    """
    Swaps every pair of adjacent nodes in a linked list and returns the new head.
    For example: 1->2->3->4 becomes 2->1->4->3

    Args:
    head: The head node of the linked list

    Returns:
    The new head of the modified linked list after swapping pairs
    """

    # Base case: if list is empty or has only one node, return head as no swap needed
    if head is None or head.next is None:
        return head

    # Store the next node (this will become the new head of the current pair)
    next_node = head.next

    # Recursively swap the remaining list (head.next.next onwards)
    # and connect it to the current first node
    head.next = node_swap(head.next.next)

    # Make the original second node point to the original first node
    next_node.next = head

    # Return the new head of this swapped pair (which was originally the second node)
    return next_node


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

Let's analyze the time and space complexity of the given `node_swap` function, which swaps nodes in pairs in a linked list.

### Time Complexity:

1. **Base Case**: The function checks if `head` is `None` or `head.next` is `None`. This is an O(1) operation.
2. **Recursive Case**: 
   - The function processes two nodes at a time (`head` and `head.next`), and then recursively calls `node_swap` on `head.next.next`
   (i.e., the rest of the list after the current pair).
   - This means the function processes each node exactly once, leading to O(n) time where `n` is the number of nodes in the linked list.
   - Each recursive call does a constant amount of work (pointer manipulations) besides the recursive call.

Thus, the time complexity is **O(n)**.

### Space Complexity:

1. **Recursion Stack**: 
   - The space complexity is determined by the depth of the recursion stack.
   - Since the function processes two nodes at a time, the maximum depth of the recursion stack is `n/2`, which simplifies to O(n).
   - For example, a list with 4 nodes will have a recursion depth of 2: `node_swap(1->2->3->4)` calls `node_swap(3->4)`, which then
   calls `node_swap(None)`.

Thus, the space complexity is **O(n)** due to the recursion stack.

### Summary for Given Code:
- **Time Complexity**: O(n)
- **Space Complexity**: O(n) (due to recursion stack)

### Iterative Alternative (for O(1) space):
If you wanted to optimize space, you could implement this iteratively.

The iterative approach uses O(1) extra space (no recursion stack), so the space complexity would be O(1).
The time complexity remains O(n).

"""
