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
    """
    Counts the number of ways to place n queens on an n x n chessboard
    such that no two queens attack each other.

    Args:
        n: The size of the chessboard and number of queens to place.

    Returns:
        The number of valid configurations.
    """

    def backtrack(row, columns, diagonals, anti_diagonals):
        """
        Recursive backtracking helper function.

        Args:
            row: Current row being considered (0 to n-1)
            columns: Set of columns already occupied by queens
            diagonals: Set of diagonals (row - col) already occupied
            anti_diagonals: Set of anti-diagonals (row + col) already occupied

        Returns:
            Number of valid configurations found from this state
        """
        # Base case: all rows have been filled successfully
        if row == n:
            return 1

        count = 0
        # Try each column in the current row
        for col in range(n):
            # Calculate diagonal and anti-diagonal identifiers
            # These identify the two types of diagonals a queen can attack along
            diagonal = row - col  # For diagonals going from top-left to bottom-right
            anti_diagonal = (
                row + col
            )  # For diagonals going from top-right to bottom-left

            # Skip if this column or diagonals are already occupied
            if (
                col in columns
                or diagonal in diagonals
                or anti_diagonal in anti_diagonals
            ):
                continue

            # Place the queen by adding to our tracking sets
            columns.add(col)
            diagonals.add(diagonal)
            anti_diagonals.add(anti_diagonal)

            # Recurse to next row and accumulate solutions
            count += backtrack(row + 1, columns, diagonals, anti_diagonals)

            # Backtrack - remove the queen to explore other possibilities
            columns.remove(col)
            diagonals.remove(diagonal)
            anti_diagonals.remove(anti_diagonal)

        return count

    # Start the backtracking from row 0 with empty sets
    return backtrack(0, set(), set(), set())


# Test Cases:

print(non_attacking_queens(4))  # Output: 2
print(non_attacking_queens(2))  # Output: 0
print(non_attacking_queens(10))  # Output: 724
