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
    # Initialize pointers to track the two nodes that are swapped
    # and the previous node during in-order traversal
    node_one = node_two = previous_node = None

    # Use a stack for iterative in-order traversal
    stack = []
    current_node = tree

    # Perform in-order traversal of the BST
    while current_node is not None or len(stack) > 0:
        # Go to the leftmost node (standard in-order traversal)
        while current_node is not None:
            stack.append(current_node)
            current_node = current_node.left

        # Current node is now the leftmost node not yet processed
        current_node = stack.pop()

        # Check if current node's value is less than previous node's value
        # (which violates BST property)
        if previous_node is not None and previous_node.value > current_node.value:
            # If this is the first violation, set node_one to previous_node
            if node_one is None:
                node_one = previous_node

            # Always update node_two to current_node to handle cases where
            # the swapped nodes are adjacent or not
            node_two = current_node

        # Move to the next node in in-order sequence
        previous_node = current_node
        current_node = current_node.right

    # After finding the two swapped nodes, swap their values back
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

The given function `repair_bst` is designed to identify and swap two misplaced nodes in a Binary Search Tree (BST) to restore
its correct structure. Here's the breakdown of the time complexity:

1. **Traversal of the BST**: The algorithm performs an in-order traversal of the BST using an iterative approach with a stack. 
   - In-order traversal visits each node exactly once.
   - For each node, operations like pushing to the stack, popping from the stack, and comparing values are O(1) operations.
   - Therefore, the traversal itself is O(N), where N is the number of nodes in the tree.

2. **Identifying the misplaced nodes**: During the traversal, the algorithm checks if the current node's value is less than the
previous node's value (which violates the BST property). This check is done in O(1) time for each node.
   - The first violation is stored in `node_one`, and the second violation is stored in `node_two`.
   - This process doesn't add any additional time complexity beyond the traversal.

3. **Swapping the values**: Once the two misplaced nodes are identified, their values are swapped in O(1) time.

**Overall Time Complexity**: The dominant factor is the in-order traversal, which is O(N). Thus, the time complexity is **O(N)**.

### Space Complexity Analysis

The space complexity is determined by the additional data structures used during the execution:

1. **Stack**: The iterative in-order traversal uses a stack to keep track of nodes.
   - In the worst case (a skewed tree), the stack can hold all nodes at once (e.g., for a left-skewed tree, all nodes are pushed
   to the stack before starting to pop).
   - Thus, the stack can grow up to O(N) in size.

2. **Other variables**: The variables `node_one`, `node_two`, `previous_node`, and `current_node` use O(1) space.

**Overall Space Complexity**: The stack dominates the space usage, so the space complexity is **O(N)** in the worst case. In
the best case (a balanced tree), the space complexity would be O(log N), but we typically consider the worst case for analysis.

### Summary
- **Time Complexity**: O(N)
- **Space Complexity**: O(N) (worst case, due to the stack)

### Additional Notes
- The algorithm correctly identifies the two swapped nodes in a BST where exactly two nodes are misplaced. The in-order traversal
helps identify these nodes because in a correct BST, the in-order traversal should yield a strictly increasing sequence.
- The swap operation is efficient (O(1)) and doesn't affect the overall time complexity.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
Let's break down our entire code in **clear parts** and explain each section's logic and role in the full flow of:

* **Building a tree from input data**
* **Detecting and repairing the binary search tree (BST)**
* **Printing the BST in a structured way**

---

## 🔷 1. Class Definition: `BST`

```
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
```

### ✅ Purpose:

This defines the **binary search tree node class**. Each node holds:

* a `value`
* a pointer to the `left` child
* a pointer to the `right` child

---

## 🔷 2. Function: `build_tree(data)`

```
def build_tree(data):
    ...
```

### ✅ Purpose:

Builds a tree from a **dictionary format** (with nodes and root ID).

### 🔁 Steps:

1. **Create all nodes (without connecting them)**:

   ```
   for node_data in data["nodes"]:
       node = BST(node_data["value"])
       nodes[node_data["id"]] = node
   ```

