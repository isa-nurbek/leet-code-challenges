# Problem Description:

"""
                                                Merge Sort

Write a function that takes in an array of integers and returns a `sorted` version of that array. Use the `Merge Sort` algorithm
to sort the array.


## Sample Input:
```
array = [8, 5, 2, 9, 5, 6, 3]
```

## Sample Output:
```
[2, 3, 5, 5, 6, 8, 9]
```

## Optimal Time & Space Complexity:
```
Best: O(n log(n)) time | O(n) space - where `n` is the length of the input array.
Average: O(n log(n)) time | O(n) space - where `n` is the length of the input array.
Worst: O(n log(n)) time | O(n) space - where `n` is the length of the input array.
```

"""

# =========================================================================================================================== #

# Solution:


# Best: O(n log(n)) time | O(n) space
# Average: O(n log(n)) time | O(n) space
# Worst: O(n log(n)) time | O(n) space
def merge_sort(arr):
    """
    Main merge sort function that initiates the sorting process.
    Creates a temporary array once to be used for all merging operations.

    Args:
        arr: The array to be sorted

    Returns:
        The sorted array
    """
    # Create a temporary array for merging once (to avoid repeated allocations)
    temp = [0] * len(arr)
    # Start the recursive sorting process
    _merge_sort(arr, temp, 0, len(arr) - 1)

    return arr


def _merge_sort(arr, temp, left, right):
    """
    Recursive helper function that divides the array into halves and sorts them.

    Args:
        arr: The array being sorted
        temp: Temporary array for merging
        left: Left index of the current subarray
        right: Right index of the current subarray
    """
    # Only proceed if there's more than one element in the subarray
    if left < right:
        # Find the middle point to divide the array into two halves
        mid = (left + right) // 2
        # Recursively sort the left half
        _merge_sort(arr, temp, left, mid)
        # Recursively sort the right half
        _merge_sort(arr, temp, mid + 1, right)
        # Merge the two sorted halves
        merge(arr, temp, left, mid, right)


def merge(arr, temp, left, mid, right):
    """
    Merges two sorted subarrays into one sorted subarray.
    The subarrays are arr[left..mid] and arr[mid+1..right].

    Args:
        arr: The main array being sorted
        temp: Temporary array used for merging
        left: Left index of the first subarray
        mid: End index of the first subarray
        right: End index of the second subarray
    """
    i = left  # Pointer for left subarray (starts at beginning)
    j = mid + 1  # Pointer for right subarray (starts at middle + 1)
    k = left  # Pointer for temp array (starts at beginning of current range)

    # Traverse both subarrays and copy the smaller element to temp
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]  # Left element is smaller or equal
            i += 1
        else:
            temp[k] = arr[j]  # Right element is smaller
            j += 1
        k += 1

    # Copy any remaining elements from left subarray
    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    # Copy any remaining elements from right subarray
    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1

    # Copy the merged elements from temp back to the original array
    for k in range(left, right + 1):
        arr[k] = temp[k]


# Test Cases:

print(merge_sort([8, 5, 2, 9, 5, 6, 3]))
# Output: [2, 3, 5, 5, 6, 8, 9]

print(merge_sort([38, 27, 43, 3, 9, 82, 10]))
# Output: [3, 9, 10, 27, 38, 43, 82]

print(merge_sort([5, -2, 2, -8, 3, -10, -6, -1, 2, -2, 9, 1, 1]))
# Output: [-10, -8, -6, -2, -2, -1, 1, 1, 2, 2, 3, 5, 9]

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

Let's analyze the time and space complexity of this Merge Sort implementation.

### Time Complexity:

Merge Sort is a divide-and-conquer algorithm with consistent performance. 

1. **Divide Step**: The array is recursively divided into halves until we reach subarrays of size 1.
This takes O(log n) levels of recursion since we're halving the array each time.

2. **Merge Step**: At each level of recursion, we merge all the subarrays at that level, which takes O(n) time since we're
processing all n elements.

Since we have O(log n) levels and each level takes O(n) time, the **total time complexity is O(n log n)** in all cases
(best, average, and worst).

### Space Complexity:

1. **Temporary Array**: The implementation uses a temporary array `temp` of size n, which is the main additional space used.
2. **Recursion Stack**: The recursion depth is O(log n), but this doesn't dominate over the temporary array.

Thus, the **space complexity is O(n)** due to the temporary array. This is the standard space complexity for the top-down
Merge Sort implementation.

### Key Points:

- Time Complexity: **O(n log n)** (always, very consistent).
- Space Complexity: **O(n)** (due to the temporary array).

- Merge Sort is stable (preserves order of equal elements) and works well for large datasets, but it uses additional space
unlike in-place sorts like Quick Sort.

This implementation is efficient and correct, following the standard Merge Sort approach.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
Here's a **detailed explanation** of the `merge_sort` implementation, including how each part of the code works:

---

### 🔷 Overview: What is Merge Sort?

**Merge Sort** is a classic **Divide and Conquer** algorithm:

