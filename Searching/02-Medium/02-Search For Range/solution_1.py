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


# O(log(n)) time | O(log(n)) space
def search_for_range(array, target):
    """
    Finds the starting and ending positions of a target value in a sorted array.

    Args:
        array: A sorted list of integers.
        target: The integer value to search for in the array.

    Returns:
        A list containing the first and last indices of the target value.
        Returns [-1, -1] if the target is not found.
    """
    # Initialize the result range with [-1, -1] in case target is not found
    final_range = [-1, -1]

    # First search to find the left boundary (start index) of the target
    altered_binary_search(array, target, 0, len(array) - 1, final_range, True)
    # Second search to find the right boundary (end index) of the target
    altered_binary_search(array, target, 0, len(array) - 1, final_range, False)

    return final_range


def altered_binary_search(array, target, left, right, final_range, go_left):
    """
    A modified binary search that searches for the boundaries of a target value.

    Args:
        array: The sorted list to search in.
        target: The value to search for.
        left: The left boundary of the current search range.
        right: The right boundary of the current search range.
        final_range: The result array that stores the start and end indices.
        go_left: Boolean flag indicating whether we're searching for the left boundary (True)
                 or right boundary (False) of the target range.
    """
    # Base case: stop when left pointer exceeds right pointer
    if left > right:
        return

    # Calculate middle index
    middle = (left + right) // 2

    if array[middle] < target:
        # Target is in the right half
        altered_binary_search(array, target, middle + 1, right, final_range, go_left)
    elif array[middle] > target:
        # Target is in the left half
        altered_binary_search(array, target, left, middle - 1, final_range, go_left)
    else:
        # Found the target value
        if go_left:
            # We're searching for the left boundary
            if middle == 0 or array[middle - 1] != target:
                # Found the left boundary (either at start of array or previous element is different)
                final_range[0] = middle
            else:
                # Continue searching left to find the earliest occurrence
                altered_binary_search(
                    array, target, left, middle - 1, final_range, go_left
                )
        else:
            # We're searching for the right boundary
            if middle == len(array) - 1 or array[middle + 1] != target:
                # Found the right boundary (either at end of array or next element is different)
                final_range[1] = middle
            else:
                # Continue searching right to find the last occurrence
                altered_binary_search(
                    array, target, middle + 1, right, final_range, go_left
                )


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

Let's analyze the time and space complexity of the given `search_for_range` algorithm.

### **Time Complexity: O(log n)**

The algorithm performs two modified binary searches:
1. One to find the leftmost occurrence of the target (`go_left = True`).
2. One to find the rightmost occurrence of the target (`go_left = False`).

Each binary search runs in **O(log n)** time because, in the worst case, it halves the search space in each recursive call.
Since we perform **two independent binary searches**, the total time remains **O(log n)**.

#### **Why not O(2 log n)?**
- In Big-O notation, we drop constant factors, so **O(2 log n) = O(log n)**.

### **Space Complexity: O(log n) (due to recursion stack)**

The algorithm uses recursion, and the maximum depth of the recursion stack is determined by the number of times we split
the array in half:
- Each binary search has a recursion depth of **O(log n)**.
- Since the two searches are independent (not nested), the space complexity remains **O(log n)**.

### **Summary**

| Complexity  | Value                                             |
|-------------|---------------------------------------------------|
| **Time**    | O(log n)                                          |
| **Space**   | O(log n) (can be O(1) if implemented iteratively) |

#### **Can we optimize space to O(1)?**

Yes! If we rewrite the binary search iteratively instead of recursively, the space complexity reduces to **O(1)** because
we no longer use the call stack.

This algorithm efficiently finds the range of a target in a sorted array using a modified binary search approach.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
This Python code is designed to **find the first and last position of a target element** in a **sorted array** using a **modified
binary search** algorithm. It returns a list with two values: the start and end indices of the target in the array. If the target
is not found, it returns `[-1, -1]`.

---

## ✅ Code Breakdown

### 1. `search_for_range(array, target)`

This is the main function that:

* Initializes a result list `final_range` to `[-1, -1]`.
* Calls a helper function `altered_binary_search()` twice:

  * Once to find the **leftmost** (first) index.
  * Once to find the **rightmost** (last) index.
* Returns `final_range`.

```
final_range = [-1, -1]
altered_binary_search(array, target, 0, len(array) - 1, final_range, True)   # Find leftmost index
altered_binary_search(array, target, 0, len(array) - 1, final_range, False)  # Find rightmost index
return final_range
```

