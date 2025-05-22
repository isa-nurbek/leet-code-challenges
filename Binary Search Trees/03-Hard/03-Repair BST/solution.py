# Problem Description:

"""
                                                Repair BST

You're given a `Binary Search Tree (BST)` that has at least 2 nodes and that only has nodes with unique values (no duplicate
values). Exactly two nodes in the BST have had their values swapped, therefore breaking the BST. Write a function that returns a
repaired version of the tree with all values on the correct nodes.

Your function can mutate the original tree; you do not need to create a new one. Moreover, the shape of the returned tree should
be exactly the same as that of the original input tree.

Each `BST` node has an integer `value`, a `left` child node, and a `right` child node. A node is said to be a valid `BST` node if
and only if it satisfies the `BST` property: its `value` is strictly greater than the values of every node to its left; its `value`
is less than or equal to the values of every node to its right; and its children nodes are either valid `BST` nodes themselves or `None`.


## Sample Input:
```
tree =    10
        /     \
       7       20
     /   \    /  \
   3     12  8   22
  /           \
2              14
```

## Sample Output:
```
          10
        /     \
       7       20
     /   \    /  \
   3      8  12   22
  /           \
2              14
```

## Optimal Time & Space Complexity:
```
O(n) time | O(h) space - where `n` is the number of nodes in the tree and `h` is the height of the tree.
```

"""

# =========================================================================================================================== #

# Solution:


# Binary Search Tree (BST) node class
from collections import deque


class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def build_tree(data):
    if not data:
        return None
    nodes = {}
    for node_data in data["nodes"]:
        node = BST(node_data["value"])
        nodes[node_data["id"]] = node
    for node_data in data["nodes"]:
        node = nodes[node_data["id"]]
        if node_data["left"] is not None:
            node.left = nodes[node_data["left"]]
        if node_data["right"] is not None:
            node.right = nodes[node_data["right"]]
    return nodes[data["root"]]


def print_tree(root):
    if not root:
        print("Empty tree")
        return
    q = deque([root])
    levels = []
    while q:
        level_size = len(q)
        current_level = []
        for _ in range(level_size):
            node = q.popleft()
            if node:
                current_level.append(str(node.value))
                q.append(node.left)
                q.append(node.right)
            else:
                current_level.append("None")
        levels.append(current_level)

    # Print tree structure
    for i, level in enumerate(levels):
        print(" " * (2 ** (len(levels) - i - 1) - 1), end="")
        for _, val in enumerate(level):
            print(val, end=" " * (2 ** (len(levels) - i) - 1))
        print()


def repair_bst(tree):
    node_one = node_two = previous_node = None

    def in_order_traversal(node):
        nonlocal node_one, node_two, previous_node
        if node is None:
            return
        in_order_traversal(node.left)
        if previous_node is not None and previous_node.value > node.value:
            if node_one is None:
                node_one = previous_node
            node_two = node
        previous_node = node
        in_order_traversal(node.right)

    in_order_traversal(tree)
    if node_one and node_two:
        node_one.value, node_two.value = node_two.value, node_one.value
    return tree


# Input Tree data
input_data = {
    "nodes": [
        {"id": "1", "value": 10, "left": "2", "right": "3"},
        {"id": "2", "value": 7, "left": "4", "right": "5"},
        {"id": "3", "value": 20, "left": "6", "right": "7"},
        {"id": "4", "value": 3, "left": "8", "right": None},
        {"id": "5", "value": 12, "left": None, "right": "9"},
        {"id": "6", "value": 8, "left": None, "right": None},
        {"id": "7", "value": 22, "left": None, "right": None},
        {"id": "8", "value": 2, "left": None, "right": None},
        {"id": "9", "value": 14, "left": None, "right": None},
    ],
    "root": "1",
}

# Test Case:

# Build and print input tree
input_tree = build_tree(input_data)
print("Input Tree:")
print_tree(input_tree)

# Repair BST
output_tree = repair_bst(input_tree)

# Print output tree
print("\nOutput Tree:")
print_tree(output_tree)

# Output:

"""
Input Tree:
        10 
    7         20 
  3   12   8     22 
2  None None 14 None None None None 

Output Tree:
        10 
    7         20 
  3   8   12     22 
2  None None 14 None None None None 
"""
