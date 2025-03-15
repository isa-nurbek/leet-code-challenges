# Problem Description:

"""

                                        # Spiral Traverse

Write a function that takes in an `n x m` two-dimensional array (that can be square-shaped when `n == m`) and returns
a one-dimensional array of all the array's elements in spiral order.

Spiral order starts at the top left corner of the two-dimensional array, goes to the right, and proceeds in a spiral
pattern all the way until every element has been visited.


## Sample Input:
```
array = [
  [1,   2,  3, 4],
  [12, 13, 14, 5],
  [11, 16, 15, 6],
  [10,  9,  8, 7],
]
```

## Sample Output:
```
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
```

## Optimal Time & Space Complexity:
```
O(n) time | O(n) space - where `n` is the total number of elements in the array.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n) time | O(n) space - where `n` is the total number of elements in the array.
def spiral_traverse(array):
    # Initialize an empty list to store the result of the spiral traversal
    result = []
    # Call the helper function to fill the result list in a spiral order
    spiral_fill(array, 0, len(array) - 1, 0, len(array[0]) - 1, result)

    return result


def spiral_fill(array, start_row, end_row, start_col, end_col, result):
    # Base case: If the start row/column is greater than the end row/column, we stop the recursion
    if start_row > end_row or start_col > end_col:
        return

    # Traverse from the start column to the end column in the current start row
    for col in range(start_col, end_col + 1):
        result.append(array[start_row][col])

    # Traverse from the start row + 1 to the end row in the current end column
    for row in range(start_row + 1, end_row + 1):
        result.append(array[row][end_col])

    # Traverse from the end column - 1 back to the start column in the current end row
    # Only if the start row is not equal to the end row (to avoid duplicate traversal)
    for col in reversed(range(start_col, end_col)):
        if start_row == end_row:
            break  # Avoid duplicate traversal if the current layer is a single row

        result.append(array[end_row][col])

    # Traverse from the end row - 1 back to the start row + 1 in the current start column
    # Only if the start column is not equal to the end column (to avoid duplicate traversal)
    for row in reversed(range(start_row + 1, end_row)):
        if start_col == end_col:
            break  # Avoid duplicate traversal if the current layer is a single column

        result.append(array[row][start_col])

    # Recursively call the function to traverse the next inner layer of the spiral
    spiral_fill(array, start_row + 1, end_row - 1, start_col + 1, end_col - 1, result)


# Test cases:
array = [
    [1, 2, 3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10, 9, 8, 7],
]

array_2 = [
    [1, 2, 3],
    [8, 9, 4],
    [7, 6, 5],
]

array_3 = [
    [1],
]

print(spiral_traverse(array))
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

print(spiral_traverse(array_2))
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(spiral_traverse(array_3))
# Output: [1]

# =========================================================================================================================== #
