# Problem Description:

"""
                                                Validate Three Nodes

You're given `three nodes` that are contained in the same `Binary Search Tree`: `node_one`, `node_two`, and `node_three`. Write a
function that returns a boolean representing whether one of `node_one` or `node_three` is an ancestor of `node_two` and the other
node is a descendant of `node_two`. For example, if your function determines that `node_one` is an ancestor of `node_two`, then it
needs to see if `node_three` is a descendant of `node_two`. If your function determines that `node_three` is an ancestor, then it
needs to see if `node_one` is a descendant.

A *descendant* of a node `N` is defined as a node contained in the tree rooted at `N`. A node `N` is an ancestor of another node
`M` if `M` is a descendant of `N`.

It isn't guaranteed that `node_one` or `node_three` will be ancestors or descendants of `node_two`, but it is guaranteed that all
three nodes will be unique and will never be `None`. In other words, you'll be given valid input nodes.

Each `BST` node has an integer `value`, a `left` child node, and a `right` child node. A node is said to be a valid `BST` node if
and only if it satisfies the `BST` property: its `value` is strictly greater than the values of every node to its left; its `value`
is less than or equal to the values of every node to its right; and its children nodes are either valid `BST` nodes themselves or `None`.


## Sample Input:
```
tree =    5
       /     \
      2       7
    /   \   /   \
   1     4 6     8
  /     /
 0     3  

// This tree won't actually be passed as an input; it's here to help you visualize the problem.

node_one = 5  // The actual node with value 5.
node_two = 2  // The actual node with value 2.
node_three = 3  // The actual node with value 3.
```

## Sample Output:
```
True 

// node_one is an ancestor of node_two, and node_three is a descendant of node_two.
```

## Optimal Time & Space Complexity:
```
O(d) time | O(1) space - where `d` is the distance between `node_one` and `node_three`.
```

"""

# =========================================================================================================================== #

# Solution:


# Binary Search Tree (BST) node class
class BST:
    def __init__(self, value, left=None, right=None):
        # Binary Search Tree node constructor
        self.value = value  # The value stored in the node
        self.left = left  # Left child node
        self.right = right  # Right child node


def build_tree(data):
    # Builds a BST from dictionary representation
    if not data:
        return None  # Empty tree if no data

    # Create all nodes first and store them in a dictionary by their IDs
    nodes = {}
    for node_data in data["nodes"]:
        node = BST(node_data["value"])
        nodes[node_data["id"]] = node

    # Connect the nodes by setting left and right children based on the IDs
    for node_data in data["nodes"]:
        node = nodes[node_data["id"]]
        if node_data["left"] is not None:
            node.left = nodes[node_data["left"]]
        if node_data["right"] is not None:
            node.right = nodes[node_data["right"]]

    # Return the root node of the tree
    return nodes[data["root"]]


# O(h) time | O(h) space
def validate_three_nodes(node_one, node_two, node_three):
    # Validates if one of these conditions is true:
    # 1. node_one is ancestor of node_two, and node_two is ancestor of node_three
    # 2. node_three is ancestor of node_two, and node_two is ancestor of node_one

    # Check if node_two is descendant of node_one and node_three is descendant of node_two
    if is_descendant(node_two, node_one):
        return is_descendant(node_three, node_two)

    # Check if node_two is descendant of node_three and node_one is descendant of node_two
    if is_descendant(node_two, node_three):
        return is_descendant(node_one, node_two)

    # If neither condition is met, return False
    return False


def is_descendant(node, target):
    # Checks if target is a descendant of node in the BST
    if node is None:
        return False  # Reached leaf node, target not found
    if node is target:
        return True  # Found the target node

    # Recursively search left or right subtree based on BST properties
    # If target value is less than current node's value, search left subtree
    # Otherwise, search right subtree
    return (
        is_descendant(node.left, target)
        if target.value < node.value
        else is_descendant(node.right, target)
    )


# Tree representation as a dictionary
tree_dict = {
    "nodes": [
        {"id": "0", "left": None, "right": None, "value": 0},
        {"id": "1", "left": "0", "right": None, "value": 1},
        {"id": "2", "left": "1", "right": "4", "value": 2},
        {"id": "3", "left": None, "right": None, "value": 3},
        {"id": "4", "left": "3", "right": None, "value": 4},
        {"id": "5", "left": "2", "right": "7", "value": 5},
        {"id": "6", "left": None, "right": None, "value": 6},
        {"id": "7", "left": "6", "right": "8", "value": 7},
        {"id": "8", "left": None, "right": None, "value": 8},
    ],
    "root": "5",  # Root node ID
}


# Build the tree from the dictionary
root = build_tree(tree_dict)

# Test Case: validate_three_nodes(5, 2, 3)

node_one = root  # 5 (root node)
node_two = root.left  # 2
node_three = root.left.right.left  # 3

print(validate_three_nodes(node_one, node_two, node_three))
# Output: True

# Visual representation of the tree:
#            5
#         /     \
#        2       7
#      /   \   /   \
#     1     4 6     8
#    /     /
#   0     3

# =========================================================================================================================== #

# Big O Analysis:

"""
# Time and Space Complexity Analysis:

### Time Complexity:

1. **`is_descendant(node, target)` function**:
   - This function performs a search for the `target` node starting from the given `node`.
   - In the worst case, it traverses a path from the root to a leaf in the BST (or until it finds the target).
   - The time complexity is `O(h)`, where `h` is the height of the tree. 
     - For a balanced BST, `h = O(log n)` (where `n` is the number of nodes).
     - For a skewed BST (worst case), `h = O(n)`.

2. **`validate_three_nodes(node_one, node_two, node_three)` function**:
   - This function calls `is_descendant` up to 4 times (2 in the first case and 2 in the second case).
   - Each call to `is_descendant` is `O(h)`, so the total time complexity is `O(h)` (since constants are dropped in Big-O notation).

### Space Complexity:

1. **`is_descendant(node, target)` function**:
   - This is a recursive function, and the maximum depth of recursion is equal to the height of the tree (`h`).
   - Thus, the space complexity is `O(h)` due to the recursion stack.
     - For a balanced BST, this is `O(log n)`.
     - For a skewed BST, this is `O(n)`.

2. **`validate_three_nodes(node_one, node_two, node_three)` function**:
   - The space complexity is determined by the deepest recursion stack in the `is_descendant` calls, which is `O(h)`.

### Summary:
- **Time Complexity**: `O(h)` (where `h` is the height of the BST).
- **Space Complexity**: `O(h)` (due to recursion stack).

### Notes:
- If the BST is balanced, `h = O(log n)`, so both time and space complexity become `O(log n)`.
- If the BST is skewed (e.g., a linked list), `h = O(n)`, so both time and space complexity become `O(n)`.

"""
