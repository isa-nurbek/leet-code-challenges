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
    edits = [[x for x in range(len(str_1) + 1)] for y in range(len(str_2) + 1)]

    for i in range(1, len(str_2) + 1):
        edits[i][0] = edits[i - 1][0] + 1

    for i in range(1, len(str_2) + 1):
        for j in range(1, len(str_1) + 1):
            if str_2[i - 1] == str_1[j - 1]:
                edits[i][j] = edits[i - 1][j - 1]
            else:
                edits[i][j] = 1 + min(
                    edits[i - 1][j - 1], edits[i - 1][j], edits[i][j - 1]
                )

    return edits[-1][-1]


# Test Cases:

print(levenshtein_distance("abc", "yabd"))
# Output: 2

print(levenshtein_distance("", ""))
# Output: 0

print(levenshtein_distance("cereal", "saturdzz"))
# Output: 7
