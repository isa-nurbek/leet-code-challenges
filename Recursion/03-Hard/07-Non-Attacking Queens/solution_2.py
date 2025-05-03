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

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis

### Time Complexity:
The algorithm uses a backtracking approach to explore all possible valid queen placements.

1. **Branching Factor**: At each row, we have up to `N` possible columns to place the queen.
2. **Depth of Recursion**: The recursion goes up to `N` levels (one for each row).
3. **Pruning**: The algorithm prunes invalid paths early (when a column, diagonal, or anti-diagonal is already occupied).

In the worst case, the algorithm explores all possible configurations, leading to a time complexity of O(N!).
Here's why:
- 1st row: N choices
- 2nd row: at most N-1 choices (pruning invalid columns/diagonals)
- 3rd row: at most N-2 choices
- ...
- Nth row: 1 choice

Thus, the total number of recursive calls is bounded by N × (N-1) × (N-2) × ... × 1 = N!.

However, due to pruning, the actual number of recursive calls is much smaller in practice, but the worst-case time complexity
remains O(N!).

### Space Complexity:

The space complexity is determined by:
1. **Recursion Depth**: The recursion goes up to `N` levels, so the call stack uses O(N) space.
2. **Sets for Tracking Conflicts**: The `columns`, `diagonals`, and `anti_diagonals` sets each can grow up to O(N) size
(since at most N elements are stored at any time).

Thus, the total space complexity is O(N) (for recursion and the sets).

### Summary:
- **Time Complexity**: O(N!) (worst-case, though pruning makes it faster in practice).
- **Space Complexity**: O(N) (for recursion and tracking conflicts). 

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
The provided function `non_attacking_queens(n)` solves the classic **N-Queens problem**, which asks: *How many ways can you place
`n` queens on an `n x n` chessboard so that no two queens attack each other?* Queens attack along rows, columns, and diagonals,
so we need to place them such that **no two queens share the same row, column, or diagonal**.

---

### ✅ Key Concepts

* **Backtracking**: Try placing queens one row at a time, exploring only valid positions. If a placement leads to a conflict,
backtrack and try a different position.

* **Sets**:

  * `columns`: Tracks which columns already have a queen.
  * `diagonals`: Tracks `row - col` (main diagonals: ↘ direction).
  * `anti_diagonals`: Tracks `row + col` (anti-diagonals: ↙ direction).

---

### 🔍 Step-by-Step Explanation

#### Function: `non_attacking_queens(n)`

This is the entry point. It calls a helper function `backtrack` with:

* `row = 0`: We start placing queens from the top row.
* Three empty sets to track constraints: `columns`, `diagonals`, and `anti_diagonals`.

---

#### Function: `backtrack(row, columns, diagonals, anti_diagonals)`

This function recursively tries to place a queen in a valid position in the current `row`.

##### Base Case:

```
if row == n:
    return 1
```

* If we've successfully placed queens in all `n` rows, it's a valid solution. Return `1` to count it.

##### Loop Through Columns:

```
for col in range(n):
```

* Try placing a queen in each column of the current row.

##### Diagonal Identifiers:

```
diagonal = row - col
anti_diagonal = row + col
```

* These values uniquely identify the diagonals.

##### Check Conflicts:

```
if col in columns or diagonal in diagonals or anti_diagonal in anti_diagonals:
    continue
```

* Skip the column if a queen already attacks from the same column, diagonal, or anti-diagonal.

##### Place the Queen:

```
columns.add(col)
diagonals.add(diagonal)
anti_diagonals.add(anti_diagonal)
```

* Mark the position as occupied.

##### Recursive Call:

```
count += backtrack(row + 1, columns, diagonals, anti_diagonals)
```

* Move to the next row to place another queen.

##### Backtrack:

```
columns.remove(col)
diagonals.remove(diagonal)
anti_diagonals.remove(anti_diagonal)
```

* Remove the queen and try the next column.

##### Return the Count:

```
return count
```

* This accumulates the number of valid arrangements for the current path.

---

### 📌 Test Cases

```
print(non_attacking_queens(4))  # Output: 2
```

* For 4x4 board, there are 2 valid configurations.

```
print(non_attacking_queens(2))  # Output: 0
```

* For 2x2 board, it's impossible to place 2 queens without conflict.

```
print(non_attacking_queens(10))  # Output: 724
```

* For 10x10 board, there are 724 valid ways.

---

### 🧠 Why It Works Efficiently

* **Backtracking + Pruning**: Quickly skips invalid placements using sets.
* **Diagonal encoding** is a clever trick to avoid a full `n x n` matrix.

---

Here's an **ASCII visualization** of how queens are placed on a chessboard for `n = 4`, showing the **two valid solutions**
to the 4-Queens problem:

---

### ✅ First Valid Configuration (Solution 1)

Each row has exactly **one `Q`** (queen), and `.` represents an empty square.

```
. Q . .
. . . Q
Q . . .
. . Q .
```

Explanation:

* Row 0 → Column 1
* Row 1 → Column 3
* Row 2 → Column 0
* Row 3 → Column 2

No two queens are in the same row, column, or diagonal.

---

### ✅ Second Valid Configuration (Solution 2)

```
. . Q .
Q . . .
. . . Q
. Q . .
```

Explanation:

* Row 0 → Column 2
* Row 1 → Column 0
* Row 2 → Column 3
* Row 3 → Column 1

Again, all queens are placed safely.

---

### 🔥 Diagonal Explanation

Let’s take the first solution:

```
. Q . .   ← Row 0, Col 1 → Diagonal = -1, Anti-diagonal = 1
. . . Q   ← Row 1, Col 3 → Diagonal = -2, Anti-diagonal = 4
Q . . .   ← Row 2, Col 0 → Diagonal = 2, Anti-diagonal = 2
. . Q .   ← Row 3, Col 2 → Diagonal = 1, Anti-diagonal = 5
```

None of the diagonal or anti-diagonal values repeat → queens do **not attack** each other diagonally.

"""
