# Problem Description:

"""
                                               Levenshtein Distance

Write a function that takes in `two strings` and returns the minimum number of edit operations that need to be performed on the
first string to obtain the second string.

There are three edit operations: `insertion` of a character, `deletion` of a character, and `substitution` of a character for another.


## Sample Input:
```
str_1 = "abc"
str_2 = "yabd"
```

## Sample Output:
```
2

// insert "y"; substitute "c" for "d"
```

## Optimal Time & Space Complexity:
```
O(n * m) time | O(min(n, m)) space - where `n` and `m` are the lengths of the two input strings.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n * m) time | O(n * m) space
def levenshtein_distance(str_1, str_2):
    """
    Calculate the minimum number of single-character edits (insertions, deletions, or substitutions)
    required to change one string into another.

    Args:
        str_1: The first string to compare
        str_2: The second string to compare

    Returns:
        The Levenshtein distance between the two strings
    """

    # Initialize a 2D array (matrix) to store edit distances
    # Rows represent characters in str_2, columns represent characters in str_1
    # The size is (len(str_2)+1) x (len(str_1)+1) to account for empty strings
    edits = [[x for x in range(len(str_1) + 1)] for y in range(len(str_2) + 1)]

    # Initialize the first column:
    # The distance between empty str_1 and str_2[0..i] is i (i insertions needed)
    for i in range(1, len(str_2) + 1):
        edits[i][0] = edits[i - 1][0] + 1

    # Fill the edit distance matrix
    for i in range(1, len(str_2) + 1):
        for j in range(1, len(str_1) + 1):
            if str_2[i - 1] == str_1[j - 1]:
                # Characters match - no edit needed, take diagonal value
                edits[i][j] = edits[i - 1][j - 1]
            else:
                # Characters don't match - take minimum of possible edits and add 1
                edits[i][j] = 1 + min(
                    edits[i - 1][j - 1],  # substitution (diagonal)
                    edits[i - 1][j],  # deletion (left)
                    edits[i][j - 1],  # insertion (up)
                )

    # The bottom-right cell contains the edit distance between full str_1 and str_2
    return edits[-1][-1]


# Test Cases:

print(levenshtein_distance("abc", "yabd"))
# Output: 2

print(levenshtein_distance("", ""))
# Output: 0

print(levenshtein_distance("cereal", "saturdzz"))
# Output: 7

# =========================================================================================================================== #

# Big O Analysis:

"""
# Time and Space Complexity Analysis:

### Time Complexity:

The algorithm uses a dynamic programming approach with a 2D table (`edits`) of size `(len(str_2) + 1) × (len(str_1) + 1)`.

- The outer loop runs `len(str_2) + 1` times (rows).
- The inner loop runs `len(str_1) + 1` times (columns).

For each cell `(i, j)`, the computation involves:
1. A constant-time check (`if str_2[i - 1] == str_1[j - 1]`).
2. Either a constant-time assignment (`edits[i][j] = edits[i - 1][j - 1]`) or a constant-time `min` operation over 3 values.

Thus, the total time complexity is:

    O((m + 1) * (n + 1)) = O(m * n)

where:
- m = len(str_2)
- n = len(str_1)

### Space Complexity:

The algorithm constructs a 2D table (`edits`) of size `(m + 1) × (n + 1)`, where:
- m = len(str_2)
- n = len(str_1)

Thus, the space complexity is: O(m * n)

### Summary:
- **Time Complexity:** O(m * n) 
- **Space Complexity:** O(m * n) 

Where `m` and `n` are the lengths of `str_2` and `str_1`, respectively.

### Optimization Note:

The space complexity can be optimized to O(min(m, n)) by using two 1D arrays instead of a full 2D table, since we only need the
previous row to compute the current row.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
The function `levenshtein_distance(str_1, str_2)` computes the **Levenshtein distance** between two strings. This is the
**minimum number of single-character edits** (insertions, deletions, or substitutions) required to change one string into the other.

