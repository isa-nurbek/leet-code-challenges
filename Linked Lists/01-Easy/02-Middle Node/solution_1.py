# Problem Description:

"""
                                            Middle Node

You're given a Linked List with at least one node. Write a function that returns the middle node of the Linked List. If there are
two middle nodes (i.e. an even length list), your function should return the second of these nodes.

Each `LinkedList` node has an integer `value` as well as a `next` node pointing to the next node in the list or to `None` if it's
the tail of the list.

## Sample Input:
```
linked_list = 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> None
```

## Sample Output:
```
5 -> 6 -> 7 -> 8 -> 9 -> None
```

## Optimal Time & Space Complexity:
```
O(n) time | O(1) space - where `n` is the number of nodes in the linked list.
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


# Function to find the middle node
# O(n) time | O(1) space
def middle_node(linked_list):
    # Initialize a counter to keep track of the number of nodes
    count = 0
    # Start with the head/first node of the linked list
    current_node = linked_list

    # First pass: traverse the entire linked list to count nodes
    while current_node is not None:
        count += 1  # Increment counter for each node
        current_node = current_node.next  # Move to next node

    # Reset to the head/first node for second traversal
    middle_node = linked_list

    # Second pass: traverse to the middle node
    # We only need to go halfway (count // 2) through the list
    for _ in range(count // 2):
        middle_node = middle_node.next  # Move forward node by node

    # Return the node at the middle position
    return middle_node


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
    "head": "1",
    "nodes": [
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

# Remove duplicates
result = middle_node(linked_list)

print_linked_list(result)
# Output: 5 -> 6 -> 7 -> 8 -> 9 -> None

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

Let's analyze the time and space complexity of the `middle_node` function.

### Time Complexity:

1. **First Loop (Counting Nodes):**
   - The first `while` loop iterates through each node in the linked list exactly once to count the total number of nodes (`count`). 
   - If the linked list has `n` nodes, this loop runs `n` times.
   - Time complexity for this part: **O(n)**.

2. **Second Loop (Finding Middle Node):**
   - The `for` loop runs from the head of the linked list to the middle node, which takes `count // 2` steps.
   - Since `count` is `n`, this loop runs `n // 2` times, which is **O(n)** in asymptotic terms.
   - Time complexity for this part: **O(n)**.

- **Total Time Complexity:** O(n) + O(n) = **O(n)**.

### Space Complexity:

- The function uses a constant amount of additional space (variables like `count`, `current_node`, `middle_node`, and
the loop counter `_`). 
- No additional data structures or recursive calls are used that grow with the input size.
- **Space Complexity:** **O(1)** (constant space).

### Summary:
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

### Alternative Approach (Optimized):
You can also solve this problem in **O(n) time** and **O(1) space** using the **"fast and slow pointer"** technique (tortoise
and hare), where the fast pointer moves two steps at a time and the slow pointer moves one step at a time. When the fast pointer
reaches the end, the slow pointer will be at the middle. This approach only requires **one traversal** of the linked list.

"""
