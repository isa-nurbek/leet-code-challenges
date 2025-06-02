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
    """
    Finds the maximum sum increasing subsequence in the given array.
    An increasing subsequence is a sequence of elements where each element is greater than the previous.
    Among all such subsequences, this function returns the one with the maximum sum.

    Args:
        array: List of numbers to process

    Returns:
        A list where first element is the maximum sum, and second element is the subsequence as a list
    """

    # Initialize sequences array to keep track of previous indices
    # sequences[i] stores the index of the previous element in the optimal subsequence ending at i
    sequences = [None for x in array]

    # Initialize sums array to store maximum sums up to each index
    # sums[i] stores the maximum sum of increasing subsequence ending at array[i]
    sums = [num for num in array]  # Start with each element itself as base case

    max_sum_idx = 0  # Tracks index of maximum sum found so far

    for i in range(len(array)):
        current_num = array[i]

        # Compare with all previous elements to find increasing subsequences
        for j in range(0, i):
            other_num = array[j]

            # If previous element is smaller and including it gives better sum
            if other_num < current_num and sums[j] + current_num >= sums[i]:
                sums[i] = sums[j] + current_num  # Update maximum sum for current index
                sequences[i] = j  # Record that the best sequence comes from j

        # Update overall maximum sum index if current sum is larger
        if sums[i] >= sums[max_sum_idx]:
            max_sum_idx = i

    # Return both the maximum sum and the corresponding sequence
    return [sums[max_sum_idx], build_sequence(array, sequences, max_sum_idx)]


def build_sequence(array, sequences, current_idx):
    """
    Helper function to reconstruct the sequence from the sequences array.

    Args:
        array: Original input array
        sequences: Array tracking previous indices in optimal subsequences
        current_idx: Index where the maximum sum subsequence ends

    Returns:
        The reconstructed subsequence in correct order
    """
    sequence = []

    # Backtrack from current_idx following the sequence chain
    while current_idx is not None:
        sequence.append(array[current_idx])
        current_idx = sequences[current_idx]  # Move to previous element in sequence

    # Reverse to get the correct order (from start to end)
    return list(reversed(sequence))


# Test Cases:

print(max_sum_increasing_subsequence([10, 70, 20, 30, 50, 11, 30]))
# Output: [110, [10, 20, 30, 50]]

print(max_sum_increasing_subsequence([-5, -4, -3, -2, -1]))
# Output: [-1, [-1]]

print(max_sum_increasing_subsequence([8, 12, 2, 3, 15, 5, 7]))
# Output: [35, [8, 12, 15]]
