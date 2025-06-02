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


# O(m * n * min(m, n)) time | O(m * n * min(m, n)) space
def longest_common_subsequence(str_1, str_2):
    """
    Finds the longest common subsequence (LCS) between two strings.
    A subsequence is a sequence that appears in the same relative order but not necessarily contiguous.

    Args:
        str_1: First input string
        str_2: Second input string

    Returns:
        A list of characters representing the longest common subsequence
    """

    # Create a 2D array (matrix) to store LCS solutions for subproblems
    # Dimensions: (len(str_2)+1) x (len(str_1)+1)
    # Initialize each cell with an empty list (will store subsequence characters)
    lcs = [[[] for x in range(len(str_1) + 1)] for y in range(len(str_2) + 1)]

    # Build the solution matrix bottom-up
    for i in range(1, len(str_2) + 1):  # Loop through each character of str_2 (rows)
        # Loop through each character of str_1 (columns)
        for j in range(1, len(str_1) + 1):

            # If current characters match, build on previous diagonal solution
            if str_2[i - 1] == str_1[j - 1]:
                # Take the LCS from the diagonal (top-left) cell and append current character
                lcs[i][j] = lcs[i - 1][j - 1] + [str_2[i - 1]]
            else:
                # Characters don't match - take the longer of either:
                # 1. The LCS from the cell above (lcs[i-1][j])
                # 2. The LCS from the cell to the left (lcs[i][j-1])
                lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1], key=len)

    # The bottom-right cell contains the LCS for the full strings
    return lcs[-1][-1]


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

### Time Complexity:

The function uses dynamic programming to fill a 2D table `lcs` of size `(len(str_2) + 1) × (len(str_1) + 1)`. 

- The outer loop runs `len(str_2)` times (from `1` to `len(str_2)`).
- The inner loop runs `len(str_1)` times (from `1` to `len(str_1)`).
- Inside the inner loop, the operations are:
  - Comparing characters (`str_2[i - 1] == str_1[j - 1]`), which is `O(1)`.
  - Concatenating lists (`lcs[i - 1][j - 1] + [str_2[i - 1]]`), which is `O(k)` where `k` is the length of the LCS up to that point.
  - Comparing lengths of two lists (`max(lcs[i - 1][j], lcs[i][j - 1], key=len)`), which is `O(1)`.

In the worst case (when the two strings are identical), the LCS grows linearly with the length of the strings, so the concatenation
operation (`lcs[i - 1][j - 1] + [str_2[i - 1]]`) could take up to `O(min(m, n))` time, where `m` and `n` are the lengths of
`str_2` and `str_1`, respectively.

Thus, the total time complexity is:
- Best case (when the two strings share no common characters): `O(m * n)`, since the concatenation is `O(1)` (empty list).
- Worst case (when the two strings are identical): `O(m * n * min(m, n))`, because the concatenation can be up to
`O(min(m, n))` for each cell.

### Space Complexity:

The space complexity is dominated by the `lcs` table, which has dimensions `(m + 1) × (n + 1)`, where `m = len(str_2)` and
`n = len(str_1)`. 

Each cell in the table stores a list representing the LCS up to that point. In the worst case (when the two strings are identical),
the LCS stored in the last cell will be of length `min(m, n)`. However, since the table is filled row by row, and each row depends
only on the previous row, you could optimize the space complexity to `O(min(m, n) * n)` or `O(min(m, n) * m)` by keeping only two
rows (current and previous) at a time. However, the given implementation does not do this, so the space complexity is:

- `O(m * n * min(m, n))`, because each of the `m * n` cells could store a list of size up to `min(m, n)`.

### Summary:
- **Time Complexity**: 
  - Best case: `O(m * n)` (no common subsequence).
  - Worst case: `O(m * n * min(m, n))` (strings are identical).
  
- **Space Complexity**: `O(m * n * min(m, n))`.

### Note:
The implementation can be optimized to use `O(min(m, n))` space by only storing the length of the LCS and reconstructing the
sequence afterward, but the given implementation explicitly builds the LCS strings at each step, leading to higher space usage.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
This function, `longest_common_subsequence`, computes the **Longest Common Subsequence (LCS)** between two strings using
**Dynamic Programming**. The **LCS** is the longest sequence of characters that appear left-to-right (not necessarily consecutively)
in both strings.

---

## 🔧 Function Definition

```
def longest_common_subsequence(str_1, str_2):
```

* Takes two strings `str_1` and `str_2` as input.
* Returns a **list of characters** representing their LCS.

---

## 🧱 Step-by-Step Explanation

### Step 1: Initialize the 2D Table

