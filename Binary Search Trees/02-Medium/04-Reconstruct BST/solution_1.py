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


# O(n²) time | O(n) space
def reconstruct_bst(pre_order_traversal_values):
    """
    Reconstructs a BST from its pre-order traversal values.

    Pre-order traversal visits nodes in the order: root -> left -> right.
    The first element is always the root, followed by left subtree nodes (all < root),
    then right subtree nodes (all >= root).

    Args:
        pre_order_traversal_values: List of values in pre-order traversal order

    Returns:
        The root node of the reconstructed BST
    """
    # Base case: empty list means we've reached a leaf node's child
    if not pre_order_traversal_values:
        return None

    # The first value in pre-order is always the root of current subtree
    current_value = pre_order_traversal_values[0]

    # Initialize the right subtree start index as end of list (case where no right subtree exists)
    right_subtree_root_idx = len(pre_order_traversal_values)

    # Find the first value >= current_value (marks start of right subtree)
    for idx in range(1, len(pre_order_traversal_values)):
        value = pre_order_traversal_values[idx]
        if value >= current_value:
            right_subtree_root_idx = idx
            break  # Found the divider between left and right subtrees

    # Recursively reconstruct left subtree (values between current root and right subtree start)
    left_subtree = reconstruct_bst(pre_order_traversal_values[1:right_subtree_root_idx])
    # Recursively reconstruct right subtree (remaining values after left subtree ends)
    right_subtree = reconstruct_bst(pre_order_traversal_values[right_subtree_root_idx:])

    # Create and return current node with its left and right subtrees
    return BST(current_value, left_subtree, right_subtree)


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

## Time Complexity Analysis

The time complexity of the given `reconstruct_bst` function can be analyzed as follows:

1. **Base Case**: If the input list is empty, the function returns `None` in constant time, O(1).
2. **Recursive Case**:
   - The function processes the first element as the root of the current subtree (O(1)).
   - It then iterates through the remaining elements to find the first value that is greater than or equal to the root value
   (this divides the list into left and right subtrees). In the worst case, this loop runs through all remaining elements (O(n)
   for the current call, where n is the number of elements in the current list).
   - The function then recursively processes the left and right subtrees.

### Worst-Case Time Complexity

- In the worst case, the tree is highly unbalanced (e.g., a linked list), where each recursive call processes one node and
the rest are in the right subtree.
For example:
  - First call: processes root, loops through n-1 elements.
  - Second call: processes next root, loops through n-2 elements.
  - ...
  - Total work: O(n + (n-1) + (n-2) + ... + 1) = O(n²).
- Thus, the worst-case time complexity is **O(n²)**.

### Best-Case Time Complexity

- In the best case, the tree is perfectly balanced. At each level, the loop splits the list roughly in half:
  - Top level: O(n) work to split.
  - Next level: Two calls, each O(n/2) work.
  - Next level: Four calls, each O(n/4) work.
  - ...
  - Total work: O(n log n), similar to the analysis of quicksort with good pivots.
- Thus, the best-case time complexity is **O(n log n)**.

### Average-Case Time Complexity

- For a random BST (where the input is a random permutation of values), the average-case time complexity is **O(n log n)**,
similar to the best case.

### Space Complexity Analysis

The space complexity is determined by:
1. **Recursion Stack**: The maximum depth of the recursion stack.
   - In the worst case (unbalanced tree), the depth is O(n).
   - In the best case (balanced tree), the depth is O(log n).
2. **Output BST**: The space required to store the BST is O(n) (for the nodes), which is unavoidable for the output.

Thus:
- Worst-case space complexity: **O(n)** (due to recursion stack).
- Best-case space complexity: **O(log n)** (due to recursion stack).

### Final Answer

- **Time Complexity**:
  - Worst-case: O(n²)
  - Best-case: O(n log n)
  - Average-case: O(n log n)
  
- **Space Complexity**:
  - Worst-case: O(n)
  - Best-case: O(log n)

### Optimizing the Algorithm

The current implementation has O(n²) worst-case time complexity. This can be optimized to O(n) by:
1. Using a helper function with bounds (min and max) to track valid ranges for subtrees, eliminating the need to scan
for the right subtree root in each step.
2. Processing the pre-order traversal in reverse or with an index, incrementally building the tree.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
Let's break this down step by step.

