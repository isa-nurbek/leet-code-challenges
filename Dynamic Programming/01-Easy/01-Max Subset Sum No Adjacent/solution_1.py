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


# O(n) time | O(n) space
def max_subset_sum_no_adjacent(array):
    # Handle edge cases:
    # If array is empty, maximum sum is 0
    if not len(array):
        return 0
    # If array has only one element, that's the maximum sum
    elif len(array) == 1:
        return array[0]

    # Create a copy of the array to store maximum sums at each position
    max_sums = array[:]

    # For the second element, the maximum sum is either:
    # - the first element (if we skip this one), or
    # - the second element itself (if we take it and skip the first)
    max_sums[1] = max(array[0], array[1])

    # Iterate through the rest of the array starting from index 2
    for i in range(2, len(array)):
        # At each position, the maximum sum is either:
        # 1. The maximum sum up to the previous position (we don't take current element)
        # OR
        # 2. The maximum sum up to two positions back plus current element (we take current)
        max_sums[i] = max(max_sums[i - 1], max_sums[i - 2] + array[i])

    # The last element in max_sums contains the maximum sum for the entire array
    return max_sums[-1]


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

### **Time Complexity:**

1. **Initial Checks:**
   - The first two conditions (checking for empty array or single-element array) are O(1) operations.
   
2. **Initialization:**
   - Creating the `max_sums` array as a copy of the input array takes O(n) time, where n is the length of the input array.

3. **Loop:**
   - The loop runs from `i = 2` to `i = len(array) - 1`, which is O(n) iterations.
   - Inside the loop, each iteration involves a constant-time operation (a `max` comparison and an addition).

Thus, the **total time complexity is O(n)**.

---

### **Space Complexity:**

1. **Auxiliary Array (`max_sums`):**
   - The `max_sums` array is created with the same size as the input array, so it takes O(n) space.

2. **Other Variables:**
   - The rest of the variables (`i` in the loop) use constant space (O(1)).

Thus, the **total space complexity is O(n)**.

---

### Final Complexity Analysis:

| Time Complexity | Space Complexity  |
|-----------------|-------------------|
| O(n)            | O(n)              |

---

### Optimization Note:

The space complexity can be optimized to **O(1)** by realizing that we only need to keep track of the last two values
(`max_sums[i-1]` and `max_sums[i-2]`) at any point in the iteration, instead of storing the entire `max_sums` array.

The given solution is already optimal in terms of time, but space can be improved further.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
This function `max_subset_sum_no_adjacent` solves a classic **dynamic programming** problem.
Its goal is to **find the maximum sum of a subset of non-adjacent elements** in an input array.

---

## 🧠 Problem Explanation

You are given a list of **positive integers**, and you **cannot pick adjacent numbers** (i.e., if you pick index `i`,
you can't pick `i-1` or `i+1`).

### Example:

Given: `[75, 105, 120, 75, 90, 135]`

Valid picks (non-adjacent):

* Pick `75 (0) + 120 (2) + 135 (5)` → Total: `330`
* Pick `105 (1) + 75 (3) + 135 (5)` → Total: `315`

---

## 🧩 Code Breakdown

```
def max_subset_sum_no_adjacent(array):
```

Defines a function that takes a list of numbers.

### Base Cases:

```
    if not len(array):
        return 0
```

If the array is empty, return 0.

```
    elif len(array) == 1:
        return array[0]
```

If the array has one element, return that single element.

---

### Initialization:

```
    max_sums = array[:]
```

Creates a copy of the original array (to hold our DP results).

```
    max_sums[1] = max(array[0], array[1])
```

The best sum we can get from the first two elements is just the **maximum** of them (since they are adjacent, you can't pick both).

---

### Dynamic Programming Loop:

```
    for i in range(2, len(array)):
        max_sums[i] = max(max_sums[i - 1], max_sums[i - 2] + array[i])
```

At each index `i`, you have two choices:

1. **Don't pick current element** → use the best sum until index `i-1`
2. **Pick current element** → add it to best sum from index `i-2`

Take the **maximum** of the two choices.

---

### Final Result:

```
    return max_sums[-1]
```

The last value in `max_sums` holds the **maximum sum with no adjacent elements**.

---

## 🧪 Test Cases Explained:

### 1. `[75, 105, 120, 75, 90, 135]`

DP Table evolution:

```
Index:     0    1     2     3     4     5
Array:    75  105   120    75    90   135
max_sums: 75  105   195   180   285   330
```

Return: `330`

---

### 2. `[]`

Empty array → Return `0`

---

### 3. `[30, 25, 50, 55, 100]`

DP Table:

```
max_sums: 30  30  80  85  180
```

Return: `180` (30 + 50 + 100)

---

## ✅ Summary

* This is a bottom-up **dynamic programming** approach.
* It keeps track of the best possible sum at each step **without including adjacent elements**.
* Time complexity: **O(n)**.
* Space complexity: **O(n)** (can be reduced to O(1) with optimization).

---

Here's an **ASCII visualization** of how the function works on the input:

```
array = [75, 105, 120, 75, 90, 135]
```

---

### 🧮 Step-by-step DP Table Update

```
Index:       0     1     2     3     4     5
Value:      75   105   120    75    90   135

Step 0: Initialize first element
max_sums[0] = 75

Step 1: Pick max of first two
max_sums[1] = max(75, 105) = 105

Step 2:
max_sums[2] = max(105, 75 + 120) = max(105, 195) = 195

Step 3:
max_sums[3] = max(195, 105 + 75) = max(195, 180) = 195

Step 4:
max_sums[4] = max(195, 195 + 90) = max(195, 285) = 285

Step 5:
max_sums[5] = max(285, 195 + 135) = max(285, 330) = 330
```

---

### 📊 Final DP Table

```
         +-----+-----+-----+-----+-----+-----+
Index:   |  0  |  1  |  2  |  3  |  4  |  5  |
         +-----+-----+-----+-----+-----+-----+
Value:   |  75 | 105 | 120 |  75 |  90 | 135 |
         +-----+-----+-----+-----+-----+-----+
max_sum: |  75 | 105 | 195 | 195 | 285 | 330 |
         +-----+-----+-----+-----+-----+-----+
```

✅ **Final Answer: 330**

(Chosen path: `75 (0)` + `120 (2)` + `135 (5)`)

"""
