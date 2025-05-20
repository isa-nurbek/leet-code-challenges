# Problem Description:

"""
                                                Find Kth Largest Value In BST

Write a function that takes in a `Binary Search Tree (BST)` and a positive integer `k` and returns the `k`th largest integer
contained in the BST.

You can assume that there will only be integer values in the BST and that `k` is less than or equal to the number of nodes in
the tree.

Also, for the purpose of this question, duplicate integers will be treated as distinct values. In other words, the second largest
value in a BST containing values `{5, 7, 7}` will be `7`—not `5`.

Each `BST` node has an integer `value`, a `left` child node, and a `right` child node. A node is said to be a valid `BST` node if
and only if it satisfies the `BST` property: its `value` is strictly greater than the values of every node to its left; its `value`
is less than or equal to the values of every node to its right; and its children nodes are either valid `BST` nodes themselves or `None`.


## Sample Input:
```
tree =   15
       /     \
      5      20
    /   \   /   \
   2     5 17   22
 /   \         
1     3   

k = 3
```

## Sample Output:
```
17
```

## Optimal Time & Space Complexity:
```
O(h + k) time | O(h) space - where `h` is the height of the tree and `k` is the input parameter.
```

"""

# =========================================================================================================================== #

# Solution:


# Binary Search Tree (BST) node class
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Function to build a BST from dictionary data
def build_tree(data):
    if not data:  # If data is empty, return None (empty tree)
        return None

    nodes = {}  # Dictionary to store nodes by their IDs

    # First pass: create all node objects
    for node_data in data["nodes"]:
        node = BST(node_data["value"])  # Create new node with value
        nodes[node_data["id"]] = node  # Store node in dictionary with its ID as key

    # Second pass: connect child nodes to their parents
    for node_data in data["nodes"]:
        node = nodes[node_data["id"]]  # Get current node

        # If left child exists, connect it
        if node_data["left"] is not None:
            node.left = nodes[node_data["left"]]

        # If right child exists, connect it
        if node_data["right"] is not None:
            node.right = nodes[node_data["right"]]

    # Return the root node (first node in the nodes list)
    return nodes[data["nodes"][0]["id"]]


# O(n) time | O(n) space
def find_kth_largest_value_in_bst(tree, k):
    """
    Finds the kth largest value in a Binary Search Tree (BST).

    Args:
        tree: The root node of the BST
        k: The position of the desired value when sorted in ascending order
           (1 would be the largest, 2 second largest, etc.)

    Returns:
        The kth largest value in the BST
    """

    # Initialize an empty list to store node values in sorted order
    sorted_node_values = []

    # Perform in-order traversal to get all values in sorted (ascending) order
    in_order_traverse(tree, sorted_node_values)

    # The kth largest value is at position len(sorted_node_values) - k in the sorted list
    # (since Python lists are 0-indexed)
    return sorted_node_values[len(sorted_node_values) - k]


def in_order_traverse(node, sorted_node_values):
    """
    Performs an in-order traversal of the BST and stores values in sorted order.

    In-order traversal of a BST yields values in ascending order.

    Args:
        node: Current node being processed
        sorted_node_values: List to accumulate node values in sorted order
    """

    # Base case: if node is None, return without doing anything
    if node is None:
        return

    # 1. Recursively traverse the left subtree (smaller values)
    in_order_traverse(node.left, sorted_node_values)

    # 2. Visit the current node (add its value to the list)
    sorted_node_values.append(node.value)

    # 3. Recursively traverse the right subtree (larger values)
    in_order_traverse(node.right, sorted_node_values)


# Example tree data structure
tree_dict = {
    "nodes": [
        {"id": "15", "left": "5", "right": "20", "value": 15},
        {"id": "20", "left": "17", "right": "22", "value": 20},
        {"id": "22", "left": None, "right": None, "value": 22},
        {"id": "17", "left": None, "right": None, "value": 17},
        {"id": "5", "left": "2", "right": "5-2", "value": 5},
        {"id": "5-2", "left": None, "right": None, "value": 5},
        {"id": "2", "left": "1", "right": "3", "value": 2},
        {"id": "3", "left": None, "right": None, "value": 3},
        {"id": "1", "left": None, "right": None, "value": 1},
    ],
    "root": "15",
}

# The tree structure represented by this dictionary:

#           15
#        /     \
#       5      20
#     /   \   /   \
#    2     5 17   22
#  /   \
# 1     3

# Test Case:

# Build the tree
tree = build_tree(tree_dict)

# Find closest value
result = find_kth_largest_value_in_bst(tree, 3)

print(result)  # Output: 17

# =========================================================================================================================== #

# Big O Analysis:

"""
# Time and Space Complexity Analysis:

Let's analyze the time and space complexity of the given code for finding the k-th largest value in a BST.

### **Time Complexity:**

1. **In-order Traversal (`in_order_traverse`):**
   - The in-order traversal visits every node exactly once, performing an `O(1)` operation (appending the value to the list)
   for each node.
   - **Time: `O(N)`**, where `N` is the number of nodes in the BST.

2. **Accessing the k-th largest value:**
   - After traversal, accessing `sorted_node_values[len(sorted_node_values) - k]` is an `O(1)` operation since list indexing
   in Python is constant time.

**Total Time Complexity: `O(N)`**  
*(Dominant term is the traversal.)*

---

### **Space Complexity:**

1. **Recursion Stack:**
   - In the worst case (a completely skewed BST), the recursion depth is `O(N)`.
   - In a balanced BST, the recursion depth is `O(log N)`.

2. **Storage for `sorted_node_values`:**
   - The list stores all `N` node values, so it takes `O(N)` space.

**Total Space Complexity: `O(N)`**  
*(The `sorted_node_values` list dominates the space usage.)*

### Summary:
- **Time Complexity**: **O(n)** 
- **Space Complexity**: **O(n)** 

---

### **Optimization Insight:**

The current approach is not optimal for very large BSTs because it stores all node values. A better approach would be to perform
a **reverse in-order traversal (right-root-left)** and stop early once the k-th largest element is found. This reduces the space
complexity to `O(k)` (or `O(1)` if done iteratively with early termination) and avoids unnecessary traversals.

"""