1. **Divide** the array into halves until subarrays have only one element.
2. **Conquer** (i.e., merge) those subarrays back together in sorted order.

---

## 🔹 `merge_sort(arr)`

```
def merge_sort(arr):
    # Create a temporary array for merging once
    temp = [0] * len(arr)
    _merge_sort(arr, temp, 0, len(arr) - 1)
    return arr
```

* **Purpose**: Entry point of the algorithm. It prepares a temporary array to avoid reallocating memory during recursive calls.
* `temp`: This array will be reused for all merging operations, improving performance.

---

## 🔹 `_merge_sort(arr, temp, left, right)`

```
def _merge_sort(arr, temp, left, right):
    if left < right:
        mid = (left + right) // 2
        _merge_sort(arr, temp, left, mid)         # Sort left half
        _merge_sort(arr, temp, mid + 1, right)    # Sort right half
        merge(arr, temp, left, mid, right)        # Merge the two halves
```

* **Recursive Function**: It keeps dividing the array into two halves.
* `mid` is the midpoint index between `left` and `right`.
* Eventually, recursion breaks the array into single-element parts.
* Then it starts **merging** those sorted parts using the `merge` function.

---

## 🔹 `merge(arr, temp, left, mid, right)`

```
def merge(arr, temp, left, mid, right):
    i = left
    j = mid + 1
    k = left
```

### Initial Setup:

* `i` tracks position in the left subarray.
* `j` tracks position in the right subarray.
* `k` tracks position in the temp array (for merged result).

---

### Merging Two Sorted Subarrays:

```
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1
```

* Elements from `arr[i]` and `arr[j]` are compared.
* Smaller element is placed in `temp[k]`.
* `i` or `j` and `k` are incremented accordingly.

---

### Copy Remaining Elements (if any):

```
    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1
```

* After the loop above, **at most one** of the two subarrays may have elements left.
* These loops copy those remaining elements directly into `temp`.

---

### Copy Back to Original Array:

```
    for k in range(left, right + 1):
        arr[k] = temp[k]
```

* After merging, the sorted subarray is copied back from `temp` to `arr`.

---

## ✅ Test Cases:

### Test Case 1:

```
merge_sort([8, 5, 2, 9, 5, 6, 3])
# Output: [2, 3, 5, 5, 6, 8, 9]
```

### Test Case 2:

```
merge_sort([38, 27, 43, 3, 9, 82, 10])
# Output: [3, 9, 10, 27, 38, 43, 82]
```

### Test Case 3:

```
merge_sort([5, -2, 2, -8, 3, -10, -6, -1, 2, -2, 9, 1, 1])
# Output: [-10, -8, -6, -2, -2, -1, 1, 1, 2, 2, 3, 5, 9]
```

---

## 🧠 Time & Space Complexity

### Time Complexity:

* **Worst, Best, and Average**: O(n log n)
* Due to:

  * `log n` levels of recursion.
  * Merging takes O(n) at each level.

### Space Complexity:

* O(n) for the temporary array `temp`.

---

## 🔚 Summary

* This is an efficient **top-down merge sort**.
* It uses a single reusable `temp` array for merging to reduce memory allocation overhead.
* It is a stable sort (preserves order of equal elements).
* Suitable for sorting large arrays where performance matters.

---

Let’s visualize **bottom-up merge sort** on the array:

```
[8, 5, 2, 9, 5, 6, 3]
```

---

## 🔄 Bottom-Up Merge Sort: ASCII Visualization

We’ll show how the array is sorted level by level.

### Initial array (size = 1 chunks):

```
[8] [5] [2] [9] [5] [6] [3]
```

---

### 🔹 Pass 1: size = 1

Merge adjacent pairs:

```
[8] + [5] → [5, 8]
[2] + [9] → [2, 9]
[5] + [6] → [5, 6]
[3]       → remains unpaired

Result:
[5, 8] [2, 9] [5, 6] [3]
```

---

### 🔹 Pass 2: size = 2

Now merge adjacent 2-element groups:

```
[5, 8] + [2, 9] → [2, 5, 8, 9]
[5, 6] + [3]    → [3, 5, 6]

Result:
[2, 5, 8, 9] [3, 5, 6]
```

---

### 🔹 Pass 3: size = 4

Final merge (since next block would be > array size):

```
[2, 5, 8, 9] + [3, 5, 6] → [2, 3, 5, 5, 6, 8, 9]
```

---

## ✅ Final Output:

```
[2, 3, 5, 5, 6, 8, 9]
```

---

## 🧱 Layered ASCII Merge Diagram

```
Level 0 (initial):  [8] [5] [2] [9] [5] [6] [3]

Level 1 (size=1):   [5,8] [2,9] [5,6] [3]

Level 2 (size=2):   [2,5,8,9] [3,5,6]

Level 3 (size=4):   [2,3,5,5,6,8,9]
```

Each level doubles the size of chunks being merged until the full array is sorted.

"""
