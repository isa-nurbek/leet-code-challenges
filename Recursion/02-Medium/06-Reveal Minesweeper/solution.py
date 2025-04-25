# Problem Description:

"""

                                          Reveal Minesweeper

Minesweeper is a popular video game. From Wikipedia, "The game features a grid of clickable squares, with hidden "mines" scattered
throughout the board. The objective is to clear the board without detonating any mines, with help from clues about the number of
neighboring mines in each field." Specifically, when a player clicks on a square (also called a cell) that doesn't contain a mine,
the square reveals a number representing the number of immediately adjacent mines (including diagonally adjacent mines).

You're given a two-dimensional array of strings that represents a Minesweeper board for a game in progress. You're also given a row
and a column representing the indices of the next square that the player clicks on the board. Write a function that returns an
updated board after the click (your function can mutate the input board).

The board will always contain only strings, and each string will be one of the following:

- `"M"`: A mine that has not been clicked on.
- `"X"`: A mine that has been clicked on, indicating a lost game.
- `"H"`: A cell with no mine, but whose content is still hidden to the player.
- `"0-8"`: A cell with no mine, with an integer from 0 to 8 representing the number of adjacent mines. Note that this is a single-digit integer represented as a string. For example `"2"` would mean there are 2 adjacent cells with mines. Numbered
cells are not clickable as they have already been revealed.
If the player clicks on a mine, replace the `"M"` with `"X"`, indicating the game was lost.

If the player clicks on a cell adjacent to a mine, replace the `"H"` with a string representing the number of adjacent mines.

If the player clicks on a cell with no adjacent mines, replace the `"H"` with `"0"`. Additionally, reveal all of the adjacent
hidden cells as if the player had clicked on those cells as well.

You can assume the given row and column will always represent a legal move. The board can be of any size and have any number of
mines in it.


## Sample Input
```
board = [
  ["M", "M"],
  ["H", "H"],
  ["H", "H"]
]
row = 2
column = 0
```

## Sample Output
```
[
  ["M", "M"],
  ["2", "2"],
  ["0", "0"]
]
```

## Optimal Time & Space Complexity:
```
O(w * h) time | O(w * h) space - where `w` is the width of the board, and `h` is the height of the board.
```
"""

# =========================================================================================================================== #

# Solution:


# O(w * h) time | O(w * h) space
def reveal_minesweeper(board, row, column):
    """
    Reveals the selected cell in a Minesweeper board and updates the board accordingly.

    Args:
        board: 2D list representing the Minesweeper game board
        row: row index of the selected cell
        column: column index of the selected cell

    Returns:
        The updated board after revealing the selected cell
    """

    # If the selected cell is a mine, mark it with 'X' (player loses)
    if board[row][column] == "M":
        board[row][column] = "X"
        return board

    # Get all adjacent cells (neighbors) to the selected cell
    neighbors = get_neighbors(board, row, column)
    adjacent_minutes_count = 0

    # Count how many mines are adjacent to the selected cell
    for neighbor_row, neighbor_column in neighbors:
        if board[neighbor_row][neighbor_column] == "M":
            adjacent_minutes_count += 1

    if adjacent_minutes_count > 0:
        # If there are adjacent mines, show the count
        board[row][column] = str(adjacent_minutes_count)
    else:
        # If no adjacent mines, mark as '0' and reveal all adjacent hidden cells
        board[row][column] = "0"

        for neighbor_row, neighbor_column in neighbors:
            # Recursively reveal adjacent hidden cells ('H')
            if board[neighbor_row][neighbor_column] == "H":
                reveal_minesweeper(board, neighbor_row, neighbor_column)

    return board


def get_neighbors(board, row, column):
    """
    Gets all valid adjacent cells (neighbors) for a given cell position.

    Args:
        board: 2D list representing the game board
        row: row index of the cell
        column: column index of the cell

    Returns:
        List of [row, column] pairs representing valid neighbor positions
    """
    # All 8 possible directions for adjacent cells
    directions = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),  # up, down, right, left
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1),
    ]  # diagonals
    neighbors = []

    for direction_row, direction_column in directions:
        new_row = row + direction_row
        new_column = column + direction_column

        # Check if the new position is within board boundaries
        if 0 <= new_row < len(board) and 0 <= new_column < len(board[0]):
            neighbors.append([new_row, new_column])

    return neighbors


# Test Cases:

# Test Case 1: Simple 3x2 board
board = [["M", "M"], ["H", "H"], ["H", "H"]]
row = 2
column = 0

# Test Case 2: More complex 4x5 board
board_2 = [
    ["H", "H", "H", "H", "M"],
    ["H", "1", "M", "H", "1"],
    ["H", "H", "H", "H", "H"],
    ["H", "H", "H", "H", "H"],
]
row_2 = 3
column_2 = 4

print(reveal_minesweeper(board, row, column))
# Expected Output: [['M', 'M'], ['2', '2'], ['0', '0']]

