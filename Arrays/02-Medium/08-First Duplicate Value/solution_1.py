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


# O(n^2) time | O(1) space - where `n` is the length of the input array.
def first_duplicate_value(array):
    # Initialize the variable to store the index of the first duplicate found.
    # We start with the length of the array, which is an invalid index, to indicate no duplicate has been found yet.
    minimum_second_index = len(array)

    # Loop through each element in the array.
    for i in range(len(array)):
        value = array[i]  # Get the current element to compare with the rest.

        # Loop through the elements that come after the current element.
        for j in range(i + 1, len(array)):
            value_to_compare = array[j]  # Get the next element to compare.

            # If a duplicate is found, update the minimum_second_index if this duplicate appears earlier.
            if value == value_to_compare:
                minimum_second_index = min(minimum_second_index, j)

    # If no duplicate was found, return -1.
    if minimum_second_index == len(array):
        return -1

    # Return the value of the first duplicate found.
    return array[minimum_second_index]


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