2. **Link each node to its left and right children**:

   ```
   for node_data in data["nodes"]:
       node = nodes[node_data["id"]]
       if node_data["left"] is not None:
           node.left = nodes[node_data["left"]]
       if node_data["right"] is not None:
           node.right = nodes[node_data["right"]]
   ```

3. **Return the root node** using the `root` ID:

   ```
   return nodes[data["root"]]
   ```

---

## 🔷 3. Function: `print_tree(root)`

```
def print_tree(root):
    ...
```

### ✅ Purpose:

Prints the BST level-by-level (breadth-first), making it easier to visualize tree structure.

### 🔁 Steps:

1. **Breadth-first traversal using a queue (`deque`)**:

   * Store each level's values (`current_level`)
   * For each node, enqueue its `left` and `right` children
   * Append `"None"` if a child is missing

2. **Pretty-print each level** with spacing:

   * Space depends on the level depth
   * Example output:

     ```
           10
       7      20
     3  12   8  22
     ...
     ```

---

## 🔷 4. Function: `repair_bst(tree)`

```
def repair_bst(tree):
    ...
```

### ✅ Purpose:

Fixes a **corrupted BST** in which two nodes were accidentally swapped.

### ✅ Constraints:

* Time: O(n)
* Space: O(h) — where `h` is height of the tree

---

### 💡 Logic:

In a **correct BST**, an **in-order traversal** gives sorted values.
So, if two values are swapped, the in-order traversal will **violate the ascending order rule** **once or twice**.

### 🔁 Steps:

1. **Use in-order traversal (left → root → right)** with a manual stack:

   ```
   while current_node is not None or len(stack) > 0:
   ```

2. **Track nodes** where order is violated:

   ```
   if previous_node is not None and previous_node.value > current_node.value:
       if node_one is None:
           node_one = previous_node  # First wrong node
       node_two = current_node      # Second wrong node (can be updated)
   ```

3. **After traversal, swap values of node_one and node_two**:

   ```
   node_one.value, node_two.value = node_two.value, node_one.value
   ```

---

## 🔷 5. Tree Data and Execution

```
input_data = {
    ...
}
```

The input dictionary describes the tree structure with node IDs and pointers to child node IDs.

In the example:

* Node `12` and `8` are wrongly placed.
* So, the in-order traversal becomes:

  ```
  [2, 3, 7, 12, 10, 8, 20, 14, 22] ❌
  ```

After `repair_bst()` is applied, it becomes:

```
[2, 3, 7, 8, 10, 12, 20, 14, 22] ✅

(Note: 14 might still be in wrong place, but only 2 nodes are assumed swapped)
```

---

## 🔚 Summary of Flow

```
1. Input dictionary ➝ build_tree() ➝ BST structure created
2. print_tree() ➝ Shows initial corrupted BST
3. repair_bst() ➝ Fixes the two swapped nodes in-place
4. print_tree() again ➝ Shows repaired BST
```

---

## ✅ Output Before and After

### Before Repair:

```
        10
    7         20
  3   12   8     22
2  None None 14 None None None None
```

### After Repair:

```
        10
    7         20
  3   8   12     22
2  None None 14 None None None None
```

---

Here's an **ASCII visualization** of the Binary Search Tree before and after running `repair_bst`.

---

## 🌳 Input Tree (Before Repair)

```
              10
           /      \
         7         20
       /   \     /    \
     3     12   8     22
    /             \
   2              14
```

### 🔎 What's wrong?

* `12` (right child of 7) and `8` (left child of 20) are **swapped**.
* In a valid BST, all left-side nodes should be **less than** their parents, and right-side nodes **greater than**.
* `12` is greater than `10` but is placed in the left subtree.
* `8` is less than `10` but is placed in the right subtree.

---

## 🔧 Repaired Tree (After `repair_bst()`)

```
              10
           /      \
         7         20
       /   \     /    \
     3     8   12     22
    /             \
   2              14
```

### ✅ What's fixed?

* Now:

  * `8` is the right child of 7 (makes sense as `8 > 7`).
  * `12` is the left child of 20 (makes sense as `12 < 20`).
* This is now a **valid BST**.

"""
