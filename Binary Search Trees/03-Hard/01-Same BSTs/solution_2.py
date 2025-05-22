# Problem Description:

"""
                                                Same BSTs

An array of integers is said to represent the `Binary Search Tree (BST)` obtained by inserting each integer in the array, from left
to right, into the `BST`.

Write a function that takes in two arrays of integers and determines whether these arrays represent the same `BST`.

Note that you're not allowed to construct any `BST`s in your code.

A `BST` is a `Binary Tree` that consists only of `BST` nodes. A node is said to be a valid `BST` node if and only if it satisfies
the `BST` property: its value is strictly greater than the values of every node to its left; its value is less than or equal to the
values of every node to its right; and its children nodes are either valid `BST` nodes themselves or `None`.


## Sample Input:
```
array_one = [10, 15, 8, 12, 94, 81, 5, 2, 11]
array_two = [10, 8, 5, 15, 2, 12, 11, 94, 81]
```

## Sample Output:
```
True 
// Both arrays represent the BST below

          10
       /     \
      8      15
    /       /   \
   5      12    94
 /       /     /
2       11    81
```

## Optimal Time & Space Complexity:
```
O(n²) time | O(d) space - where `n` is the number of nodes in each array, respectively, and `d` is the depth
of the BST that they represent.
```

"""

# =========================================================================================================================== #

# Solution:


# Binary Search Tree (BST) node class
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n²) time | O(d) space
def same_bsts(array_one, array_two):
    # First check if the arrays have the same length - if not, BSTs can't be same
    if len(array_one) != len(array_two):
        return False
    # Start the recursive helper function with initial parameters
    return _same_bsts_helper(array_one, array_two, 0, 0, float("-inf"), float("inf"))


def _same_bsts_helper(
    array_one, array_two, root_idx_one, root_idx_two, min_val, max_val
):
    """
    Recursive helper function to determine if two arrays represent the same BST.

    Parameters:
    - array_one, array_two: The input arrays representing BST insertions
    - root_idx_one, root_idx_two: Current root indices being compared
    - min_val, max_val: The valid range for child nodes of current root
    """

    # If both roots are -1 (no children), return True (base case)
    if root_idx_one == -1 and root_idx_two == -1:
        return True

    # If one root exists but the other doesn't, trees are different
    if (root_idx_one == -1) != (root_idx_two == -1):
        return False

    # If root values don't match, trees are different
    if array_one[root_idx_one] != array_two[root_idx_two]:
        return False

    # Find the index of first element in array_one that would be in left subtree
    left_root_one = _find_next_smaller(array_one, root_idx_one, min_val)
    # Find the index of first element in array_two that would be in left subtree
    left_root_two = _find_next_smaller(array_two, root_idx_two, min_val)

    # Find the index of first element in array_one that would be in right subtree
    right_root_one = _find_next_larger_or_equal(array_one, root_idx_one, max_val)
    # Find the index of first element in array_two that would be in right subtree
    right_root_two = _find_next_larger_or_equal(array_two, root_idx_two, max_val)

    # Recursively check both left and right subtrees:
    # For left subtrees: update max_val to current root's value (left must be smaller)
    # For right subtrees: update min_val to current root's value (right must be larger/equal)
    return _same_bsts_helper(
        array_one,
        array_two,
        left_root_one,
        left_root_two,
        min_val,
        array_one[root_idx_one],
    ) and _same_bsts_helper(
        array_one,
        array_two,
        right_root_one,
        right_root_two,
        array_one[root_idx_one],
        max_val,
    )


def _find_next_smaller(array, start_idx, min_val):
    """
    Finds the index of the first element after start_idx that is:
    - Smaller than array[start_idx] (would be in left subtree)
    - Greater than or equal to min_val (within valid range)
    Returns -1 if no such element found
    """
    for i in range(start_idx + 1, len(array)):
        if array[i] < array[start_idx] and array[i] >= min_val:
            return i
    return -1


def _find_next_larger_or_equal(array, start_idx, max_val):
    """
    Finds the index of the first element after start_idx that is:
    - Greater than or equal to array[start_idx] (would be in right subtree)
    - Less than or equal to max_val (within valid range)
    Returns -1 if no such element found
    """
    for i in range(start_idx + 1, len(array)):
        if array[i] >= array[start_idx] and array[i] <= max_val:
            return i
    return -1


# Test Case:

array_one = [10, 15, 8, 12, 94, 81, 5, 2, 11]
array_two = [10, 8, 5, 15, 2, 12, 11, 94, 81]

