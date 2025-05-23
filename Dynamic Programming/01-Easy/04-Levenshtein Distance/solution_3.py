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
    if len(str_1) < len(str_2):
        return levenshtein_distance(str_2, str_1)

    m = len(str_1)
    n = len(str_2)

    dp = list(range(m + 1))

    for i in range(1, n + 1):
        prev_diagonal = dp[0]
        dp[0] = i

        for j in range(1, m + 1):
            temp = dp[j]

            if str_1[j - 1] == str_2[i - 1]:
                dp[j] = prev_diagonal
            else:
                dp[j] = 1 + min(prev_diagonal, dp[j], dp[j - 1])

            prev_diagonal = temp

    return dp[m]


# Test Cases:

print(levenshtein_distance("abc", "yabd"))
# Output: 2

print(levenshtein_distance("", ""))
# Output: 0

print(levenshtein_distance("cereal", "saturdzz"))
# Output: 7
