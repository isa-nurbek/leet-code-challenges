# Problem Description:

"""
                                                Max Subset Sum No Adjacent

Write a function that takes in an array of `positive integers` and returns the `maximum sum of non-adjacent elements` in the array.

If the input array is empty, the function should return `0`.


## Sample Input:
```
array = [75, 105, 120, 75, 90, 135]
```

## Sample Output:
```
330

// 75 + 120 + 135
```

## Optimal Time & Space Complexity:
```
O(n) time | O(1) space - where `n` is the length of the input array.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n) time | O(1) space
def max_subset_sum_no_adjacent(array):
    """
    Calculate the maximum sum of a subset of non-adjacent elements in the array.

    Args:
    array: List of numbers to process

    Returns:
    Maximum sum of non-adjacent elements
    """

    # Handle edge cases
    if not len(array):
        return 0  # Empty array has sum 0
    elif len(array) == 1:
        return array[0]  # Only one element, so it's the max

    # Initialize variables to keep track of maximum sums:
    # second_prev represents max sum up to i-2
    # first_prev represents max sum up to i-1
    second_prev = array[0]  # Max sum for first element
    first_prev = max(array[0], array[1])  # Max sum for first two elements

    # Iterate through remaining elements starting from index 2
    for i in range(2, len(array)):
        # Current max is either:
        # 1. The max sum up to previous element (don't take current element)
        # 2. The max sum up to second previous element plus current element
        current = max(first_prev, second_prev + array[i])

        # Update the tracking variables for next iteration:
        # second_prev becomes the old first_prev
        # first_prev becomes the current max
        second_prev, first_prev = first_prev, current

    # After processing all elements, first_prev holds the maximum sum
    return first_prev


# Test Cases:

print(max_subset_sum_no_adjacent([75, 105, 120, 75, 90, 135]))
# Output: 330

print(max_subset_sum_no_adjacent([]))
# Output: 0

print(max_subset_sum_no_adjacent([30, 25, 50, 55, 100]))
# Output: 180

# =========================================================================================================================== #

# Big O Analysis:

"""
# Time and Space Complexity Analysis:

Let's analyze the time and space complexity of the given `max_subset_sum_no_adjacent` function.

### **Time Complexity**

The function iterates through the input array once, starting from index 2 to the end. For each element, it performs a
constant amount of work (comparisons and assignments). 

- **Number of iterations**: `n - 2` (where `n` is the length of the array).
- **Work per iteration**: O(1) (just a few comparisons and assignments).

Thus, the **time complexity is O(n)** (linear time).

### **Space Complexity**

The function uses a few extra variables (`second_prev`, `first_prev`, and `current`) to keep track of the maximum sums
at different positions. 

- **Extra space used**: O(1) (constant space, no additional data structures like arrays or hash tables are used).

Thus, the **space complexity is O(1)** (constant space).

### **Summary**
- **Time Complexity**: **O(n)**
- **Space Complexity**: **O(1)**

This is an optimal solution for the problem of finding the maximum subset sum with no adjacent elements, using
dynamic programming with constant space optimization.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
Let's go through the function `max_subset_sum_no_adjacent(array)` step by step and understand how it works.

---

### **Purpose of the Function**

This function finds the **maximum sum of non-adjacent numbers** in a list of integers. This means we cannot include two elements
that are next to each other in the array.

### **Problem Example**

Given:

```
[75, 105, 120, 75, 90, 135]
```

We must choose numbers **not adjacent to each other** that add up to the largest possible total.

Valid combinations:

* 75 + 120 + 135 = 330 ✅ (maximum)
* 75 + 120 + 90 = 285 ❌
* 105 + 75 + 135 = 315 ❌

---

### **Step-by-Step Explanation of the Code**

```
def max_subset_sum_no_adjacent(array):
    if not len(array):
        return 0
```

* If the array is empty, there is nothing to add, so return 0.

```
    elif len(array) == 1:
        return array[0]
```

* If the array has only one element, return that element (it's the only choice).

---

### **Initialization**

```
    second_prev = array[0]  # Max sum up to the first element
    first_prev = max(array[0], array[1])  # Max sum up to the second element
```

* We start tracking:

  * `second_prev`: the max sum up to the first element
  * `first_prev`: the max sum up to the second element (which could be just the second element, or still the first if it’s larger)

---

### **Dynamic Programming Loop**

```
    for i in range(2, len(array)):
        current = max(first_prev, second_prev + array[i])
        second_prev, first_prev = first_prev, current
```

* For each element from index 2 onwards:

  * We have two choices:

    1. **Exclude** current element → max sum is `first_prev`
    2. **Include** current element → we must **skip previous**, so add current element to `second_prev`
  * Take the **maximum of the two** and store in `current`.
  * Then shift values:

    * `second_prev` becomes old `first_prev`
    * `first_prev` becomes new `current`

---

### **Final Return**

```
    return first_prev
```

* `first_prev` holds the **maximum subset sum** at the end of the array.

---

### **Dry Run of Example**

Input:

```
[75, 105, 120, 75, 90, 135]
```

Step-by-step values:

* `second_prev = 75`
* `first_prev = max(75, 105) = 105`

Loop:

* i = 2 → `current = max(105, 75 + 120) = max(105, 195) = 195`
* i = 3 → `current = max(195, 105 + 75) = max(195, 180) = 195`
* i = 4 → `current = max(195, 195 + 90) = max(195, 285) = 285`
* i = 5 → `current = max(285, 195 + 135) = max(285, 330) = 330`

Return `330`

---

### ✅ Final Result

```
max_subset_sum_no_adjacent([75, 105, 120, 75, 90, 135]) = 330
```

---

Here's an **ASCII visualization** of how the algorithm progresses through the array `[75, 105, 120, 75, 90, 135]` step-by-step:

### Input Array (Indexed)

```
Index:     0     1     2     3     4     5
Value:    75   105   120    75    90   135
```

We are computing the **maximum sum of non-adjacent numbers** from this array.

---

### Initialization:

```
second_prev = 75           (from index 0)
first_prev  = 105          (max of index 0 and 1)
```

---

### Loop Iteration Breakdown:

#### i = 2 (value = 120)

```
Option 1: Exclude 120 → first_prev = 105
Option 2: Include 120 → second_prev + 120 = 75 + 120 = 195

Choose max(105, 195) = 195
Update: second_prev = 105, first_prev = 195
```

#### i = 3 (value = 75)

```
Option 1: Exclude 75  → first_prev = 195
Option 2: Include 75  → second_prev + 75 = 105 + 75 = 180

Choose max(195, 180) = 195
Update: second_prev = 195, first_prev = 195
```

#### i = 4 (value = 90)

```
Option 1: Exclude 90  → first_prev = 195
Option 2: Include 90  → second_prev + 90 = 195 + 90 = 285

Choose max(195, 285) = 285
Update: second_prev = 195, first_prev = 285
```

#### i = 5 (value = 135)

```
Option 1: Exclude 135 → first_prev = 285
Option 2: Include 135 → second_prev + 135 = 195 + 135 = 330

Choose max(285, 330) = 330
Update: second_prev = 285, first_prev = 330
```

---

### Final State:

```
Maximum subset sum with no adjacent elements = first_prev = 330
```

---

### Summary of Computation:

```
Index:         0     1     2     3     4     5
Value:        75   105   120    75    90   135
Choose:       ✓     ✗     ✓     ✗     ✗    ✓

Chosen values: 75 + 120 + 135 = 330 ✅
```

"""
