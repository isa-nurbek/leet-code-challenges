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