---

## 🔧 **Class and Function Overview**

### 1. `class BST`:

This is a simple class representing a **node** in a **Binary Search Tree (BST)**.

```
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
```

Each node stores:

* `value`: the integer stored at that node.
* `left`: pointer/reference to the left child node.
* `right`: pointer/reference to the right child node.

---

### 2. `reconstruct_bst(pre_order_traversal_values)`

This is the main function that reconstructs a **Binary Search Tree (BST)** from its **pre-order traversal**.

#### Pre-order Traversal Recap:

* Visit **root** first
* Then recursively visit **left subtree**
* Then recursively visit **right subtree**

---

## 🧠 How the Code Works

Let's go through it in detail.

### Step-by-step breakdown:

```
def reconstruct_bst(pre_order_traversal_values):
    if not pre_order_traversal_values:
        return None
```

* If the list is empty, return `None`. Base case for recursion.

---

```
    current_value = pre_order_traversal_values[0]
```

* The **first value** in the pre-order list is the **root** of the current (sub)tree.

---

```
    right_subtree_root_idx = len(pre_order_traversal_values)

    for idx in range(1, len(pre_order_traversal_values)):
        value = pre_order_traversal_values[idx]
        if value >= current_value:
            right_subtree_root_idx = idx
            break
```

* The rest of the list contains the **left** and **right** subtrees.
* All values **less than `current_value`** will be in the **left subtree**.
* The **first value ≥ `current_value`** indicates the **start of the right subtree**.
* So, we find the **split point** between left and right subtrees.

---

```
    left_subtree = reconstruct_bst(pre_order_traversal_values[1:right_subtree_root_idx])
    right_subtree = reconstruct_bst(pre_order_traversal_values[right_subtree_root_idx:])
```

* Recursively build the **left subtree** from values between index 1 and the split point.
* Recursively build the **right subtree** from values after the split point.

---

```
    return BST(current_value, left_subtree, right_subtree)
```

* Construct and return a new `BST` node with the current value and the left/right subtrees.

---

### 🌳 Helper: `in_order_traversal`

```
def in_order_traversal(tree):
    if tree is not None:
        in_order_traversal(tree.left)
        print(tree.value, end=" ")
        in_order_traversal(tree.right)
```

* This function prints the values of the BST **in in-order traversal**:

  * First visit left subtree
  * Then visit root
  * Then visit right subtree

📌 For a **Binary Search Tree**, in-order traversal will always print the values in **ascending order**.

---

## 🧪 Test Case

```
pre_order = [10, 4, 2, 1, 5, 17, 19, 18]
tree = reconstruct_bst(pre_order)
in_order_traversal(tree)
```

### Tree structure being built:

```
         10
        /  \
       4    17
      / \     \
     2   5     19
    /         /
   1         18
```

### Output:

```
1 2 4 5 10 17 18 19
```

Correct ascending order — confirms the BST is built properly.

---

## ✅ Summary

* **Input**: Pre-order traversal of a BST
* **Goal**: Reconstruct the original BST
* **Method**:

  * Use recursion
  * First value = root
  * Find split index where right subtree starts
  * Recurse for left and right parts
* **Efficiency**: Runs in O(n²) worst-case due to slicing and scanning — can be improved using index bounds for better performance.

---

Here’s a clear **ASCII visualization** of the BST reconstructed from:

```
pre_order = [10, 4, 2, 1, 5, 17, 19, 18]
```

### 🔍 ASCII Tree Diagram:

```
         10
        /  \
       4    17
      / \     \
     2   5     19
    /         /
   1         18
```

### 🌿 Breakdown of Tree Structure:

* `10` is the **root**.
* `4` is on the **left** of `10`.
* `17` is on the **right** of `10`.
* Under `4`:

  * `2` is left of `4`, and `5` is right of `4`.
  * `1` is left of `2`.
* Under `17`:

  * `19` is right of `17`.
  * `18` is left of `19`.

This structure reflects the BST properties:

* Left subtree nodes < root
* Right subtree nodes ≥ root

"""
