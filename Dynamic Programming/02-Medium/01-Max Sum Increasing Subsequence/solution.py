# Problem Description:

"""
                                               Max Sum Increasing Subsequence

Write a function that takes in a `non-empty` array of integers and returns the greatest sum that can be generated from a
strictly-increasing subsequence in the array as well as an array of the numbers in that subsequence.

A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array but that are in the same order as they
appear in the array. For instance, the numbers `[1, 3, 4]` form a subsequence of the array `[1, 2, 3, 4]`, and so do the numbers
`[2, 4]`.

> Note that a single number in an array and the array itself are both valid subsequences of the array.

You can assume that there will only be one increasing subsequence with the greatest sum.


## Sample Input:
```
array = [10, 70, 20, 30, 50, 11, 30]
```

## Sample Output:
```
[110, [10, 20, 30, 50]]

// The subsequence [10, 20, 30, 50] is strictly increasing and yields the greatest sum: 110.
```

## Optimal Time & Space Complexity:
```
O(n²) time | O(n) space - where `n` is the length of the input array.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n²) time | O(n) space
def max_sum_increasing_subsequence(array):
    sequences = [None for x in array]
    sums = [num for num in array]

    max_sum_idx = 0
    for i in range(len(array)):
        current_num = array[i]

        for j in range(0, i):
            other_num = array[j]

            if other_num < current_num and sums[j] + current_num >= sums[i]:
                sums[i] = sums[j] + current_num
                sequences[i] = j

        if sums[i] >= sums[max_sum_idx]:
            max_sum_idx = i

    return [sums[max_sum_idx], build_sequence(array, sequences, max_sum_idx)]


def build_sequence(array, sequences, current_idx):
    sequence = []

    while current_idx is not None:
        sequence.append(array[current_idx])
        current_idx = sequences[current_idx]

    return list(reversed(sequence))


# Test Cases:

print(max_sum_increasing_subsequence([10, 70, 20, 30, 50, 11, 30]))
# Output: [110, [10, 20, 30, 50]]

print(max_sum_increasing_subsequence([-5, -4, -3, -2, -1]))
# Output: [-1, [-1]]

print(max_sum_increasing_subsequence([8, 12, 2, 3, 15, 5, 7]))
# Output: [35, [8, 12, 15]]
