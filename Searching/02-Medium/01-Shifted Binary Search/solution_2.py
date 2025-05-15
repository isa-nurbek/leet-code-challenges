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


# O(log(n)) time | O(1) space
def shifted_binary_search(array, target):
    """
    Performs a binary search on a shifted sorted array to find the target value.

    Args:
    array: A sorted array that has been shifted (rotated) at some pivot point.
    target: The value to search for in the array.

    Returns:
    The index of the target in the array, or -1 if not found.
    """
    return shifted_binary_search_helper(array, target, 0, len(array) - 1)


def shifted_binary_search_helper(array, target, left, right):
    """
    Helper function that performs the actual shifted binary search recursively.

    Args:
    array: The shifted sorted array to search.
    target: The value to search for.
    left: The left boundary of the current search range.
    right: The right boundary of the current search range.

    Returns:
    The index of the target in the array, or -1 if not found.
    """
    while left <= right:
        middle = (left + right) // 2  # Calculate the middle index
        potential_match = array[middle]  # Value at middle index

        left_num = array[left]  # Value at left boundary
        right_num = array[right]  # Value at right boundary

        if target == potential_match:
            return middle  # Found the target

        # Check if left half is normally ordered (not shifted)
        elif left_num <= potential_match:
            # If target is in the normally ordered left half
            if target < potential_match and target >= left_num:
                right = middle - 1  # Search left half
            else:
                left = middle + 1  # Search right half

        # Right half must be normally ordered (since left half isn't)
        else:
            # If target is in the normally ordered right half
            if target > potential_match and target <= right_num:
                left = middle + 1  # Search right half
            else:
                right = middle - 1  # Search left half

    return -1  # Target not found in array


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

Let's analyze the time and space complexity of the given `shifted_binary_search` algorithm.

### Time Complexity:

The algorithm is a modified binary search that works on a rotated sorted array. At each step, it:
1. Calculates the middle index
2. Compares the middle element with the target
3. Determines which half of the array is properly sorted
4. Decides whether to search in the left or right half based on where the target could be

Since we're effectively dividing the search space in half with each iteration (similar to standard binary search),
the time complexity is **O(log n)**, where n is the number of elements in the array.

### Space Complexity:

The algorithm is implemented iteratively (using a while loop) rather than recursively. It only uses a constant amount of
additional space (for variables like `left`, `right`, `middle`, etc.), so the space complexity is **O(1)**.

### Summary:
- **Time Complexity:** O(log n)
- **Space Complexity:** O(1)

This makes it very efficient for searching in rotated sorted arrays, maintaining the same logarithmic time complexity as
standard binary search while using constant space.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
This implementation solves the **Shifted Binary Search** problem. Let's go step-by-step to understand:

---

### 🔍 Problem Overview:

You're given a **sorted array** that has been **rotated (or shifted)** at some pivot unknown to you in advance. Your task is to
search for a `target` element in this array **in O(log n)** time, using a modified binary search.

#### Example:

Original sorted array:
`[0, 1, 2, 3, 4, 5, 6]`

After shifting:
`[4, 5, 6, 0, 1, 2, 3]`

The goal is to locate the index of the target number efficiently despite the shift.

---

### 🧠 Key Insight:

Even though the array is rotated, **one of the two halves (left or right of the middle) is always sorted**.

### 🔄 Approach:

* Use binary search logic with an additional check to determine which half is **sorted**.
* Based on where the `target` lies, narrow the search to the correct half.

---

### 📜 Code Breakdown:

#### 1. **Entry Function**

```
def shifted_binary_search(array, target):
    return shifted_binary_search_helper(array, target, 0, len(array) - 1)
```

Just a wrapper function that calls the helper with the initial bounds `left = 0` and `right = len(array) - 1`.

---

#### 2. **Helper Function**

```
def shifted_binary_search_helper(array, target, left, right):
    while left <= right:
        middle = (left + right) // 2
        potential_match = array[middle]
```

