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


# O(n * m) time | O(min(n,m)) space
def levenshtein_distance(str_1, str_2):
    """
    Calculate the Levenshtein distance (edit distance) between two strings.
    This is the minimum number of single-character edits (insertions, deletions,
    or substitutions) required to change one string into the other.
    """

    # Make sure str_1 is the longer string to optimize space usage
    if len(str_1) < len(str_2):
        return levenshtein_distance(str_2, str_1)

    m = len(str_1)  # Length of longer string
    n = len(str_2)  # Length of shorter string

    # Initialize previous row of distances (represents the empty string case)
    # This row stores the distances for transforming prefixes of str_1 into empty str_2
    # For example, prev_row[j] = j (since we'd need j deletions)
    prev_row = list(range(m + 1))

    # Iterate through each character of the shorter string (str_2)
    for i in range(1, n + 1):
        # Initialize current row with distance for empty str_1 case
        # The first element is i (would need i insertions)
        curr_row = [i] + [0] * m

        # Iterate through each character of the longer string (str_1)
        for j in range(1, m + 1):
            if str_1[j - 1] == str_2[i - 1]:
                # Characters match - no operation needed, take diagonal value
                curr_row[j] = prev_row[j - 1]
            else:
                # Characters don't match - take minimum of possible operations:
                # 1. Substitution (diagonal) - prev_row[j-1] + 1
                # 2. Deletion (left) - curr_row[j-1] + 1
                # 3. Insertion (up) - prev_row[j] + 1
                curr_row[j] = 1 + min(prev_row[j - 1], prev_row[j], curr_row[j - 1])

        # Current row becomes previous row for next iteration
        prev_row = curr_row

    # The final element in the last row contains the Levenshtein distance
    return prev_row[m]


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

## **1. Time Complexity:**

The algorithm computes the Levenshtein distance using dynamic programming with **two nested loops**:
- **Outer loop**: Runs `n` times (where `n = len(str_2)`).
- **Inner loop**: Runs `m` times (where `m = len(str_1)`).

**Operations per cell `(i, j)`**:
1. **Character comparison** (`str_1[j-1] == str_2[i-1]`): O(1)
2. **Minimum of 3 values** (`prev_row[j-1]`, `prev_row[j]`, `curr_row[j-1]`): O(1)

**Total Time Complexity**:

    O(n * m)

- If m ≈ n, this simplifies to O(n²).

---

## **2. Space Complexity:**

The algorithm optimizes space by **only storing two rows** (`prev_row` and `curr_row`) instead of a full 2D table.

- **`prev_row`**: Size `m + 1` (stores the previous row of DP values).
- **`curr_row`**: Size `m + 1` (stores the current row being computed).

**Total Space Used**:

    O(2 * (m + 1)) ≈ O(m)

Since we ensure `m ≥ n` (by swapping `str_1` and `str_2` if necessary), the space complexity is: O(min(m, n))

---

### Summary:
- **Time Complexity:** O(m * n) 
- **Space Complexity:** O(min(m, n)) 

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
This function computes the **Levenshtein distance** between two strings. The **Levenshtein distance** is a metric that measures
how many **single-character edits** (insertions, deletions, or substitutions) are required to change one string into another.

---

### ✅ **Function Definition**

```
def levenshtein_distance(str_1, str_2):
```

This defines a function that takes two strings as input: `str_1` and `str_2`.

---

### 🔁 **Step 1: Ensure str_1 is the longer string**

```
    if len(str_1) < len(str_2):
        return levenshtein_distance(str_2, str_1)
```

* This ensures that `str_1` is **not shorter than** `str_2`.
* Why? To **optimize memory usage** by keeping the number of columns smaller in the dynamic programming table (fewer elements per row).

---

### 📏 **Step 2: Lengths**

```
    m = len(str_1)
    n = len(str_2)
```

`m` is the length of the longer string. `n` is the shorter one.

---

### 📐 **Step 3: Initialize previous row**

```
    prev_row = list(range(m + 1))
```

