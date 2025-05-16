# Problem Description:

"""
                                             Index Equals Value

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


# O(log(min(n, m))) time | O(1) space
def median_of_two_sorted_arrays(array_one, array_two):
    # Ensure array_one is the smaller array to reduce binary search range
    if len(array_one) > len(array_two):
        array_one, array_two = array_two, array_one

    n, m = len(array_one), len(array_two)
    total = n + m
    half = (total + 1) // 2  # This works for both even and odd total lengths

    # Initialize binary search bounds for the smaller array
    left, right = 0, n

    while left <= right:
        # Partition position in array_one
        mid = (left + right) // 2
        # Corresponding partition position in array_two
        remaining = half - mid

        # Handle edge cases where partition might be at the beginning or end
        # of either array by using +/- infinity as appropriate
        max_left_one = float("-inf") if mid == 0 else array_one[mid - 1]
        min_right_one = float("inf") if mid == n else array_one[mid]
        max_left_two = float("-inf") if remaining == 0 else array_two[remaining - 1]
        min_right_two = float("inf") if remaining == m else array_two[remaining]

        # Check if we've found the correct partition
        if max_left_one <= min_right_two and max_left_two <= min_right_one:
            # If total length is odd, median is the max of left partitions
            if total % 2 == 1:
                return max(max_left_one, max_left_two)
            else:
                # If even, median is average of max left and min right partitions
                return (
                    max(max_left_one, max_left_two) + min(min_right_one, min_right_two)
                ) / 2
        # If array_one's left partition is too big, move partition left
        elif max_left_one > min_right_two:
            right = mid - 1
        # Otherwise, move partition right
        else:
            left = mid + 1

    # This should theoretically never be reached with valid sorted input
    raise ValueError("Input arrays are not sorted or invalid.")


# Test Cases:

print(median_of_two_sorted_arrays([1, 3, 4, 5], [2, 3, 6, 7]))
# Output: 3.5

print(median_of_two_sorted_arrays([2, 2, 2, 2, 2], [3, 3, 3, 3]))
# Output: 2

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### Time Complexity Analysis:

The algorithm performs a binary search on the smaller of the two arrays (`array_one`). In each iteration of the binary search,
it checks a partition of `array_one` and computes the corresponding partition in `array_two` to determine if the correct partition
for the median has been found. 

1. **Binary Search**: The binary search runs on the smaller array of size `n`, so it performs `O(log n)` iterations.
2. **Work per Iteration**: In each iteration, the algorithm performs a constant number of operations (accessing elements,
comparisons, and arithmetic operations). No loops or recursive calls are present within the binary search loop.
   
Thus, the **time complexity is `O(log(min(n, m)))`**, where `n` and `m` are the lengths of the two input arrays. This is because
the binary search is performed on the smaller array, and the larger array's partition is derived in constant time.

---

### Space Complexity Analysis:

The algorithm uses a constant amount of additional space, regardless of the input sizes. It only stores a few variables (`left`,
`right`, `mid`, `remaining`, `max_left_one`, `min_right_one`, `max_left_two`, `min_right_two`, etc.), and no additional data
structures or recursive calls are involved.

Thus, the **space complexity is `O(1)`**.

---

### Summary:
- **Time Complexity**: `O(log(min(n, m)))`  
- **Space Complexity**: `O(1)`  

This is an optimal solution for finding the median of two sorted arrays, as it efficiently narrows down the search space using
binary search without requiring extra memory.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
This function efficiently computes the **median of two sorted arrays** using a **binary search** technique with a time complexity
of **O(log(min(n, m)))**, where `n` and `m` are the lengths of the two input arrays.

---

## ✅ Problem:

Given two sorted arrays, `array_one` and `array_two`, find the **median** of the combined data **without fully merging** the arrays.

---

## ✅ High-Level Idea:

We simulate the **partitioning** of the two arrays such that:

* The left half of the partition contains the **first half** of the merged array elements.
* The right half contains the **remaining** elements.
* The **maximum** of the left part and **minimum** of the right part can be used to compute the median.

---

## ✅ Step-by-Step Explanation:

### Step 1: Ensure `array_one` is the shorter array

```
if len(array_one) > len(array_two):
    array_one, array_two = array_two, array_one
```

* Binary search is applied on the **shorter array** for efficiency.
* This guarantees `n <= m`.

---

### Step 2: Initial setup

```
n, m = len(array_one), len(array_two)
total = n + m
half = (total + 1) // 2
```

* `total` is the total number of elements.
* `half` is the number of elements we want on the **left partition**.

  * The `+1` ensures correct median calculation in **odd-length** combined arrays.

---

### Step 3: Binary search on `array_one`

```
left, right = 0, n
while left <= right:
    mid = (left + right) // 2
    remaining = half - mid
```

* `mid` is the number of elements we choose from `array_one` in the left partition.
* `remaining` is how many we must take from `array_two` to reach `half`.

---

### Step 4: Define partition values

```
max_left_one = float("-inf") if mid == 0 else array_one[mid - 1]
min_right_one = float("inf") if mid == n else array_one[mid]

max_left_two = float("-inf") if remaining == 0 else array_two[remaining - 1]
min_right_two = float("inf") if remaining == m else array_two[remaining]
```

* We simulate a partition:

  * Left part contains: `array_one[:mid] + array_two[:remaining]`
  * Right part contains: `array_one[mid:] + array_two[remaining:]`
* `max_left_*` = largest value on the left of the partition.
* `min_right_*` = smallest value on the right of the partition.
* Use `-inf` and `inf` to handle edge cases (empty partitions).

---

### Step 5: Check partition correctness

```
if max_left_one <= min_right_two and max_left_two <= min_right_one:
```

* This checks if we have **correctly partitioned** the arrays such that:

  * Every value on the left is less than or equal to every value on the right.

---

### Step 6: Compute median

```
if total % 2 == 1:
    return max(max_left_one, max_left_two)
else:
    return (max(max_left_one, max_left_two) + min(min_right_one, min_right_two)) / 2
```

* **Odd total length**: Median is the **max of the left half**.
* **Even total length**: Median is the **average of the middle two**:

  * `max of left half` and `min of right half`.

---

### Step 7: Adjust search space

```
elif max_left_one > min_right_two:
    right = mid - 1
else:
    left = mid + 1
```

* If left part of `array_one` is too large, move left.
* If too small, move right.

---

### Step 8: Error Handling

```
raise ValueError("Input arrays are not sorted or invalid.")
```

* This shouldn't trigger if inputs are valid and sorted.

---

## ✅ Test Case Walkthrough

### Example:

```
median_of_two_sorted_arrays([1, 3, 4, 5], [2, 3, 6, 7])
```

* Combined: [1, 2, 3, 3, 4, 5, 6, 7]
* Median = (3 + 4) / 2 = **3.5**

---

## ✅ Time and Space Complexity

* **Time:** `O(log(min(n, m)))` due to binary search.
* **Space:** `O(1)` – no extra space used apart from variables.

---

Here's an **ASCII visualization** of the core partitioning idea behind the binary search to find the median of two sorted arrays.

Suppose the two arrays are:

```
array_one = [1, 3, 4, 5]
array_two = [2, 3, 6, 7]
```

We want to partition these two arrays into two halves:

* Left half contains `half = (n + m + 1) // 2 = (4 + 4 + 1) // 2 = 4` elements.
* Right half contains the rest.

---

### Step 1: Visualize the arrays before partition

```
array_one:  1    3    4    5
index:      0    1    2    3

array_two:  2    3    6    7
index:      0    1    2    3
```

---

### Step 2: Assume a partition in `array_one` at `mid = 2` (take first 2 elements on the left):

```
Left partition (array_one):  [1, 3]  | Right partition (array_one):  [4, 5]
                          mid=2                                mid=2

Remaining elements needed from array_two to reach half = 4 - 2 = 2

Left partition (array_two):  [2, 3]  | Right partition (array_two):  [6, 7]
                           remaining=2                                remaining=2
```

---

### Step 3: Visualize the merged partitions

```
Left partition combined:  [1, 3] + [2, 3] = [1, 3, 2, 3] (unsorted, but partitioned)
Right partition combined: [4, 5] + [6, 7] = [4, 5, 6, 7]
```

We are trying to verify if:

* max_left_one <= min_right_two
  i.e. 3 <= 6 ✔️

* max_left_two <= min_right_one
  i.e. 3 <= 4 ✔️

Since both conditions are true, partition is valid.

---

### Step 4: Median calculation for even total length

* max_left = max(3, 3) = 3
* min_right = min(4, 6) = 4

Median = (3 + 4) / 2 = 3.5

---

### Summary:

```
array_one:  [1, 3] | [4, 5]
array_two:  [2, 3] | [6, 7]

max_left_one = 3
min_right_one = 4

max_left_two = 3
min_right_two = 6

Conditions hold:

max_left_one <= min_right_two (3 <= 6)
max_left_two <= min_right_one (3 <= 4)

Median = (max(max_left_one, max_left_two) + min(min_right_one, min_right_two)) / 2
       = (3 + 4) / 2 = 3.5
```

---

### If the partition was incorrect (e.g., max_left_one > min_right_two), the binary search adjusts to find a better partition.

---

Let’s do a **step-by-step walkthrough** of how the binary search moves the pointers (`left`, `right`) to find the correct
partition for the arrays:

```
array_one = [1, 3, 4, 5]
array_two = [2, 3, 6, 7]
```

---

### Initial setup:

* `n = 4`, `m = 4`
* `total = 8`
* `half = (8 + 1) // 2 = 4`
* Search space on `array_one` indices: `left = 0`, `right = 4`

---

### Iteration 1:

* `mid = (0 + 4) // 2 = 2`
* `remaining = half - mid = 4 - 2 = 2`

Partitions:

```
array_one left = [1, 3]
array_one right = [4, 5]

array_two left = [2, 3]
array_two right = [6, 7]
```

Values:

* `max_left_one = array_one[1] = 3`
* `min_right_one = array_one[2] = 4`
* `max_left_two = array_two[1] = 3`
* `min_right_two = array_two[2] = 6`

Check conditions:

* `max_left_one <= min_right_two` → `3 <= 6` ✔️
* `max_left_two <= min_right_one` → `3 <= 4` ✔️

Partition is **valid** → We found the median!

---

### If it wasn’t valid, say:

If `max_left_one > min_right_two`, e.g., `max_left_one = 7`, `min_right_two = 6`, then:

* `right = mid - 1` → we reduce the search space because we took too many elements from `array_one`.
* Move left pointer **left** in `array_one`.

If `max_left_two > min_right_one`, then:

* `left = mid + 1` → we need more elements from `array_one`.
* Move right pointer **right** in `array_one`.

---

### Let's simulate a case where the first partition guess fails

Imagine:

* Initial `left = 0`, `right = 4`

Try `mid = 2` — partition is good (from above).

Try `mid = 3` (for illustration):

* `mid = 3`
* `remaining = 4 - 3 = 1`

Partitions:

```
array_one left = [1, 3, 4]
array_one right = [5]

array_two left = [2]
array_two right = [3, 6, 7]
```

Values:

* `max_left_one = 4`
* `min_right_one = 5`
* `max_left_two = 2`
* `min_right_two = 3`

Check conditions:

* `max_left_one <= min_right_two` → `4 <= 3` ✘ (False)
* `max_left_two <= min_right_one` → `2 <= 5` ✔️

Since `max_left_one > min_right_two`, we reduce right:

* `right = mid - 1 = 2`

---

### Next iteration:

* `left = 0`, `right = 2`
* `mid = 1`
* `remaining = 4 - 1 = 3`

Partitions:

```
array_one left = [1]
array_one right = [3, 4, 5]

array_two left = [2, 3, 6]
array_two right = [7]
```

Values:

* `max_left_one = 1`
* `min_right_one = 3`
* `max_left_two = 6`
* `min_right_two = 7`

Check conditions:

* `max_left_one <= min_right_two` → `1 <= 7` ✔️
* `max_left_two <= min_right_one` → `6 <= 3` ✘ (False)

Since `max_left_two > min_right_one`, move left up:

* `left = mid + 1 = 2`

---

### Final iteration:

* `left = 2`, `right = 2`
* `mid = 2`
* `remaining = 4 - 2 = 2`

Back to the partition in **Iteration 1** — correct partition.

---

### Summary of pointer moves:

```
left=0, right=4 → mid=2 → valid → median found
mid=3 (too far right) → right moves to 2
mid=1 (too far left) → left moves to 2
mid=2 → correct partition
```

"""
