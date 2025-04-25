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

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis

Let's analyze the time and space complexity of the `interweaving_strings` function, which uses memoization to determine if `three`
is an interweaving of `one` and `two`.

### Definitions:
- Let `m` be the length of string `one`.
- Let `n` be the length of string `two`.
- The length of `three` is `m + n` (otherwise, the function returns early).

### Time Complexity:

The function explores all possible ways to interleave `one` and `two` to form `three` using memoization to avoid redundant
computations.

1. **Memoization Table**: The memoization table stores results for all possible `(i, j)` pairs where `i` ranges from `0` to `m`
and `j` ranges from `0` to `n`. Thus, there are `(m + 1) * (n + 1)` possible unique states.
2. **Work per State**: For each state `(i, j)`, the function performs a constant amount of work (checking characters and making
recursive calls). The recursive calls are memoized, so each state is computed only once.
3. **Total Time**: The total time is proportional to the number of unique states, which is `O(m * n)`.

Thus, the time complexity is **`O(m * n)`**.

### Space Complexity:

The space complexity is determined by:
1. **Memoization Table**: The memoization table stores `O(m * n)` entries. Each entry is a boolean value, but the overhead of the
dictionary (or hash map) is still `O(m * n)`.
2. **Recursion Stack**: In the worst case, the recursion depth can go up to `m + n` (when you fully traverse one string before the
other). However, since the function uses memoization, the recursion stack does not explode beyond `O(m + n)`.

Thus, the space complexity is **`O(m * n)`** (dominated by the memoization table).

### Summary:
- **Time Complexity**: `O(m * n)`
- **Space Complexity**: `O(m * n)`

This is a classic dynamic programming approach where memoization avoids recomputing overlapping subproblems, leading to an
efficient solution.

"""
