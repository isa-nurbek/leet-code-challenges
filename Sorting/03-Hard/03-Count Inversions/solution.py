# Problem Description:

"""
                                                Count Inversions

Write a function that takes in an array of integers and returns the number of `inversions` in the array. An `inversion` occurs
if for any valid indices `i` and `j`, `i < j` and `array[i] > array[j]`.

For example, given `array = [3, 4, 1, 2]`, there are `4 inversions`. The following pairs of indices represent inversions:
`[0, 2], [0, 3], [1, 2], [1, 3]`.

Intuitively, the number of inversions is a measure of how unsorted the array is.


## Sample Input:
```
array = [2, 3, 3, 1, 9, 5, 6]
```

## Sample Output:
```
5

// The following pairs of indices represent inversions: [0, 3], [1, 3], [2, 3], [4, 5], [4, 6]
```

## Optimal Time & Space Complexity:
```
O(n log n) time | O(n) space - where `n` is the length of the array.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n log n) time | O(n) space
def count_inversions(array):
    return count_sub_array_inversions(array, 0, len(array))


def count_sub_array_inversions(array, start, end):
    if end - start <= 1:
        return 0

    middle = start + (end - start) // 2

    left_inversions = count_sub_array_inversions(array, start, middle)
    right_inversions = count_sub_array_inversions(array, middle, end)
    merged_array_inversions = merge_sort_and_count_inversions(array, start, middle, end)

    return left_inversions + right_inversions + merged_array_inversions


def merge_sort_and_count_inversions(array, start, middle, end):
    sorted_array = []

    left = start
    right = middle
    inversions = 0

    while left < middle and right < end:
        if array[left] <= array[right]:
            sorted_array.append(array[left])
            left += 1
        else:
            inversions += middle - left
            sorted_array.append(array[right])
            right += 1

    sorted_array += array[left:middle] + array[right:end]

    for idx, num in enumerate(sorted_array):
        array[start + idx] = num

    return inversions


# Test Cases:

print(count_inversions([2, 3, 3, 1, 9, 5, 6]))
# Output: 5

print(count_inversions([5, -1, 2, -4, 3, 4, 19, 87, 762, -8, 0]))
# Output: 23

print(count_inversions([]))
# Output: 0
