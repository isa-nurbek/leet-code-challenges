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
    column_placements = [0] * n

    return get_number_of_non_attacking_queen_placements(0, column_placements, n)


def get_number_of_non_attacking_queen_placements(row, column_placements, board_size):
    if row == board_size:
        return 1

    valid_placements = 0
    for col in range(board_size):
        if is_non_attacking_placement(row, col, column_placements):
            column_placements[row] = col

            valid_placements += get_number_of_non_attacking_queen_placements(
                row + 1, column_placements, board_size
            )

    return valid_placements


def is_non_attacking_placement(row, col, column_placements):
    for previous_row in range(row):
        column_to_check = column_placements[previous_row]
        same_column = column_to_check == col

        on_diagonal = abs(column_to_check - col) == row - previous_row
        if same_column or on_diagonal:
            return False

    return True


# Test Cases:

print(non_attacking_queens(4))  # Output: 2
print(non_attacking_queens(2))  # Output: 0
print(non_attacking_queens(10))  # Output: 724
