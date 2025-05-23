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
O(nm) time | O(min(n, m)) space - where `n` and `m` are the lengths of the two input strings.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n * m) time | O(m) space
def levenshtein_distance(str_1, str_2):
    # Ensure str_1 is the longer string to optimize space (we only need O(m) space)
    if len(str_1) < len(str_2):
        return levenshtein_distance(str_2, str_1)

    m = len(str_1)  # Length of longer string
    n = len(str_2)  # Length of shorter string

    # Initialize dp array where dp[j] represents the edit distance between
    # the first j characters of str_1 and empty string (base case)
    # This is equivalent to j deletions needed
    dp = list(range(m + 1))

    for i in range(1, n + 1):
        # prev_diagonal stores the value from the previous diagonal (dp[i-1][j-1])
        # which would be used for character match cases
        prev_diagonal = dp[0]
        # Update base case (comparing empty string with first i characters of str_2)
        dp[0] = i

        for j in range(1, m + 1):
            # Store current dp[j] before updating (will become prev_diagonal for next iteration)
            temp = dp[j]

            if str_1[j - 1] == str_2[i - 1]:
                # Characters match - no operation needed, carry forward the diagonal value
                dp[j] = prev_diagonal
            else:
                # Characters don't match - take minimum of three possible operations:
                # 1. Replace (prev_diagonal + 1)
                # 2. Delete (dp[j] + 1)
                # 3. Insert (dp[j - 1] + 1)
                dp[j] = 1 + min(prev_diagonal, dp[j], dp[j - 1])

            # Update prev_diagonal for next iteration
            prev_diagonal = temp

    # The final result is in dp[m], representing the edit distance between
    # the full str_1 (length m) and full str_2 (length n)
    return dp[m]


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

## Time Complexity Analysis

The time complexity of the given Levenshtein distance algorithm is **O(m * n)**, where:
- `m` is the length of `str_1` (the longer string, due to the initial swap if necessary),
- `n` is the length of `str_2` (the shorter string).

### Explanation:
1. The outer loop runs `n` times (for each character in `str_2`).
2. The inner loop runs `m` times (for each character in `str_1`).
3. Inside the inner loop, the operations (comparisons, min calculations, and assignments) are all **O(1)**.
4. Thus, the total time is proportional to `m * n`.

## Space Complexity Analysis

The space complexity is **O(m)**, where `m` is the length of the longer string (`str_1`).

### Explanation:
1. The algorithm uses a 1D array `dp` of size `m + 1` (initialized as `list(range(m + 1))`).
2. It also uses a few extra variables (`prev_diagonal`, `temp`), but these are **O(1)** and do not depend on input size.
3. The space is dominated by the `dp` array, so it is **O(m)**.

### Summary:
- **Time Complexity:** O(m * n) 
- **Space Complexity:** O(m) 

### Why not O(m * n)?

A naive implementation of Levenshtein distance might use a 2D `dp` table, which would require **O(m * n)** space. However, this
implementation optimizes space by observing that only the previous row (or column) is needed at any step, so it uses a 1D array
and tracks the diagonal value manually.

### Key Observations:

- The initial swap ensures we always use the shorter string for the outer loop, but the time complexity remains **O(m * n)**
(no asymptotic improvement, though practical speed may vary slightly).
- The space optimization to **O(m)** is significant, especially for long strings.

### Example:
For two strings of lengths 5 and 3:
- Time: 5 * 3 = 15 operations.
- Space: Array of size 5 + 1 = 6.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
This function calculates the **Levenshtein distance** (also known as edit distance) between two strings. The **Levenshtein
distance** is the minimum number of single-character **insertions**, **deletions**, or **substitutions** required to change
one string into the other.

---

### ✅ **Code Overview**

```
def levenshtein_distance(str_1, str_2):
```

* Takes two strings `str_1` and `str_2` as input.

---

### 🔄 **Step 1: Ensure str_1 is the longer string**

```
    if len(str_1) < len(str_2):
        return levenshtein_distance(str_2, str_1)
```

* If `str_1` is shorter than `str_2`, swap them by calling the function again with reversed inputs.
* This is done for memory optimization because we use a 1D array for dynamic programming. Using the shorter string for the
number of rows minimizes space usage.

---

### 📏 **Step 2: Initialize variables**

```
    m = len(str_1)
    n = len(str_2)
```

* `m`: length of the longer string
* `n`: length of the shorter string

---

