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
    if len(three) != len(one) + len(two):
        return False

    # Initialize memoization table: (i, j) -> bool
    memo = {}
    return are_interwoven(one, two, three, 0, 0, memo)


def are_interwoven(one, two, three, i, j, memo):
    # Check if we've already computed this (i, j) pair
    if (i, j) in memo:
        return memo[(i, j)]

    k = i + j

    # Base case: reached the end of 'three'
    if k == len(three):
        return True

    # Try taking a character from 'one' if possible
    if i < len(one) and one[i] == three[k]:
        memo[(i, j)] = are_interwoven(one, two, three, i + 1, j, memo)
        if memo[(i, j)]:
            return True

    # Try taking a character from 'two' if possible
    if j < len(two) and two[j] == three[k]:
        memo[(i, j)] = are_interwoven(one, two, three, i, j + 1, memo)
        return memo[(i, j)]

    # Neither option worked
    memo[(i, j)] = False
    return False


# Test Cases:
print(interweaving_strings("algoexpert", "your-dream-job", "your-algodream-expertjob"))
# Output: True

print(interweaving_strings("aabcc", "dbbca", "aadbbbaccc"))
# Output: False

print(interweaving_strings("a", "b", "ab"))
# Output: True