```
lcs = [[[] for x in range(len(str_1) + 1)] for y in range(len(str_2) + 1)]
```

* A 2D list `lcs` of size `(len(str_2)+1) x (len(str_1)+1)` is created.
* Each cell `lcs[i][j]` will store the **LCS between the first `i` characters of `str_2` and the first `j` characters
of `str_1`** as a list.
* It's initialized with empty lists.

---

### Step 2: Fill the Table

```
for i in range(1, len(str_2) + 1):
    for j in range(1, len(str_1) + 1):
```

* Loops through all characters of `str_2` (outer loop) and `str_1` (inner loop).
* The indexing starts from `1` to align with the characters (since `lcs[0][*]` and `lcs[*][0]` represent empty prefixes).

#### Step 2a: Characters Match

```
if str_2[i - 1] == str_1[j - 1]:
    lcs[i][j] = lcs[i - 1][j - 1] + [str_2[i - 1]]
```

* If the characters match, that character is **part of the LCS**.
* Append it to the LCS of the previous characters: `lcs[i-1][j-1]`.

#### Step 2b: Characters Don’t Match

```
else:
    lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1], key=len)
```

* If the characters don't match, choose the **longer LCS** between:

  * `lcs[i-1][j]`: skipping current character of `str_2`
  * `lcs[i][j-1]`: skipping current character of `str_1`

---

### Step 3: Return the Final Result

```
return lcs[-1][-1]
```

* This cell contains the LCS between the full `str_1` and `str_2`.

---

## 📦 Test Case Walkthrough

### Example:

```
print(longest_common_subsequence("ZXVVYZW", "XKYKZPW"))
```

**Step-by-step matching:**

* Comparing characters in `"ZXVVYZW"` and `"XKYKZPW"`.
* Matching characters in sequence: **X → Y → Z → W**
* Final result: `['X', 'Y', 'Z', 'W']`

---

## 💡 Key Concepts Used

* **Dynamic Programming**: Builds up solutions to subproblems.
* **2D Table**: Tracks intermediate LCS solutions.
* **List Concatenation**: Builds LCS step-by-step.
* **Immutable vs Mutable Structures**: Each `lcs[i][j]` is a new list, avoiding mutation issues.

---

## ✅ Pros

* Clear logic.
* Easy to understand how LCS builds up.
* Returns the **actual sequence**, not just its length.

---

## ❗ Potential Improvements

* Memory Optimization: You can use only 2 rows instead of the full 2D table if only the length is needed.
* Performance: This is `O(m*n)` in time and space, where `m` and `n` are lengths of the strings.

---

Here's a **step-by-step ASCII visualization** of how the **Longest Common Subsequence (LCS)** algorithm works using dynamic
programming for this test case:

```
str_1 = "ZXVVYZW"
str_2 = "XKYKZPW"
```

We'll construct a 2D table where:

* Rows = characters from `str_2` (with an empty prefix `''` at the top)
* Columns = characters from `str_1` (with an empty prefix `''` at the left)
* Each cell shows the **LCS (as a string)** between the prefixes up to that point.

---

### 📊 Table Initialization (Empty LCS Everywhere)

```
      ''   Z   X   V   V   Y   Z   W
   +----+---+---+---+---+---+---+---+
'' |    |   |   |   |   |   |   |   |
X  |    |   | X | X | X | X | X | X |
K  |    |   | X | X | X | X | X | X |
Y  |    |   | X | X | X | XY| XY| XY|
K  |    |   | X | X | X | XY| XY| XY|
Z  |    | Z | Z | Z | Z | ZY| ZY| ZY|
P  |    | Z | Z | Z | Z | ZY| ZY| ZY|
W  |    | Z | Z | Z | Z | ZY| ZY| ZYW|
```

---

### ✅ Explanation of Some Key Cells

* `lcs[1][2]`: comparing `X` and `X` → match → `['X']`
* `lcs[3][5]`: comparing `Y` and `Y` → match → append `Y` to previous `['X']` → `['X', 'Y']`
* `lcs[5][1]`: comparing `Z` and `Z` → match → `['Z']`
* `lcs[7][7]`: comparing `W` and `W` → match → append `W` to `['Z', 'Y']` → `['Z', 'Y', 'W']`
(but keep LCS `['X', 'Y', 'Z', 'W']` from earlier branch)

---

### 🎯 Final Result

From the bottom-right cell:

```
lcs[7][7] = ['X', 'Y', 'Z', 'W']
```

---

### 🧠 Legend

* Each cell shows the best **LCS so far** between the prefixes of `str_1` and `str_2`.
* At each match, we extend the diagonal LCS.
* Otherwise, we take the longer LCS from top or left.

"""
