# Problem Description:

"""
                                              Longest Common Subsequence

Write a function that takes in two strings and returns their longest common subsequence.

A subsequence of a string is a set of characters that aren't necessarily adjacent in the string but that are in the same order as
they appear in the string. For instance, the characters `["a", "c", "d"]` form a subsequence of the string `"abcd"`, and so do the
characters `["b", "d"]`.

> Note that a single character in a string and the string itself are both valid subsequences of the string.

You can assume that there will only be one longest common subsequence.


## Sample Input:
```
str_1 = "ZXVVYZW"
str_2 = "XKYKZPW"
```

## Sample Output:
```
["X", "Y", "Z", "W"]
```

## Optimal Time & Space Complexity:
```
O(n * m) time | O(n * m) space - where `n` and `m` are the lengths of the two input strings.
```

"""

# =========================================================================================================================== #

# Solution:


# O(m * n) time | O(m * n) space
def longest_common_subsequence(str_1, str_2):
    # Get lengths of both input strings
    m, n = len(str_1), len(str_2)

    # Create a DP (Dynamic Programming) table of size (m+1) x (n+1) initialized with 0s
    # dp[i][j] will store the length of LCS of str_1[0..i-1] and str_2[0..j-1]
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the DP table
    for i in range(1, m + 1):  # for each character in str_1
        for j in range(1, n + 1):  # for each character in str_2
            if str_1[i - 1] == str_2[j - 1]:
                # If characters match, take diagonal value + 1
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                # If no match, take maximum of top or left cell
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Now we'll reconstruct the LCS from the DP table
    lcs = []  # This will store the characters of the LCS
    i, j = m, n  # Start from the bottom-right corner of the DP table

    # Backtrack through the DP table
    while i > 0 and j > 0:
        if str_1[i - 1] == str_2[j - 1]:
            # If characters match, it's part of LCS
            lcs.append(str_1[i - 1])
            # Move diagonally up-left
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            # If top cell has higher value than left cell, move up
            i -= 1
        else:
            # Otherwise move left
            j -= 1

    # The LCS was built in reverse order, so reverse it before returning
    return lcs[::-1]


# Test Cases:

print(longest_common_subsequence("ZXVVYZW", "XKYKZPW"))
# Output: ['X', 'Y', 'Z', 'W']

print(longest_common_subsequence("", "ABCDEFG"))
# Output: []

print(longest_common_subsequence("ABCDEFG", "APPLES"))
# Output: ['A', 'E']

# =========================================================================================================================== #

# Big O Analysis:

