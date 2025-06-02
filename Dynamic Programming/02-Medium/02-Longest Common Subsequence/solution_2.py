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


# O(m * n) time | O(n) space
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
