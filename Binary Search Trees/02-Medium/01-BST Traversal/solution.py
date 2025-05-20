# Problem Description:

"""
                                                BST Traversal

Write `three` functions that take in a `Binary Search Tree (BST)` and an `empty array`, traverse the BST, add its nodes' values
to the input array, and return that array. The `three` functions should traverse the BST using the `in-order`, `pre-order`, and
`post-order` tree-traversal techniques, respectively.

Each `BST` node has an integer `value`, a `left` child node, and a `right` child node. A node is said to be a valid `BST` node if
and only if it satisfies the BST property: its `value` is strictly greater than the values of every node to its left; its `value`
is less than or equal to the values of every node to its right; and its children nodes are either valid `BST` nodes themselves or `None`.


## Sample Input:
```
tree =   10
       /     \
      5      15
    /   \       \
   2     5       22
 /
1

array = []
```

## Sample Output:
```
in_order_traverse: [1, 2, 5, 5, 10, 15, 22]   // where the array is the input array
pre_order_traverse: [10, 5, 2, 1, 5, 15, 22]  // where the array is the input array
post_order_traverse: [1, 2, 5, 5, 22, 15, 10]  // where the array is the input array
```

## Optimal Time & Space Complexity:
```
All **three methods**: `O(n)` time | `O(n)` space - where `n` is the number of nodes in the BST.
```

"""

# =========================================================================================================================== #

# Solution:


# Binary Search Tree (BST) node class
class BST:
    def __init__(self, value):
        self.value = value  # The value stored in the node
        self.left = None  # Reference to the left child node
        self.right = None  # Reference to the right child node


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
    return nodes[data["root"]]


# O(n) time | O(n) space
def in_order_traverse(tree, array):
    if tree is not None:
        in_order_traverse(tree.left, array)
        array.append(tree.value)
        in_order_traverse(tree.right, array)

    return array


# O(n) time | O(n) space
def pre_order_traverse(tree, array):
    if tree is not None:
        array.append(tree.value)
        pre_order_traverse(tree.left, array)
        pre_order_traverse(tree.right, array)

    return array


# O(n) time | O(n) space
def post_order_traverse(tree, array):
    if tree is not None:
        post_order_traverse(tree.left, array)
        post_order_traverse(tree.right, array)
        array.append(tree.value)

    return array


# Example tree data structure
tree_dict = {
    "nodes": [
        {"id": "10", "left": "5", "right": "15", "value": 10},
        {"id": "15", "left": None, "right": "22", "value": 15},
        {"id": "22", "left": None, "right": None, "value": 22},
        {"id": "5", "left": "2", "right": "5-2", "value": 5},
        {"id": "5-2", "left": None, "right": None, "value": 5},
        {"id": "2", "left": "1", "right": None, "value": 2},
        {"id": "1", "left": None, "right": None, "value": 1},
    ],
    "root": "10",
}

# Test Case:

# Build the tree
tree = build_tree(tree_dict)

# Perform traversals
in_order = in_order_traverse(tree, [])
pre_order = pre_order_traverse(tree, [])
post_order = post_order_traverse(tree, [])

print("In-order traversal:", in_order)
# In-order traversal: [1, 2, 5, 5, 10, 15, 22]

print("Pre-order traversal:", pre_order)
# Pre-order traversal: [10, 5, 2, 1, 5, 15, 22]

print("Post-order traversal:", post_order)
# Post-order traversal: [1, 2, 5, 5, 22, 15, 10]
