# Problem Description:

"""

                                            Non-Attacking Queens

Write a function that takes in a positive integer `n` and returns the number of non-attacking placements of `n` queens on an
`n x n` chessboard.

A non-attacking placement is one where no queen can attack another queen in a single turn. In other words, it's a placement where
no queen can move to the same position as another queen in a single turn.

In chess, queens can move any number of squares horizontally, vertically, or diagonally in a single turn.

```
+--+--+--+--+
|  |Q |  |  |
+--+--+--+--+
|  |  |  |Q |
+--+--+--+--+
|Q |  |  |  |
+--+--+--+--+
|  |  |Q |  |
+--+--+--+--+
```

The chessboard above is an example of a non-attacking placement of `4` queens on a `4x4` chessboard. For reference, there are
only `2` non-attacking placements of `4` queens on a `4x4` chessboard.


## Sample Input
```
n = 4
```

## Sample Output
```
2
```

## Optimal Time & Space Complexity:
```
Upper Bound: O(n!) time | O(n) space - where `n` is the input number.
```
"""

# =========================================================================================================================== #

# Solution:


# Lower Bound: O(n!) time | O(n) space
def non_attacking_queens(n):
    # Initialize a list to keep track of queen positions in each row
    # column_placements[r] = c means there's a queen at row r and column c
    column_placements = [0] * n

    # Start the recursive process from row 0
    return get_number_of_non_attacking_queen_placements(0, column_placements, n)


def get_number_of_non_attacking_queen_placements(row, column_placements, board_size):
    # Base case: if we've placed queens in all rows successfully
    if row == board_size:
        return 1  # Found a valid configuration

    valid_placements = 0
    # Try placing queen in each column of the current row
    for col in range(board_size):
        # Check if this placement is valid (no attacks)
        if is_non_attacking_placement(row, col, column_placements):
            # Place the queen at (row, col)
            column_placements[row] = col

            # Recursively count valid placements for next rows
            valid_placements += get_number_of_non_attacking_queen_placements(
                row + 1, column_placements, board_size
            )

    return valid_placements


def is_non_attacking_placement(row, col, column_placements):
    # Check if placing a queen at (row, col) conflicts with any previous queens
    for previous_row in range(row):
        column_to_check = column_placements[previous_row]

        # Check if queens are in the same column
        same_column = column_to_check == col

        # Check if queens are on the same diagonal
        # (Diagonal conflict exists if column difference equals row difference)
        on_diagonal = abs(column_to_check - col) == row - previous_row

        if same_column or on_diagonal:
            return False  # Placement is attacking

    return True  # Placement is non-attacking


# Test Cases:

print(non_attacking_queens(4))  # Output: 2
print(non_attacking_queens(2))  # Output: 0
print(non_attacking_queens(10))  # Output: 724
