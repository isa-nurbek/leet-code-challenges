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

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis

### Time Complexity Analysis

The problem is to place `n` queens on an `n x n` chessboard such that no two queens attack each other. The solution uses a
backtracking approach to explore all possible valid configurations.

1. **Recursive Tree Structure**: 
   - At each row `row`, the algorithm tries to place a queen in each column `col` from `0` to `n-1`.
   - For each valid placement (where the queen doesn't attack any previously placed queens), it proceeds to the next row.
   - The recursion continues until all `n` queens are placed (`row == n`), at which point a valid configuration is found.

2. **Branching Factor**:
   - At the first row (`row = 0`), there are `n` possible columns to place the queen.
   - At the second row (`row = 1`), the number of valid columns depends on the placement of the first queen. In the worst case,
   it could still be `n` (but in practice, it's less due to constraints).
   - This branching continues until the last row.

3. **Worst-Case Scenario**:
   - The worst-case time complexity is upper-bounded by `O(n!)`. This is because:
     - The first queen has `n` choices.
     - The second queen has at most `n-1` choices (excluding the column of the first queen and diagonals).
     - The third queen has at most `n-2` choices, and so on.
     - This leads to `n * (n-1) * (n-2) * ... * 1 = n!` possibilities in the worst case.
   - However, in practice, the actual number is much less than `n!` because many branches are pruned early when a placement is
   invalid. But for big-O analysis, we consider the worst case.

4. **Checking Validity (`is_non_attacking_placement`)**:
   - For each placement at `(row, col)`, the function checks against all previously placed queens (up to `row` queens).
   - This check takes `O(row)` time (since it loops through `previous_row` from `0` to `row-1`).
   - In the worst case (when `row = n`), this is `O(n)` time per check.
   - Since this check is done for each node in the recursive tree, the total time complexity becomes `O(n! * n)`.

### Space Complexity Analysis

1. **Recursion Stack**:
   - The maximum depth of the recursion is `n` (one level for each row).
   - At each level, local variables and parameters are stored. This contributes `O(n)` space for the recursion stack.

2. **Storage for `column_placements`**:
   - The `column_placements` array stores the column position of the queen in each row, so it takes `O(n)` space.

3. **Total Space Complexity**:
   - The total space complexity is `O(n)` (for recursion stack and `column_placements`). No additional significant space is used.

### Final Answer

- **Time Complexity**: `O(n! * n)`
  - The `n!` comes from the number of possible valid queen placements (which is less than `n!` but upper-bounded by it).
  - The `n` factor comes from the `is_non_attacking_placement` check at each step.
  
- **Space Complexity**: `O(n)`
  - This is due to the recursion stack depth (`O(n)`) and the `column_placements` array (`O(n)`). 

### Additional Notes

- The actual number of valid configurations for the N-Queens problem is much less than `n!`, but the time complexity is still
`O(n! * n)` in the worst case because we cannot do better than exploring all possible valid branches.
- The space complexity is efficient (`O(n)`) because the algorithm uses backtracking and reuses the `column_placements` array
instead of storing all possible configurations.

"""
