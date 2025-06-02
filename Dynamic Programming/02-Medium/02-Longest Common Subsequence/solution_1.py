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
