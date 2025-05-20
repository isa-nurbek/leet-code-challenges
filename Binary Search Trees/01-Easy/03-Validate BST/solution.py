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

# The tree structure represented by this dictionary:
#            10
#          /    \
#        5       15
#      /   \     / \
#     2     5   13  22
#    /           \
#   1             14

# Test Case:

# Build the tree
tree = build_tree(tree_dict)

# Find closest value
result = validate_bst(tree)

print(result)  # Output: True

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### **Time Complexity Analysis**

The time complexity of the `validate_bst` function is **O(N)**, where **N** is the number of nodes in the binary tree.
This is because the function visits each node exactly once during the traversal. 

Here's why:
- For each node, the function performs a constant amount of work (checking the node's value against `min_value` and `max_value`).
- The recursion explores both the left and right subtrees, but no node is visited more than once.

### **Space Complexity Analysis**

The space complexity of the `validate_bst` function is **O(H)**, where **H** is the height of the binary tree.
This space is used by the call stack during the recursive traversal.

Here's why:
- In the **best case** (a perfectly balanced tree), the height is **O(log N)**, so the space complexity is **O(log N)**.
- In the **worst case** (a completely unbalanced tree, e.g., a linked list), the height is **O(N)**,
so the space complexity is **O(N)**.

### **Summary**
- **Time Complexity:** **O(N)** (visits every node once).
- **Space Complexity:** **O(H)** (due to recursion stack, where **H** is the height of the tree).

This is an optimal solution for validating a BST.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
Let’s walk through the code step by step and explain how it works in detail.

## 1. **Class `BST`**

```
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
```

This defines a basic **Binary Search Tree (BST)** node.

* Each node stores a **value**
* It has a reference to a **left** child and a **right** child (both initialized to `None`)

This class is used to create nodes for our binary tree.

---

## 2. **Function `build_tree(data)`**

```
def build_tree(data):
    if not data:
        return None
```

This function builds the tree from a dictionary that contains node definitions.

### Two-pass approach:

### **Pass 1: Create all nodes**

```
    nodes = {}
    for node_data in data["nodes"]:
        node = BST(node_data["value"])
        nodes[node_data["id"]] = node
```

* We loop through every node entry in `data["nodes"]` and create a `BST` instance for each.
* Each node has a unique `"id"` used as a key to store it in the `nodes` dictionary.

### **Pass 2: Link child nodes**

```
    for node_data in data["nodes"]:
        node = nodes[node_data["id"]]
        if node_data["left"] is not None:
            node.left = nodes[node_data["left"]]
        if node_data["right"] is not None:
            node.right = nodes[node_data["right"]]
```

* Loop again over the node data.
* For each node, if it has a left or right child ID, we use that ID to find the corresponding `BST` node from the dictionary
and set it as a child.

### **Return the root node**

```
    return nodes[data["nodes"][0]["id"]]
```

* The root is assumed to be the first node in the `nodes` list.

---

## 3. **Function `validate_bst(tree)`**

```
def validate_bst(tree):
    return validate_bst_helper(tree, float("-inf"), float("inf"))
```

* This is a wrapper function that calls `validate_bst_helper`.
* It starts with the entire possible range of values (from negative infinity to positive infinity).

---

## 4. **Function `validate_bst_helper(tree, min_value, max_value)`**

```
def validate_bst_helper(tree, min_value, max_value):
    if tree is None:
        return True

    if tree.value < min_value or tree.value >= max_value:
        return False

    left_is_valid = validate_bst_helper(tree.left, min_value, tree.value)
    return left_is_valid and validate_bst_helper(tree.right, tree.value, max_value)
```

### This is a **recursive function** that validates the BST by checking the following:

1. **Base Case**: If the node is `None`, it’s valid (empty trees are valid).
2. **Value Check**:

   * The node's value must lie between `min_value` (exclusive) and `max_value` (inclusive on the left, exclusive on the right).
   * This ensures all values in the left subtree are `< current.value`, and all values in the right are `≥ current.value`.
3. **Recursive Calls**:

   * Left subtree must be valid in range (`min_value`, `tree.value`)
   * Right subtree must be valid in range (`tree.value`, `max_value`)
   * Both must be true for the whole tree to be valid

### Time and Space Complexity:

* **Time:** O(n), where n is the number of nodes (we visit each node once)
* **Space:** O(d), where d is the depth of the tree (space used by recursion stack)

---

## 5. **Example Tree**

The tree is encoded as a dictionary:

```
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
    "root": "10",
}
```

### Let's visualize the tree:

```
        10
       /  \
      5    15
     / \   / \
    2   5 13 22
   /
  1
       \
       14
```

### Why this is still a valid BST:

* Every left child is **strictly less** than its parent.
* Every right child is **greater than or equal** to the parent.
* Duplicate value `5` is on the **right** side of the node with value `5`, which is valid under the rule: left < node ≤ right.

---

## 6. **Execution and Output**

```
tree = build_tree(tree_dict)
result = validate_bst(tree)
print(result)  # Output: True
```

* We build the tree from the dictionary.
* Then validate if it is a proper BST.
* It returns `True`, which means the tree satisfies BST properties.

---

### Summary

This code:

* Constructs a binary tree from a structured dictionary.
* Validates if the tree is a Binary Search Tree using recursive min/max constraints.
* Returns `True` if valid, `False` otherwise.

---

Here's an **ASCII visualization** of the binary search tree defined by your `tree_dict`:

```
               10
             /    \
           5        15
         /   \     /   \
        2     5   13    22
       /           \
      1             14
```

### Node Details:

* Root: `10`
* Left Subtree:

  * `5` has:

    * Left child `2`, which has:

      * Left child `1`
    * Right child `5` (duplicate, id `"5-2"`)
* Right Subtree:

  * `15` has:

    * Left child `13`, which has:

      * Right child `14`
    * Right child `22`

### Notes:

* This tree **allows duplicates**, as shown by the second node with value `5` (`id: "5-2"`) on the **right** side.
* BST property is maintained:

  * All values in the left subtree of a node are `< node.value`
  * All values in the right subtree are `≥ node.value`

"""
