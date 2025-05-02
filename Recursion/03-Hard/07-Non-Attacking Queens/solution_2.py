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


# Lower Bound: O(n!) time | O(1) space
def non_attacking_queens(n):
    def backtrack(row, columns, diagonals, anti_diagonals):
        if row == n:
            return 1

        count = 0
        for col in range(n):
            diagonal = row - col
            anti_diagonal = row + col

            if (
                col in columns
                or diagonal in diagonals
                or anti_diagonal in anti_diagonals
            ):
                continue

            columns.add(col)
            diagonals.add(diagonal)
            anti_diagonals.add(anti_diagonal)

            count += backtrack(row + 1, columns, diagonals, anti_diagonals)

            columns.remove(col)
            diagonals.remove(diagonal)
            anti_diagonals.remove(anti_diagonal)

        return count

    return backtrack(0, set(), set(), set())


# Test Cases:

print(non_attacking_queens(4))  # Output: 2
print(non_attacking_queens(2))  # Output: 0
print(non_attacking_queens(10))  # Output: 724
