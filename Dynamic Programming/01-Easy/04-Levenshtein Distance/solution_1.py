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