---

### 2. `altered_binary_search(array, target, left, right, final_range, go_left)`

This is a recursive function that:

* Works like binary search but is **altered to keep going left or right** depending on whether we are finding the first or
last occurrence of the target.
* Parameters:

  * `go_left = True`: We are searching for the **first** occurrence (leftmost).
  * `go_left = False`: We are searching for the **last** occurrence (rightmost).

#### Main Logic:

```
if left > right:
    return
```

If the search space is invalid, return immediately.

#### Find the middle:

```
middle = (left + right) // 2
```

#### Recurse based on comparison:

```
if array[middle] < target:
    altered_binary_search(array, target, middle + 1, right, final_range, go_left)
elif array[middle] > target:
    altered_binary_search(array, target, left, middle - 1, final_range, go_left)
```

#### When `array[middle] == target`:

We’ve found the target! Now we must check:

##### A. If we're looking for the **leftmost index** (`go_left = True`):

```
if middle == 0 or array[middle - 1] != target:
    final_range[0] = middle  # Found the first occurrence
else:
    altered_binary_search(array, target, left, middle - 1, final_range, go_left)
```

##### B. If we're looking for the **rightmost index** (`go_left = False`):

```
if middle == len(array) - 1 or array[middle + 1] != target:
    final_range[1] = middle  # Found the last occurrence
else:
    altered_binary_search(array, target, middle + 1, right, final_range, go_left)
```

---

## 🧪 Test Case Walkthrough

### Example:

```
search_for_range([0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73], 45)
```

* The target `45` appears from index 4 to 9.
* First call (go_left = True):

  * Modified binary search narrows to leftmost `45` at index 4.
* Second call (go_left = False):

  * Modified binary search finds rightmost `45` at index 9.
* Returns `[4, 9]`.

---

## 🧠 Why Use This Approach?

* **Time Complexity**: `O(log n)`

  * We use binary search twice, so total time complexity is still logarithmic.
* **Space Complexity**: `O(log n)` due to recursion stack.

  * Could be made `O(1)` with an iterative version.

---

## ✅ Summary

* This code efficiently finds the **range** (start and end indices) of a target value in a sorted array using two passes of
**recursive binary search**.
* It's much faster than linear search, especially for large datasets.
* Edge cases (e.g. not found, one occurrence) are handled naturally.

---

Let’s visualize the algorithm using **ASCII diagrams** to show how it performs **binary search** to find the **first and
last occurrence** of a target value.

---

### 🎯 Example:

```
array = [0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73]
target = 45
```

Indices:

```
         0   1   2   3   4   5   6   7   8   9  10  11  12
array = [0,  1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73]
```

---

## 🔍 First Occurrence (go_left = True)

We search **left** for the **first 45**.

### Step 1:

Search from index 0 to 12
Middle = (0+12)//2 = 6 → `array[6] = 45`

```
      L                         M                         R
      ↓                         ↓                         ↓
[0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73]
                └── Target found at index 6, go left
```

Since `array[5] = 45` → keep searching left.

---

### Step 2:

Search from index 0 to 5
Middle = (0+5)//2 = 2 → `array[2] = 21`

```
  L         M                   R
  ↓         ↓                   ↓
[0, 1, 21, 33, 45, 45, ...]
        └── array[2] < target → search right
```

---

### Step 3:

Search from index 3 to 5
Middle = (3+5)//2 = 4 → `array[4] = 45`

```
        L     M     R
        ↓     ↓     ↓
[33, 45, 45]
      └── array[3] = 33 ≠ target → we found 45 at index 4
      └── array[3] ≠ 45 → index 4 is the **first occurrence**
```

✅ Final left index: **4**

---

## 🔎 Last Occurrence (go_left = False)

We search **right** for the **last 45**.

### Step 1:

Search from index 0 to 12
Middle = 6 → `array[6] = 45`

```
      L                         M                         R
      ↓                         ↓                         ↓
[0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73]
                └── Target found at index 6, go right
```

---

### Step 2:

Search from index 7 to 12
Middle = 9 → `array[9] = 45`

```
                        L     M     R
                        ↓     ↓     ↓
                  [45, 45, 61, 71, 73]
                              └── array[10] ≠ 45 → index 9 is the last occurrence
```

✅ Final right index: **9**

---

## ✅ Final Output:

```
[4, 9]
```

"""
