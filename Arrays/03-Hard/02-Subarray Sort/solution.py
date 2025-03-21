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
