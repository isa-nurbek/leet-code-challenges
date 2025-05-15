# Problem Description:

"""
                                             Search For Range

Write a function that takes in a `sorted array` of integers as well as a `target integer`. The function should use a variation of
the `Binary Search` algorithm to find a range of indices in between which the target number is contained in the array and should
return this range in the form of an array.

The first number in the output array should represent the first index at which the target number is located, while the second number
should represent the last index at which the target number is located. The function should return `[-1, -1]` if the integer isn't
contained in the array.


## Sample Input:
```
array = [0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73]
target = 45
```

## Sample Output:
```
[4, 9]
```

## Optimal Time & Space Complexity:
```
O(log(n)) time | O(1) space - where `n` is the length of the input array.
```

"""

# =========================================================================================================================== #

# Solution:


# O(log(n)) time | O(log(n)) space
def search_for_range(array, target):
    final_range = [-1, -1]

    altered_binary_search(array, target, 0, len(array) - 1, final_range, True)
    altered_binary_search(array, target, 0, len(array) - 1, final_range, False)

    return final_range


def altered_binary_search(array, target, left, right, final_range, go_left):
    if left > right:
        return

    middle = (left + right) // 2

    if array[middle] < target:
        altered_binary_search(array, target, middle + 1, right, final_range, go_left)
    elif array[middle] > target:
        altered_binary_search(array, target, left, middle - 1, final_range, go_left)
    else:
        if go_left:
            if middle == 0 or array[middle - 1] != target:
                final_range[0] = middle
            else:
                altered_binary_search(
                    array, target, left, middle - 1, final_range, go_left
                )
        else:
            if middle == len(array) - 1 or array[middle + 1] != target:
                final_range[1] = middle
            else:
                altered_binary_search(
                    array, target, middle + 1, right, final_range, go_left
                )


# Test Cases:

print(search_for_range([0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73], 45))
# Output: [4, 9]

print(search_for_range([5, 7, 7, 8, 8, 10], 5))
# Output: [0, 0]

print(search_for_range([0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73], -1))
# Output: [-1, -1]