* Classic binary search loop.
* Compute the middle index and store the value.

```
left_num = array[left]
right_num = array[right]
```

* Store the values at the current `left` and `right` pointers for reference.

---

#### 3. **Target Found?**

```
if target == potential_match:
    return middle
```

* If `target` is found at `middle`, return the index.

---

#### 4. **Determine Which Side is Sorted**

```
elif left_num <= potential_match:
```

* If the **left half is sorted**, then check if the `target` lies in this half.

```
if target < potential_match and target >= left_num:
    right = middle - 1
```

* If `target` lies between `left_num` and `potential_match`, then **search in left half**.

```
else:
    left = middle + 1
```

* Otherwise, search in the **right half**.

---

#### 5. **Otherwise, Right Side is Sorted**

```
else:
    if target > potential_match and target <= right_num:
        left = middle + 1
```

* If the `target` lies within the sorted **right half**, search there.

```
else:
    right = middle - 1
```

* Otherwise, search the **left half**.

---

#### 6. **Target Not Found**

```
return -1
```

If the loop exits, the target is not in the array.

---

### ✅ Test Case Analysis

```
print(shifted_binary_search([45, 61, 71, 72, 73, 0, 1, 21, 33, 37], 33))
# Output: 8
```

* Correct: 33 is at index 8.

```
print(shifted_binary_search([0, 1, 21, 33, 37, 45, 61, 71, 72, 73], 38))
# Output: -1
```

* 38 is not in the array.

```
print(shifted_binary_search([111, 1, 5, 23], 5))
# Output: 2
```

* 5 is at index 2.

---

### 🧠 Time & Space Complexity

* **Time**: `O(log n)` — classic binary search with a slight twist.
* **Space**: `O(1)` — iterative approach uses constant space.

---

### 🔁 Summary

This is a **clever adaptation** of binary search for rotated arrays. The core idea is always identifying which half is sorted
and deciding if the `target` is in that sorted portion.

---

Let’s visualize how **shifted binary search** works using ASCII diagrams for clarity.

### 🔍 Example:

Let's take the array:

```
array = [45, 61, 71, 72, 73, 0, 1, 21, 33, 37]
target = 33
```

This array was originally sorted, then rotated. Let's walk through how the algorithm finds the target `33`.

---

### 🧭 Initial State

```
Index:   0   1   2   3   4   5   6   7   8   9
Value:  [45, 61, 71, 72, 73,  0,  1, 21, 33, 37]
              ^                       ^
            left                    right

middle = (0 + 9) // 2 = 4
potential_match = array[4] = 73
```

* Left half (`45 ... 73`) is sorted.
* Is `33` between `45` and `73`? **No**
* Search right side (`0 ... 37`)

```
➡ Move left to middle + 1 → left = 5
```

---

### 🔁 Second Iteration

```
Index:         5   6   7   8   9
Value:       [ 0,  1, 21, 33, 37]
              ^           ^
            left        right

middle = (5 + 9) // 2 = 7
potential_match = array[7] = 21
```

* Left half (`0 ... 21`) is sorted.
* Is `33` between `0` and `21`? **No**
* Search right side (`33 ... 37`)

```
➡ Move left to middle + 1 → left = 8
```

---

### 🔁 Third Iteration

```
Index:             8   9
Value:           [33, 37]
                  ^   ^
               left  right

middle = (8 + 9) // 2 = 8
potential_match = array[8] = 33
```

✅ Match found!

---

### ✅ Final Result

```
Target 33 found at index 8
```

---

### 🔄 Summary Visualization of Steps

```
Step 1:
[45, 61, 71, 72, 73,  0,  1, 21, 33, 37]
 ^                          ^     ^
left                      middle  right

Step 2:
[45, 61, 71, 72, 73,  0,  1, 21, 33, 37]
                        ^        ^  ^
                      left     middle right

Step 3:
[45, 61, 71, 72, 73,  0,  1, 21, 33, 37]
                                ^   ^
                             left=middle=8
```

"""