"""
# Time and Space Complexity Analysis:

## Time Complexity Analysis

The time complexity of the `longest_common_subsequence` function can be broken down into two main parts:

1. **Building the DP Table**:
   - The DP table has dimensions `(m + 1) x (n + 1)`, where `m` and `n` are the lengths of `str_1` and `str_2`, respectively.
   - We fill each cell of the DP table exactly once (except the first row and first column, which are initialized to 0).
   - Filling each cell involves a constant amount of work (comparison and possibly a `max` operation).
   - Thus, the time to build the DP table is `O(m * n)`.

2. **Backtracking to Build the LCS String**:
   - During backtracking, we start at `(m, n)` and move towards `(0, 0)`.
   - In the worst case, we might move up or left at each step until we reach the top or left edge of the table.
   - The maximum number of steps is `m + n` (since we decrement `i` or `j` at each step).
   - Each step involves a constant amount of work (comparison and possibly appending to the `lcs` list).
   - Thus, the backtracking step is `O(m + n)`.

Combining these, the overall time complexity is: O(m * n) + O(m + n) = O(m * n) (since `O(m * n)` dominates
`O(m + n)` for large `m` and `n`).

## Space Complexity Analysis

The space complexity is determined by the space needed to store the DP table and the auxiliary data structures:

1. **DP Table**:
   - The DP table has dimensions `(m + 1) x (n + 1)`, so it requires `O(m * n)` space.

2. **LCS List**:
   - The `lcs` list stores the characters of the LCS, which is at most `min(m, n)` in length.
   - Thus, the space for `lcs` is `O(min(m, n))`.

3. **Other Variables**:
   - Variables like `i`, `j`, `m`, `n`, etc., use constant space (`O(1)`).

Thus, the dominant term is the DP table, giving an overall space complexity of: O(m * n)

### Summary

- **Time Complexity**: `O(m * n)`
- **Space Complexity**: `O(m * n)`

### Additional Notes

- The space complexity can be optimized to `O(min(m, n))` by observing that we only need the current and previous rows of the DP
table at any point in time (using a rolling array technique). However, the backtracking step would still require additional space
to reconstruct the LCS.
- The `O(m + n)` backtracking step does not affect the overall time complexity because it is dominated by `O(m * n)`. Similarly,
the space for `lcs` is dominated by the DP table unless you optimize the DP table space.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
Let's go through the function `longest_common_subsequence` step by step and understand how it works, including how it computes
and builds the longest common subsequence (LCS) of two strings.

---

### 🔍 **What is LCS (Longest Common Subsequence)?**

* A **subsequence** is a sequence that appears in the same relative order but **not necessarily contiguously**.
* The **longest common subsequence** is the longest sequence that appears in **both strings** in the same order.

For example:

* LCS of `"ZXVVYZW"` and `"XKYKZPW"` is `"XYZW"`.

---

## 📘 Function Breakdown

```
def longest_common_subsequence(str_1, str_2):
```

* The function takes two strings `str_1` and `str_2`.

---

### 🔹 Step 1: Create the DP Table

```
m, n = len(str_1), len(str_2)
dp = [[0] * (n + 1) for _ in range(m + 1)]
```

* `m` and `n` store the lengths of the two input strings.
* `dp[i][j]` will represent the **length of the LCS** of `str_1[:i]` and `str_2[:j]`.
* The DP table has `(m+1)` rows and `(n+1)` columns to handle base cases (empty string comparisons).

---

### 🔹 Step 2: Fill the DP Table

```
for i in range(1, m + 1):
    for j in range(1, n + 1):
        if str_1[i - 1] == str_2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
```

* This double loop goes through every character in `str_1` and `str_2`.
* If characters match: `str_1[i-1] == str_2[j-1]`

  * Then the LCS length is 1 + LCS of the previous substring.
  * So `dp[i][j] = dp[i-1][j-1] + 1`.
* Else:

  * Take the **maximum** LCS length by skipping either one character from `str_1` or `str_2`.
  * So `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`.

✅ At the end of this step, `dp[m][n]` will contain the length of the LCS.

---

### 🔹 Step 3: Backtrack to Build the LCS

```
lcs = []
i, j = m, n
while i > 0 and j > 0:
    if str_1[i - 1] == str_2[j - 1]:
        lcs.append(str_1[i - 1])
        i -= 1
        j -= 1
    elif dp[i - 1][j] > dp[i][j - 1]:
        i -= 1
    else:
        j -= 1
```

* Start from the bottom-right corner of the `dp` table.
* If characters match, it **must be part of the LCS**:

  * Add to `lcs`, move diagonally up-left.
* If not matching:

  * Move in the direction of the **larger value** (either left or up), because that path led to a longer subsequence.

---

### 🔹 Step 4: Return Result

```
return lcs[::-1]
```

* Since we backtracked from the end, we reverse the `lcs` list before returning it.

---

## ✅ Test Case Walkthrough

### Example:

```
print(longest_common_subsequence("ZXVVYZW", "XKYKZPW"))
```

Step-by-step:

* DP table is filled based on character matches.
* After filling, `dp[7][7]` contains the length of LCS = 4.
* Backtracking gives: `['W', 'Z', 'Y', 'X']` → reversed → `['X', 'Y', 'Z', 'W']`.

---

## 🧪 Other Test Cases:

```
print(longest_common_subsequence("", "ABCDEFG"))
# Output: [] → empty string has no common characters
```

```
print(longest_common_subsequence("ABCDEFG", "APPLES"))
# Output: ['A', 'E'] → only 'A' and 'E' appear in the same order
```

---

## ✅ Summary

* Uses **Dynamic Programming (DP)** to compute the length of the LCS efficiently.
* Time Complexity: **O(m * n)** where `m` and `n` are the lengths of the input strings.
* Space Complexity: **O(m * n)** for the DP table.
* Then **backtracks** to build the actual LCS.

---

Let's walk through the example:

```
longest_common_subsequence("ZXVVYZW", "XKYKZPW")
```

We’ll visualize the **DP table** in ASCII after it's fully built and also show **how backtracking finds the LCS**.

---

### 🧩 Inputs:

* `str_1 = "ZXVVYZW"` (length = 7)
* `str_2 = "XKYKZPW"` (length = 7)

---

### 📐 DP Table Layout:

We'll build a table where:

* Rows are characters from `str_1` ("Z X V V Y Z W")
* Columns are characters from `str_2` ("X K Y K Z P W")
* The top-left cell represents the empty prefixes.

Each cell contains the LCS length up to that point.

---

### 🧮 Final DP Table (after filling):

```
      ""  X  K  Y  K  Z  P  W
   +---------------------------
"" |  0  0  0  0  0  0  0  0
Z  |  0  0  0  0  0  1  1  1
X  |  0  1  1  1  1  1  1  1
V  |  0  1  1  1  1  1  1  1
V  |  0  1  1  1  1  1  1  1
Y  |  0  1  1  2  2  2  2  2
Z  |  0  1  1  2  2  3  3  3
W  |  0  1  1  2  2  3  3  4
```

🟢 `dp[7][7] = 4` → The length of the LCS is **4**.

---

### 🔄 Backtracking Path

Start from bottom-right: `(7,7)`
Follow arrows:

```
dp[7][7] = 4 → W == W → add 'W' ← ↖
dp[6][6] = 3 → Z == Z → add 'Z' ← ↖
dp[5][5] = 2 → Y == Y → add 'Y' ← ↖
dp[4][4] = 1 → no match, go up ← ↑
dp[3][4] = 1 → no match, go up ← ↑
dp[2][4] = 1 → no match, go left ← ←
dp[2][3] = 1 → no match, go left ← ←
dp[2][2] = 1 → no match, go left ← ←
dp[2][1] = 1 → X == X → add 'X' ← ↖
```

✔ Found characters in reverse: `['W', 'Z', 'Y', 'X']`
✔ Reverse it to get the final LCS: `['X', 'Y', 'Z', 'W']`

---

### ✅ Final Answer:

```
LCS: ['X', 'Y', 'Z', 'W']
```

"""
