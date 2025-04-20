# Problem Description:

"""

                                            Powerset

Write a function that takes in an array of unique integers and returns its powerset.

The powerset `P(X)` of a set `X` is the set of all subsets of `X`. For example, the powerset of `[1, 2]` is `[[], [1], [2], [1,2]]`.

> Note that the sets in the powerset do not need to be in any particular order.


## Sample Input
```
array = [1, 2, 3]
```

## Sample Output
```
[[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
```

## Optimal Time & Space Complexity:
```
O(n * 2ⁿ) time | O(n * 2ⁿ) space - where `n` is the length of the input array.
```
"""

# =========================================================================================================================== #

# Solution:


# O(n * 2ⁿ) time | O(n * 2ⁿ) space
def powerset(array, idx=None):
    # Handle initial call (no index provided)
    if idx is None:
        # Start with the last index of the array
        idx = len(array) - 1

    # Base case: when we've gone past the first element
    if idx < 0:
        # Return a list containing just the empty subset
        return [[]]

    # Get the current element we're processing
    elem = array[idx]

    # Recursively get all subsets without the current element
    subsets = powerset(array, idx - 1)

    # Return:
    # 1. All subsets that don't include the current element
    # 2. All subsets that do include the current element (created by adding
    #    the current element to each existing subset)
    return subsets + [subset + [elem] for subset in subsets]


# Test Cases:

print(powerset([1, 2, 3]))
# Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

print(powerset([]))
# Output: [[]]

# =========================================================================================================================== #

# Big O Analysis:

"""

## Time and Space Complexity Analysis

### Time Complexity:
- Let `n` be the length of the input array.
- The number of subsets in a powerset is `2ⁿ` (since each element can either be included or excluded from a subset).
- For each recursive call, the function processes one element (`elem = array[idx]`) and combines the existing subsets
with new subsets that include `elem`.
- The work done at each step is proportional to the number of subsets at that step, which is `2^k` where `k` is the number
of elements processed so far.

- The total work is `2^0 + 2^1 + 2^2 + ... + 2^(n-1) = 2^n - 1`, which is `O(2ⁿ)`.

Thus, the **time complexity is `O(n * 2ⁿ)`**. The `n` factor comes from the fact that, for each of the `2ⁿ` subsets,
we may need to copy/modify the subset (which takes O(n) time in the worst case when copying).

### Space Complexity:
- The space complexity is determined by the output (the powerset itself) and the recursion stack.
- The powerset contains `2^n` subsets, and the total number of elements across all subsets is `n * 2^(n-1)`
(since each element appears in exactly half of the subsets, i.e., `2ⁿ⁻¹` times). This dominates the space usage.
- The recursion depth is `O(n)` (since we make `n` recursive calls), but this is negligible compared to the output size.

Thus, the **space complexity is `O(n * 2ⁿ)`** (required to store all subsets).

### Summary:
- Time Complexity: **O(n * 2ⁿ)**
- Space Complexity: **O(n * 2ⁿ)**

This is optimal for generating the powerset since the output itself has exponential size.

"""
