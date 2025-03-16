# Problem Description:

"""

                                         # First Duplicate Value

Given an array of integers between `1` and `n`, inclusive, where `n` is the length of the array, write a function that
returns the first integer that appears more than once (when the array is read from left to right).

In other words, out of all the integers that might occur more than once in the input array, your function should return
the one whose first duplicate value has the minimum index.

If no integer appears more than once, your function should return `-1`.

Note that you're allowed to mutate the input array.


## Sample Input 1:
```
array = [2, 1, 5, 2, 3, 3, 4]
```

## Sample Output 2:
```
2 // 2 is the first integer that appears more than once.
// 3 also appears more than once, but the second 3 appears after the second 2.
```

## Sample Input 3:
```
array = [2, 1, 5, 3, 3, 2, 4]
```

## Sample Output 3:
```
3 // 3 is the first integer that appears more than once.
// 2 also appears more than once, but the second 2 appears after the second 3.
```

## Optimal Time & Space Complexity:
```
O(n) time | O(1) space - where `n` is the length of the input array.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n) time | O(1) space - where `n` is the length of the input array.
def first_duplicate_value(array):
    # Iterate through each value in the array
    for value in array:
        # Take the absolute value of the current element
        # This is because we might have marked the value as negative in previous steps
        abs_value = abs(value)

        # Check if the value at the index (abs_value - 1) is negative
        # If it is negative, it means we have seen this value before (i.e., it's a duplicate)
        if array[abs_value - 1] < 0:
            # Return the duplicate value
            return abs_value

        # If the value at the index (abs_value - 1) is not negative,
        # mark it as negative to indicate that we have seen this value
        array[abs_value - 1] *= -1

    # If no duplicates are found, return -1
    return -1


# Test Cases:

print(first_duplicate_value([2, 1, 5, 2, 3, 3, 4]))
# Output: 2

print(first_duplicate_value([2, 1, 5, 3, 3, 2, 4]))
# Output: 3

print(first_duplicate_value([6, 6, 5, 1, 3, 7, 7, 8]))
# Output: 6

print(first_duplicate_value([1]))
# Output: -1

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### Time Complexity Analysis

The time complexity of the `first_duplicate_value` function is **O(n)**, where `n` is the length of the input array.

Here's why:

1. **Loop through the array**: The function iterates through each element in the array exactly once. This is a single pass,
so it takes **O(n)** time.

2. **Operations inside the loop**:
   - Calculating the absolute value (`abs(value)`) is a constant-time operation, **O(1)**.
   - Accessing and updating the array at a specific index (`array[abs_value - 1]`) is also **O(1)**.
   - The condition check (`if array[abs_value - 1] < 0`) is **O(1)**.

Since all operations inside the loop are constant time, the overall time complexity remains **O(n)**.

---

### Space Complexity Analysis

The space complexity of the function is **O(1)**, meaning it uses constant extra space.

Here's why:

1. **No additional data structures**: The function does not use any extra data structures (like hash tables or sets)
that grow with the input size.

2. **In-place modification**: The function modifies the input array in place by marking visited indices with negative values.
This does not require additional space proportional to the input size.

Thus, the space complexity is **O(1)**.

---

### Summary

- **Time Complexity**: **O(n)** (linear time).
- **Space Complexity**: **O(1)** (constant space).

"""

# =========================================================================================================================== #
