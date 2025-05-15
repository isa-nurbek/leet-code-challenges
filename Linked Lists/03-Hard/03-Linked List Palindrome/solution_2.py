# Problem Description:

"""
                                            Linked List Palindrome

Write a function that takes in the head of a Singly Linked List and returns a `boolean` representing whether the linked list's
nodes form a palindrome. Your function shouldn't make use of any auxiliary data structure.

A palindrome is usually defined as a string that's written the same `forward` and `backward`. For a linked list's nodes to form
a palindrome, their values must be the same when read from left to right and from right to left.
> Note that single-character strings are palindromes, which means that single-node linked lists form palindromes.

Each `LinkedList` node has an integer `value` as well as a `next` node pointing to the next node in the list or to `None` if it's
the tail of the list.

You can assume that the input linked list will always have at least one node; in other words, the head will never be `None`.


## Sample Input:
```
head = 0 -> 1 -> 2 -> 2 -> 1 -> 0 -> None

// The head node with value 0
```

## Sample Output:
```
True
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
def linkedList_palindrome(head):
    # Edge case: empty list or single node is always a palindrome
    if not head or not head.next:
        return True

    # Step 1: Find the middle of the linked list using slow and fast pointers
    # Slow moves 1 step at a time, fast moves 2 steps
    # When fast reaches end, slow will be at middle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse the second half of the linked list
    # We'll reverse starting from the middle node (slow)
    prev = None
    current = slow
    while current:
        # Store next node before we overwrite current.next
        next_node = current.next
        # Reverse the link
        current.next = prev
        # Move pointers forward
        prev = current
        current = next_node
    # After loop, prev will be the head of reversed second half

    # Step 3: Compare the first half with the reversed second half
    left = head  # Pointer to start of first half
    right = prev  # Pointer to start of reversed second half
    is_palindrome = True
    while right:
        if left.value != right.value:
            is_palindrome = False
            break
        left = left.next
        right = right.next

    # Step 4 (Optional): Restore the original list by reversing the second half back
    # This is good practice when you don't want to modify input data structure
    current = prev  # prev is head of reversed second half
    prev = None
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    # Reattach the restored second half to the middle node
    slow.next = prev

    return is_palindrome


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
        {"id": "2", "next": "2-2", "value": 2},
        {"id": "2-2", "next": "1-2", "value": 2},
        {"id": "1-2", "next": "0-2", "value": 1},
        {"id": "0-2", "next": None, "value": 0},
    ],
}

# Test Case:

# Build and print the linked list
linked_list = build_linked_list(linked_list_dict)

print("Linked list:")
print_linked_list(linked_list)

# Check if palindrome
is_palindrome = linkedList_palindrome(linked_list)
print("\nIs palindrome?", is_palindrome)

# Output:

"""
Linked list:
0 -> 1 -> 2 -> 2 -> 1 -> 0 -> None

Is palindrome? True

"""

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

Let's analyze the time and space complexity of the `linkedList_palindrome` function step by step.

### Time Complexity:

1. **Finding the middle of the linked list (Step 1):**
   - The `slow` pointer moves one step at a time, while the `fast` pointer moves two steps at a time.
   - This takes `O(n/2)` time, which simplifies to `O(n)`.

2. **Reversing the second half of the linked list (Step 2):**
   - We reverse the second half of the list starting from the `slow` pointer.
   - This also takes `O(n/2)` time, which simplifies to `O(n)`.

3. **Comparing the first half with the reversed second half (Step 3):**
   - We compare up to `n/2` nodes in the worst case.
   - This takes `O(n/2)` time, which simplifies to `O(n)`.

4. **(Optional) Restoring the linked list (Step 4):**
   - We reverse the second half back to its original order.
   - This takes `O(n/2)` time, which simplifies to `O(n)`.

**Total Time Complexity:**
- `O(n) + O(n) + O(n) + O(n) = O(n)`.
- The dominant term is linear, so the overall time complexity is `O(n)`.

### Space Complexity:

- The algorithm uses a constant amount of extra space for pointers (`slow`, `fast`, `prev`, `current`, `next_node`, `left`, `right`, etc.).
- No additional data structures (like stacks or arrays) are used.
- Thus, the space complexity is `O(1)` (constant space).

### Summary:
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

### Note:
The optional step (Step 4) restores the linked list to its original state, which is good practice if you don't want to modify the
input data structure. However, if you don't care about restoring the list, you can omit Step 4, and the time complexity remains
`O(n)` (since `O(n)` still dominates). The space complexity remains `O(1)` either way.

"""
