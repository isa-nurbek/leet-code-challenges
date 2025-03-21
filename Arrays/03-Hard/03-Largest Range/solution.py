# Problem Description:

"""

                                                # Largest Range

Write a function that takes in an array of integers and returns an array of length 2 representing the largest range of integers
contained in that array.

The first number in the output array should be the first number in the range, while the second number should be the last number
in the range.

A range of numbers is defined as a set of numbers that come right after each other in the set of real integers. For instance,
the output array `[2, 6]` represents the range `{2, 3, 4, 5, 6}`, which is a range of length 5. Note that numbers don't need
to be sorted or adjacent in the input array in order to form a range.

You can assume that there will only be one largest range.


## Sample Input:
```
array = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
```

## Sample Output:
```
[0, 7]
```

## Optimal Time & Space Complexity:
```
O(n) time | O(n) space - where `n` is the length of the input array.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n) time | O(n) space
def largest_range(array):
    # Initialize the best_range to store the result (the largest range)
    best_range = []

    # Initialize longest_length to keep track of the length of the largest range found
    longest_length = 0

    # Create a dictionary to store all the numbers in the array as keys.
    # The value `True` indicates that the number has not been processed yet.
    nums = {}
    for num in array:
        nums[num] = True

    # Iterate through each number in the array
    for num in array:
        # If the number has already been processed, skip it
        if not nums[num]:
            continue

        # Mark the current number as processed
        nums[num] = False

        # Initialize the current_length to 1 (since we have at least one number in the range)
        current_length = 1

        # Initialize pointers to explore the range to the left and right of the current number
        left = num - 1
        right = num + 1

        # Explore the range to the left of the current number
        while left in nums:
            # Mark the left number as processed
            nums[left] = False
            # Increase the current_length since we found a consecutive number
            current_length += 1
            # Move the left pointer further to the left
            left -= 1

        # Explore the range to the right of the current number
        while right in nums:
            # Mark the right number as processed
            nums[right] = False
            # Increase the current_length since we found a consecutive number
            current_length += 1
            # Move the right pointer further to the right
            right += 1

        # After exploring both left and right, check if the current range is the longest found so far
        if current_length > longest_length:
            # Update the longest_length with the current_length
            longest_length = current_length
            # Update the best_range with the new range [left + 1, right - 1]
            # left + 1 because we decremented left one extra time in the while loop
            # right - 1 because we incremented right one extra time in the while loop
            best_range = [left + 1, right - 1]

    # Return the best_range, which represents the largest range of consecutive numbers
    return best_range


# Test Cases:

print(largest_range([1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]))
# Output: [0, 7]

print(largest_range([-1, 0, 1]))
# Output: [-1, 1]

print(largest_range([0, 9, 19, -1, 18, 17, 2, -10, 3, 12, 5, -16, 4, 11, 8, 7, 6, 15]))
# Output: [2, 9]

# =========================================================================================================================== #
