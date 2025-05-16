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
    idx_one, idx_two = 0, 0
    total_length = len(array_one) + len(array_two)
    middle_idx = (total_length - 1) // 2
    next_middle_idx = middle_idx + 1 if total_length % 2 == 0 else None

    while idx_one + idx_two < middle_idx:
        if idx_one >= len(array_one):
            idx_two += 1
        elif idx_two >= len(array_two):
            idx_one += 1
        elif array_one[idx_one] < array_two[idx_two]:
            idx_one += 1
        else:
            idx_two += 1

    if next_middle_idx is None:
        if idx_one >= len(array_one):
            return array_two[idx_two]
        if idx_two >= len(array_two):
            return array_one[idx_one]
        return min(array_one[idx_one], array_two[idx_two])
    else:
        values = []
        for _ in range(2):
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
        return sum(values) / 2


# Test Cases:

print(median_of_two_sorted_arrays([1, 3, 4, 5], [2, 3, 6, 7]))
# Output: 3.5

print(median_of_two_sorted_arrays([2, 2, 2, 2, 2], [3, 3, 3, 3]))
# Output: 2

print(median_of_two_sorted_arrays([-100, -50, -1, 15, 3], [1, 20, 50, 100]))
# Output: 15
