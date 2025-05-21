# Problem Description:

"""
                                                Reconstruct BST

The pre-order traversal of a Binary Tree is a traversal technique that starts at the tree's root node and visits nodes in the
following order:

1. Current node
2. Left subtree
3. Right subtree

Given a `non-empty` array of integers representing the `pre-order traversal` of a `Binary Search Tree (BST)`, write a function that
creates the relevant BST and returns its root node.

The input array will contain the values of BST nodes in the order in which these nodes would be visited with a pre-order traversal.

Each `BST` node has an integer `value`, a `left` child node, and a `right` child node. A node is said to be a valid `BST` node if
and only if it satisfies the `BST` property: its `value` is strictly greater than the values of every node to its left; its `value`
is less than or equal to the values of every node to its right; and its children nodes are either valid `BST` nodes themselves or `None`.


## Sample Input:
```
pre_order_traversal_values = [10, 4, 2, 1, 5, 17, 19, 18]
```

## Sample Output:
```
        10 
      /    \
     4      17
   /   \      \
  2     5     19
 /           /
1           18 
```

## Optimal Time & Space Complexity:
```
O(n) time | O(n) space - where `n` is the length of the input array.
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


# O(n) time | O(n) space
def reconstruct_bst(pre_order_traversal_values):
    """
    Reconstructs a Binary Search Tree (BST) from its pre-order traversal values.

    Args:
        pre_order_traversal_values: List of integers representing the pre-order traversal of a BST

    Returns:
        The root node of the reconstructed BST
    """

    def helper(lower_bound, upper_bound):
        """
        Helper function to recursively build the BST.

        Args:
            lower_bound: The minimum value a node in this subtree can have
            upper_bound: The maximum value a node in this subtree can have

        Returns:
            A BST node or None if no valid node can be created
        """
        nonlocal idx  # Use the idx variable from the outer function

        # If we've processed all values, return None (base case)
        if idx >= len(pre_order_traversal_values):
            return None

        current_value = pre_order_traversal_values[idx]

        # Check if current value is within valid BST bounds for this position
        if not (lower_bound <= current_value < upper_bound):
            return None  # Not a valid BST node here

        # Move to next value in pre-order list since we're using this one
        idx += 1

        # Recursively build left subtree with updated bounds:
        # - Left subtree values must be greater than lower_bound
        # - But less than current node's value
        left_subtree = helper(lower_bound, current_value)

        # Recursively build right subtree with updated bounds:
        # - Right subtree values must be greater than current node's value
        # - But less than upper_bound
        right_subtree = helper(current_value, upper_bound)

        # Create and return the current node with its subtrees
        return BST(current_value, left_subtree, right_subtree)

    # Initialize index to start of pre-order list
    idx = 0

    # Start the reconstruction with infinite bounds that will get refined
    return helper(float("-inf"), float("inf"))


def in_order_traversal(tree):
    """
    Performs in-order traversal (left -> root -> right) and prints node values.
    For a BST, this should print values in sorted order.
    """
    if tree is not None:
        in_order_traversal(tree.left)
        print(tree.value, end=" ")
        in_order_traversal(tree.right)


# Test Case:

pre_order = [10, 4, 2, 1, 5, 17, 19, 18]
tree = reconstruct_bst(pre_order)

in_order_traversal(tree)  # Output: 1 2 4 5 10 17 18 19

# Visual representation of the reconstructed tree:
#         10
#        /  \
#       4    17
#      / \    \
#     2   5    19
#    /        /
#   1        18

# =========================================================================================================================== #

# Big O Analysis:

"""
# Time and Space Complexity Analysis:

### Time Complexity Analysis

The time complexity of this algorithm is **O(N)**, where **N** is the number of nodes in the BST.

Here's why:

1. **Each node is visited exactly once**: The algorithm processes each element in the `pre_order_traversal_values` array exactly
once. The `idx` variable ensures that no element is revisited after it's processed.

2. **Constant work per node**: For each node, the algorithm performs a constant amount of work (checking bounds, incrementing `idx`,
and making recursive calls).

3. **No redundant work**: The bounds (`lower_bound` and `upper_bound`) ensure that the algorithm does not explore invalid paths,
making the traversal efficient.

Thus, the total time complexity is linear in the number of nodes.

---

### Space Complexity Analysis

The space complexity is **O(N)** in the worst case and **O(H)** in the average case (where **H** is the height of the BST).

Here's why:

1. **Recursion stack space**: The algorithm uses recursion, so the maximum depth of the call stack determines the space complexity.
   - In the **worst case** (a skewed tree, e.g., a linked list), the recursion depth is **O(N)**.
   - In the **average case** (a balanced BST), the recursion depth is **O(log N)** (since the height of a balanced BST is logarithmic in the number of nodes).
2. **Output space**: The space required to store the reconstructed BST is **O(N)**, but this is typically considered separate
from the auxiliary space used by the algorithm.

Thus:
- **Worst-case space complexity (skewed tree)**: **O(N)** (due to recursion stack).
- **Average-case space complexity (balanced BST)**: **O(log N)**.

