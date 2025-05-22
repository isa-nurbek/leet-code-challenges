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
    """Binary Search Tree node class."""

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Function to build a BST from dictionary data
def build_tree(data):
    """Builds a BST from dictionary data.

    Args:
        data: Dictionary containing "nodes" list and "root" id

    Returns:
        The root node of the constructed BST
    """
    if not data:
        return None
    nodes = {}
    # First pass: create all nodes without connections
    for node_data in data["nodes"]:
        node = BST(node_data["value"])
        nodes[node_data["id"]] = node
    # Second pass: connect child nodes
    for node_data in data["nodes"]:
        node = nodes[node_data["id"]]
        if node_data["left"] is not None:
            node.left = nodes[node_data["left"]]
        if node_data["right"] is not None:
            node.right = nodes[node_data["right"]]
    return nodes[data["root"]]


# Function to print a BST from dictionary data
def print_tree(root):
    """Prints the BST in a tree-like structure.

    Args:
        root: Root node of the BST to print
    """
    if not root:
        print("Empty tree")
        return
    q = deque([root])
    levels = []
    # Level-order traversal to collect nodes by level
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

    # Print tree structure with proper spacing
    for i, level in enumerate(levels):
        # Calculate spacing based on tree depth
        print(" " * (2 ** (len(levels) - i - 1) - 1), end="")
        for _, val in enumerate(level):
            print(val, end=" " * (2 ** (len(levels) - i) - 1))
        print()


# O(n) time | O(h) space
def repair_bst(tree):
    """Repairs a BST where exactly two nodes have been swapped.

    Args:
        tree: Root node of the BST to repair

    Returns:
        The repaired BST (modified in-place)
    """
    node_one = node_two = previous_node = None

    def in_order_traversal(node):
        """Performs in-order traversal to find swapped nodes."""
        nonlocal node_one, node_two, previous_node
        if node is None:
            return
        # Traverse left subtree
        in_order_traversal(node.left)

        # Check if current node is out of order
        if previous_node is not None and previous_node.value > node.value:
            # First violation
            if node_one is None:
                node_one = previous_node
            # Second violation (or adjacent nodes in first violation)
            node_two = node
        previous_node = node

        # Traverse right subtree
        in_order_traversal(node.right)

    # Find the two nodes that need to be swapped
    in_order_traversal(tree)

    # Swap the values of the two nodes
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

# Visual representation of input tree:
#            10
#         /     \
#        7       20
#      /   \    /  \
#    3     12  8   22
#   /           \
# 2              14

# Test Case:

# Build and print input tree
print("Input Tree:")
input_tree = build_tree(input_data)
print_tree(input_tree)

# Repair BST by finding and swapping the two incorrect nodes
output_tree = repair_bst(input_tree)

# Print output tree
print("\nOutput Tree:")
print_tree(output_tree)

# Visual representation of output tree:
#           10
#         /     \
#        7       20
#      /   \    /  \
#    3      8  12   22
#   /           \
# 2              14

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

# =========================================================================================================================== #

# Big O Analysis:

"""
# Time and Space Complexity Analysis:

### Time Complexity Analysis

The time complexity of the `repair_bst` function is determined by the in-order traversal of the binary search tree (BST). 

1. **In-order Traversal**: The function performs an in-order traversal of the entire BST. In-order traversal visits each node
exactly once. For a BST with `n` nodes, this traversal takes `O(n)` time.

2. **Swapping Values**: After the traversal, the function swaps the values of two nodes if they are found. This operation
takes `O(1)` time since it involves only a few assignments.

Thus, the overall time complexity of the function is **O(n)**, where `n` is the number of nodes in the BST.

### Space Complexity Analysis

The space complexity is determined by the space used during the in-order traversal, which is primarily due to the recursion stack.

1. **Recursion Stack**: The in-order traversal is implemented recursively. In the worst case, the maximum depth of the recursion
stack is equal to the height of the BST. 
   - For a balanced BST, the height is `O(log n)`, so the space complexity is `O(log n)`.
   - For a skewed BST (e.g., a tree that degenerates into a linked list), the height is `O(n)`, so the space complexity is `O(n)`.

2. **Additional Space**: The function uses a few additional variables (`node_one`, `node_two`, `previous_node`), but these
occupy `O(1)` space regardless of the input size.

Thus, the space complexity is:
- **O(log n)** for a balanced BST.
- **O(n)** for a skewed BST.

### Summary
- **Time Complexity**: O(n)
- **Space Complexity**: O(log n) (balanced BST) or O(n) (skewed BST)

"""

