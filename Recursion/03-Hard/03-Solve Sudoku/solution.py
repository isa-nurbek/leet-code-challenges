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

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis

### Time Complexity:

The Sudoku solver uses a backtracking approach, which is essentially a brute-force method with pruning. Here's how the time
complexity breaks down:

1. **Worst-case scenario**: In the worst case, the algorithm tries every possible digit (1-9) in every empty cell until it finds
a solution. For an empty Sudoku board (all cells are 0), this would be O(9^(n)), where n is the number of empty cells. Since a
Sudoku board has 81 cells, the worst-case time complexity is O(9^(81)).

2. **Pruning**: The `is_valid_at_position` function checks if a digit is valid in the current row, column, and 3x3 subgrid, which
prunes the search space significantly. However, in the worst case, the time complexity remains exponential.

3. **Practical performance**: In practice, the algorithm performs much better than the worst case because:
   - Many cells are already filled (reducing n).
   - The validity checks prune invalid paths early.
   - The order of trying digits (1-9) and the order of filling cells (left to right, top to bottom) can lead to early solutions.

### Space Complexity:

The space complexity is determined by the recursion stack and the board itself:

1. **Recursion stack**: The maximum depth of the recursion stack is equal to the number of empty cells (since each recursive call
fills one cell). In the worst case, this is O(81) = O(1) (since the board size is fixed).

2. **Board**: The board is passed by reference (or modified in place), so no additional space is used for the board.

Thus, the space complexity is **O(1)** (constant) because the recursion depth is bounded by the fixed size of the Sudoku board
(81 cells).

### Summary:
- **Time Complexity**: O(9^(n)), where n is the number of empty cells. In the worst case (empty board), this is O(9^81).
- **Space Complexity**: O(1) (constant), due to fixed board size and in-place modifications.

### Notes:
- The worst-case time complexity is extremely high, but in practice, the solver works efficiently for most standard Sudoku puzzles
because of the pruning and the constraints reducing the search space.
- The space complexity is efficient because no additional data structures are used, and the recursion depth is limited.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
Let’s walk through the **Sudoku solver** code step by step. The program uses **backtracking**, a common technique for solving
constraint satisfaction problems like Sudoku.

---

## 🧩 Problem Overview: Sudoku Rules

You are given a 9x9 board where some cells are filled (digits 1-9) and others are `0` (empty). Your task is to fill the empty
cells so that:
- Each row has digits 1-9 with no repetition.
- Each column has digits 1-9 with no repetition.
- Each 3x3 subgrid has digits 1-9 with no repetition.

---

## 🔍 Function by Function Explanation

### 1. `solve_sudoku(board)`

```
def solve_sudoku(board):
    solve_partial_sudoku(0, 0, board)
    return board
```

This is the **main function**. It calls the recursive backtracking function `solve_partial_sudoku` starting from the top-left
cell `(0, 0)`. Once done, it returns the filled board.

---

### 2. `solve_partial_sudoku(row, col, board)`

```
def solve_partial_sudoku(row, col, board):
    current_row = row
    current_col = col

    if current_col == len(board[current_row]):
        current_row += 1
        current_col = 0

        if current_row == len(board):
            return True  # Finished the entire board

    if board[current_row][current_col] == 0:
        return try_digits_at_position(current_row, current_col, board)

    return solve_partial_sudoku(current_row, current_col + 1, board)
```

This function:
- Moves through the board **cell by cell**, from left to right and top to bottom.
- If the current column goes past the last column, it **moves to the next row**.
- If we reach past the last row, that means the board is complete, so we return `True`.
- If the current cell is `0`, we try placing a valid digit using `try_digits_at_position`.
- If the current cell already has a digit, just move to the **next column**.

---

### 3. `try_digits_at_position(row, col, board)`

```
def try_digits_at_position(row, col, board):
    for digit in range(1, 10):
        if is_valid_at_position(digit, row, col, board):
            board[row][col] = digit

            if solve_partial_sudoku(row, col + 1, board):
                return True

    board[row][col] = 0
    return False
```