print(same_bsts(array_one, array_two))  # Output: True

# Both arrays represent the BST below
#           10
#        /     \
#       8      15
#     /       /   \
#    5      12    94
#  /       /     /
# 2       11    81

# =========================================================================================================================== #

# Big O Analysis:

"""
# Time and Space Complexity Analysis:

### Time Complexity Analysis

Let's analyze the time and space complexity of the given same_bsts function.

1. **Initial Check**: The initial length check `if len(array_one) != len(array_two)` is an O(1) operation.

2. **Helper Function `_same_bsts_helper`**:
   - The helper function is called recursively for each node in the BST.
   - For each node, we perform two searches:
     - `_find_next_smaller`: This function scans the array from `start_idx + 1` to the end to find the first element that is
     smaller than `array[start_idx]` and >= `min_val`. In the worst case, this is O(n) for each call.
     - `_find_next_larger_or_equal`: Similarly, this scans the array from `start_idx + 1` to the end to find the first element
     that is >= `array[start_idx]` and <= `max_val`. This is also O(n) for each call.
   - These searches are performed for each node in the BST, and in the worst case, the BST could be a degenerate tree
   (a linked list), leading to O(n) recursive calls.
   - Therefore, the total time complexity is O(n²) in the worst case.

3. **Best Case**: If the BST is balanced, the depth of recursion is O(log n), and the total time complexity would be O(n log n),
since at each level of the tree, we process O(n) elements in total across all nodes at that level.

### Space Complexity Analysis

1. **Recursion Stack**:
   - The space complexity is determined by the depth of the recursion stack.
   - In the worst case (degenerate tree), the recursion depth is O(n), leading to O(n) space.
   - In the best case (balanced tree), the recursion depth is O(log n), leading to O(log n) space.

2. **Additional Space**:
   - No additional data structures are used that grow with the input size, so the space complexity is dominated by the recursion stack.

### Summary

- **Time Complexity**:
  - Worst Case: O(n²) (degenerate tree)
  - Best Case: O(n log n) (balanced tree)
  
- **Space Complexity**:
  - Worst Case: O(n) (degenerate tree)
  - Best Case: O(log n) (balanced tree)

### Optimizations

The current approach is correct but can be optimized to O(n) time by avoiding repeated scans of the array. One way to do this is by
using pointers or iterators to track the current position in the array for each subtree, but this would require a more sophisticated
approach or preprocessing (e.g., building the BST and comparing directly). However, the current approach is straightforward and
works for the problem constraints where the arrays are small to moderate in size.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
Let's break down the code step by step and explain **what it's doing**, **why it works**, and **how it checks whether
two arrays represent the same BST**.

---

### ✅ **Goal of the code:**

Determine if **two arrays** represent the same **Binary Search Tree (BST)**, assuming that the elements are inserted into the
BST **from left to right**, just like in the arrays.

---

## 🔧 BST Insertion Principle Recap

In a BST:

* All values in the **left subtree** are **less than the root**.
* All values in the **right subtree** are **greater than or equal to the root**.
* Inserting values into a BST follows this rule recursively.

---

## 🧠 Concept Behind the Solution

The arrays don’t build an actual tree. Instead, the function simulates **how the BST would look** if the values were inserted
one by one **from each array**, and checks if both would create **the same tree structure**.

It does so by:

* Comparing roots of subtrees.
* Recursively checking left and right subtree roots and their valid value ranges.
* Ensuring both arrays follow the **same structure** during simulated insertion.

---

## 🔍 Breakdown of the Code

### 1. `same_bsts(array_one, array_two)`

* First, it checks if arrays are the same length — if not, they can’t represent the same tree.
* Then it calls the helper `_same_bsts_helper` starting from index `0` (the root of the BST) with an initial range of allowed
values (`-inf` to `inf`).

---

### 2. `_same_bsts_helper(...)`

#### Parameters:

* `array_one`, `array_two`: the two arrays to compare.
* `root_idx_one`, `root_idx_two`: current "root" index in each array.
* `min_val`, `max_val`: value boundaries valid for this subtree (BST constraints).

#### Step-by-step:

1. **Base Case:**

   ```
   if root_idx_one == -1 and root_idx_two == -1:
       return True
   ```

   If both subtrees are empty (no valid roots), then they are equal.

2. **Mismatch Check:**

   ```
   if (root_idx_one == -1) != (root_idx_two == -1):
       return False
   ```

   If one subtree is empty and the other is not → Not same BST.

3. **Root Value Check:**

   ```
   if array_one[root_idx_one] != array_two[root_idx_two]:
       return False
   ```

   If the roots don’t match → Not same BST.

4. **Find the next root indices** for left and right subtrees in both arrays:

   ```
   left_root_one = _find_next_smaller(...)
   right_root_one = _find_next_larger_or_equal(...)
   ```

   These functions search for the **next element** in the array that would be part of:

   * The **left subtree** (smaller than current root, but ≥ min_val).
   * The **right subtree** (≥ current root, but ≤ max_val).

5. **Recursive Calls**:
   Check both left and right subtrees recursively.

   ```
   return _same_bsts_helper(...) and _same_bsts_helper(...)
   ```

---

### 3. `_find_next_smaller(array, start_idx, min_val)`

Looks for the **next index** after `start_idx` with a value:

* Smaller than the current root.
* Greater than or equal to `min_val`.

This will be the left child in the BST (if any).

---

### 4. `_find_next_larger_or_equal(array, start_idx, max_val)`

Looks for the **next index** after `start_idx` with a value:

* Greater than or equal to the current root.
* Less than or equal to `max_val`.

This will be the right child in the BST (if any).

---

## 🧪 Example Test Case

```
array_one = [10, 15, 8, 12, 94, 81, 5, 2, 11]
array_two = [10, 8, 5, 15, 2, 12, 11, 94, 81]
```

Both arrays represent the same BST when inserted in order:

```
           10
        /      \
       8        15
     /         /   \
    5        12     94
  /         /      /
 2        11      81
```

So the function returns `True`.

---

## ⏱ Time & Space Complexity

### ⏱ Time: **O(n²)** worst case

* Because for each element, the helper functions `_find_next_smaller` and `_find_next_larger_or_equal` may scan the rest of the
array (O(n) each), and we do this recursively up to n times.

### 🧠 Space: **O(d)**

* Where `d` is the depth of the tree (because of the recursive call stack).

---

## ✅ Summary

This approach **does not build trees**, which saves memory, and instead simulates how values would be inserted. It checks:

* Root values match.
* Structure of left and right subtrees match recursively.
* Valid BST constraints at each level.

---

Here's a clear **ASCII diagram** that shows how both arrays:

```
array_one = [10, 15, 8, 12, 94, 81, 5, 2, 11]
array_two = [10, 8, 5, 15, 2, 12, 11, 94, 81]
```

both produce the **same Binary Search Tree (BST)** when the elements are inserted **from left to right**.

---

### 🔢 BST built from both arrays:

```
           10
         /    \
       8        15
     /        /    \
    5       12      94
   /       /       /
  2       11      81
```

---

### 🛠 Insertion Explanation for array_one = [10, 15, 8, 12, 94, 81, 5, 2, 11]

1. Insert 10 → root
2. Insert 15 → right of 10
3. Insert 8 → left of 10
4. Insert 12 → left of 15
5. Insert 94 → right of 15
6. Insert 81 → left of 94
7. Insert 5 → left of 8
8. Insert 2 → left of 5
9. Insert 11 → left of 12

---

### 🛠 Insertion Explanation for array_two = [10, 8, 5, 15, 2, 12, 11, 94, 81]

1. Insert 10 → root
2. Insert 8 → left of 10
3. Insert 5 → left of 8
4. Insert 15 → right of 10
5. Insert 2 → left of 5
6. Insert 12 → left of 15
7. Insert 11 → left of 12
8. Insert 94 → right of 15
9. Insert 81 → left of 94

---

Despite the different orders, **both arrays produce the exact same structure** — the BST shown above. The function `same_bsts`
compares them without building the tree by simulating this process using recursive constraints.

---

Great! Let's walk through how the recursive helper function `_same_bsts_helper(...)` works **step-by-step** using:

```
array_one = [10, 15, 8, 12, 94, 81, 5, 2, 11]
array_two = [10, 8, 5, 15, 2, 12, 11, 94, 81]
```

---

## 🧠 Step-by-Step Simulation of `_same_bsts_helper`

Initial call:

```
_same_bsts_helper(array_one, array_two, 0, 0, -∞, ∞)
```

**Compare root values:**

* `array_one[0] == 10`
* `array_two[0] == 10` → ✅ Match

---

### 🔽 Step 1: Go to Left Subtree of 10

Find next left children:

* `_find_next_smaller(array_one, 0, -∞)` → index `2` (value `8`)
* `_find_next_smaller(array_two, 0, -∞)` → index `1` (value `8`)

Recursive call:

```
_same_bsts_helper(array_one, array_two, 2, 1, -∞, 10)
```

**Compare:**

* `array_one[2] == 8`
* `array_two[1] == 8` → ✅ Match

---

### 🔽 Step 2: Left Subtree of 8

Find:

* `_find_next_smaller(array_one, 2, -∞)` → index `6` (value `5`)
* `_find_next_smaller(array_two, 1, -∞)` → index `2` (value `5`)

Call:

```
_same_bsts_helper(array_one, array_two, 6, 2, -∞, 8)
```

**Compare:**

* `array_one[6] == 5`
* `array_two[2] == 5` → ✅ Match

---

### 🔽 Step 3: Left Subtree of 5

Find:

* `_find_next_smaller(array_one, 6, -∞)` → index `7` (value `2`)
* `_find_next_smaller(array_two, 2, -∞)` → index `4` (value `2`)

Call:

```
_same_bsts_helper(array_one, array_two, 7, 4, -∞, 5)
```

**Compare:**

* `array_one[7] == 2`
* `array_two[4] == 2` → ✅ Match

---

#### Step 4: Left and Right of 2

* `_find_next_smaller(...)` returns -1 → no left child
* `_find_next_larger_or_equal(...)` returns -1 → no right child

Two base cases called:

```
_same_bsts_helper(..., -1, -1, -∞, 2) → True
_same_bsts_helper(..., -1, -1, 2, 5) → True
```

✅ Done with node 2

---

✅ Done with node 5
(backtrack to 8)

---

### 🔼 Step 5: Right Subtree of 8

Find:

* `_find_next_larger_or_equal(array_one, 2, 10)` → no match → `-1`
* `_find_next_larger_or_equal(array_two, 1, 10)` → no match → `-1`

Both `-1` → no right child

✅ Done with node 8
(backtrack to 10)

---

### 🔽 Step 6: Right Subtree of 10

Find:

* `_find_next_larger_or_equal(array_one, 0, ∞)` → index `1` (value `15`)
* `_find_next_larger_or_equal(array_two, 0, ∞)` → index `3` (value `15`)

Call:

```
_same_bsts_helper(array_one, array_two, 1, 3, 10, ∞)
```

**Compare:**

* `array_one[1] == 15`
* `array_two[3] == 15` → ✅ Match

---

### 🔽 Step 7: Left Subtree of 15

Find:

* `_find_next_smaller(array_one, 1, 10)` → index `3` (value `12`)
* `_find_next_smaller(array_two, 3, 10)` → index `5` (value `12`)

Call:

```
_same_bsts_helper(array_one, array_two, 3, 5, 10, 15)
```

**Compare:**

* `array_one[3] == 12`
* `array_two[5] == 12` → ✅ Match

---

### 🔽 Step 8: Left Subtree of 12

Find:

* `_find_next_smaller(array_one, 3, 10)` → index `8` (value `11`)
* `_find_next_smaller(array_two, 5, 10)` → index `6` (value `11`)

Call:

```
_same_bsts_helper(array_one, array_two, 8, 6, 10, 12)
```

**Compare:**

* `array_one[8] == 11`
* `array_two[6] == 11` → ✅ Match

#### Left and Right of 11:

* No valid smaller or larger children → return True twice

✅ Done with node 11 → Done with node 12 → Done with left of 15

---

### 🔼 Step 9: Right Subtree of 15

Find:

* `_find_next_larger_or_equal(array_one, 1, ∞)` → index `4` (value `94`)
* `_find_next_larger_or_equal(array_two, 3, ∞)` → index `7` (value `94`)

Call:

```
_same_bsts_helper(array_one, array_two, 4, 7, 15, ∞)
```

**Compare:**

* `array_one[4] == 94`
* `array_two[7] == 94` → ✅ Match

---

### 🔽 Step 10: Left Subtree of 94

Find:

* `_find_next_smaller(array_one, 4, 15)` → index `5` (value `81`)
* `_find_next_smaller(array_two, 7, 15)` → index `8` (value `81`)

Call:

```
_same_bsts_helper(array_one, array_two, 5, 8, 15, 94)
```

**Compare:**

* `array_one[5] == 81`

* `array_two[8] == 81` → ✅ Match

* Left/right of 81 = `-1` → return True

✅ Done with node 81 → Done with 94 → Done with 15 → Done with 10

---

## ✅ Final Output: `True`

All recursive calls matched correctly, so `same_bsts(array_one, array_two)` returns **`True`**.

"""