If we consider the space required for the output BST, then it is always **O(N)** (since we need to store all nodes), but this is
usually considered separate from the algorithm's auxiliary space.

---

### Summary
- **Time Complexity**: **O(N)** (linear time, each node processed once).
- **Space Complexity**:
  - **Worst case (skewed tree)**: **O(N)** (recursion stack).
  - **Best/average case (balanced BST)**: **O(log N)** (recursion stack proportional to tree height).

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
Let's go step by step to **understand the code**, **how it works**, and **why it reconstructs a Binary Search Tree (BST)
correctly from a preorder traversal**.

---

## 🌳 Problem Summary

You're given a list of integers that represents the **pre-order traversal** of a Binary Search Tree (BST). You need to reconstruct
the **original BST** from this list.

---

## 📌 What is Preorder Traversal?

In **preorder traversal**, nodes are visited in this order:

```
Root → Left → Right
```

So, given:

```
pre_order = [10, 4, 2, 1, 5, 17, 19, 18]
```

This means:

* `10` is the **root**
* The values that come **after** 10 and are **less than 10** belong to the **left subtree**
* The values that are **greater than 10** belong to the **right subtree**

---

## 🔍 Breakdown of the Code

### 1. Class Definition

```
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
```

This is a basic Binary Search Tree node:

* `value`: stores the node’s value.
* `left`: reference to left child.
* `right`: reference to right child.

---

### 2. `reconstruct_bst(pre_order_traversal_values)`

This is the main function that reconstructs the tree from a preorder traversal list.

#### Key Concepts Used:

* You use an **index pointer `idx`** to iterate through the preorder list.
* You use **boundaries** (`lower_bound` and `upper_bound`) to determine if a value fits in the current position of the BST.

#### Function Structure:

```
def reconstruct_bst(pre_order_traversal_values):
    def helper(lower_bound, upper_bound):
        nonlocal idx
        ...
    idx = 0
    return helper(float("-inf"), float("inf"))
```

The `helper` is a recursive function that:

* Uses `lower_bound` and `upper_bound` to ensure the BST properties are followed.
* Builds the left and right subtrees recursively.

---

## 🧠 How the `helper()` Works

```
def helper(lower_bound, upper_bound):
    nonlocal idx
```

You keep `idx` as a **shared state** across recursive calls (using `nonlocal`).

```
    if idx >= len(pre_order_traversal_values):
        return None
```

* Base case: If you reach the end of the list, stop.

```
    current_value = pre_order_traversal_values[idx]
    if not (lower_bound <= current_value < upper_bound):
        return None
```

* Each recursive call has a valid range (`lower_bound`, `upper_bound`) where the current node value must fall.
* If the current value is out of this range, **it doesn’t belong** in this subtree, so return `None`.

```
    idx += 1
    left_subtree = helper(lower_bound, current_value)
    right_subtree = helper(current_value, upper_bound)
```

* Increment `idx` to move to the next node in preorder list.
* Recursively construct the left subtree first (`left = helper(...)`)
* Then the right subtree.

```
    return BST(current_value, left_subtree, right_subtree)
```

* Finally, return the constructed node with its left and right children.

---

### 3. `in_order_traversal(tree)`

```
def in_order_traversal(tree):
    if tree is not None:
        in_order_traversal(tree.left)
        print(tree.value, end=" ")
        in_order_traversal(tree.right)
```

* This prints nodes in **ascending order** (for BSTs).
* So if the BST was constructed correctly, the output should be sorted.

---

## ✅ Example Input

```
pre_order = [10, 4, 2, 1, 5, 17, 19, 18]
```

This represents:

```
Preorder:
10 → Root
4, 2, 1, 5 → Left subtree
17, 19, 18 → Right subtree
```

Reconstructed Tree:

```
        10
       /  \
      4    17
     / \     \
    2   5     19
   /         /
  1         18
```

---

## 🧾 Output of `in_order_traversal(tree)`

```
1 2 4 5 10 17 18 19
```

Which confirms the BST was reconstructed correctly!

---

## ⏱ Time and Space Complexity

### Time: **O(n)**

* You visit each node **once** using a single `idx` pointer.

### Space: **O(n)**

* Due to recursion stack (in the worst case for skewed trees).
* Plus, `n` nodes in the resulting BST.

---

## 🧠 Summary

* You're reconstructing a BST from its preorder traversal using **bounds to enforce BST rules**.
* The helper function uses **recursive depth-first construction**, and `idx` ensures you process each node **only once**
in the correct order.
* In-order traversal is a great way to verify correctness, as it should always print a sorted list for a valid BST.

---

Here's an **ASCII visualization** of the reconstructed BST from the preorder traversal:

```
pre_order = [10, 4, 2, 1, 5, 17, 19, 18]
```

---

### 🌳 ASCII Tree:

```
         10
        /  \
       4    17
      / \     \
     2   5     19
    /         /
   1         18
```

---

### 🧭 How to Read It:

* Each node is **indented** to represent its depth in the tree.
* **Left children** are placed to the left, **right children** to the right.
* The structure respects **BST rules**:

  * Left subtree contains values `< parent`
  * Right subtree contains values `> parent`

"""
