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


# O(2ⁿ) time | O(2ⁿ * n) space
def powerset_iterative(array):
    result = [[]]  # start with the empty subset

    for elem in array:
        # For each element, add it to all existing subsets
        new_subsets = [subset + [elem] for subset in result]
        result.extend(new_subsets)

    return result


# Test Cases:

print(powerset_iterative([1, 2, 3]))
# Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

print(powerset_iterative([]))
# Output: [[]]

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis

### **Time Complexity:**

The function generates all subsets of the input array. For an array of size `n`, there are `2ⁿ` possible subsets
(including the empty set).

- **Outer Loop:** Runs `n` times (once for each element in the array).
- **Inner List Comprehension:** For each element, it iterates over all existing subsets (which grow exponentially).  
  - At step `i`, there are (2^i) subsets, and we create (2^i) new subsets by appending the current element to each of them.

Thus, the total number of operations is: 1 + 2 + 4 + 8 + ... + 2ⁿ⁻¹ = 2ⁿ - 1

This gives a **time complexity of O(2ⁿ)**, since we generate `2ⁿ` subsets, each requiring O(1) work (amortized).


### **Space Complexity:**

The space complexity is determined by the storage required for all subsets.

- The total number of subsets is (`2ⁿ`).
- The average subset size is (`n / 2`) (since each element appears in half of all subsets).
- Thus, the total space used is O(2ⁿ * n).

However, in the worst case (when subsets are of size `n`, we store O(2ⁿ * n) elements.

Thus, the **space complexity is O(2ⁿ * n)**.

### **Summary:**
- **Time Complexity:** O(2ⁿ)
- **Space Complexity:** O(2ⁿ * n)

This is optimal for generating the powerset since there are `2ⁿ` subsets, each potentially of size up to `n`.

"""
