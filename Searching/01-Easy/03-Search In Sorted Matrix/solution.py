# Problem Description:

"""
                                             Search In Sorted Matrix

You're given a `two-dimensional` array (a `matrix`) of distinct integers and a `target` integer. Each row in the matrix is sorted,
and each column is also sorted; the matrix doesn't necessarily have the same height and width.

Write a function that returns an array of the row and column indices of the target integer if it's contained in the matrix,
otherwise `[-1, -1]`.


## Sample Input:
```
matrix = [
  [1, 4, 7, 12, 15, 1000],
  [2, 5, 19, 31, 32, 1001],
  [3, 8, 24, 33, 35, 1002],
  [40, 41, 42, 44, 45, 1003],
  [99, 100, 103, 106, 128, 1004],
]

target = 44
```

## Sample Output:
```
[3, 3]
```

## Optimal Time & Space Complexity:
```
O(n + m) time | O(1) space - where `n` is the length of the matrix's rows and `m` is the length of the matrix's columns.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n + m) time | O(1) space
def search_in_sorted_matrix(matrix, target):
    """
    Searches for a target value in a 2D matrix where:
    - Each row is sorted in ascending order
    - Each column is sorted in ascending order

    Args:
    matrix: List[List[int]] - The 2D sorted matrix to search in
    target: int - The value to search for

    Returns:
    List[int] - The [row, col] indices if found, else [-1, -1]
    """

    # Start from the top-right corner of the matrix
    # This position gives us a "middle" point where:
    # - Moving left decreases values
    # - Moving down increases values
    row = 0
    col = len(matrix[0]) - 1

    # Continue searching while within matrix bounds
    while row < len(matrix) and col >= 0:
        if matrix[row][col] > target:
            # Current value is too large, move left to smaller values
            col -= 1
        elif matrix[row][col] < target:
            # Current value is too small, move down to larger values
            row += 1
        else:
            # Found the target, return its position
            return [row, col]

    # Target not found in matrix
    return [-1, -1]


# Test Case 1:

matrix = [
    [1, 4, 7, 12, 15, 1000],
    [2, 5, 19, 31, 32, 1001],
    [3, 8, 24, 33, 35, 1002],
    [40, 41, 42, 44, 45, 1003],
    [99, 100, 103, 106, 128, 1004],
]

target = 44

print(search_in_sorted_matrix(matrix, target))
# Output: [3, 3]

# Test Case 2:

matrix = [
    [1, 4, 7, 12, 15, 1000],
    [2, 5, 19, 31, 32, 1001],
    [3, 8, 24, 33, 35, 1002],
    [40, 41, 42, 44, 45, 1003],
    [99, 100, 103, 106, 128, 1004],
]

target = 12

print(search_in_sorted_matrix(matrix, target))
# Output: [0, 3]

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### Time Complexity Analysis:

The algorithm starts at the top-right corner of the matrix (or bottom-left could also work) and moves either **left** (to
decrease the value) or **down** (to increase the value) based on the comparison with the `target`.

- **Worst Case**: The algorithm traverses at most one full row and one full column.  
  - For an `m x n` matrix, the maximum steps taken are `m + n - 1` (since you can go from the top-right to the bottom-left corner).  
  - Thus, the time complexity is **O(m + n)**.

### Space Complexity Analysis:

- The algorithm uses a constant amount of extra space (only `row` and `col` variables are modified).  
- Thus, the space complexity is **O(1)**.

### Summary:
- **Time Complexity**: **O(m + n)**  
- **Space Complexity**: **O(1)**  

This is optimal for this problem since in the worst case, you must check at least one full row or column to confirm
the absence of the target.

"""
