# Problem Description:

"""

                                         # Longest Peak

Write a function that takes in an array of integers and returns the length of the longest peak in the array.

A peak is defined as adjacent integers in the array that are strictly increasing until they reach a tip (the highest
value in the peak), at which point they become strictly decreasing. At least three integers are required to form a peak.

For example, the integers `1, 4, 10, 2` form a peak, but the integers `4, 0, 10` don't and neither do the integers `1, 2, 2, 0`.
Similarly, the integers `1, 2, 3` don't form a peak because there aren't any strictly decreasing integers after the `3`.


## Sample Input:
```
array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
```

## Sample Output:
```
6 // 0, 10, 6, 5, -1, -3
```

## Optimal Time & Space Complexity:
```
O(n) time | O(1) space - where `n` is the length of the input array.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n) time | O(1) space - where `n` is the length of the input array.
def longest_peak(array):
    # Initialize the length of the longest peak found so far
    longest_peak_length = 0

    # Start iterating through the array from the second element to the second-to-last element
    i = 1
    while i < len(array) - 1:
        # Check if the current element is a peak
        # A peak is defined as an element that is greater than its immediate neighbors
        is_peak = array[i - 1] < array[i] and array[i] > array[i + 1]

        # If the current element is not a peak, move to the next element
        if not is_peak:
            i += 1
            continue

        # If the current element is a peak, expand to the left to find the start of the peak
        left_idx = i - 2
        while left_idx >= 0 and array[left_idx] < array[left_idx + 1]:
            left_idx -= 1

        # Expand to the right to find the end of the peak
        right_idx = i + 2
        while right_idx < len(array) and array[right_idx] < array[right_idx - 1]:
            right_idx += 1

        # Calculate the length of the current peak
        current_peak_length = right_idx - left_idx - 1

        # Update the longest peak length if the current peak is longer
        longest_peak_length = max(longest_peak_length, current_peak_length)

        # Move the index to the end of the current peak to avoid overlapping peaks
        i = right_idx

    # Return the length of the longest peak found
    return longest_peak_length


# Test Cases:

print(longest_peak([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]))
# Output: 6

print(longest_peak([5, 4, 3, 2, 1, 2, 10, 12, -3, 5, 6, 7, 10]))
# Output: 5

print(longest_peak([]))
# Output: 0

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### Time Complexity Analysis

The time complexity of the `longest_peak` function can be analyzed as follows:

1. **Outer Loop**: The outer `while` loop runs from `i = 1` to `i < len(array) - 1`. In the worst case, this loop
iterates over the entire array, so it runs in O(n) time, where `n` is the length of the array.

2. **Peak Check**: For each iteration of the outer loop, the function checks if the current element is a peak.
This check is done in constant time O(1).

3. **Left Expansion**: If a peak is found, the function expands to the left to find the start of the peak. This inner
`while` loop runs until it finds an element that is not part of the increasing sequence. In the worst case, this could
run up to O(n) times, but since each element is only processed once across all peaks, the total time for all
left expansions across the entire array is O(n).

4. **Right Expansion**: Similarly, the function expands to the right to find the end of the peak. This inner `while`
loop also runs in O(n) time in total across all peaks.

5. **Peak Length Calculation**: The calculation of the current peak length and updating the `longest_peak_length` is
done in constant time O(1).

6. **Update `i`**: After processing a peak, the outer loop skips to the end of the current peak by setting `i = right_idx`.
This ensures that each element is processed at most once.

### Overall Time Complexity

Since each element in the array is processed at most once during the left and right expansions, and the outer loop
runs in O(n) time, the overall time complexity of the function is: O(n)

---

### Space Complexity Analysis

The space complexity of the function is determined by the amount of additional memory used:

1. **Variables**: The function uses a few variables (`longest_peak_length`, `i`, `left_idx`, `right_idx`, `current_peak_length`,
etc.), which require constant space O(1).

2. **No Additional Data Structures**: The function does not use any additional data structures like arrays, stacks, or 
queues that grow with the input size.

### Overall Space Complexity

Since the function uses only a constant amount of extra space, the space complexity is: O(1)

---

### Summary

- **Time Complexity**: O(n)
- **Space Complexity**: O(1)

"""

# =========================================================================================================================== #