* This represents the distance from an **empty prefix of `str_2`** to **each prefix of `str_1`**.
* For example, to convert "" into "abc", you need 3 insertions. So this row would look like `[0, 1, 2, 3]`.

---

### 🔄 **Step 4: Loop over str_2 characters (outer loop)**

```
    for i in range(1, n + 1):
        curr_row = [i] + [0] * m
```

* We're building the current row of the DP table.
* `curr_row[0] = i` because converting the first `i` characters of `str_2` to an empty string takes `i` deletions.

---

### 🔁 **Step 5: Loop over str_1 characters (inner loop)**

```
    for j in range(1, m + 1):
        if str_1[j - 1] == str_2[i - 1]:
            curr_row[j] = prev_row[j - 1]
        else:
            curr_row[j] = 1 + min(
                prev_row[j - 1],   # substitution
                prev_row[j],       # deletion
                curr_row[j - 1]    # insertion
            )
```

* If the characters match (`str_1[j-1] == str_2[i-1]`), no operation is needed → cost is same as top-left (`prev_row[j - 1]`).
* Otherwise, we compute the minimum cost of:

  * Substitution (`prev_row[j - 1]`)
  * Deletion from `str_2` (`prev_row[j]`)
  * Insertion into `str_2` (`curr_row[j - 1]`)
* We add 1 to that minimum, because one operation was needed.

---

### 🔄 **Step 6: Update prev_row**

```
    prev_row = curr_row
```

* Move to the next row. What was current becomes previous.

---

### ✅ **Step 7: Return final answer**

```
    return prev_row[m]
```

* This is the cost to convert full `str_2` into full `str_1`.

---

### 📌 **Example: `levenshtein_distance("abc", "yabd")`**

|   |   | a | b | c |
| - | - | - | - | - |
|   | 0 | 1 | 2 | 3 |
| y | 1 | 1 | 2 | 3 |
| a | 2 | 1 | 2 | 3 |
| b | 3 | 2 | 1 | 2 |
| d | 4 | 3 | 2 | 2 |

Answer: **2**

---

### ✅ Test Case Explanation

```
print(levenshtein_distance("abc", "yabd"))  # Output: 2
```

* "abc" → "yabd"
* Edit 1: insert `y`
* Edit 2: change `c` to `d`

```
print(levenshtein_distance("", ""))  # Output: 0
```

* No change needed.

```
print(levenshtein_distance("cereal", "saturdzz"))  # Output: 7
```

* Many edits needed → substitution, insertions, etc.

---

Let's walk through a **visual ASCII representation** of the **Levenshtein distance matrix** for this example:

```
levenshtein_distance("abc", "yabd")
```

---

### 🧠 Strings:

* `str_1 = "abc"` (columns)
* `str_2 = "yabd"` (rows)

We’ll build a matrix where each cell `[i][j]` contains the **Levenshtein distance** between:

* the first `i` characters of `"yabd"` and
* the first `j` characters of `"abc"`

---

### 📐 Initialization:

We start by filling in the base cases (empty prefixes).

```
      ""  a  b  c
   +---------------
"" |  0  1  2  3
y  |  1
a  |  2
b  |  3
d  |  4
```

---

### 🛠 Step-by-step Matrix Fill:

We fill this matrix using the logic:

* If characters match: take diagonal value.
* Else: min(diagonal, left, top) + 1

```
      ""  a  b  c
   +---------------
"" |  0  1  2  3
y  |  1  1  2  3
a  |  2  1  2  3
b  |  3  2  1  2
d  |  4  3  2  2  ← answer: 2
```

---

### 🔍 Matrix Explanation:

Each number means: minimum operations needed to convert that substring of `"yabd"` into that of `"abc"`.

For example:

* To convert `"yab"` to `"abc"` takes 2 edits:

  * Substitute `'y'` → `'a'`
  * Keep `'a'`
  * Keep `'b'`
  * Substitute `'c'` → `'d'`

---

### ✅ Final Result:

```
levenshtein_distance("abc", "yabd") == 2
```

"""