---

## 🔍 Step-by-Step Explanation

### 📌 Step 1: Initialize the matrix

```
edits = [[x for x in range(len(str_1) + 1)] for y in range(len(str_2) + 1)]
```

* Creates a 2D list (matrix) of size `(len(str_2)+1) x (len(str_1)+1)`
* The first row (`edits[0]`) is initialized with values `0 to len(str_1)` (i.e., `[0, 1, 2, ..., len(str_1)]`)
* Each column in the first row represents the cost of deleting characters from `str_1` to get an empty string.

📌 Example for `str_1="abc"` and `str_2="yabd"`:

```
Initial matrix:
[[0, 1, 2, 3],
 [0, 0, 0, 0],
 [0, 0, 0, 0],
 [0, 0, 0, 0],
 [0, 0, 0, 0]]
```

---

### 📌 Step 2: Fill the first column

```
for i in range(1, len(str_2) + 1):
    edits[i][0] = edits[i - 1][0] + 1
```

* Sets up the cost of inserting characters into an empty `str_1` to form `str_2`
* `edits[i][0]` = number of insertions needed

📌 After this step:

```
[[0, 1, 2, 3],
 [1, 0, 0, 0],
 [2, 0, 0, 0],
 [3, 0, 0, 0],
 [4, 0, 0, 0]]
```

---

### 📌 Step 3: Fill the matrix (core logic)

```
for i in range(1, len(str_2) + 1):
    for j in range(1, len(str_1) + 1):
        if str_2[i - 1] == str_1[j - 1]:
            edits[i][j] = edits[i - 1][j - 1]
        else:
            edits[i][j] = 1 + min(
                edits[i - 1][j - 1],  # substitution
                edits[i - 1][j],      # insertion
                edits[i][j - 1]       # deletion
            )
```

* **Substitution**: If characters don’t match, try replacing one (diagonal value `edits[i-1][j-1]`)
* **Insertion**: Try inserting a character from `str_2` into `str_1` (top value `edits[i-1][j]`)
* **Deletion**: Try deleting a character from `str_1` (left value `edits[i][j-1]`)
* Add `1` to represent the cost of this operation

If the characters match: no change (use diagonal value directly)

---

### 📌 Step 4: Return the result

```
return edits[-1][-1]
```

* Bottom-right value of the matrix: minimum number of operations to transform `str_1` to `str_2`

---

## ✅ Test Case Breakdown

### 1. `levenshtein_distance("abc", "yabd")`

Matrix is filled as:

```
    ""  a  b  c
""  0   1  2  3
y   1   1  2  3
a   2   1  2  3
b   3   2  1  2
d   4   3  2  2  <-- Result
```

✅ Output: `2`

Operations:

* Insert `'y'`
* Replace `'c'` with `'d'`

---

### 2. `levenshtein_distance("", "")`

* No operations needed
  ✅ Output: `0`

---

### 3. `levenshtein_distance("cereal", "saturdzz")`

✅ Output: `7`

Operations:

* Multiple substitutions and insertions required

---

## 🧠 Summary

* The matrix represents edit distances between all prefixes of the two strings.
* Dynamic programming is used to build up the solution from smaller subproblems.
* Final result is in the bottom-right cell of the matrix.

---

Let's visualize the **Levenshtein distance matrix** in **ASCII** for this example:

```
levenshtein_distance("abc", "yabd")
```

We will build a matrix with `"abc"` along the top (horizontally), `"yabd"` along the side (vertically), and
show how the matrix fills up.

---

## 🔤 Strings:

* `str_1 = "abc"` (columns)
* `str_2 = "yabd"` (rows)

---

### 🧮 Final Matrix:

Each cell represents the **edit distance** to get from the prefix of `str_1[:j]` to `str_2[:i]`.

```
      ''  a  b  c
   +---------------
'' |  0  1  2  3
y  |  1  1  2  3
a  |  2  1  2  3
b  |  3  2  1  2
d  |  4  3  2  2
```

