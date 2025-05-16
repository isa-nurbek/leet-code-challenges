# Problem Description:

"""
                                             Search For Range

Write a function that takes in a `sorted array` of integers as well as a `target integer`. The function should use a variation of
the `Binary Search` algorithm to find a range of indices in between which the target number is contained in the array and should
return this range in the form of an array.

The first number in the output array should represent the first index at which the target number is located, while the second number
should represent the last index at which the target number is located. The function should return `[-1, -1]` if the integer isn't
contained in the array.


## Sample Input:
```
array = [0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73]
target = 45
```

## Sample Output:
```
[4, 9]
```

## Optimal Time & Space Complexity:
```
O(log(n)) time | O(1) space - where `n` is the length of the input array.
```

"""

# =========================================================================================================================== #

# Solution:


# O(log(n)) time | O(1) space
def search_for_range(array, target):
    # Initialize the final range with [-1, -1] in case target is not found
    final_range = [-1, -1]

    # First search to find the leftmost index of target (go_left = True)
    altered_binary_search(array, target, 0, len(array) - 1, final_range, True)
    # Second search to find the rightmost index of target (go_left = False)
    altered_binary_search(array, target, 0, len(array) - 1, final_range, False)

    return final_range


def altered_binary_search(array, target, left, right, final_range, go_left):
    """
    A modified binary search that searches for the leftmost or rightmost
    occurrence of target in array and updates final_range accordingly.

    Args:
        array: The sorted array to search in
        target: The value to search for
        left: Left boundary of current search range
        right: Right boundary of current search range
        final_range: The result array to store start/end indices
        go_left: Boolean indicating whether we're searching for leftmost (True)
                 or rightmost (False) occurrence
    """
    while left <= right:
        middle = (left + right) // 2

        if array[middle] < target:
            # Target is in right half
            left = middle + 1
        elif array[middle] > target:
            # Target is in left half
            right = middle - 1
        else:
            # Found target value at middle index
            if go_left:
                # We're searching for left boundary
                if middle == 0 or array[middle - 1] != target:
                    # Found left boundary (either at start of array or previous
                    # element isn't target)
                    final_range[0] = middle
                    return
                else:
                    # Continue searching left half for earlier occurrences
                    right = middle - 1
            else:
                # We're searching for right boundary
                if middle == len(array) - 1 or array[middle + 1] != target:
                    # Found right boundary (either at end of array or next
                    # element isn't target)
                    final_range[1] = middle
                    return
                else:
                    # Continue searching right half for later occurrences
                    left = middle + 1


# Test Cases:

print(search_for_range([0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73], 45))
# Output: [4, 9]

print(search_for_range([5, 7, 7, 8, 8, 10], 5))
# Output: [0, 0]

print(search_for_range([0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73], -1))
# Output: [-1, -1]

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

Let's analyze the time and space complexity of the given `search_for_range` function and its helper `altered_binary_search`.

### Time Complexity:

1. **Binary Search Variant**: The `altered_binary_search` function is a modified binary search. In the worst case, it will run
in O(log n) time, where n is the number of elements in the array. This is because, like standard binary search, it halves the
search space in each iteration.

2. **Two Binary Searches**: The `search_for_range` function calls `altered_binary_search` twice—once to find the left boundary
(`go_left=True`) and once to find the right boundary (`go_left=False`). Each of these calls is O(log n).

3. **Total Time Complexity**: Since we perform two O(log n) operations, the total time complexity remains **O(log n)**.
The constants (2 in this case) are dropped in Big-O notation.

### Space Complexity:

1. **Recursive vs. Iterative**: The `altered_binary_search` function is implemented iteratively (using a `while` loop), so it does
not use additional space on the call stack. This is in contrast to a recursive binary search, which would use O(log n) space due
to the call stack.

2. **Variables**: The function uses a constant amount of extra space (variables like `left`, `right`, `middle`, etc.), and the
`final_range` array is passed by reference and has a fixed size of 2.

3. **Total Space Complexity**: The space complexity is **O(1)** (constant space), as no additional space is used that scales with
the input size.

### Summary:
- **Time Complexity**: O(log n)
- **Space Complexity**: O(1)

This is an efficient solution for finding the range of a target value in a sorted array. The two-pass binary search approach
ensures we correctly identify the boundaries of the target range.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
Let’s break down the code step by step and explain **how it works**, **why it works**, and **what it's doing under the hood**.

---

## 🎯 **Goal of the Code**

The function `search_for_range(array, target)` searches for the **first and last occurrence (range)** of a given `target` in a
sorted array.

For example, if the array is:

```
[0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73]
```

and the target is `45`, the output will be `[4, 9]` — because the first occurrence is at index 4 and the last at index 9.

---

## 🔍 High-Level Overview

The algorithm uses **modified binary search** to efficiently find the:

* **First occurrence** of the target (leftmost),
* **Last occurrence** of the target (rightmost).

This is done in **O(log n)** time instead of O(n) that a linear scan would take.

---

## 🧠 Main Function: `search_for_range`

```
def search_for_range(array, target):
    final_range = [-1, -1]  # Default value if target is not found

    altered_binary_search(array, target, 0, len(array) - 1, final_range, True)   # Search for first index
    altered_binary_search(array, target, 0, len(array) - 1, final_range, False)  # Search for last index

    return final_range
```

