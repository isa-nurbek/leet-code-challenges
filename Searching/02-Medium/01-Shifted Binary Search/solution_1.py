# Problem Description:

"""
                                             Shifted Binary Search

Write a function that takes in a sorted array of distinct integers as well as a target integer. The caveat is that the integers in
the array have been shifted by some amount; in other words, they've been moved to the left or to the right by one or more positions.
For example, `[1, 2, 3, 4]` might have turned into `[3, 4, 1, 2]`.

The function should use a variation of the `Binary Search` algorithm to determine if the target integer is contained in the array
and should return its `index` if it is, otherwise `-1`.


## Sample Input:
```
array = [45, 61, 71, 72, 73, 0, 1, 21, 33, 37]
target = 33
```

## Sample Output:
```
8
```

## Optimal Time & Space Complexity:
```
O(log(n)) time | O(1) space - where `n` is the length of the input array.
```

"""

# =========================================================================================================================== #

# Solution:


# O(log(n)) time | O(log(n)) space
def shifted_binary_search(array, target):
    """Performs a binary search on a shifted sorted array.

    Args:
        array: A sorted array that has been shifted (rotated) by some unknown offset.
        target: The value to search for in the array.

    Returns:
        The index of the target if found, otherwise -1.
    """
    return shifted_binary_search_helper(array, target, 0, len(array) - 1)


def shifted_binary_search_helper(array, target, left, right):
    """Helper function that performs the actual shifted binary search recursively.

    Args:
        array: The input array.
        target: The value to search for.
        left: The left boundary of the current search range.
        right: The right boundary of the current search range.

    Returns:
        The index of the target if found, otherwise -1.
    """
    # Base case: target not found in current search range
    if left > right:
        return -1

    middle = (left + right) // 2
    potential_match = array[middle]

    # These are used to determine which side is properly ordered
    left_num = array[left]
    right_num = array[right]

    # Target found at middle index
    if target == potential_match:
        return middle

    # Case 1: Left half is properly ordered (left_num <= potential_match)
    elif left_num <= potential_match:
        # If target is in the left ordered half, search there
        if target < potential_match and target >= left_num:
            return shifted_binary_search_helper(array, target, left, middle - 1)
        # Otherwise search the right half (which might be shifted)
        else:
            return shifted_binary_search_helper(array, target, middle + 1, right)

    # Case 2: Right half is properly ordered (left_num > potential_match)
    else:
        # If target is in the right ordered half, search there
        if target > potential_match and target <= right_num:
            return shifted_binary_search_helper(array, target, middle + 1, right)
        # Otherwise search the left half (which might contain the shift point)
        else:
            return shifted_binary_search_helper(array, target, left, middle - 1)


# Test Cases:

print(shifted_binary_search([45, 61, 71, 72, 73, 0, 1, 21, 33, 37], 33))
# Output: 8

print(shifted_binary_search([0, 1, 21, 33, 37, 45, 61, 71, 72, 73], 38))
# Output: -1

print(shifted_binary_search([111, 1, 5, 23], 5))
# Output: 2

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### Time Complexity Analysis:

The time complexity of the `shifted_binary_search` algorithm is **O(log n)**, where `n` is the number of elements in the array. Here's why:

1. **Binary Search Approach**: The algorithm is a modified binary search. In each recursive call, it divides the search space
(the current `left` to `right` range) roughly in half, similar to standard binary search.

2. **Constant Work per Recursive Call**: In each recursive call, the algorithm performs a constant amount of work (calculating
`middle`, comparing `target` with `potential_match`, `left_num`, and `right_num`, and deciding which half to recurse into).

3. **Number of Recursive Calls**: Since the search space is halved in each step, the maximum number of recursive calls is
proportional to the height of the recursion tree, which is `log₂ n`. Thus, the total time is O(log n).

### Space Complexity Analysis:

The space complexity is **O(log n)** due to the recursive nature of the algorithm. Here's why:

1. **Recursive Call Stack**: Each recursive call adds a new layer to the call stack. In the worst case, the depth of the recursion
tree is `log₂ n` (same as the time complexity), so the space used by the call stack is O(log n).

2. **No Additional Space**: The algorithm does not use any additional data structures or allocate significant extra memory beyond
the call stack.

### Summary:
- Time Complexity: **O(log n)**
- Space Complexity: **O(log n)** (due to recursion)

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
The function `shifted_binary_search` is designed to efficiently find a target element in a **shifted (or rotated) sorted array**.
A shifted sorted array is an array that was initially sorted in ascending order but then rotated (or shifted) at some pivot point.
For example:

Original sorted array:

```
[0, 1, 2, 3, 4, 5, 6]
```

Shifted version:

