# Problem Description:

"""
                                                Find Closest Value In BST

Write a function that takes in a `Binary Search Tree (BST)` and a target integer value and returns the closest value to that target
value contained in the BST.

You can assume that there will only be one closest value.

Each `BST` node has an integer `value`, a `left` child node, and a `right` child node. A node is said to be a valid `BST` node if
and only if it satisfies the BST property: its `value` is strictly greater than the values of every node to its left; its `value` is
less than or equal to the values of every node to its right; and its children nodes are either valid `BST` nodes themselves or None.


## Sample Input:
```
tree =   10
       /     \
      5      15
    /   \   /   \
   2     5 13   22
 /           \
1            14

target = 12
```

## Sample Output:
```
13
```

## Optimal Time & Space Complexity:
```
Average: O(log(n)) time | O(1) space - where `n` is the number of nodes in the BST.
Worst: O(n) time | O(1) space - where `n` is the number of nodes in the BST.
```

"""

# =========================================================================================================================== #

# Solution:


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


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

    return nodes[data["nodes"][0]["id"]]


# Average: O(log(n)) time | O(1) space
# Worst: O(n) time | O(1) space
def find_closest_value_in_bst(tree, target):
    return find_closest_value_in_bst_helper(tree, target, tree.value)


def find_closest_value_in_bst_helper(tree, target, closest):
    if tree is None:
        return closest

    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value

    if target < tree.value:
        return find_closest_value_in_bst_helper(tree.left, target, closest)
    elif target > tree.value:
        return find_closest_value_in_bst_helper(tree.right, target, closest)
    else:
        return closest


tree_dict = {
    "nodes": [
        {"id": "10", "left": "5", "right": "15", "value": 10},
        {"id": "15", "left": "13", "right": "22", "value": 15},
        {"id": "22", "left": None, "right": None, "value": 22},
        {"id": "13", "left": None, "right": "14", "value": 13},
        {"id": "14", "left": None, "right": None, "value": 14},
        {"id": "5", "left": "2", "right": "5-2", "value": 5},
        {"id": "5-2", "left": None, "right": None, "value": 5},
        {"id": "2", "left": "1", "right": None, "value": 2},
        {"id": "1", "left": None, "right": None, "value": 1},
    ],
}

# Build the tree
tree = build_tree(tree_dict)

# Find closest value
result = find_closest_value_in_bst(tree, 12)

print(result)  # Output: 13