### 🧮 **Step 3: Initialize DP array**

```
    dp = list(range(m + 1))
```

* `dp` is a 1D list that stores current edit distances.
* Initially: `[0, 1, 2, ..., m]`
* Represents the cost of converting an empty `str_2` prefix to every prefix of `str_1`.

---

### 🔁 **Step 4: Fill DP table row by row**

```
    for i in range(1, n + 1):
        prev_diagonal = dp[0]
        dp[0] = i
```

* Loop over characters of `str_2`. For each row `i` (from 1 to n):

  * Save `dp[0]` as `prev_diagonal` (it will become the diagonal value in the DP matrix).
  * Set `dp[0]` to `i`: converting the first `i` characters of `str_2` to empty string takes `i` deletions.

---

### 🔁 **Step 5: Update each cell in the row**

```
    for j in range(1, m + 1):
        temp = dp[j]
```

* Loop over characters of `str_1`. For each column `j` (from 1 to m):

  * Store the current `dp[j]` temporarily, because it will be used as the diagonal in the next iteration.

```
    if str_1[j - 1] == str_2[i - 1]:
        dp[j] = prev_diagonal
```

* If characters match, no edit needed: copy the diagonal value (top-left cell in 2D matrix).

```
    else:
        dp[j] = 1 + min(prev_diagonal, dp[j], dp[j - 1])
```

* Else, calculate cost:

  * `prev_diagonal` → substitution
  * `dp[j]`        → deletion
  * `dp[j - 1]`    → insertion
  * Add 1 to the minimum of the three.

```
    prev_diagonal = temp
```

* Update `prev_diagonal` to the old value of `dp[j]` for the next iteration.

---

### ✅ **Step 6: Return final result**

```
    return dp[m]
```

* The last value in the `dp` array represents the edit distance between the full strings.

---

### 📊 Example Breakdown

```
levenshtein_distance("abc", "yabd")
```

Convert `"abc"` to `"yabd"`:

* insert `'y'` → `"yabc"`
* substitute `'c'` → `'d'`: `"yabd"`
* Total operations = **2**

---

### ✅ Test Cases Output

```
levenshtein_distance("abc", "yabd") → 2
levenshtein_distance("", "") → 0
levenshtein_distance("cereal", "saturdzz") → 7
```

---

### 🧠 Key Concepts

* **Dynamic Programming**: Uses a 1D DP array instead of a 2D matrix to save space.
* **Memory Optimization**: Only stores one row at a time using rolling computation.
* **Levenshtein Distance**: Measures how similar two strings are.

---

Let’s walk through an **ASCII visualization** of the **Levenshtein distance matrix** for this example:

---

### Example:

```
levenshtein_distance("abc", "yabd")
```

We’ll compare `"abc"` (length 3) and `"yabd"` (length 4).

Let:

* `str_1 = "abc"`
* `str_2 = "yabd"`

---

### 📐 2D Matrix Representation

We build a `(len(str_2)+1) x (len(str_1)+1)` matrix:

Each cell `[i][j]` represents the **edit distance** between:

* the first `i` characters of `"yabd"` (vertical),
* and the first `j` characters of `"abc"` (horizontal).

---

### 🧾 Initialization

We initialize the first row and column to represent conversions to/from empty strings.

```
      a  b  c       ← str_1 (columns)
   ┌─────────────
   │ 0  1  2  3
 y │ 1
 a │ 2
 b │ 3
 d │ 4
```

Now we fill the rest of the matrix based on:

* If characters match → copy diagonal value.
* Else → 1 + min(diagonal, left, top)

---

### 🧮 Fill In

We'll now fill the table step by step.

```
      a  b  c
   ┌─────────────
   │ 0  1  2  3
 y │ 1  1  2  3
 a │ 2  1  2  3
 b │ 3  2  1  2
 d │ 4  3  2  2
```

---

### 🔍 Explanation of Some Cells:

* Cell `[1][1]` → comparing `'y'` and `'a'` → different → min(0,1,1)+1 = 1
* Cell `[2][1]` → `'a'` and `'a'` → match → diagonal → 1
* Cell `[3][2]` → `'b'` and `'b'` → match → diagonal → 1
* Cell `[4][3]` → `'d'` and `'c'` → different → min(2,2,2)+1 = 3

---

### ✅ Final Result

Bottom-right cell = `2`, so:

```
levenshtein_distance("abc", "yabd") = 2
```

"""
