# Problem Description:

"""
                                             Quickselect

Write a function that takes in an array of distinct integers as well as an integer `k` and that returns the `k`th smallest integer
in that array.

The function should do this in `linear time`, on average.


## Sample Input:
```
array = [8, 5, 2, 9, 7, 6, 3]
k = 3
```

## Sample Output:
```
5
```

## Optimal Time & Space Complexity:
```
Best: O(n) time | O(1) space - where `n` is the length of the input array.
Average: O(n) time | O(1) space - where `n` is the length of the input array.
Worst: O(n²) time | O(1) space - where `n` is the length of the input array.
```

"""

# =========================================================================================================================== #

# Solution:


# Best: O(n) time | O(1) space
# Average: O(n) time | O(1) space
# Worst: O(n²) time | O(1)
def quick_select(array, k):
    position = k - 1

    return quick_select_helper(array, 0, len(array) - 1, position)


def quick_select_helper(array, start_idx, end_idx, position):
    while True:
        if start_idx > end_idx:
            raise Exception("Your algorithm should never arrive here!")

        pivot_idx = start_idx
        left_idx = start_idx + 1
        right_idx = end_idx

        while left_idx <= right_idx:
            if (
                array[left_idx] > array[pivot_idx]
                and array[right_idx] < array[pivot_idx]
            ):
                swap(left_idx, right_idx, array)

            if array[left_idx] <= array[pivot_idx]:
                left_idx += 1

            if array[right_idx] >= array[pivot_idx]:
                right_idx -= 1

        swap(pivot_idx, right_idx, array)

        if right_idx == position:
            return array[right_idx]
        elif right_idx < position:
            start_idx = right_idx + 1
        else:
            end_idx = right_idx - 1


def swap(one, two, array):
    array[one], array[two] = array[two], array[one]


# Test Cases:

print(quick_select([8, 5, 2, 9, 7, 6, 3], 3))
# Output: 5

print(quick_select([102, 41, 58, 81, 2, -5, 1000, 10021, 181, -14515, 25, 15], 5))
# Output: 25

print(quick_select([43, 24, 37], 2))
# Output: 37
