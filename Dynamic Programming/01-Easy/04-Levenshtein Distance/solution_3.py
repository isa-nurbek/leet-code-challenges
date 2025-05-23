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