"""
Let's go through the code **step by step**, explaining how it builds a Binary Search Tree (BST), repairs it if it has two
nodes swapped, and prints its structure in a visually hierarchical format.

---

## 1. **BST Node Class**

```
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
```

This defines a **Binary Search Tree node**:

* `value`: the value of the node.
* `left`: reference to the left child.
* `right`: reference to the right child.

---

## 2. **Tree Construction: `build_tree(data)`**

```
def build_tree(data):
    if not data:
        return None
    nodes = {}
    for node_data in data["nodes"]:
        node = BST(node_data["value"])
        nodes[node_data["id"]] = node
```

### What’s happening:

* It parses a dictionary input that includes a list of nodes.
* Each node has an `id`, a `value`, and optional `left`/`right` child IDs.
* First loop: creates all node objects and stores them in a `nodes` dictionary by their `id`.

```
    for node_data in data["nodes"]:
        node = nodes[node_data["id"]]
        if node_data["left"] is not None:
            node.left = nodes[node_data["left"]]
        if node_data["right"] is not None:
            node.right = nodes[node_data["right"]]
```

* Second loop: links left and right children by using the stored IDs.

```
    return nodes[data["root"]]
```

* Returns the root node using the `root` ID.

---

## 3. **Tree Printing: `print_tree(root)`**

```
def print_tree(root):
    ...
```

### Purpose:

To print the **tree level by level** in a structured format.

### Key Concepts:

* Uses **Breadth-First Search (BFS)** using a queue (`deque`).
* Appends `"None"` for missing children to keep the structure aligned.

```
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
```

* For each level:

  * Print the node values.
  * Add child nodes to the queue.

```
    for i, level in enumerate(levels):
        print(" " * (2 ** (len(levels) - i - 1) - 1), end="")
        for _, val in enumerate(level):
            print(val, end=" " * (2 ** (len(levels) - i) - 1))
        print()
```

* Pretty-prints the tree structure with spacing based on depth.

---

## 4. **BST Repair Function: `repair_bst(tree)`**

### Problem it solves:

If two nodes in a BST are **accidentally swapped**, the BST property is broken.

```
def repair_bst(tree):
    node_one = node_two = previous_node = None
```

### Solution approach:

Use **In-Order Traversal** (which yields sorted order in BST). If two nodes are out of order, they are detected during traversal.

```
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
```

### Details:

* `previous_node` keeps track of the last visited node.
* If `previous_node.value > current.value`, a violation is found.
* First violation: store `node_one = previous_node`, `node_two = current`.
* Second violation (optional): update `node_two`.

```
    if node_one and node_two:
        node_one.value, node_two.value = node_two.value, node_one.value
```

* Finally, swap the values of the two nodes to fix the BST.

---

## 5. **Input Tree and Execution**

The input JSON-like dictionary builds the following tree (with a mistake):

```
        10
     /     \
    7       20
   / \     /  \
  3  12   8   22
 /       \
2        14
```

Notice the problem: **12** and **8** are swapped. For BST property:

* Left < Root < Right
* Node `7` has right child `12` (OK), but
* Node `20` has left child `8`, which should be greater than `10` but **not** less than `12` (mistake)

### Repair:

The function detects 12 and 8 are in the wrong order during traversal and swaps their values.

---

## 6. **Output Tree After Repair**

Corrected BST becomes:

```
        10
     /     \
    7       20
   / \     /  \
  3   8   12  22
 /       \
2        14
```

Now the tree is valid.

---

## Summary

| Component              | Purpose                                                                      |
| ---------------------- | ---------------------------------------------------------------------------- |
| `BST` class            | Defines a node in the binary search tree                                     |
| `build_tree()`         | Builds the tree from input data                                              |
| `print_tree()`         | Prints the tree in level-order with spacing to show structure                |
| `repair_bst()`         | Fixes two swapped nodes in a BST using in-order traversal                    |
| `in_order_traversal()` | Detects misplaced nodes by comparing previous and current nodes in traversal |

---

Let's visualize the input and output trees **before and after repair** using an **ASCII diagram**.

---

## ✅ Legend:

* Each node is shown with its value.
* Child nodes are connected using lines (`/` and `\`).
* Indentation shows depth.

---

## 🌲 Input Tree (Before Repair)

Two nodes are swapped: **8** and **12**

```
           10
         /    \
       7       20
      / \     /  \
     3  12   8   22
    /       \
   2        14
```

### 🔍 Problems:

* `12` should not be the right child of `7` in a valid BST — it's greater than `10` but should be on the right subtree.
* `8` should not be in the left subtree of `20` — it's smaller than `10`.

---

## 🔧 After `repair_bst()` (Output Tree)

Now `8` and `12` have been swapped back.

```
           10
         /    \
       7       20
      / \     /  \
     3   8   12   22
    /       \
   2        14
```

### ✅ Fixed:

* Now, all left children < parent, and all right children > parent at every level.

---

## 🔁 In-Order Traversal Output

You can verify the repair by doing an **in-order traversal** (left-root-right):

### Before Repair:

```
2, 3, 7, 12, 10, 8, 20, 14, 22  ← ❌ Not sorted
```

### After Repair:

```
2, 3, 7, 8, 10, 12, 14, 20, 22  ← ✅ Correct BST order
```

"""
