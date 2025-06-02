# Problem Description:

"""
                                            Min Number Of Jumps

You're given a `non-empty` array of positive integers where each integer represents the maximum number of steps you can take
forward in the array. For example, if the element at index `1` is `3`, you can go from index `1` to index `2`, `3`, or `4`.

Write a function that returns the minimum number of jumps needed to reach the final index.

> Note that jumping from index `i` to index `i + x` always constitutes one jump, no matter how large `x` is.


## Sample Input:
```
array = [3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]
```

## Sample Output:
```
4

// 3 --> (4 or 2) --> (2 or 3) --> 7 --> 3
```

## Optimal Time & Space Complexity:
```
O(n) time | O(1) space - where `n` is the length of the input array.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n) time | O(1) space
def min_number_of_jumps(array):
    # If the array has 0 or 1 elements, no jumps are needed
    if len(array) <= 1:
        return 0

    jumps = 0  # Counts the number of jumps made
    max_reach = array[0]  # The farthest index that can be reached with current jumps
    current_end = array[0]  # The end of the current jump's range

    # Iterate through the array (excluding the last element)
    for i in range(1, len(array) - 1):
        # Update the maximum reachable index from the current position
        max_reach = max(max_reach, i + array[i])

        # When we reach the end of the current jump's range,
        # we need to make another jump
        if i == current_end:
            jumps += 1
            # The new jump's range extends to the max_reach
            current_end = max_reach

    # We need one more jump to reach the end from the last position
    return jumps + 1


# Test Cases:

print(min_number_of_jumps([3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]))
# Output: 4

print(min_number_of_jumps([2, 1, 2, 3, 1]))
# Output: 2

print(min_number_of_jumps([1]))
# Output: 0
