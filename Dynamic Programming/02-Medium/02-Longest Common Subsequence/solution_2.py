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
    if len(str_1) < len(str_2):
        str_1, str_2 = str_2, str_1

    m, n = len(str_1), len(str_2)
    dp_prev = [0] * (n + 1)

    for i in range(1, m + 1):
        dp_curr = [0] * (n + 1)
        for j in range(1, n + 1):
            if str_1[i - 1] == str_2[j - 1]:
                dp_curr[j] = dp_prev[j - 1] + 1
            else:
                dp_curr[j] = max(dp_prev[j], dp_curr[j - 1])
        dp_prev = dp_curr

    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if str_1[i - 1] == str_2[j - 1]:
            lcs.append(str_1[i - 1])
            i -= 1
            j -= 1
        elif dp_prev[j] > dp_curr[j - 1]:
            i -= 1
        else:
            j -= 1

    return lcs[::-1]


# Test Cases:

print(longest_common_subsequence("ZXVVYZW", "XKYKZPW"))
# Output: ['X', 'Y', 'Z', 'W']

print(longest_common_subsequence("", "ABCDEFG"))
# Output: []

print(longest_common_subsequence("ABCDEFG", "APPLES"))
# Output: ['A', 'E']
