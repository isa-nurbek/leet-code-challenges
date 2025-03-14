# Problem Description:

"""

                                        # Monotonic Array

Write a function that takes in an array of integers and returns a boolean representing whether the array is monotonic.

An array is said to be monotonic if its elements, from left to right, are entirely non-increasing or entirely non-decreasing.

Non-increasing elements aren't necessarily exclusively decreasing; they simply don't increase. Similarly, non-decreasing
elements aren't necessarily exclusively increasing; they simply don't decrease.

Note that empty arrays and arrays of one element are monotonic.


## Sample Input:
```
array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
```

## Sample Output:
```
True
```

## Optimal Time & Space Complexity:
```
O(n) time | O(1) space - where `n` is the length of the array.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n) time | O(1) space - where `n` is the length of the array
def is_monotonic(array):
    # Initialize two flags to track the array's monotonicity
    is_non_decreasing = True  # Assumes the array is non-decreasing initially
    is_non_increasing = True  # Assumes the array is non-increasing initially

    # Iterate through the array starting from the second element
    for i in range(1, len(array)):
        # Check if the current element is less than the previous element
        if array[i] < array[i - 1]:
            # If true, the array is not non-decreasing
            is_non_decreasing = False

        # Check if the current element is greater than the previous element
        if array[i] > array[i - 1]:
            # If true, the array is not non-increasing
            is_non_increasing = False

    # The array is monotonic if it is either non-decreasing or non-increasing
    return is_non_decreasing or is_non_increasing


# Test cases:

print(is_monotonic([-1, -5, -10, -1100, -1100, -1101, -1102, -9001]))
# Output: True

print(is_monotonic([2, 2, 2, 1, 4, 5]))
# Output: False

print(is_monotonic([]))
# Output: True

print(is_monotonic([7]))
# Output: True

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### Time Complexity:

- The function iterates through the array once, comparing each element with the previous one.
- This results in a single pass over the array, so the time complexity is **O(n)**, where `n` is the length of the array.

### Space Complexity:

- The function uses a constant amount of extra space (two boolean variables, `is_non_decreasing` and `is_non_increasing`).
- No additional space is used that scales with the input size, so the space complexity is **O(1)**.

---

### Summary:
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
### Explanation of the `is_monotonic` function

The function `is_monotonic(array)` checks whether a given list of numbers is **monotonic**. A sequence is 
considered **monotonic** if it is entirely **non-decreasing** or **non-increasing**.

### Step-by-Step Breakdown

#### 1. **Initialize Flags**
```
is_non_decreasing = True
is_non_increasing = True
```
- `is_non_decreasing`: Assumes that the array is increasing or remains constant.
- `is_non_increasing`: Assumes that the array is decreasing or remains constant.

#### 2. **Iterate Through the Array**
```
for i in range(1, len(array)):
```
- The loop starts from index `1` and iterates through the array, comparing each element with its previous element.

#### 3. **Check for Violations**
```
if array[i] < array[i - 1]:
    is_non_decreasing = False
```
- If the current element is **less than** the previous one, the array is **not non-decreasing**, so `is_non_decreasing`
is set to `False`.

```
if array[i] > array[i - 1]:
    is_non_increasing = False
```
- If the current element is **greater than** the previous one, the array is **not non-increasing**, so `is_non_increasing`
is set to `False`.

#### 4. **Return the Result**
```
return is_non_decreasing or is_non_increasing
```
- If either `is_non_decreasing` or `is_non_increasing` remains `True`, the array is monotonic.

---

### Example Walkthroughs

#### 1. **Example: `[-1, -5, -10, -1100, -1100, -1101, -1102, -9001]`**
```
is_monotonic([-1, -5, -10, -1100, -1100, -1101, -1102, -9001])
```
- The values are either decreasing or staying the same.
- `is_non_decreasing` will become `False` because elements are decreasing.
- `is_non_increasing` remains `True`, so the function returns `True`.

#### 2. **Example: `[2, 2, 2, 1, 4, 5]`**
```
is_monotonic([2, 2, 2, 1, 4, 5])
```
- The array **decreases** from `2 → 1` and then **increases** from `1 → 4 → 5`.
- This breaks both monotonic conditions, so the function returns `False`.

#### 3. **Example: `[]` (Empty Array)**
```
is_monotonic([])
```
- An empty list is trivially monotonic.
- The loop does not execute, and both flags remain `True`, so the function returns `True`.

#### 4. **Example: `[7]` (Single Element)**
```
is_monotonic([7])
```
- A single-element list is always monotonic.
- The loop does not execute, and both flags remain `True`, so the function returns `True`.

This implementation is efficient and easy to understand for checking monotonicity. 

"""
