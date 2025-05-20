# Problem Description:

"""
                                                Validate BST

Write a function that takes in a potentially invalid `Binary Search Tree (BST)` and returns a `boolean` representing whether the
BST is valid.

Each `BST` node has an integer `value`, a `left` child node, and a `right` child node. A node is said to be a valid `BST` node if
and only if it satisfies the `BST` property: its `value` is strictly greater than the values of every node to its left; its `value`
is less than or equal to the values of every node to its right; and its children nodes are either valid `BST` nodes themselves or `None`.

A BST is valid if and only if all of its nodes are valid `BST` nodes.


## Sample Input:
```
tree =   10
       /     \
      5      15
    /   \   /   \
   2     5 13   22
 /           \
1            14
```

## Sample Output:
```
True
```

## Optimal Time & Space Complexity:
```
O(n) time | O(d) space - where `n` is the number of nodes in the BST and `d` is the depth (height) of the BST.
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
    return nodes[data["nodes"][0]["id"]]


# O(n) time | O(d) space
def validate_bst(tree):
    """
    Validates whether a binary tree is a valid Binary Search Tree (BST).

    A BST is valid if for every node:
    - All values in its left subtree are less than the node's value
    - All values in its right subtree are greater than or equal to the node's value

    Args:
        tree: The root node of the binary tree to validate

    Returns:
        bool: True if the tree is a valid BST, False otherwise
    """
    # Start with the root node, allowing any value between -infinity and +infinity
    return validate_bst_helper(tree, float("-inf"), float("inf"))


def validate_bst_helper(tree, min_value, max_value):
    """
    Helper function that recursively validates BST property with range checking.

    Args:
        tree: Current node being checked
        min_value: The minimum value this node can have (exclusive)
        max_value: The maximum value this node can have (inclusive)

    Returns:
        bool: True if subtree rooted at 'tree' is valid, False otherwise
    """
    # An empty tree is trivially valid
    if tree is None:
        return True

    # Check if current node's value violates BST property
    # - Value must be > min_value (from parent's left subtree requirement)
    # - Value must be <= max_value (from parent's right subtree requirement)
    if tree.value <= min_value or tree.value > max_value:
        return False

    # Check left subtree:
    # - All values must be < current node's value
    # - Must still be > the inherited min_value
    left_is_valid = validate_bst_helper(tree.left, min_value, tree.value)

    # Check right subtree:
    # - All values must be >= current node's value
    # - Must still be < the inherited max_value
    # Only check right subtree if left is already valid (short-circuit evaluation)
    return left_is_valid and validate_bst_helper(tree.right, tree.value, max_value)


# Example tree data structure

tree_dict = {
    "nodes": [
        {"id": "10", "left": "5", "right": "15", "value": 10},  # Root node 10
        {"id": "15", "left": "13", "right": "22", "value": 15},  # Right child of root
        {"id": "22", "left": None, "right": None, "value": 22},  # Right child of 15
        {"id": "13", "left": None, "right": "14", "value": 13},  # Left child of 15
        {"id": "14", "left": None, "right": None, "value": 14},  # Right child of 13
        {"id": "5", "left": "2", "right": "5-2", "value": 5},  # Left child of root
        {"id": "5-2", "left": None, "right": None, "value": 5},  # Right child of 5
        {"id": "2", "left": "1", "right": None, "value": 2},  # Left child of 5
        {"id": "1", "left": None, "right": None, "value": 1},  # Left child of 2
    ],
    "root": "10",
}


# Build the tree
tree = build_tree(tree_dict)

# Find closest value
result = validate_bst(tree)

print(result)  # Output: True
