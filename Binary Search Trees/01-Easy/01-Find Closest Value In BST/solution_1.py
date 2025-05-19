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


# Average: O(log(n)) time | O(1) space
# Worst: O(n) time | O(1) space
def find_closest_value_in_bst(tree, target):
    # Start the helper function with the tree's root value as initial closest
    return find_closest_value_in_bst_helper(tree, target, tree.value)


# Recursive helper function to find closest value
def find_closest_value_in_bst_helper(tree, target, closest):
    # Base case: if we've reached a leaf node, return current closest
    if tree is None:
        return closest

    # Check if current node's value is closer than previous closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value  # Update closest if current node is better

    # Decide which subtree to explore next based on target value
    if target < tree.value:
        # Target is smaller, so search in left subtree
        return find_closest_value_in_bst_helper(tree.left, target, closest)
    elif target > tree.value:
        # Target is larger, so search in right subtree
        return find_closest_value_in_bst_helper(tree.right, target, closest)
    else:
        # Found exact match, return it immediately
        return closest


# Example tree data structure

tree_dict = {
    "nodes": [
        {"id": "10", "left": "5", "right": "15", "value": 10},  # Root node
        {"id": "15", "left": "13", "right": "22", "value": 15},  # Right child of root
        {"id": "22", "left": None, "right": None, "value": 22},  # Right child of 15
        {"id": "13", "left": None, "right": "14", "value": 13},  # Left child of 15
        {"id": "14", "left": None, "right": None, "value": 14},  # Right child of 13
        {"id": "5", "left": "2", "right": "5-2", "value": 5},  # Left child of root
        {"id": "5-2", "left": None, "right": None, "value": 5},  # Right child of 5
        {"id": "2", "left": "1", "right": None, "value": 2},  # Left child of 5
        {"id": "1", "left": None, "right": None, "value": 1},  # Left child of 2
    ],
}

# Test Case:

# Build the tree
tree = build_tree(tree_dict)

# Find closest value
result = find_closest_value_in_bst(tree, 12)

print(result)  # Output: 13

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

Let's analyze the time and space complexity of the given `find_closest_value_in_bst` algorithm.

### Time Complexity:

- **Best Case:** O(1) - When the target value is equal to the root node's value.
- **Average Case:** O(log n) - In a balanced BST, with each recursive call, we eliminate half of the remaining tree
(similar to binary search).
- **Worst Case:** O(n) - If the BST is completely unbalanced (essentially a linked list), we might have to traverse all nodes.

### Space Complexity:

- **Best Case:** O(1) - When the target is found at the root (no recursive calls).
- **Average Case:** O(log n) - Due to the recursion stack in a balanced BST (depth of recursion is log n).
- **Worst Case:** O(n) - If the BST is completely unbalanced, the recursion stack could grow to size n.

### Explanation:

1. **Time Complexity:**
   - The algorithm works by traversing a path from the root to a leaf, adjusting the closest value along the way.
   - In a balanced BST, the height is log n, so the number of recursive calls is O(log n).
   - In the worst case (unbalanced BST), the height is n, leading to O(n) time.

2. **Space Complexity:**

   - The space is determined by the recursion stack.
   - For a balanced BST, the maximum stack depth is O(log n).
   - In the worst case (unbalanced BST), it's O(n).

### Notes:

- The algorithm could be optimized to use an iterative approach (instead of recursion), reducing the space complexity to O(1)
in all cases while keeping the same time complexity.
- The initial closest value is set to `tree.value`, which is a reasonable starting point.

"""