### What it does:

* Initializes `final_range` to `[-1, -1]` which will be returned if the target is not found.
* Calls `altered_binary_search` **twice**:

  * Once to find the **left boundary** (first occurrence),
  * Once to find the **right boundary** (last occurrence).
* Returns the result.

---

## 🔍 Helper Function: `altered_binary_search`

```
def altered_binary_search(array, target, left, right, final_range, go_left):
```

### Parameters:

* `array`: the sorted list.
* `target`: the number we’re searching for.
* `left`, `right`: current binary search boundaries.
* `final_range`: list storing the result (`[start, end]`).
* `go_left`: boolean flag to indicate if we’re searching for the **leftmost** or **rightmost** occurrence.

---

## 🔁 Inside the While Loop

```
while left <= right:
    middle = (left + right) // 2
```

Classic binary search loop. `middle` is the mid-index.

---

### 🔀 Case 1: `array[middle] < target`

```
left = middle + 1
```

The target must be in the right half.

---

### 🔀 Case 2: `array[middle] > target`

```
right = middle - 1
```

The target must be in the left half.

---

### ✅ Case 3: `array[middle] == target`

This means we've found *an* occurrence of the target, but we may not yet be at the leftmost or rightmost occurrence.

Now we use `go_left` to decide whether to move left or right:

#### ⬅️ If `go_left == True`: search for **left boundary**

```
if middle == 0 or array[middle - 1] != target:
    final_range[0] = middle
    return
else:
    right = middle - 1  # keep moving left
```

* If `middle` is at the beginning, or the previous element is not equal to the target → this is the first occurrence.
* Otherwise, keep going left.

---

#### ➡️ If `go_left == False`: search for **right boundary**

```
if middle == len(array) - 1 or array[middle + 1] != target:
    final_range[1] = middle
    return
else:
    left = middle + 1  # keep moving right
```

* If `middle` is at the end, or the next element is not equal to the target → this is the last occurrence.
* Otherwise, keep going right.

---

## ✅ Example Walkthrough

### Input:

```
search_for_range([0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73], 45)
```

### Steps:

1. First binary search (go_left = True) → finds **first 45** at index 4.
2. Second binary search (go_left = False) → finds **last 45** at index 9.
3. Output → `[4, 9]`

---

## 🧪 Edge Cases Handled

* Target not in array → `final_range` remains `[-1, -1]`.
* Target occurs only once → both left and right are the same index.
* All elements are the target → returns `[0, len(array) - 1]`.

---

## 🧠 Time and Space Complexity

* **Time Complexity**: `O(log n)` — Two binary searches.
* **Space Complexity**: `O(1)` — Only a few variables used.

---

## ✅ Test Outputs Recap

```
print(search_for_range([0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73], 45))
# ➜ [4, 9]

print(search_for_range([5, 7, 7, 8, 8, 10], 5))
# ➜ [0, 0]

print(search_for_range([0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73], -1))
# ➜ [-1, -1]
```

---

Let's walk through an **ASCII visualization** of how this code searches for the **first and last occurrence** of the target
using **binary search**.

We'll use this example:

```
array = [0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73]
target = 45
```

Indexes:

```
Index:   0   1   2   3   4   5   6   7   8   9   10  11  12
Array:  [0,  1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73]
```

---

## 🔍 Step-by-Step ASCII: Finding First Occurrence (`go_left = True`)

```
Initial left = 0, right = 12

# Step 1:
middle = (0 + 12) // 2 = 6
array[6] = 45 (== target)

   left                   mid                  right
    ↓                     ↓                      ↓
[ 0,  1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73 ]
                          ^-- Found target, check left neighbor (array[5] = 45)
                          => Not leftmost, move right to mid - 1 = 5

# Step 2:
middle = (0 + 5) // 2 = 2
array[2] = 21 (< target)
→ Move left to mid + 1 = 3

# Step 3:
middle = (3 + 5) // 2 = 4
array[4] = 45 (== target)

        left      mid     right
         ↓         ↓        ↓
[ 0,  1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73 ]
                   ^-- Found target, check left (array[3] = 33 ≠ 45)
                   => Leftmost found! final_range[0] = 4
```

---

## 🔍 Step-by-Step ASCII: Finding Last Occurrence (`go_left = False`)

```
Initial left = 0, right = 12

# Step 1:
middle = (0 + 12) // 2 = 6
array[6] = 45 (== target)

   left                   mid                  right
    ↓                     ↓                      ↓
[ 0,  1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73 ]
                          ^-- Found target, check right (array[7] = 45)
                          => Not rightmost, move left to mid + 1 = 7

# Step 2:
middle = (7 + 12) // 2 = 9
array[9] = 45 (== target)

                              mid
                               ↓
[ 0,  1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73 ]
                               ^-- Found target, check right (array[10] = 61 ≠ 45)
                               => Rightmost found! final_range[1] = 9
```

---

### ✅ Final Result:

```
final_range = [4, 9]
```

---

### Summary Diagram:

```
[ 0,  1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73 ]
                   ↑                      ↑
                First 45              Last 45
                index = 4            index = 9
```

"""
