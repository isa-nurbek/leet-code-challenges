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


from collections import deque


# O(w * h) time | O(w * h) space
def reveal_minesweeper_bfs(board, row, column):
    """
    Reveals cells on a Minesweeper board using BFS starting from the given position.

    Args:
        board: 2D list representing the Minesweeper board
        row: Starting row index
        column: Starting column index

    Returns:
        The modified board with revealed cells
    """

    # If the starting cell is a mine, reveal it as 'X' and return immediately
    if board[row][column] == "M":
        board[row][column] = "X"
        return board

    # Initialize a queue for BFS and add the starting position
    queue = deque()
    queue.append((row, column))

    while queue:
        r, c = queue.popleft()

        # Skip if this cell is already revealed (not 'H')
        if board[r][c] != "H":
            continue

        # Get all valid neighboring cells
        neighbors = get_neighbors(board, r, c)
        # Count how many neighbors are mines
        mine_count = sum(1 for nr, nc in neighbors if board[nr][nc] == "M")

        if mine_count > 0:
            # If there are adjacent mines, show the count
            board[r][c] = str(mine_count)
        else:
            # If no adjacent mines, mark as '0' and explore neighbors
            board[r][c] = "0"
            for nr, nc in neighbors:
                # Only add hidden cells to the queue
                if board[nr][nc] == "H":
                    queue.append((nr, nc))

    return board


def get_neighbors(board, row, column):
    """
    Returns all valid neighboring cells (including diagonals) for a given position.

    Args:
        board: 2D list representing the Minesweeper board
        row: Current row index
        column: Current column index

    Returns:
        List of (row, column) tuples representing valid neighbors
    """
    # All 8 possible directions (horizontal, vertical, diagonal)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    neighbors = []

    for dr, dc in directions:
        nr, nc = row + dr, column + dc
        # Check if the neighbor is within board boundaries
        if 0 <= nr < len(board) and 0 <= nc < len(board[0]):
            neighbors.append((nr, nc))

    return neighbors


# Test Cases:

# Test Case 1: Simple 3x2 board
board = [["M", "M"], ["H", "H"], ["H", "H"]]
print(reveal_minesweeper_bfs(board, 2, 0))
# Expected Output: [['M', 'M'], ['2', '2'], ['0', '0']]

# Test Case 2: More complex board
board_2 = [
    ["H", "H", "H", "H", "M"],
    ["H", "1", "M", "H", "1"],
    ["H", "H", "H", "H", "H"],
    ["H", "H", "H", "H", "H"],
]
print(reveal_minesweeper_bfs(board_2, 3, 4))
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

1. **BFS Traversal**: In the worst case, we might need to visit every cell on the board once. For a board of size `m x n`,
this gives us `O(m * n)` time.
2. **Neighbor Check**: For each cell, we check up to 8 neighbors (constant time per cell). This doesn't change the overall
complexity since `O(8 * m * n)` is still `O(m * n)`.

Thus, the **time complexity is `O(m * n)`**, where `m` is the number of rows and `n` is the number of columns in the board.

### Space Complexity:

