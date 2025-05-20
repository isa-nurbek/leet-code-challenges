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


# O(n) time | O(1) space
# Morris Traversal
def find_kth_largest_value_in_bst(tree, k):
    current = tree
    count = 0

    while current is not None:
        if current.right is None:
            count += 1
            if count == k:
                return current.value
            current = current.left
        else:
            predecessor = current.right
            while predecessor.left is not None and predecessor.left != current:
                predecessor = predecessor.left

            if predecessor.left is None:

                predecessor.left = current
                current = current.right
            else:

                predecessor.left = None

                count += 1
                if count == k:
                    return current.value
                current = current.left

    return None


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