This function:
- Tries digits from 1 to 9 in the current cell.
- For each digit, it checks if it's valid using `is_valid_at_position`.
- If valid, it places the digit and recursively solves the rest of the board.
- If no digit works, it **resets the cell to 0** and returns `False` to backtrack.

---

### 4. `is_valid_at_position(value, row, col, board)`

```
def is_valid_at_position(value, row, col, board):
    row_is_valid = value not in board[row]
    column_is_valid = value not in map(lambda r: r[col], board)

    if not row_is_valid or not column_is_valid:
        return False

    subgrid_row_start = (row // 3) * 3
    subgrid_col_start = (col // 3) * 3

    for row_idx in range(3):
        for col_idx in range(3):
            row_to_check = subgrid_row_start + row_idx
            col_to_check = subgrid_col_start + col_idx
            existing_value = board[row_to_check][col_to_check]

            if existing_value == value:
                return False

    return True
```

This function:
- Checks if the digit is already in the **row** or **column**.
- Then finds the **3x3 subgrid** that the current cell belongs to.
- It checks if the digit is already used in the subgrid.
- If all checks pass, it returns `True`; otherwise, `False`.

---

## 🔄 How Backtracking Works

1. The algorithm tries a digit at a position.
2. If it’s valid, it goes to the next empty cell.
3. If it eventually finds a dead end (no digit fits), it **backs up** and tries a different digit at the previous step.
4. This process repeats until the entire board is filled.

---

## ✅ Final Output

After running `solve_sudoku(board)`, the input board is **modified in place** to be a fully solved Sudoku puzzle.

---

Let’s walk through the **first few steps** of solving the Sudoku board using ASCII visualization. I’ll show:

1. The **initial board**.
2. A couple of **steps** where digits are placed.
3. Backtracking if needed (not shown here but I’ll explain how it would look).

---

### 🧩 Initial Sudoku Board

Empty cells are represented as `.` for clarity.

```
[7 8 . | 4 . . | 1 2 .]
[6 . . | . 7 5 | . . 9]
[. . . | 6 . 1 | . 7 8]
-----------------------
[. . 7 | . 4 . | 2 6 .]
[. . 1 | . 5 . | 9 3 .]
[9 . 4 | . 6 . | . . 5]
-----------------------
[. 7 . | 3 . . | . 1 2]
[1 2 . | . . 7 | 4 . .]
[. 4 9 | 2 . 6 | . . 7]
```

---

### 🧮 Step 1: Try Filling First Empty Cell (0,2)

We try digits `1` to `9`:
- `1`, `2`, `4`, `7`, `8` are already in row/column/subgrid.
- Try `3` → ✅ valid!

Place `3` at (0,2):

```
[7 8 3 | 4 . . | 1 2 .]
```

---

### 🧮 Step 2: Move to (0,4)

Try digits `1–9`:
- `1`, `2`, `3`, `4`, `7`, `8` are taken.
- Try `5` → ✅ valid!

Place `5` at (0,4):

```
[7 8 3 | 4 5 . | 1 2 .]
```

---

### ⏪ Backtracking (if needed)

If no valid digit can be placed later, the algorithm will **undo**:
- It will **reset (0,4) back to `.`**
- Try next digit at (0,2)
- Repeat...

We’d see a move like:

```
Backtracking: Resetting cell (0,4) from 5 to .
Backtracking: Resetting cell (0,2) from 3 to .
```

---

Here’s the **fully solved Sudoku board** represented in clean ASCII format, with each 3x3 block separated for readability:

```
[7 8 5 | 4 3 9 | 1 2 6]
[6 1 2 | 8 7 5 | 3 4 9]
[4 9 3 | 6 2 1 | 5 7 8]
-----------------------
[8 5 7 | 9 4 3 | 2 6 1]
[2 6 1 | 7 5 8 | 9 3 4]
[9 3 4 | 1 6 2 | 7 8 5]
-----------------------
[5 7 8 | 3 9 4 | 6 1 2]
[1 2 6 | 5 8 7 | 4 9 3]
[3 4 9 | 2 1 6 | 8 5 7]
```

✅ Every row, column, and 3x3 subgrid has digits from `1` to `9` with no repetition.

"""
