# Problem Description:

"""
                                             Index Equals Value

You're given `two sorted arrays` of integers `array_one` and `array_two`. Write a function that returns the `median` of these arrays.

You can assume both arrays have at least one value. However, they could be of different lengths. If the `median` is a decimal value,
it should not be rounded (beyond the inevitable rounding of floating point math).


## Sample Input:
```
array_one = [1, 3, 4, 5]
array_two = [2, 3, 6, 7]
```

## Sample Output:
```
3.5

// The combined array is [1, 2, 3, 3, 4, 5, 6, 7]
```

## Optimal Time & Space Complexity:
```
O(log(min(n, m)) time | O(1) space - where `n` is the length of `array_one` and `m` is the length of `array_two`.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n + m) time | O(1) space
def median_of_two_sorted_arrays(array_one, array_two):
    # Initialize pointers for both arrays
    idx_one, idx_two = 0, 0

    # Calculate total length of combined arrays
    total_length = len(array_one) + len(array_two)

    # Calculate middle index (for odd length) or first middle index (for even length)
    middle_idx = (total_length - 1) // 2

    # For even length, we need the next index after middle to calculate median
    next_middle_idx = middle_idx + 1 if total_length % 2 == 0 else None

    # Move pointers forward until we reach the middle index of the combined array
    while idx_one + idx_two < middle_idx:
        # If we've exhausted array_one, move array_two's pointer
        if idx_one >= len(array_one):
            idx_two += 1
        # If we've exhausted array_two, move array_one's pointer
        elif idx_two >= len(array_two):
            idx_one += 1
        # Otherwise, move the pointer of the array with smaller current element
        elif array_one[idx_one] < array_two[idx_two]:
            idx_one += 1
        else:
            idx_two += 1

    # Handle case where total length is odd (single middle element)
    if next_middle_idx is None:
        # If array_one is exhausted, return current element from array_two
        if idx_one >= len(array_one):
            return array_two[idx_two]

        # If array_two is exhausted, return current element from array_one
        if idx_two >= len(array_two):
            return array_one[idx_one]

        # Otherwise return the smaller of current elements (since arrays are sorted)
        return min(array_one[idx_one], array_two[idx_two])
    # Handle case where total length is even (average of two middle elements)
    else:
        values = []
        # We need to collect the next two elements (current and next)
        for _ in range(2):
            # Similar logic as above to get next elements
            if idx_one >= len(array_one):
                values.append(array_two[idx_two])
                idx_two += 1
            elif idx_two >= len(array_two):
                values.append(array_one[idx_one])
                idx_one += 1
            elif array_one[idx_one] < array_two[idx_two]:
                values.append(array_one[idx_one])
                idx_one += 1
            else:
                values.append(array_two[idx_two])
                idx_two += 1
        # Return average of the two middle elements
        return sum(values) / 2


# Test Cases:

print(median_of_two_sorted_arrays([1, 3, 4, 5], [2, 3, 6, 7]))
# Output: 3.5

print(median_of_two_sorted_arrays([2, 2, 2, 2, 2], [3, 3, 3, 3]))
# Output: 2

print(median_of_two_sorted_arrays([-100, -50, -1, 15, 3], [1, 20, 50, 100]))
# Output: 15
