# Problem Description:

"""
                                                Same BSTs

An array of integers is said to represent the `Binary Search Tree (BST)` obtained by inserting each integer in the array, from left
to right, into the `BST`.

Write a function that takes in two arrays of integers and determines whether these arrays represent the same `BST`.

Note that you're not allowed to construct any `BST`s in your code.

A `BST` is a `Binary Tree` that consists only of `BST` nodes. A node is said to be a valid `BST` node if and only if it satisfies
the `BST` property: its value is strictly greater than the values of every node to its left; its value is less than or equal to the
values of every node to its right; and its children nodes are either valid `BST` nodes themselves or `None`.


## Sample Input:
```
array_one = [10, 15, 8, 12, 94, 81, 5, 2, 11]
array_two = [10, 8, 5, 15, 2, 12, 11, 94, 81]
```

## Sample Output:
```
True 
// Both arrays represent the BST below

          10
       /     \
      8      15
    /       /   \
   5      12    94
 /       /     /
2       11    81
```

## Optimal Time & Space Complexity:
```
O(n²) time | O(d) space - where `n` is the number of nodes in each array, respectively, and `d` is the depth
of the BST that they represent.
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


# O(n²) time | O(d) space
def same_bsts(array_one, array_two):
    # First check if the arrays have the same length - if not, BSTs can't be same
    if len(array_one) != len(array_two):
        return False
    # Start the recursive helper function with initial parameters
    return _same_bsts_helper(array_one, array_two, 0, 0, float("-inf"), float("inf"))


def _same_bsts_helper(
    array_one, array_two, root_idx_one, root_idx_two, min_val, max_val
):
    """
    Recursive helper function to determine if two arrays represent the same BST.

    Parameters:
    - array_one, array_two: The input arrays representing BST insertions
    - root_idx_one, root_idx_two: Current root indices being compared
    - min_val, max_val: The valid range for child nodes of current root
    """

    # If both roots are -1 (no children), return True (base case)
    if root_idx_one == -1 and root_idx_two == -1:
        return True

    # If one root exists but the other doesn't, trees are different
    if (root_idx_one == -1) != (root_idx_two == -1):
        return False

    # If root values don't match, trees are different
    if array_one[root_idx_one] != array_two[root_idx_two]:
        return False

    # Find the index of first element in array_one that would be in left subtree
    left_root_one = _find_next_smaller(array_one, root_idx_one, min_val)
    # Find the index of first element in array_two that would be in left subtree
    left_root_two = _find_next_smaller(array_two, root_idx_two, min_val)

    # Find the index of first element in array_one that would be in right subtree
    right_root_one = _find_next_larger_or_equal(array_one, root_idx_one, max_val)
    # Find the index of first element in array_two that would be in right subtree
    right_root_two = _find_next_larger_or_equal(array_two, root_idx_two, max_val)

    # Recursively check both left and right subtrees:
    # For left subtrees: update max_val to current root's value (left must be smaller)
    # For right subtrees: update min_val to current root's value (right must be larger/equal)
    return _same_bsts_helper(
        array_one,
        array_two,
        left_root_one,
        left_root_two,
        min_val,
        array_one[root_idx_one],
    ) and _same_bsts_helper(
        array_one,
        array_two,
        right_root_one,
        right_root_two,
        array_one[root_idx_one],
        max_val,
    )


def _find_next_smaller(array, start_idx, min_val):
    """
    Finds the index of the first element after start_idx that is:
    - Smaller than array[start_idx] (would be in left subtree)
    - Greater than or equal to min_val (within valid range)
    Returns -1 if no such element found
    """
    for i in range(start_idx + 1, len(array)):
        if array[i] < array[start_idx] and array[i] >= min_val:
            return i
    return -1


def _find_next_larger_or_equal(array, start_idx, max_val):
    """
    Finds the index of the first element after start_idx that is:
    - Greater than or equal to array[start_idx] (would be in right subtree)
    - Less than or equal to max_val (within valid range)
    Returns -1 if no such element found
    """
    for i in range(start_idx + 1, len(array)):
        if array[i] >= array[start_idx] and array[i] <= max_val:
            return i
    return -1


# Test Case:

array_one = [10, 15, 8, 12, 94, 81, 5, 2, 11]
array_two = [10, 8, 5, 15, 2, 12, 11, 94, 81]

print(same_bsts(array_one, array_two))  # Output: True

# Both arrays represent the BST below
#           10
#        /     \
#       8      15
#     /       /   \
#    5      12    94
#  /       /     /
# 2       11    81

# =========================================================================================================================== #

# Big O Analysis:

"""
# Time and Space Complexity Analysis:

### Time Complexity Analysis

Let's analyze the time and space complexity of the given same_bsts function.

1. **Initial Check**: The initial length check `if len(array_one) != len(array_two)` is an O(1) operation.

2. **Helper Function `_same_bsts_helper`**:
   - The helper function is called recursively for each node in the BST.
   - For each node, we perform two searches:
     - `_find_next_smaller`: This function scans the array from `start_idx + 1` to the end to find the first element that is
     smaller than `array[start_idx]` and >= `min_val`. In the worst case, this is O(n) for each call.
     - `_find_next_larger_or_equal`: Similarly, this scans the array from `start_idx + 1` to the end to find the first element
     that is >= `array[start_idx]` and <= `max_val`. This is also O(n) for each call.
   - These searches are performed for each node in the BST, and in the worst case, the BST could be a degenerate tree
   (a linked list), leading to O(n) recursive calls.
   - Therefore, the total time complexity is O(n²) in the worst case.

3. **Best Case**: If the BST is balanced, the depth of recursion is O(log n), and the total time complexity would be O(n log n),
since at each level of the tree, we process O(n) elements in total across all nodes at that level.

### Space Complexity Analysis

1. **Recursion Stack**:
   - The space complexity is determined by the depth of the recursion stack.
   - In the worst case (degenerate tree), the recursion depth is O(n), leading to O(n) space.
   - In the best case (balanced tree), the recursion depth is O(log n), leading to O(log n) space.

2. **Additional Space**:
   - No additional data structures are used that grow with the input size, so the space complexity is dominated by the recursion stack.

### Summary

- **Time Complexity**:
  - Worst Case: O(n²) (degenerate tree)
  - Best Case: O(n log n) (balanced tree)
  
- **Space Complexity**:
  - Worst Case: O(n) (degenerate tree)
  - Best Case: O(log n) (balanced tree)

### Optimizations

The current approach is correct but can be optimized to O(n) time by avoiding repeated scans of the array. One way to do this is by
using pointers or iterators to track the current position in the array for each subtree, but this would require a more sophisticated
approach or preprocessing (e.g., building the BST and comparing directly). However, the current approach is straightforward and
works for the problem constraints where the arrays are small to moderate in size.

"""
