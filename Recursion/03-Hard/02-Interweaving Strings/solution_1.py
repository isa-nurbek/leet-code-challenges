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
O(nm) time | O(nm) space - where `n` is the length of the first string and `m` is the length of the second string.
```
"""

# =========================================================================================================================== #

# Solution:


# O(2^(n + m)) time | O(n + m) space
def interweaving_strings(one, two, three):
    if len(three) != len(one) + len(two):
        return False

    return are_interwoven(one, two, three, 0, 0)


def are_interwoven(one, two, three, i, j):
    k = i + j

    if k == len(three):
        return True

    if i < len(one) and one[i] == three[k]:
        if are_interwoven(one, two, three, i + 1, j):
            return True

    if j < len(two) and two[j] == three[k]:
        return are_interwoven(one, two, three, i, j + 1)

    return False


# Test Cases:
print(interweaving_strings("algoexpert", "your-dream-job", "your-algodream-expertjob"))
# Output: True

print(interweaving_strings("aabcc", "dbbca", "aadbbbaccc"))
# Output: False

print(interweaving_strings("a", "b", "ab"))
# Output: True
