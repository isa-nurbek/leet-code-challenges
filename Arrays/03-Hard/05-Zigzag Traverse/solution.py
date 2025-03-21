# Problem Description:

"""

                                                # Zigzag Traverse

Write a function that takes in an n x m two-dimensional array (that can be square-shaped when n == m) and returns a one-dimensional
array of all the array's elements in zigzag order.

Zigzag order starts at the top left corner of the two-dimensional array, goes down by one element, and proceeds in a zigzag pattern
all the way to the bottom right corner.


## Sample Input:
```
array = [
  [1,  3,  4, 10],
  [2,  5,  9, 11],
  [6,  8, 12, 15],
  [7, 13, 14, 16],
]
```

## Sample Output:
```
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
```

## Optimal Time & Space Complexity:
```
O(n) time | O(n) space - where `n` is the total number of elements in the two-dimensional array.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n) time | O(n) space
def zigzag_traverse(array):
    # Determine the height and width of the 2D array
    height = len(array) - 1  # Last row index
    width = len(array[0]) - 1  # Last column index

    # Initialize an empty list to store the result of the traversal
    result = []

    # Start from the top-left corner of the array (first element)
    row, col = 0, 0

    # A flag to indicate the direction of traversal:
    # `going_down = True` means we're moving diagonally down,
    # `going_down = False` means we're moving diagonally up.
    going_down = True

    # Loop until we go out of bounds (i.e., traverse the entire array)
    while not is_out_of_bounds(row, col, height, width):
        # Append the current element to the result list
        result.append(array[row][col])

        # If we're moving diagonally down
        if going_down:
            # Check if we've hit the left wall or the bottom row
            if col == 0 or row == height:
                # Change direction to move diagonally up
                going_down = False

                # If we're at the bottom row, move right
                if row == height:
                    col += 1
                # Otherwise, move down
                else:
                    row += 1
            else:
                # Move diagonally down-left
                row += 1
                col -= 1
        # If we're moving diagonally up
        else:
            # Check if we've hit the top row or the right wall
            if row == 0 or col == width:
                # Change direction to move diagonally down
                going_down = True

                # If we're at the right wall, move down
                if col == width:
                    row += 1
                # Otherwise, move right
                else:
                    col += 1
            else:
                # Move diagonally up-right
                row -= 1
                col += 1

    # Return the result of the zigzag traversal
    return result


# Helper function to check if the current position is out of bounds
def is_out_of_bounds(row, col, height, width):
    return row < 0 or row > height or col < 0 or col > width


# Test Cases:

array = [
    [1, 3, 4, 10],
    [2, 5, 9, 11],
    [6, 8, 12, 15],
    [7, 13, 14, 16],
]

array_2 = [[1, 2, 3, 4, 5]]

array_3 = [[1]]


print(zigzag_traverse(array))
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

print(zigzag_traverse(array_2))
# Output: [1, 2, 3, 4, 5]

print(zigzag_traverse(array_3))
# Output: [1]

# =========================================================================================================================== #