print(reveal_minesweeper(board_2, row_2, column_2))
# Expected Output:
"""
[
  ["0", "1", "H", "H", "M"],
  ["0", "1", "M", "2", "1"],
  ["0", "1", "1", "1", "0"],
  ["0", "0", "0", "0", "0"],
]  
"""

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis

### Time Complexity:

1. **Base Case (clicking on a mine 'M'):**  
   - Constant time O(1), as it just marks the cell as 'X' and returns.

2. **Counting Adjacent Mines:**  
   - The `get_neighbors` function checks up to 8 directions (constant time O(1)), but in the worst case, it could be fewer
   if the cell is on the edge/corner of the board.  
   - For each neighbor, checking if it's a mine is O(1).  
   - Overall, counting adjacent mines is O(1).

3. **Recursive Reveal for Empty Cells ('0'):**  
   - If the cell has no adjacent mines (`adjacent_minutes_count == 0`), the algorithm recursively reveals all neighboring
   hidden cells ('H').  
   - In the worst case (e.g., a large empty region), this can traverse the entire board, leading to O(N * M) time, where
   N is the number of rows and M is the number of columns.  
   - However, each cell is processed at most once (since it's marked as '0' or a number and won't be reprocessed), so the
   total work is proportional to the number of cells.

**Overall Time Complexity:**  
- **Worst Case:** O(N * M), where N is the number of rows and M is the number of columns. This happens when you click on an
empty cell with no adjacent mines, and the algorithm reveals the entire board.  
- **Best Case:** O(1), when clicking on a mine or a cell with adjacent mines (no recursion).  
- **Average Case:** Depends on the board configuration, but typically less than O(N * M) unless the board is mostly empty.

---

### Space Complexity:

1. **Recursion Stack:**  
   - In the worst case (revealing a large empty region), the recursion depth could be O(N * M) (e.g., a snake-like empty path).  
   - However, in practice, the recursion depth is limited by the size of the region being revealed, which is O(max(N, M)) in 
   most realistic scenarios (e.g., a spiral or a rectangular area).  

2. **No Additional Data Structures:**  
   - The algorithm modifies the board in place and doesn't use extra space proportional to the input.  

**Overall Space Complexity:**  
- **Worst Case:** O(N * M) due to recursion stack (unlikely in practice but possible).  
- **Best Case:** O(1) (no recursion).  
- **Typical Case:** O(max(N, M)) for the recursion stack when revealing a large empty region.  

---

### Summary:
- **Time Complexity:** O(N * M) in the worst case, O(1) in the best case.  
- **Space Complexity:** O(N * M) in the worst case (due to recursion), O(1) in the best case.  

### Notes:
- The worst-case time and space complexity occur when the entire board is revealed recursively (e.g., clicking on an
empty cell in a board with no mines).  
- For typical Minesweeper boards (with some mines), the average time and space complexity are much better.  
- You could optimize the space complexity to O(1) (no recursion overhead) by using an iterative approach with a queue
(BFS), but the current implementation uses recursion.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
The `reveal_minesweeper` function is designed to simulate the behavior of revealing a cell in a **Minesweeper game**.
When a cell is clicked, the function either:

1. Ends the game if a **mine ('M')** is clicked.
2. Reveals the **number of adjacent mines** if there are any.
3. Recursively reveals **neighboring cells** if there are no adjacent mines (flood fill behavior).

Let’s break down the **code step by step**, including both functions and then the test cases.

---

### 🔧 `get_neighbors` Function

```
def get_neighbors(board, row, column):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), 
                  (1, 1), (1, -1), (-1, 1), (-1, -1)]
    neighbors = []

    for direction_row, direction_column in directions:
        new_row = row + direction_row
        new_column = column + direction_column

        if 0 <= new_row < len(board) and 0 <= new_column < len(board[0]):
            neighbors.append([new_row, new_column])

    return neighbors
```

#### ✅ Purpose:
Finds the 8 possible neighbors (horizontal, vertical, diagonal) around a given cell.

#### ⚙️ How it works:
- It adds directional offsets to the current cell.
- It ensures the new cell is **within bounds** before adding it to the list.

---

### 🎯 `reveal_minesweeper` Function

```
def reveal_minesweeper(board, row, column):
    if board[row][column] == "M":
        board[row][column] = "X"
        return board
```

#### ☠️ Case 1: Clicked on a Mine
- If the clicked cell is `'M'`, it’s replaced with `'X'` (indicating game over).
- Returns the board immediately.

---

```
neighbors = get_neighbors(board, row, column)
adjacent_minutes_count = 0

for neighbor_row, neighbor_column in neighbors:
    if board[neighbor_row][neighbor_column] == "M":
        adjacent_minutes_count += 1
```

#### 🔍 Case 2: Count Adjacent Mines
- Gathers all 8 neighboring cells.
- Counts how many are `'M'` (mines).

---

```
if adjacent_minutes_count > 0:
    board[row][column] = str(adjacent_minutes_count)
```

