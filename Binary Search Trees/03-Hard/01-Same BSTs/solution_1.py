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
    """
    Determines if two arrays represent the same Binary Search Tree (BST).

    Args:
        array_one: First array representing BST nodes in insertion order
        array_two: Second array representing BST nodes in insertion order

    Returns:
        bool: True if both arrays represent the same BST, False otherwise
    """

    # First check: if arrays have different lengths, they can't represent same BST
    if len(array_one) != len(array_two):
        return False

    # Base case: empty arrays are considered same BSTs
    if len(array_one) == 0 and len(array_two) == 0:
        return True

    # Root values must be equal for BSTs to be same
    if array_one[0] != array_two[0]:
        return False

    # Get all elements less than root (left subtree) for both arrays
    left_one = get_smaller(array_one)
    left_two = get_smaller(array_two)

    # Get all elements greater than or equal to root (right subtree) for both arrays
    right_one = get_bigger_or_equal(array_one)
    right_two = get_bigger_or_equal(array_two)

    # Recursively check if both left and right subtrees are same BSTs
    return same_bsts(left_one, left_two) and same_bsts(right_one, right_two)


def get_smaller(array):
    """
    Helper function to get all elements smaller than the first element (root).

    Args:
        array: Input array representing a BST

    Returns:
        list: Elements smaller than root (left subtree elements)
    """
    smaller = []
    # Start from index 1 since index 0 is the root
    for i in range(1, len(array)):
        if array[i] < array[0]:
            smaller.append(array[i])

    return smaller


def get_bigger_or_equal(array):
    """
    Helper function to get all elements greater than or equal to the first element (root).

    Args:
        array: Input array representing a BST

    Returns:
        list: Elements greater than or equal to root (right subtree elements)
    """
    bigger_or_equal = []
    # Start from index 1 since index 0 is the root
    for i in range(1, len(array)):
        if array[i] >= array[0]:
            bigger_or_equal.append(array[i])

    return bigger_or_equal


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

Let's analyze the time and space complexity of the `same_bsts` function.

### Time Complexity:

1. **Base Cases**: The base cases (checking lengths and root values) are all O(1) operations.
2. **Splitting Arrays**: The `get_smaller` and `get_bigger_or_equal` functions both iterate over the array
(excluding the first element) to partition the elements into left and right subtrees. This is O(n) for each call,
where `n` is the length of the current array.
3. **Recursive Calls**: The function makes two recursive calls, one for the left subtrees and one for the right subtrees.
In the worst case, the array could be split unevenly (e.g., all elements are smaller or all are bigger than the root),
leading to a depth of recursion of `n` (degenerate tree). However, on average, for balanced BSTs, the depth is log(n).

- **Worst Case (Unbalanced Trees)**: O(n²)  
  - Each level of recursion processes a subarray of size `n-1`, `n-2`, ..., `1`, leading to a total of O(n²) operations.
- **Average Case (Balanced Trees)**: O(n log n)  
  - The array is split roughly in half at each level, leading to log(n) levels, each doing O(n) work (for partitioning).

### Space Complexity:

1. **Auxiliary Arrays**: The `get_smaller` and `get_bigger_or_equal` functions create new arrays for the left and right subtrees,
which requires O(n) space per recursive call.
2. **Recursion Stack**: The depth of the recursion stack depends on the height of the tree.
   - **Worst Case (Unbalanced Trees)**: O(n) space for the recursion stack.
   - **Average Case (Balanced Trees)**: O(log n) space for the recursion stack.

- **Worst Case (Unbalanced Trees)**: O(n²)  
  - Each recursive call creates O(n) space, and there are O(n) such calls.
- **Average Case (Balanced Trees)**: O(n log n)  
  - Each level of recursion requires O(n) space (sum of all subarrays at that level), and there are O(log n) levels.

### Final Answer:

- **Time Complexity**: O(n²) in the worst case, O(n log n) on average.
- **Space Complexity**: O(n²) in the worst case, O(n log n) on average (due to auxiliary arrays).  
  (Can be optimized to O(n) worst-case and O(log n) average space complexity with an index-based approach.)

### Optimizations:

The current approach uses extra space for creating subarrays. An optimized approach could use indices to represent subarrays
in the original array, reducing space complexity to O(d) (where `d` is the depth of recursion) for the recursion stack, without
creating new arrays. This would make the space complexity O(n) in the worst case and O(log n) on average, while the time
complexity remains the same.

"""
