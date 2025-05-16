# Problem Description:

"""
                                             Median Of Two Sorted Arrays

You're given `two sorted arrays` of integers `array_one` and `array_two`. Write a function that returns the `median` of these arrays.

You can assume both arrays have at least one value. However, they could be of different lengths. If the `median` is a decimal value,
it should not be rounded (beyond the inevitable rounding of floating point math).


## Sample Input:
```
array_one = [1, 3, 4, 5]
array_two = [2, 3, 6, 7]
```

## Sample Output:
```
3.5

// The combined array is [1, 2, 3, 3, 4, 5, 6, 7]
```

## Optimal Time & Space Complexity:
```
O(log(min(n, m)) time | O(1) space - where `n` is the length of `array_one` and `m` is the length of `array_two`.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n + m) time | O(1) space
def median_of_two_sorted_arrays(array_one, array_two):
    # Initialize pointers for both arrays
    idx_one, idx_two = 0, 0

    # Calculate total length of combined arrays
    total_length = len(array_one) + len(array_two)

    # Calculate middle index (for odd length) or first middle index (for even length)
    middle_idx = (total_length - 1) // 2

    # For even length, we need the next index after middle to calculate median
    next_middle_idx = middle_idx + 1 if total_length % 2 == 0 else None

    # Move pointers forward until we reach the middle index of the combined array
    while idx_one + idx_two < middle_idx:
        # If we've exhausted array_one, move array_two's pointer
        if idx_one >= len(array_one):
            idx_two += 1
        # If we've exhausted array_two, move array_one's pointer
        elif idx_two >= len(array_two):
            idx_one += 1
        # Otherwise, move the pointer of the array with smaller current element
        elif array_one[idx_one] < array_two[idx_two]:
            idx_one += 1
        else:
            idx_two += 1

    # Handle case where total length is odd (single middle element)
    if next_middle_idx is None:
        # If array_one is exhausted, return current element from array_two
        if idx_one >= len(array_one):
            return array_two[idx_two]

        # If array_two is exhausted, return current element from array_one
        if idx_two >= len(array_two):
            return array_one[idx_one]

        # Otherwise return the smaller of current elements (since arrays are sorted)
        return min(array_one[idx_one], array_two[idx_two])
    # Handle case where total length is even (average of two middle elements)
    else:
        values = []
        # We need to collect the next two elements (current and next)
        for _ in range(2):
            # Similar logic as above to get next elements
            if idx_one >= len(array_one):
                values.append(array_two[idx_two])
                idx_two += 1
            elif idx_two >= len(array_two):
                values.append(array_one[idx_one])
                idx_one += 1
            elif array_one[idx_one] < array_two[idx_two]:
                values.append(array_one[idx_one])
                idx_one += 1
            else:
                values.append(array_two[idx_two])
                idx_two += 1
        # Return average of the two middle elements
        return sum(values) / 2


# Test Cases:

print(median_of_two_sorted_arrays([1, 3, 4, 5], [2, 3, 6, 7]))
# Output: 3.5

print(median_of_two_sorted_arrays([2, 2, 2, 2, 2], [3, 3, 3, 3]))
# Output: 2

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### Time Complexity Analysis

1. **Finding the middle index(es):**  
   - The `while` loop runs until `idx_one + idx_two` reaches `middle_idx`.  
   - In the worst case, this requires traversing up to `middle_idx` elements, where `middle_idx` is roughly `(n + m) / 2`
   (where `n` and `m` are the lengths of `array_one` and `array_two`, respectively).  
   - Thus, the loop runs in `O((n + m) / 2) = O(n + m)` time.

2. **Collecting the middle value(s):**  
   - In the odd case, we perform a constant-time check (`min` of two values or a direct access).  
   - In the even case, we collect two values in a fixed number of steps (2 iterations of a loop with constant-time operations).  
   - This part is `O(1)` in both cases.

**Overall Time Complexity:**  
The dominant part is the `while` loop, so the time complexity is `O(n + m)`.

---

### Space Complexity Analysis

The algorithm uses a constant amount of additional space:
- A few variables (`idx_one`, `idx_two`, `total_length`, `middle_idx`, `next_middle_idx`).  
- In the even case, a small list (`values`) of size 2 is used.  

No additional data structures (like arrays or hash maps) are used that grow with input size.

**Overall Space Complexity:**  
`O(1)` (constant space).

---

### Summary:
- **Time Complexity**: `O(n + m)`
- **Space Complexity**: `O(1)`

### Optimization Note

This is a straightforward merge-based approach. There exists a more efficient `O(log(min(n, m)))` solution using binary search,
but it is more complex to implement. The current approach is intuitive and works well for moderately sized inputs.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
The function `median_of_two_sorted_arrays` efficiently finds the **median** of two **sorted arrays** without merging them entirely,
by iterating through them just enough to find the median. It runs in **O(n)** time where `n` is the total number of elements needed
to reach the median.

---

### 🧠 Goal:

Find the median of two sorted arrays without merging them.

---

## 🧩 Median Refresher

* **Odd total elements:** The median is the middle element.
* **Even total elements:** The median is the average of the two middle elements.

---

### 📌 Function Breakdown:

```
def median_of_two_sorted_arrays(array_one, array_two):
```

This function takes two **sorted arrays** as inputs.

---

### 🔢 Initialize pointers and median positions

```
idx_one, idx_two = 0, 0
total_length = len(array_one) + len(array_two)
middle_idx = (total_length - 1) // 2
next_middle_idx = middle_idx + 1 if total_length % 2 == 0 else None
```

* `idx_one` and `idx_two` are iterators for both arrays.
* `middle_idx` gives the **index of the median** if the total length is **odd**, or the **first of the two medians** if even.
* `next_middle_idx` is set only for even total lengths.

---

### 🔄 Walk through arrays up to `middle_idx`

```
while idx_one + idx_two < middle_idx:
    if idx_one >= len(array_one):
        idx_two += 1
    elif idx_two >= len(array_two):
        idx_one += 1
    elif array_one[idx_one] < array_two[idx_two]:
        idx_one += 1
    else:
        idx_two += 1
```

This loop moves either `idx_one` or `idx_two` forward to reach the position `middle_idx`.

It simulates the **merging process of merge sort** without actually merging, by skipping elements that are guaranteed to be smaller.

---

### 🧮 Find the median

#### 🟢 If total length is odd:

```
if next_middle_idx is None:
    if idx_one >= len(array_one):
        return array_two[idx_two]
    if idx_two >= len(array_two):
        return array_one[idx_one]
    return min(array_one[idx_one], array_two[idx_two])
```

* Just return the **next smallest** unvisited element.

#### 🔵 If total length is even:

```
else:
    values = []
    for _ in range(2):
        if idx_one >= len(array_one):
            values.append(array_two[idx_two])
            idx_two += 1
        elif idx_two >= len(array_two):
            values.append(array_one[idx_one])
            idx_one += 1
        elif array_one[idx_one] < array_two[idx_two]:
            values.append(array_one[idx_one])
            idx_one += 1
        else:
            values.append(array_two[idx_two])
            idx_two += 1
    return sum(values) / 2
```

* Collect the **next two smallest** elements and return their average.

---

## ✅ Test Cases Breakdown

### 🧪 1. `median_of_two_sorted_arrays([1, 3, 4, 5], [2, 3, 6, 7])`

Combined sorted: `[1, 2, 3, 3, 4, 5, 6, 7]`

* Length = 8 (even) → median = average of 4th and 5th elements: `(3 + 4)/2 = 3.5`

✅ Output: `3.5`

---

### 🧪 2. `median_of_two_sorted_arrays([2, 2, 2, 2, 2], [3, 3, 3, 3])`

Combined: `[2, 2, 2, 2, 2, 3, 3, 3, 3]` → median = 2 (middle element)

✅ Output: `2`

---

## ✅ Summary

### Pros:

* Efficient: avoids merging.
* Linear time: `O(m + n)` in the worst case.
* Simple and readable logic.

---

Here's an **ASCII visualization** of how the function `median_of_two_sorted_arrays` works step-by-step using the **first test case**:

---

### 📘 Test Input:

```
array_one = [1, 3, 4, 5]
array_two = [2, 3, 6, 7]
```

### ✅ Combined Sorted (for reference):

```
[1, 2, 3, 3, 4, 5, 6, 7]
             ↑   ↑
          middle  next (even-length)
```

* Total length = 8 (even)
* Median = average of 4th and 5th elements: (3 + 4) / 2 = 3.5

---

### 🔁 Visualization of the while-loop (finding middle_idx = 3):

We simulate merging by picking the smallest of the two current elements.

```
Step | idx_one | idx_two | array_one[idx_one] | array_two[idx_two] | Pick
---------------------------------------------------------------------------
  1  |    0    |    0    |         1          |         2          |  1
  2  |    1    |    0    |         3          |         2          |  2
  3  |    1    |    1    |         3          |         3          |  3
```

✅ At this point, `idx_one + idx_two = 3`, which is the `middle_idx`.

---

### 🟡 We now need the next two elements:

We fetch two more elements using the same rules:

```
Advance to get median elements:
--------------------------------------------
  4  |    1    |    2    |         3          |         6          |  3
  5  |    2    |    2    |         4          |         6          |  4
```

### 📌 Final Values:

* Picked two elements: 3 and 4
* Median = (3 + 4) / 2 = **3.5**

---

### 📊 Summary Table:

```
Array One : [1, 3, 4, 5]
               ↑
Array Two : [2, 3, 6, 7]
                    ↑

Merged Order:
Step 1 → 1 (from array_one)
Step 2 → 2 (from array_two)
Step 3 → 3 (from array_one)
Step 4 → 3 (from array_two) ← median start
Step 5 → 4 (from array_one) ← median end
```

**Median: (3 + 4) / 2 = 3.5**

"""
