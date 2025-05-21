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
