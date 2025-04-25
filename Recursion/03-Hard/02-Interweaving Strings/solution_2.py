# Problem Description:

"""

                                          Interweaving Strings

Write a function that takes in three strings and returns a boolean representing whether the third string can be formed by
interweaving the first two strings.

To interweave strings means to merge them by alternating their letters without any specific pattern. For instance, the strings
`"abc"` and `"123"` can be interwoven as `"a1b2c3"`, as `"abc123"`, and as `"ab1c23"` (this list is nonexhaustive).

Letters within a string must maintain their relative ordering in the interwoven string.


## Sample Input
```
one = "algoexpert"
two = "your-dream-job"
three = "your-algodream-expertjob"
```

## Sample Output
```
True
```

## Optimal Time & Space Complexity:
```
O(n ⋅ m) time | O(n ⋅ m) space - where `n` is the length of the first string and `m` is the length of the second string.
```
"""

# =========================================================================================================================== #

# Solution:


# O(n ⋅ m) time | O(n ⋅ m) space
def interweaving_strings(one, two, three):
    # First check: if three isn't exactly the combination of one and two lengths, return False
    if len(three) != len(one) + len(two):
        return False

    # Initialize memoization dictionary to store already computed results
    memo = {}
    # Start the recursive check from beginning of both strings (indices 0, 0)
    return are_interwoven(one, two, three, 0, 0, memo)


def are_interwoven(one, two, three, i, j, memo):
    # Check if we've already computed this (i,j) combination before
    if (i, j) in memo:
        return memo[(i, j)]

    # k is the current position in the three string we're checking
    k = i + j

    # Base case: we've reached the end of three string
    if k == len(three):
        return True

    # Option 1: Try taking next character from string 'one' if it matches three[k]
    if i < len(one) and one[i] == three[k]:
        # Recursively check if remaining strings can be interwoven
        memo[(i, j)] = are_interwoven(one, two, three, i + 1, j, memo)
        # If we found a valid interweaving, return True immediately
        if memo[(i, j)]:
            return True

    # Option 2: Try taking next character from string 'two' if it matches three[k]
    if j < len(two) and two[j] == three[k]:
        # Recursively check if remaining strings can be interwoven
        memo[(i, j)] = are_interwoven(one, two, three, i, j + 1, memo)
        return memo[(i, j)]

    # If neither option worked, memoize False for this (i,j) position
    memo[(i, j)] = False
    return False


# Test Cases:
print(interweaving_strings("algoexpert", "your-dream-job", "your-algodream-expertjob"))
# Output: True

print(interweaving_strings("aabcc", "dbbca", "aadbbbaccc"))
# Output: False

print(interweaving_strings("a", "b", "ab"))
# Output: True
