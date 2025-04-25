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