1. **Queue**: In the worst case (e.g., the entire board is empty and all cells are revealed), the queue could hold up to `O(m * n)`
cells (though in practice, it's usually less due to branching).
2. **Visited Handling**: The algorithm implicitly tracks visited cells by checking if a cell is `"H"` (hidden) before adding it
to the queue, so no extra space is used for a `visited` set.

Thus, the **space complexity is `O(m * n)`** in the worst case due to the queue.

### Summary:
- **Time Complexity**: `O(m * n)`
- **Space Complexity**: `O(m * n)`

This is optimal for a BFS approach to Minesweeper, as you must potentially reveal every cell on the board in the worst case.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
Let's go step by step to understand what the code does and how it simulates a basic **Minesweeper reveal** functionality using
**Breadth-First Search (BFS)**.

---

## 🔍 Purpose of the Code

The function `reveal_minesweeper_bfs(board, row, column)` simulates revealing a cell in a Minesweeper game:

- If the revealed cell is a **mine**, it becomes `"X"` (game over).
- If it is a **safe cell** (`"H"`), it reveals it:
  - If adjacent to any mines, it displays the **number of adjacent mines**.
  - If no adjacent mines, it becomes `"0"` and reveals its neighbors **recursively** (BFS-style).

---

## 🔁 `reveal_minesweeper_bfs(board, row, column)`

### ✅ Step 1: Check if clicked cell is a mine

```
if board[row][column] == "M":
    board[row][column] = "X"
    return board
```
- If the player clicks on a mine (`"M"`), it’s marked as `"X"` and returned immediately.

---

### 📥 Step 2: BFS Initialization

```
queue = deque()
queue.append((row, column))
```
- Initializes a **queue** (from `collections.deque`) to perform BFS.
- Starts with the cell that was clicked.

---

### 🔁 Step 3: BFS Loop

```
while queue:
    r, c = queue.popleft()

    if board[r][c] != "H":
        continue
```

- Dequeue a cell to process.
- If it's not hidden anymore (not `"H"`), skip it — already revealed.

---

### 👥 Step 4: Get Neighbors and Count Mines

```
neighbors = get_neighbors(board, r, c)
mine_count = sum(1 for nr, nc in neighbors if board[nr][nc] == "M")
```

- Get all 8 adjacent cells using `get_neighbors`.
- Count how many of them are mines.

---

### 🔣 Step 5: Reveal the Cell Based on Mine Count

```
if mine_count > 0:
    board[r][c] = str(mine_count)
```

- If there are adjacent mines, reveal the number.

---

### 🌱 Step 6: No Adjacent Mines → Reveal as "0" and Enqueue Neighbors

```
else:
    board[r][c] = "0"
    for nr, nc in neighbors:
        if board[nr][nc] == "H":
            queue.append((nr, nc))
```

- If no adjacent mines, mark it as `"0"`.
- Add all neighboring hidden cells to the queue to reveal them too — this causes a **flood fill** effect, like in real Minesweeper.

---

## 🧩 Helper: `get_neighbors(board, row, column)`

```
directions = [(0, 1), (0, -1), (1, 0), (-1, 0), 
              (1, 1), (1, -1), (-1, 1), (-1, -1)]
```

- Lists 8 directions (horizontal, vertical, diagonal).
- Returns valid in-bound neighbor coordinates.

## ✅ Summary

| Symbol | Meaning |
|--------|---------|
| `"M"`  | Hidden mine |
| `"H"`  | Hidden safe cell |
| `"X"`  | Revealed mine (game over) |
| `"0"`  | Revealed safe cell with 0 adjacent mines |
| `"1"`-`"8"` | Revealed cell with that many adjacent mines |

---

Let's walk through the **actual outputs** of both examples step by step so you can see exactly how the board is revealed.

## 🧪 **Example 1**

### Input board:
```
board = [
    ["M", "M"],
    ["H", "H"],
    ["H", "H"]
]
click = (2, 0)
```

We clicked on cell `(2, 0)`, which is `"H"`.

### Step-by-step reveal:
1. Check neighbors of `(2, 0)`:
   - Neighbors: `(1, 0)` and `(1, 1)` and `(2, 1)`
   - Mines in neighbors: `(0,0)` and `(0,1)` are mines but not directly neighboring `(2,0)`, so **no mines in direct
   neighbors** ➝ continue.

2. Since mine count is `0`, set `(2,0)` to `"0"` and enqueue its hidden neighbors:
   - Add `(1,0)`, `(1,1)`, `(2,1)` to queue.

3. Next from queue: `(1, 0)`  
   - Neighbors: `(0,0)` is a mine.
   - Mine count = 1 ➝ set `(1,0)` to `"1"`

4. Next from queue: `(1, 1)`  
   - Neighbors: `(0,1)` is a mine.
   - Mine count = 1 ➝ set `(1,1)` to `"1"`

5. Next from queue: `(2, 1)`  
   - Neighbors: `(1,1)` has already been updated to `"1"` (not a mine), and others are not mines.
   - Mine count = 0 ➝ set `(2,1)` to `"0"`

No more neighbors to reveal.

### ✅ Final board:
```
[
    ["M", "M"],
    ["1", "1"],
    ["0", "0"]
]
```

---

## 🧪 **Example 2**

```
board = [
    ["H", "H", "H", "H", "M"],
    ["H", "1", "M", "H", "1"],
    ["H", "H", "H", "H", "H"],
    ["H", "H", "H", "H", "H"],
]
click = (3, 4)
```

We click on `(3, 4)` → it's `"H"`.

### Step-by-step reveal (short summary):
- Start at `(3, 4)` → no adjacent mines → set to `"0"` → reveal neighbors.
- Keep exploring and revealing safe areas until:
  - Either cells with mine neighbors get revealed as numbers
  - Or safe zones with 0-mine neighbors get marked as `"0"` and continue the flood.

### ✅ Final board (after BFS reveal):

```
[
    ["H", "H", "H", "H", "M"],
    ["H", "1", "M", "H", "1"],
    ["H", "H", "H", "0", "0"],
    ["H", "H", "H", "0", "0"],
]
```

Only the bottom-right corner and surrounding areas are revealed, since the rest are connected to cells adjacent to
mines (like `"1"` and `"M"` in row 1).

---

Let's **simulate the flood fill step-by-step in text** for **Example 2**, showing how the board updates after each BFS step.

### 🎯 Input Board

```
board = [
    ["H", "H", "H", "H", "M"],
    ["H", "1", "M", "H", "1"],
    ["H", "H", "H", "H", "H"],
    ["H", "H", "H", "H", "H"],
]
click = (3, 4)
```

We click on `(3, 4)`. Let's visualize how this reveals more of the board.

---

### 🌀 Step 0: Start BFS from (3, 4)

- Cell `(3, 4)` has **no adjacent mines** → becomes `"0"` and adds neighbors to queue.

**Board:**
```
H H H H M
H 1 M H 1
H H H H H
H H H H 0
```

Queue: `[(2,3), (2,4), (3,3)]`

---

### 🌀 Step 1: Process (2, 3)

- Neighbors: no mines → mark `"0"` and enqueue neighbors.

**Board:**
```
H H H H M
H 1 M H 1
H H H 0 H
H H H H 0
```

Queue: `[(2,4), (3,3), (1,3), (1,4), (2,2), (3,2)]`

---

### 🌀 Step 2: Process (2, 4)

- Neighbor `(1,4)` is `"1"` (already known) → mine count = 1 → mark `"1"`

**Board:**
```
H H H H M
H 1 M H 1
H H H 0 1
H H H H 0
```

Queue: `[(3,3), (1,3), (2,2), (3,2)]`

---

### 🌀 Step 3: Process (3, 3)

- No adjacent mines → mark `"0"` and enqueue neighbors.

**Board:**
```
H H H H M
H 1 M H 1
H H H 0 1
H H H 0 0
```

Queue: `[(1,3), (2,2), (3,2), (2,3)]` ← note: (2,3) already revealed

---

### 🌀 Step 4: Process (1, 3)

- Adjacent to a mine (`(1,2)` is `"M"`) → mark `"1"`

**Board:**
```
H H H H M
H 1 M 1 1
H H H 0 1
H H H 0 0
```

Queue: `[(2,2), (3,2)]`

---

### 🌀 Step 5: Process (2, 2)

- No adjacent mines → mark `"0"` and enqueue neighbors.

**Board:**
```
H H H H M
H 1 M 1 1
H H 0 0 1
H H H 0 0
```

Queue: `[(3,2), (1,2), (2,1), (3,1)]` ← note: (1,2) is `"M"`, won’t reveal

---

### 🌀 Step 6: Process (3, 2)

- No adjacent mines → mark `"0"` and enqueue neighbors

**Board:**
```
H H H H M
H 1 M 1 1
H H 0 0 1
H H 0 0 0
```

Queue: `[(2,1), (3,1)]`

---

### 🌀 Step 7: Process (2, 1)

- No adjacent mines → mark `"0"` and enqueue neighbors

**Board:**
```
H H H H M
H 1 M 1 1
H 0 0 0 1
H H 0 0 0
```

Queue: `[(3,1), (2,0), (3,0)]`

---

### 🌀 Step 8: Process (3, 1)

- No adjacent mines → mark `"0"` and enqueue neighbors

**Board:**
```
H H H H M
H 1 M 1 1
H 0 0 0 1
H 0 0 0 0
```

Queue: `[(2,0), (3,0)]`

---

### 🌀 Step 9: Process (2, 0)

- No adjacent mines → mark `"0"`

**Board:**
```
H H H H M
H 1 M 1 1
0 0 0 0 1
H 0 0 0 0
```

Queue: `[(3,0)]`

---

### 🌀 Step 10: Process (3, 0)

- Adjacent mine at `(2,2)` is not a mine → safe → mark `"0"`

**Final Board:**
```
H H H H M
H 1 M 1 1
0 0 0 0 1
0 0 0 0 0
```

---

## 🎉 Final Revealed Board:

```
[
    ["H", "H", "H", "H", "M"],
    ["H", "1", "M", "1", "1"],
    ["0", "0", "0", "0", "1"],
    ["0", "0", "0", "0", "0"]
]
```

"""
