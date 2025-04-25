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

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
The function `interweaving_strings(one, two, three)` checks whether the string `three` is formed by **interweaving** the strings
`one` and `two`, meaning characters from `one` and `two` appear in `three` **in the same order** as in their respective strings —
though they can be mixed together.

---

## 🔍 High-Level Explanation

Given:
- `one = "abc"`
- `two = "def"`
- `three = "adbcef"`

The function returns `True` if you can **interleave** characters from `one` and `two` to get `three`, **preserving the order of
characters in each input string**.

---

## 🧠 Step-by-Step Breakdown

### ✅ Step 1: Length Check
```
if len(three) != len(one) + len(two):
    return False
```
If `three` is not the combined length of `one` and `two`, it's impossible to form it by interleaving — return `False`.

---

### ✅ Step 2: Use Memoization for Efficiency
```
memo = {}
```
`memo` is a dictionary to **cache results** for subproblems. It avoids recalculating the same `(i, j)` combination.

---

### ✅ Step 3: Recursive Function — `are_interwoven`
The function tries to build `three` from `one` and `two` character-by-character.

```
def are_interwoven(one, two, three, i, j, memo):
```

- `i`: index in `one`
- `j`: index in `two`
- `k = i + j`: index in `three`

### 🚩 Base Case
```
if k == len(three):
    return True
```
If `i + j` reaches the end of `three`, we have matched all characters successfully.

---

### 🧪 Recursive Steps
#### Option 1: Use a character from `one` if it matches `three[k]`
```
if i < len(one) and one[i] == three[k]:
    memo[(i, j)] = are_interwoven(one, two, three, i + 1, j, memo)
    if memo[(i, j)]:
        return True
```

#### Option 2: Use a character from `two` if it matches `three[k]`
```
if j < len(two) and two[j] == three[k]:
    memo[(i, j)] = are_interwoven(one, two, three, i, j + 1, memo)
    return memo[(i, j)]
```

#### If neither works:
```
memo[(i, j)] = False
return False
```

---

## 🧪 Example Walkthrough

### Test Case:
```
interweaving_strings("aabcc", "dbbca", "aadbbbaccc")
```

Try to build `"aadbbbaccc"` from `"aabcc"` and `"dbbca"`:
- Start with `"a"` from `"aabcc"` ✅
- Next `"a"` from `"aabcc"` ✅
- Then `"d"` from `"dbbca"` ✅
- Then `"b"` from `"aabcc"` or `"dbbca"`? Must try both!
- Eventually, it fails because `"b"` from `"dbbca"` is used too early, breaking the rest of the structure.

Hence, it returns **False**.

---

## ✅ Summary

- 🧮 Uses recursion + memoization (top-down dynamic programming).
- 🔄 Tries all valid ways to pick characters from `one` or `two` to match `three`.
- 🧠 Caches subproblem results to avoid recomputation.
- ❌ Returns False as soon as it detects no valid interleaving path.

---

Here’s a simplified **ASCII recursion tree** for:

```
interweaving_strings("aabcc", "dbbca", "aadbbbaccc")
```

We'll track:
- `i`: index in `"aabcc"` (`one`)
- `j`: index in `"dbbca"` (`two`)
- `k`: `i + j`, index in `"aadbbbaccc"` (`three`)

We'll also show character matches and branching choices.

```
Start: i=0, j=0, k=0 -> three[0]='a'
|
|-- i=1, j=0, k=1 -> three[1]='a' == one[1]='a' ✅
|   |
|   |-- i=2, j=0, k=2 -> three[2]='d' == two[0]='d' ✅
|       |
|       |-- i=2, j=1, k=3 -> three[3]='b'
|           |
|           |-- i=2, j=2, k=4 -> three[4]='b'
|               |
|               |-- i=2, j=3, k=5 -> three[5]='b'
|                   |
|                   |-- i=2, j=4, k=6 -> three[6]='a'
|                       |
|                       |-- i=3, j=4, k=7 -> three[7]='c'
|                           |
|                           |-- i=4, j=4, k=8 -> three[8]='c'
|                               |
|                               |-- i=5, j=4, k=9 -> three[9]='c'
|                                   ✅ All matched: return True
|
|-- Other branches (e.g., taking from `two` at the wrong time)
|   |
|   |-- i=1, j=1, k=2 -> three[2]='d' != one[1]='a' ❌
|   |-- i=1, j=1, k=2 -> memo hit → False
```

---

### 🔁 Highlights:
- ✅ Good path (leftmost) reaches the end successfully.
- ❌ Wrong choices are pruned due to mismatches.
- 🧠 Memoization prevents recomputing dead paths.

"""
