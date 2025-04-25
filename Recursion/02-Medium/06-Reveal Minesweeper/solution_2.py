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
from collections import deque


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
