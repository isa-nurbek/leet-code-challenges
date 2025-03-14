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
    result = []  # This will store the elements in spiral order

    # Initialize boundaries for the spiral
    start_row, end_row = 0, len(array) - 1  # Start and end rows
    start_col, end_col = 0, len(array[0]) - 1  # Start and end columns

    # Loop until all layers of the spiral are traversed
    while start_row <= end_row and start_col <= end_col:
        # Traverse from left to right along the current top row
        for col in range(start_col, end_col + 1):
            result.append(array[start_row][col])

        # Traverse from top to bottom along the current right column
        for row in range(start_row + 1, end_row + 1):
            result.append(array[row][end_col])

        # Traverse from right to left along the current bottom row (if applicable)
        for col in reversed(range(start_col, end_col)):
            if start_row == end_row:
                break  # Avoid duplicate traversal if only one row is left
            result.append(array[end_row][col])

        # Traverse from bottom to top along the current left column (if applicable)
        for row in reversed(range(start_row + 1, end_row)):
            if start_col == end_col:
                break  # Avoid duplicate traversal if only one column is left
            result.append(array[row][start_col])

        # Move the boundaries inward to process the next inner layer of the spiral
        start_row += 1
        end_row -= 1
        start_col += 1
        end_col -= 1

    return result  # Return the elements in spiral order


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