#### 🧮 Case 3: Show Mine Count
- If there's at least one adjacent mine, the cell is updated with the **number** (as a string).
- No further recursion happens.

---

```
else:
    board[row][column] = "0"

    for neighbor_row, neighbor_column in neighbors:
        if board[neighbor_row][neighbor_column] == "H":
            reveal_minesweeper(board, neighbor_row, neighbor_column)
```

#### 🌊 Case 4: Flood Fill
- If **no adjacent mines**, mark the cell `'0'`.
- Then recursively reveal each hidden (`'H'`) neighbor.
- This spreads outward until all reachable zero-mine cells and their boundaries are revealed.

---

### 🧪 Test Cases Explained

#### Test Case 1:
```
board = [["M", "M"], ["H", "H"], ["H", "H"]]
row = 2
column = 0
```

Initial board:
```
M M
H H
H H  <- click here (2, 0)
```

- (2,0) has 0 adjacent mines → set to `'0'`.
- Its neighbors include (1,0), (1,1), (2,1).
- (1,0) has 2 adjacent mines → becomes `'2'`.
- (1,1) also has 2 mines near → becomes `'2'`.
- (2,1) has 0 → becomes `'0'`.

Final board:
```
M M
2 2
0 0
```

---

#### Test Case 2:
```
board_2 = [
    ["H", "H", "H", "H", "M"],
    ["H", "1", "M", "H", "1"],
    ["H", "H", "H", "H", "H"],
    ["H", "H", "H", "H", "H"],
]
row_2 = 3
column_2 = 4
```

You clicked on bottom-right corner (3,4), which is `'H'`.

- It has **0 adjacent mines**, so it becomes `'0'`.
- Recursively checks neighbors like (2,3), (2,4), etc.
- Those cells might also become `'0'` or show counts depending on their adjacent mine counts.
- This triggers a **flood-fill** of all empty safe zones and boundary cells with numbers.

Final revealed board:
```
["0", "1", "H", "H", "M"],
["0", "1", "M", "2", "1"],
["0", "1", "1", "1", "0"],
["0", "0", "0", "0", "0"]
```

---

### 🧠 Summary

| Symbol | Meaning                      |
|--------|------------------------------|
| `H`    | Hidden cell                  |
| `M`    | Mine                         |
| `X`    | Clicked mine (game over)     |
| `0`    | Revealed, no adjacent mines  |
| `1-8`  | Revealed, with adjacent mines|

---

### ✅ Features Demonstrated
- Basic recursion
- Flood-fill using DFS logic
- Safe bounds checking
- Clear separation of logic via `get_neighbors`

---

Let’s walk through a **visual representation** of how the **flood-fill (recursive reveal)** propagates in **Test Case 2**,
where you click on the bottom-right corner at `(3,4)`.

---

### 🧪 Initial Board (`'H'` = hidden, `'M'` = mine)

We mark the **clicked cell** with `C`.

```
[
  ["H", "H", "H", "H", "M"],
  ["H", "1", "M", "H", "1"],
  ["H", "H", "H", "H", "H"],
  ["H", "H", "H", "H", "C"],
]
```

---

### 🔁 Step-by-Step Reveal (Flood-Fill)

#### 🔹 Step 1: Click on `(3,4)`  
- 0 adjacent mines → set to `'0'`
- Recurse on all 8 neighbors

```
(3,4) = '0'
```

Recurse into neighbors: `(2,3)`, `(2,4)`, `(3,3)`

---

#### 🔹 Step 2: Visit `(2,3)`  
- 1 adjacent mine → set to `'1'`

#### 🔹 Step 3: Visit `(2,4)`
- 0 adjacent mines → set to `'0'`
- Recurse into its neighbors: `(1,3)`, `(1,4)`, `(2,3)`

#### 🔹 Step 4: Visit `(3,3)`
- 0 adjacent mines → set to `'0'`
- Recurse into `(2,2)`, `(3,2)`, `(2,3)`

---

This process continues, **recursively visiting safe neighbors** and updating the board.

Here's a simplified order of visits (⬇️ = deeper into recursion):

```
Click (3,4) ➡️
→ (2,4) ➡️
   → (1,4)  [1 mine]
   → (1,3)  [2 mines]
   → (2,3)  [1 mine]
→ (3,3) ➡️
   → (3,2) ➡️
     → (3,1) ➡️
       → (3,0)
→ (2,2)
→ (2,1)
→ (2,0)
→ (1,0)
→ (0,0)
→ (0,1)
```

---

### 🧼 Final Revealed Board

```
[
  ["0", "1", "H", "H", "M"],
  ["0", "1", "M", "2", "1"],
  ["0", "1", "1", "1", "0"],
  ["0", "0", "0", "0", "0"],
]
```

---

### 🧠 Visualization Summary

- Safe zones (`'0'`) trigger further reveal.
- Boundary cells (with `1`, `2`, etc.) stop the recursion.
- Mines are left untouched unless clicked.

"""
