# Problem Description:

"""

                                                # Subarray Sort

Write a function that takes in an array of at least two integers and that returns an array of the starting and ending indices
of the smallest subarray in the input array that needs to be sorted in place in order for the entire input array to be sorted
(in ascending order).

If the input array is already sorted, the function should return `[-1, -1]`.


## Sample Input:
```
array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
```

## Sample Output:
```
[3, 9]
```

## Optimal Time & Space Complexity:
```
O(n) time | O(1) space - where `n` is the length of the input array.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n) time | O(1) space
def subarray_sort(array):
    # Initialize variables to track the minimum and maximum values that are out of order
    min_out_of_order = float("inf")
    max_out_of_order = float("-inf")

    # Iterate through the array to find the smallest and largest elements that are out of order
    for i in range(len(array)):
        num = array[i]

        # Check if the current element is out of order
        if is_out_of_order(i, num, array):
            # Update the minimum and maximum out-of-order elements
            min_out_of_order = min(min_out_of_order, num)
            max_out_of_order = max(max_out_of_order, num)

    # If no elements are out of order, return [-1, -1]
    if min_out_of_order == float("inf"):
        return [-1, -1]

    # Find the left index of the subarray that needs to be sorted
    subarray_left_idx = 0

    while min_out_of_order >= array[subarray_left_idx]:
        subarray_left_idx += 1

    # Find the right index of the subarray that needs to be sorted
    subarray_right_idx = len(array) - 1

    while max_out_of_order <= array[subarray_right_idx]:
        subarray_right_idx -= 1

    # Return the indices of the subarray that needs to be sorted
    return [subarray_left_idx, subarray_right_idx]


def is_out_of_order(i, num, array):
    # Check if the current element is out of order based on its position in the array

    # If it's the first element, it's out of order if it's greater than the next element
    if i == 0:
        return num > array[i + 1]

    # If it's the last element, it's out of order if it's smaller than the previous element
    if i == len(array) - 1:
        return num < array[i - 1]

    # For elements in the middle, it's out of order if it's greater than the next element
    # or smaller than the previous element
    return num > array[i + 1] or num < array[i - 1]


# Test Cases:

print(subarray_sort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]))
# Output: [3, 9]

print(subarray_sort([-41, 8, 7, 12, 11, 9, -1, 3, 9, 16, -15, 11, 57]))
# Output: [1, 11]

print(subarray_sort([1, 2]))
# Output: [-1, -1]

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### Time Complexity Analysis

The time complexity of the `subarray_sort` function can be broken down as follows:

1. **First Loop (Finding `min_out_of_order` and `max_out_of_order`):**
   - The loop iterates over the entire array once, which takes O(n) time, where `n` is the length of the array.
   - Inside the loop, the `is_out_of_order` function is called, which performs constant-time operations (comparisons).
   Thus, the `is_out_of_order` function runs in O(1) time.
   
   - Therefore, the first loop runs in O(n) * O(1) = O(n)\) time.

2. **Finding `subarray_left_idx`:**
   - This loop iterates from the start of the array until it finds the correct position for `min_out_of_order`.
   In the worst case, this could take O(n) time.

3. **Finding `subarray_right_idx`:**
   - This loop iterates from the end of the array until it finds the correct position for `max_out_of_order`.
   In the worst case, this could also take O(n) time.

4. **Overall Time Complexity:**
   - The total time complexity is the sum of the time complexities of the three steps: O(n) + O(n) + O(n) = O(n).

---

### Space Complexity Analysis

The space complexity of the `subarray_sort` function is determined by the additional space used by the algorithm:

1. **Variables:**
   - The algorithm uses a few variables (`min_out_of_order`, `max_out_of_order`, `subarray_left_idx`, `subarray_right_idx`),
   which take constant space O(1).

2. **No Additional Data Structures:**
   - The algorithm does not use any additional data structures that grow with the input size.

3. **Overall Space Complexity:**
   - The space complexity is O(1), as the algorithm uses only a constant amount of extra space regardless of the input size.

### Summary

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

This makes the algorithm efficient for large inputs, as it processes the array in linear time and uses minimal extra space.

"""

# =========================================================================================================================== #
