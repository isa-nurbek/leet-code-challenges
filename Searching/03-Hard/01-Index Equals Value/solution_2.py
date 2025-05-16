# Problem Description:

"""
                                             Index Equals Value

Write a function that takes in a sorted array of distinct integers and returns the first index in the array that is equal to the
value at that index. In other words, your function should return the minimum index where `index == array[index]`.

If there is no such index, your function should return `-1`.


## Sample Input:
```
array = [-5, -3, 0, 3, 4, 5, 9]
```

## Sample Output:
```
3

// 3 == array[3]
```

## Optimal Time & Space Complexity:
```
O(log(n)) time | O(1) space - where `n` is the length of the input array.
```

"""

# =========================================================================================================================== #

# Solution:


# O(log(n)) time | O(log(n)) space
def index_equals_value(array):
    return index_equals_value_helper(array, 0, len(array) - 1)


def index_equals_value_helper(array, left_idx, right_idx):
    if left_idx > right_idx:
        return -1

    middle_idx = left_idx + (right_idx - left_idx) // 2
    middle_value = array[middle_idx]

    if middle_value < middle_idx:
        return index_equals_value_helper(array, middle_idx + 1, right_idx)
    elif middle_value == middle_idx and middle_idx == 0:
        return middle_idx
    elif middle_value == middle_idx and array[middle_idx - 1] < middle_idx - 1:
        return middle_idx
    else:
        return index_equals_value_helper(array, left_idx, middle_idx - 1)


# Test Cases:

print(index_equals_value([-5, -3, 0, 3, 4, 5, 9]))
# Output: 3

print(index_equals_value([-12, 1, 2, 3, 12]))
# Output: 1

print(index_equals_value([-5, -4, -3, -2, -1, 0, 1, 3, 5, 6, 7, 11, 12, 14, 19, 20]))
# Output: 11
