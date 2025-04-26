# Problem Description:

"""

                                            Solve Sudoku

You're given a two-dimensional array that represents a `9x9` partially filled Sudoku board. Write a function that returns the
solved Sudoku board.

Sudoku is a famous number-placement puzzle in which you need to fill a `9x9` grid with integers in the range of `1-9`. Each `9x9`
Sudoku board is split into `9`, `3x3` subgrids, as seen in the illustration below, and starts out partially filled.

```
- - 3 | - 2 - | 6 - -
9 - - | 3 - 5 | - - 1
- - 1 | 8 - 6 | 4 - -
- - - - - - - - - - -
- - 8 | 1 - 2 | 9 - -
7 - - | - - - | - - 8
- - 6 | 7 - 8 | 2 - -
- - - - - - - - - - -
- - 2 | 6 - 9 | 5 - -
8 - - | 2 - 3 | - - 9
- - 5 | - 1 - | 3 - -
```

The objective is to fill the grid such that each row, column, and `3x3` subgrid contains the numbers `1-9` exactly once. In other
words, no row may contain the same digit more than once, no column may contain the same digit more than once, and none of the `9`,
`3x3` subgrids may contain the same digit more than once.

Your input for this problem will always be a partially filled `9x9` two-dimensional array that represents a solvable Sudoku puzzle.
Every element in the array will be an integer in the range of `0-9`, where a `0` represents an empty square that must be filled by
your algorithm.

Note that you may modify the input array and that there will always be exactly one solution to each input Sudoku board.


## Sample Input
```
board =
[
  [7, 8, 0, 4, 0, 0, 1, 2, 0],
  [6, 0, 0, 0, 7, 5, 0, 0, 9],
  [0, 0, 0, 6, 0, 1, 0, 7, 8],
  [0, 0, 7, 0, 4, 0, 2, 6, 0],
  [0, 0, 1, 0, 5, 0, 9, 3, 0],
  [9, 0, 4, 0, 6, 0, 0, 0, 5],
  [0, 7, 0, 3, 0, 0, 0, 1, 2],
  [1, 2, 0, 0, 0, 7, 4, 0, 0],
  [0, 4, 9, 2, 0, 6, 0, 0, 7],
]
```

## Sample Output
```
[
  [7, 8, 5, 4, 3, 9, 1, 2, 6],
  [6, 1, 2, 8, 7, 5, 3, 4, 9],
  [4, 9, 3, 6, 2, 1, 5, 7, 8],
  [8, 5, 7, 9, 4, 3, 2, 6, 1],
  [2, 6, 1, 7, 5, 8, 9, 3, 4],
  [9, 3, 4, 1, 6, 2, 7, 8, 5],
  [5, 7, 8, 3, 9, 4, 6, 1, 2],
  [1, 2, 6, 5, 8, 7, 4, 9, 3],
  [3, 4, 9, 2, 1, 6, 8, 5, 7],
]
```

## Optimal Time & Space Complexity:
```
O(1) time | O(1) space - assuming a `9x9` input board.
```
"""

# =========================================================================================================================== #

# Solution:


# O(1) time | O(1) space
def solve_sudoku(board):
    """Main function to solve the Sudoku puzzle.
    Starts the solving process from the top-left corner (0,0) and returns the solved board.
    """
    solve_partial_sudoku(0, 0, board)
    return board


def solve_partial_sudoku(row, col, board):
    """Recursive function to solve the Sudoku puzzle starting from a specific position.
    Handles moving through the board and deciding when to place numbers."""
    current_row = row
    current_col = col

    # If we've reached the end of a row, move to the start of the next row
    if current_col == len(board[current_row]):
        current_row += 1
        current_col = 0
        # If we've passed the last row, the board is solved
        if current_row == len(board):
            return True

    # If the current cell is empty (0), try placing digits here
    if board[current_row][current_col] == 0:
        return try_digits_at_position(current_row, current_col, board)
    # Otherwise, move to the next cell
    return solve_partial_sudoku(current_row, current_col + 1, board)


def try_digits_at_position(row, col, board):
    """Tries all possible digits (1-9) in a given empty cell.
    Backtracks if a digit leads to an unsolvable board."""
    for digit in range(1, 10):
        if is_valid_at_position(digit, row, col, board):
            # Place the digit temporarily
            board[row][col] = digit
            # Continue solving from the next cell
            if solve_partial_sudoku(row, col + 1, board):
                return True  # If this leads to a solution, return True

    # If no digit worked, reset the cell and backtrack
    board[row][col] = 0
    return False


def is_valid_at_position(value, row, col, board):
    """Checks if a value can be placed at a specific position according to Sudoku rules.
    Returns True if the placement is valid, False otherwise."""
    # Check if the value already exists in the row
    row_is_valid = value not in board[row]
    # Check if the value already exists in the column
    column_is_valid = value not in map(lambda r: r[col], board)

    if not row_is_valid or not column_is_valid:
        return False

    # Check the 3x3 subgrid
    subgrid_row_start = (row // 3) * 3  # Find starting row of the subgrid
    subgrid_col_start = (col // 3) * 3  # Find starting column of the subgrid

    # Check all cells in the 3x3 subgrid
    for row_idx in range(3):
        for col_idx in range(3):
            row_to_check = subgrid_row_start + row_idx
            col_to_check = subgrid_col_start + col_idx
            existing_value = board[row_to_check][col_to_check]
            if existing_value == value:
                return False

    return True  # The value can be placed at this position


# Test Case:

board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7],
]

print(solve_sudoku(board))

# Output:

"""
[
  [7, 8, 5, 4, 3, 9, 1, 2, 6],
  [6, 1, 2, 8, 7, 5, 3, 4, 9],
  [4, 9, 3, 6, 2, 1, 5, 7, 8],
  [8, 5, 7, 9, 4, 3, 2, 6, 1],
  [2, 6, 1, 7, 5, 8, 9, 3, 4],
  [9, 3, 4, 1, 6, 2, 7, 8, 5],
  [5, 7, 8, 3, 9, 4, 6, 1, 2],
  [1, 2, 6, 5, 8, 7, 4, 9, 3],
  [3, 4, 9, 2, 1, 6, 8, 5, 7],
]
"""
