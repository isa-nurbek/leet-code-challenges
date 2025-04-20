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

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
Let's walk through the code and understand how the `powerset` function works in detail.

### ✅ **Goal:**
The `powerset` function generates the **powerset** of a given array.

- The **powerset** of a set is the set of **all subsets**, including:
  - the empty set (`[]`)
  - the full set itself
  - and everything in between

For example, the powerset of `[1, 2, 3]` is:
```
[
  [],        # empty subset
  [1], [2], [3],       # single-element subsets
  [1, 2], [1, 3], [2, 3],  # two-element subsets
  [1, 2, 3]              # full set
]
```

---

### 🧠 **Code Explanation:**

```
def powerset(array, idx=None):
    if idx is None:
        idx = len(array) - 1
```

- The function takes two arguments:
  - `array`: the input list.
  - `idx`: the current index we're working with (defaults to the **last index** in the array on the first call).

---

```
if idx < 0:
    return [[]]
```

- **Base case**: if the index is less than 0, we've finished processing all elements.
- The only subset of an empty array is the **empty list** (`[[]]`), so return `[[]]`.

---

```
elem = array[idx]
```

- `elem` is the element at the current index. This is the element we will consider **including or not including** in each subset.

---

```
subsets = powerset(array, idx - 1)
```

- This is the **recursive call** to get the powerset of the **first `idx` elements** (excluding the current element).
- So we're breaking the problem down: if we can get all subsets without `elem`, we can then create the rest of the powerset by adding `elem` to each of those subsets.

---

```python
    return subsets + [subset + [elem] for subset in subsets]
```

- `subsets` is all subsets **without** `elem`.
- `[subset + [elem] for subset in subsets]` creates a new list of subsets, where each old subset is **augmented with `elem`**.
- We then **combine** both:
  - subsets **without `elem`**
  - subsets **with `elem`**

---

### 🔁 **How it works step-by-step:**

Let’s trace `powerset([1, 2, 3])`:

#### 1. Initial call: `powerset([1, 2, 3])`
- `idx = 2`, `elem = 3`
- recurse: `powerset([1, 2, 3], 1)`

#### 2. Second call: `powerset([1, 2, 3], 1)`
- `idx = 1`, `elem = 2`
- recurse: `powerset([1, 2, 3], 0)`

#### 3. Third call: `powerset([1, 2, 3], 0)`
- `idx = 0`, `elem = 1`
- recurse: `powerset([1, 2, 3], -1)`

#### 4. Base case: `powerset([1, 2, 3], -1)`
- returns `[[]]`

Now we **build back up**:

---

#### Going back to idx=0 (`elem = 1`):
- subsets without `1`: `[[]]`
- subsets with `1`: `[[1]]`
- return `[[], [1]]`

---

#### Going back to idx=1 (`elem = 2`):
- subsets without `2`: `[[], [1]]`
- subsets with `2`: `[[2], [1, 2]]`
- return `[[], [1], [2], [1, 2]]`

---

#### Going back to idx=2 (`elem = 3`):
- subsets without `3`: `[[], [1], [2], [1, 2]]`
- subsets with `3`: `[[3], [1, 3], [2, 3], [1, 2, 3]]`
- return:
```
[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
```

---

### 🧪 Test Case: `powerset([])`

- `idx = -1`
- returns `[[]]`, the only subset of the empty set.

---

### 🧠 Summary:

- **Recursive** approach
- Each level of recursion:
  - Gets all subsets **without** the current element
  - Adds the current element to each of those subsets to get the rest
- Combines both sets of subsets to return the result

"""
