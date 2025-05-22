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


# O(n) time | O(d) space
def same_bsts(array_one, array_two):
    # If the arrays have different lengths, they can't form same BST
    if len(array_one) != len(array_two):
        return False

    # If both arrays are empty, they represent same BST (empty tree)
    if not array_one:
        return True

    # The root values must be equal for the BSTs to be same
    if array_one[0] != array_two[0]:
        return False

    # Create dictionaries to map values to their positions in each array
    pos_one = {val: idx for idx, val in enumerate(array_one)}
    pos_two = {val: idx for idx, val in enumerate(array_two)}

    # Initialize a stack for iterative traversal of both BSTs
    stack = []
    # Each stack element contains:
    # - current value from array_one
    # - current value from array_two
    # - min bound for valid values in subtree
    # - max bound for valid values in subtree
    stack.append((array_one[0], array_two[0], float("-inf"), float("inf")))

    # Track which indices we've already used in each array
    used_one, used_two = set(), set()
    used_one.add(0)
    used_two.add(0)

    while stack:
        val_one, val_two, min_val, max_val = stack.pop()

        # Find left child in array_one (first value after current that's
        # less than current but >= min bound)
        left_one = None
        for i in range(pos_one[val_one] + 1, len(array_one)):
            if array_one[i] < val_one and array_one[i] >= min_val and i not in used_one:
                left_one = array_one[i]
                used_one.add(i)
                break

        # Find left child in array_two with same criteria
        left_two = None
        for i in range(pos_two[val_two] + 1, len(array_two)):
            if array_two[i] < val_two and array_two[i] >= min_val and i not in used_two:
                left_two = array_two[i]
                used_two.add(i)
                break

        # If one has left child but other doesn't, trees are different
        if (left_one is None) != (left_two is None):
            return False
        # If both have left children, they must be equal
        if left_one is not None:
            if left_one != left_two:
                return False
            # Push left children to stack with updated bounds
            stack.append((left_one, left_two, min_val, val_one))

        # Find right child in array_one (first value after current that's
        # >= current but <= max bound)
        right_one = None
        for i in range(pos_one[val_one] + 1, len(array_one)):
            if (
                array_one[i] >= val_one
                and array_one[i] <= max_val
                and i not in used_one
            ):
                right_one = array_one[i]
                used_one.add(i)
                break

        # Find right child in array_two with same criteria
        right_two = None
        for i in range(pos_two[val_two] + 1, len(array_two)):
            if (
                array_two[i] >= val_two
                and array_two[i] <= max_val
                and i not in used_two
            ):
                right_two = array_two[i]
                used_two.add(i)
                break

        # If one has right child but other doesn't, trees are different
        if (right_one is None) != (right_two is None):
            return False

        # If both have right children, they must be equal
        if right_one is not None:
            if right_one != right_two:
                return False
            # Push right children to stack with updated bounds
            stack.append((right_one, right_two, val_one, max_val))

    # If we processed all nodes without mismatches, trees are same
    return True


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
