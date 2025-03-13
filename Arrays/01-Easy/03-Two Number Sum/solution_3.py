# Problem Description:

"""

                                                Two Number Sum

Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. If any two
numbers in the input array sum up to the target sum, the function should return them in an array, in any order. If no two
numbers sum up to the target sum, the function should return an empty array.

Note that the target sum has to be obtained by summing two different integers in the array; you can't add a single integer
to itself in order to obtain the target sum.

You can assume that there will be at most one pair of numbers summing up to the target sum.


## Sample Input:
```
array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10
```

## Sample Output:
```
[-1, 11] // the numbers could be in reverse order
```

## Optimal Time & Space Complexity:
```
O(n) time | O(n) space - where `n` is the length of the input array
```

"""

# =========================================================================================================================== #

# Solution:


# O(n log n) time | O(n) space
def two_number_sum(array, target_sum):
    # Step 1: Sort the array in ascending order.
    # This allows us to use the two-pointer technique to find the pair.
    array.sort()

    # Step 2: Initialize two pointers, one at the start (left) and one at the end (right) of the array.
    left = 0
    right = len(array) - 1

    # Step 3: Use a while loop to iterate until the two pointers meet.
    while left < right:
        # Step 4: Calculate the current sum of the elements at the left and right pointers.
        current_sum = array[left] + array[right]

        # Step 5: Check if the current sum equals the target sum.
        if current_sum == target_sum:
            # If it does, return the pair of numbers.
            return [array[left], array[right]]

        # Step 6: If the current sum is less than the target sum, move the left pointer to the right.
        # This increases the current sum because the array is sorted.
        elif current_sum < target_sum:
            left += 1

        # Step 7: If the current sum is greater than the target sum, move the right pointer to the left.
        # This decreases the current sum because the array is sorted.
        elif current_sum > target_sum:
            right -= 1

    # Step 8: If no pair is found that adds up to the target sum, return an empty list.
    return []


# Test Cases
print(two_number_sum([5, 1, 4, 7, 9], 10))  # Output: [1, 9]
print(two_number_sum([4, 6, 1, -3, 7], 3))  # Output: [6, -3]
print(two_number_sum([3, 5, -4, 8, 11, 1, -1, 6], 10))  # Output: [11, -1]
print(two_number_sum([7], 7))  # Output: []

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### Time Complexity:

1. **Sorting the array**: The sorting step dominates the time complexity. Sorting an array of `n` elements typically
takes O(n log n) time.

2. **Two-pointer traversal**: After sorting, the two-pointer approach traverses the array once, which takes O(n) time.

Therefore, the overall time complexity is: O(n log n) + O(n) = O(n log n)


### Space Complexity:

1. **Sorting**: The space complexity of the sorting algorithm depends on the implementation. For example,
Python's `sort()` method uses Timsort, which has a space complexity of O(n) in the worst case.

2. **Two-pointer traversal**: The two-pointer approach uses a constant amount of extra space, O(1).

Therefore, the overall space complexity is: O(n)

### Summary:
- **Time Complexity**: O(n log n)
- **Space Complexity**: O(n)

This makes the algorithm efficient for finding two numbers that sum to a target value, especially when the array is not too large.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""

The `two_number_sum` function is designed to find two numbers in an array that add up to a given `target_sum`.
It uses a two-pointer technique to achieve an efficient **O(n log(n))** time complexity and **O(1)** space complexity.
Here's a step-by-step breakdown of how it works:

---

### 1. **Input Parameters**
- **array**: A list of integers.
- **target_sum**: The desired sum of two numbers.

Example:
- Input array: `[5, 1, 4, 7, 9]`
- Target sum: `10`

---

### 2. **Sorting the Array**
```
array.sort()
```
The array is sorted in ascending order to enable the two-pointer technique. Sorting takes O(n log(n)) time.

Example:
- Original array: `[5, 1, 4, 7, 9]`
- Sorted array: `[1, 4, 5, 7, 9]`

---

### 3. **Initializing Two Pointers**
```
left = 0
right = len(array) - 1
```
- **`left` pointer**: Starts at the smallest element (index 0).
- **`right` pointer**: Starts at the largest element (last index).

For the sorted array `[1, 4, 5, 7, 9]`:
- `left` = `0` (value: `1`)
- `right` = `4` (value: `9`)

---

### 4. **Iterative Process (While Loop)**
```
while left < right:
```
The loop continues until the two pointers meet. This ensures every pair of numbers is checked without repetition.

---

### 5. **Calculate Current Sum**
```
current_sum = array[left] + array[right]
```
- Adds the elements pointed to by `left` and `right`.
- Compares `current_sum` with `target_sum`.

---

### 6. **Check Conditions**
```
if current_sum == target_sum:
    return [array[left], array[right]]
```
- If the sum matches `target_sum`, the function returns the pair.

```
elif current_sum < target_sum:
    left += 1
```
- If the sum is smaller, increment `left` to increase the sum.

```
elif current_sum > target_sum:
    right -= 1
```
- If the sum is larger, decrement `right` to decrease the sum.

---

### 7. **Return Statement**
If no pair is found after the loop ends, return an empty list:
```
return []
```

---

### Examples Walkthrough

#### **Example 1**
```
print(two_number_sum([5, 1, 4, 7, 9], 10))
```
1. Sorted array: `[1, 4, 5, 7, 9]`
2. Initial pointers: `left = 0` (1), `right = 4` (9).
3. Iteration:
   - **Current sum**: `1 + 9 = 10`. Match found!
4. Output: `[1, 9]`.

---

#### **Example 2**
```
print(two_number_sum([4, 6, 1, -3, 7], 3))
```
1. Sorted array: `[-3, 1, 4, 6, 7]`
2. Initial pointers: `left = 0` (-3), `right = 4` (7).
3. Iteration:
   - **Current sum**: `-3 + 7 = 4`. Too large; move `right`.
   - **Current sum**: `-3 + 6 = 3`. Match found!
4. Output: `[6, -3]`.

---

#### **Example 3**
```
print(two_number_sum([3, 5, -4, 8, 11, 1, -1, 6], 10))
```
1. Sorted array: `[-4, -1, 1, 3, 5, 6, 8, 11]`
2. Iteration:
   - Check pairs: `[-4, 11]`, `[-1, 11]`, `[1, 11]`, `[3, 11]`.
   - Match found: `11 + (-1) = 10`.
3. Output: `[11, -1]`.

---

#### **Example 4**
```
print(two_number_sum([7], 7))
```
1. Sorted array: `[7]`.
2. Loop does not start because `left` is not less than `right`.
3. Output: `[]` (no pair exists).

---

### Key Points

1. **Two-Pointer Technique**:
   - Efficient for sorted arrays.
   - Adjusts pointers based on comparison with `target_sum`.

2. **Edge Cases**:
   - Single element: No pair exists.
   - Empty array: Returns an empty list.
   - Multiple valid pairs: Returns the first found.

"""
