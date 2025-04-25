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

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
Let's walk through the `interweaving_strings` code in detail, including the recursive function and how it handles different
scenarios.

### **Goal of the Problem**

You are given three strings:
- `one`
- `two`
- `three`

You need to determine **if `three` is a valid interleaving** of `one` and `two`.

---

### **What does interleaving mean here?**

A string `three` is an **interleaving** of `one` and `two` if:
- It contains all characters of `one` and `two`, in the **same order** they appear in their respective strings.
- But the characters from `one` and `two` can be mixed.

#### Example:
```python
one = "abc"
two = "def"
three = "adbcef"
```

Here, `three` is a valid interleaving: take "a" from `one`, "d" from `two`, "b" from `one`, "c" from `one`, "e" from `two`,
"f" from `two`.

---

### **Step-by-Step Code Explanation**

```
def interweaving_strings(one, two, three):
    if len(three) != len(one) + len(two):
        return False
```

- Before doing any recursive check, this condition ensures that the combined length of `one` and `two` must match `three`.
If not, `three` can't be an interleaving.

```
return are_interwoven(one, two, three, 0, 0)
```

- Start recursive checking from the beginning of `one` and `two` (i.e., indices `i = 0` and `j = 0`).

---

### **Recursive Function: `are_interwoven`**

```
def are_interwoven(one, two, three, i, j):
    k = i + j
```

- `k` is the current index in `three`, since the characters taken from `one` and `two` should add up to the index in `three`.

```
if k == len(three):
    return True
```

- If we've reached the end of `three`, that means every character matched from `one` and `two`, so return `True`.

---

### **Check Character Matches**

```
if i < len(one) and one[i] == three[k]:
    if are_interwoven(one, two, three, i + 1, j):
        return True
```

- If current character in `one` matches `three[k]`, we make a recursive call advancing `i` (i.e., consuming one more char from
`one`). If this path leads to success, return `True`.

```
if j < len(two) and two[j] == three[k]:
    return are_interwoven(one, two, three, i, j + 1)
```

- Similarly, if the current character in `two` matches `three[k]`, we try that path.

```
return False
```

- If neither character matches `three[k]`, this path fails, so return `False`.

---

### **Test Case Analysis**

#### ✅ `interweaving_strings("algoexpert", "your-dream-job", "your-algodream-expertjob")`
- All characters are interleaved correctly while maintaining order. **Returns: `True`**

#### ❌ `interweaving_strings("aabcc", "dbbca", "aadbbbaccc")`
- One character order mismatch causes it to fail. **Returns: `False`**

#### ✅ `interweaving_strings("a", "b", "ab")`
- Simple valid interleaving. **Returns: `True`**

---

### ⚠️ Potential Issue

This recursive solution has **no memoization**, which means it may repeat work unnecessarily for overlapping subproblems.
For large inputs, it could become very slow.

"""