---

### 🔍 How to read it:

* Top-left (0,0) is comparing two empty strings.
* Move right →: adds characters from `"abc"` (deletions from `str_1`)
* Move down ↓: adds characters from `"yabd"` (insertions into `str_1`)
* Each cell value is the **minimum edits** required to convert prefixes.

---

### 📘 Legend:

* **Diagonal** → Substitution (or match if characters equal)
* **Left** → Deletion
* **Top** → Insertion

---

### ✅ Path for conversion:

To convert `"abc"` → `"yabd"` (final result = `2`):

1. Insert `'y'` at start → `'yabc'`
2. Replace `'c'` with `'d'` → `'yabd'`

Minimum edits = **2**

---

Let's walk through the **step-by-step filling** of the Levenshtein distance matrix for:

```
levenshtein_distance("abc", "yabd")
```

---

## 📋 Strings

* `str_1 = "abc"` → horizontal (columns)
* `str_2 = "yabd"` → vertical (rows)

---

### 🧾 Step 1: Initialize the matrix

We create a `(len(str_2)+1) x (len(str_1)+1)` matrix and initialize the first row and first column with index values:

```
      ''  a  b  c
   +---------------
'' |  0  1  2  3
y  |  1  0  0  0
a  |  2  0  0  0
b  |  3  0  0  0
d  |  4  0  0  0
```

* Row 0: Cost of deleting characters from "abc"
* Column 0: Cost of inserting characters into ""

---

### 🧾 Step 2: Fill the matrix row by row

We now compute each cell:

---

#### 🧪 Row 1 (`str_2[0] = 'y'`)

Compare with each of `str_1 = "a", "b", "c"`:

* `y ≠ a` → `min(1, 2, 1) + 1 = 1`
* `y ≠ b` → `min(2, 3, 2) + 1 = 2`
* `y ≠ c` → `min(3, 4, 3) + 1 = 3`

```
      ''  a  b  c
   +---------------
'' |  0  1  2  3
y  |  1  1  2  3
a  |  2  0  0  0
b  |  3  0  0  0
d  |  4  0  0  0
```

---

#### 🧪 Row 2 (`str_2[1] = 'a'`)

* `a == a` → use diagonal: 1
* `a ≠ b` → `min(2, 3, 1) + 1 = 2`
* `a ≠ c` → `min(3, 4, 2) + 1 = 3`

```
      ''  a  b  c
   +---------------
'' |  0  1  2  3
y  |  1  1  2  3
a  |  2  1  2  3
b  |  3  0  0  0
d  |  4  0  0  0
```

---

#### 🧪 Row 3 (`str_2[2] = 'b'`)

* `b ≠ a` → `min(1, 2, 3) + 1 = 2`
* `b == b` → use diagonal: 1
* `b ≠ c` → `min(2, 3, 1) + 1 = 2`

```
      ''  a  b  c
   +---------------
'' |  0  1  2  3
y  |  1  1  2  3
a  |  2  1  2  3
b  |  3  2  1  2
d  |  4  0  0  0
```

---

#### 🧪 Row 4 (`str_2[3] = 'd'`)

* `d ≠ a` → `min(2, 3, 4) + 1 = 3`
* `d ≠ b` → `min(1, 2, 3) + 1 = 2`
* `d ≠ c` → `min(2, 3, 2) + 1 = 2`

```
      ''  a  b  c
   +---------------
'' |  0  1  2  3
y  |  1  1  2  3
a  |  2  1  2  3
b  |  3  2  1  2
d  |  4  3  2  2
```

---

### ✅ Final Result: `2`

From bottom-right cell: `2 edits` are needed to turn `"abc"` into `"yabd"`.

---

### 🧠 Summary of Edits:

1. Insert `'y'` → `'yabc'`
2. Replace `'c'` with `'d'` → `'yabd'`

"""
