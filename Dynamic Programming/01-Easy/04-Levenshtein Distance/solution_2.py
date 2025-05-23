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