```
[4, 5, 6, 0, 1, 2, 3]
```

---

### 🔍 Goal:

Find the index of a `target` number in such a shifted array using a modified binary search. If not found, return `-1`.

---

## ✅ Code Walkthrough

```
def shifted_binary_search(array, target):
    return shifted_binary_search_helper(array, target, 0, len(array) - 1)
```

* A simple wrapper function that starts the recursive binary search with full array boundaries (`left = 0`, `right = len(array) - 1`).

---

### Core Recursive Logic

```
def shifted_binary_search_helper(array, target, left, right):
    if left > right:
        return -1  # Base case: target not found
```

* If the search boundaries cross over, the target isn't in the array.

```
middle = (left + right) // 2
potential_match = array[middle]

left_num = array[left]
right_num = array[right]
```

* `middle` is the midpoint of the current subarray.
* `potential_match` is the value at the middle.
* `left_num` and `right_num` store the boundary values for reasoning about sorted halves.

---

### 🎯 Base Match Case

```
if target == potential_match:
    return middle
```

* If the middle element is the target, return the index.

---

### 🔄 Identifying Sorted Halves

A rotated array still has **at least one sorted half** (left or right), which is critical for binary search to proceed correctly.

```
elif left_num <= potential_match:
```

* If the **left half** (`left` to `middle`) is sorted:

```
if target < potential_match and target >= left_num:
    # Target is in the sorted left half
    return shifted_binary_search_helper(array, target, left, middle - 1)
else:
    # Target is in the right half
    return shifted_binary_search_helper(array, target, middle + 1, right)
```

---

```
else:
    # Right half is sorted
    if target > potential_match and target <= right_num:
        # Target is in the sorted right half
        return shifted_binary_search_helper(array, target, middle + 1, right)
    else:
        # Target is in the left half
        return shifted_binary_search_helper(array, target, left, middle - 1)
```

---

## 📊 Time & Space Complexity

* **Time Complexity:** `O(log n)` — It halves the search space each time, like standard binary search.
* **Space Complexity:** `O(log n)` due to recursion stack (can be made `O(1)` using an iterative version).

---

## 🧪 Test Case Explanation

### Test 1:

```
shifted_binary_search([45, 61, 71, 72, 73, 0, 1, 21, 33, 37], 33)
```

* Rotated at index 5. Sorted parts: `[45...73]` and `[0...37]`.
* 33 is in the right half ⇒ found at index **8** ✅

---

### Test 2:

```
shifted_binary_search([0, 1, 21, 33, 37, 45, 61, 71, 72, 73], 38)
```

* Not rotated. Standard binary search.
* 38 not found ⇒ returns **-1** ✅

---

### Test 3:

```
shifted_binary_search([111, 1, 5, 23], 5)
```

* Rotated: `[111] [1, 5, 23]`
* 5 is in the sorted right half ⇒ found at index **2** ✅

---

## ✅ Summary

This algorithm extends the classic binary search to handle **rotated sorted arrays** by intelligently determining which half
is sorted and deciding whether to search there based on the target's value range.

---

Here's a **visual ASCII explanation** of how the `shifted_binary_search` works step by step. Let's walk through this example:

### 🔍 Example:

```
array = [45, 61, 71, 72, 73, 0, 1, 21, 33, 37]
target = 33
```

---

### Step 1: Full Array View

```
Index:   0   1   2   3   4   5   6   7   8   9
Array:  [45, 61, 71, 72, 73,  0,  1, 21, 33, 37]
                  ↑                   ↑
                left                right
              = 0                   = 9
```

Midpoint is:

```
middle = (0 + 9) // 2 = 4
array[4] = 73
```

* Left half [45, 61, 71, 72, 73] is **sorted**.
* Target = 33 is **not in** [45...73], so search **right half**.

---

### Step 2: Right Half: index 5 to 9

```
Index:   0   1   2   3   4   5   6   7   8   9
Array:                     [ 0,  1, 21, 33, 37]
                            ↑             ↑
                          left          right
                        = 5             = 9
```

```
middle = (5 + 9) // 2 = 7
array[7] = 21
```

* Left half [0, 1, 21] is sorted.
* Target = 33 is **not in** [0...21], so search **right half**.

---

### Step 3: Right Half: index 8 to 9

```
Index:   0   1   2   3   4   5   6   7   8   9
Array:                            [33, 37]
                                   ↑    ↑
                                 left right
                                = 8   = 9
```

```
middle = (8 + 9) // 2 = 8
array[8] = 33
```

✅ Found! Return index **8**

---

### Final Recap:

Each time, the algorithm:

* Divides the array in half.
* Identifies which side is **sorted**.
* Narrows down search to only the half where the target **could exist**.

"""
