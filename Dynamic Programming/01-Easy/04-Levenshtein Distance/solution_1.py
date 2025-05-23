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
