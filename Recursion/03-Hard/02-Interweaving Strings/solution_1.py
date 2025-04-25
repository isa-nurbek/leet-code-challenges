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


# O(2^(n + m)) time | O(n + m) space
def interweaving_strings(one, two, three):
    # First check: if the total length of one and two doesn't match three,
    # they can't possibly be interwoven to form three
    if len(three) != len(one) + len(two):
        return False

    # Start the recursive checking process from the beginning of both strings
    return are_interwoven(one, two, three, 0, 0)


def are_interwoven(one, two, three, i, j):
    # k is the current position in the three string we're checking
    # It's the sum of our positions in one and two
    k = i + j

    # Base case: if we've reached the end of three (and thus one and two)
    if k == len(three):
        return True

    # Option 1: Take next character from one if available and it matches three[k]
    if i < len(one) and one[i] == three[k]:
        # Recursively check if the rest can be interwoven
        if are_interwoven(one, two, three, i + 1, j):
            return True

    # Option 2: Take next character from two if available and it matches three[k]
    if j < len(two) and two[j] == three[k]:
        # Recursively check if the rest can be interwoven
        return are_interwoven(one, two, three, i, j + 1)

    # If neither option worked, return False
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

### **Time Complexity:**

The function `are_interwoven` is a recursive function that explores all possible ways to interleave the strings `one` and
`two` to form `three`. 

- At each step, it checks whether the current character of `three` matches either the next character in `one` or `two` (or both).
- In the worst case, it explores all possible interleavings, which leads to a binary tree of recursive calls where each level
represents a character in `three`.
- The depth of the recursion tree is `len(three) = len(one) + len(two) = n + m` (where `n = len(one)`, `m = len(two)`).
- At each step, there are up to **2 choices** (take from `one` or `two` if both match), leading to an exponential number of
recursive calls.

Thus, the **worst-case time complexity is**: O(2^n + m) where `n` and `m` are the lengths of `one` and `two`, respectively.


### **Space Complexity:**

The space complexity is determined by the **maximum depth of the recursion stack**:
- The recursion goes up to a depth of `n + m` (since we increment `i` or `j` at each step until `i + j = len(three)`).
- No additional data structures are used (aside from the recursion stack).

Thus, the **space complexity is**: O(n + m) due to the recursion stack.

#### **Optimization Note:**
If we use memoization, the space complexity would increase to: O(n ⋅ m) to store the DP table, but recursion depth would
still be O(n + m).

---

### **Final Answer:**
- **Time Complexity:** O(2^n + m)
- **Space Complexity:** O(n + m) (due to recursion stack).

"""
