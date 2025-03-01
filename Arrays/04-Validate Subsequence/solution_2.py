# Description:

"""

                                          Validate Subsequence

Given two non-empty arrays of integers, write a function that determines whether the second array is a subsequence of the first one.

A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array but that are in the same order as they
appear in the array. For instance, the numbers [1, 3, 4] form a subsequence of the array [1, 2, 3, 4], and so do the numbers [2, 4].
Note that a single number in an array and the array itself are both valid subsequences of the array.

## Sample Input:

```
array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
```

## Sample Output:

```
true
```

## Optimal Space & Time Complexity:

```
`O(n)` time | `O(1)` space - where `n` is the length of the array
```

"""

# =============================================================================================== #

# Solution:


# O (n) time | O(1) space
def is_valid_subsequence(array, sequence):
    seq_idx = 0

    for value in array:
        if seq_idx == len(sequence):
            break
        if sequence[seq_idx] == value:
            seq_idx += 1
    return seq_idx == len(sequence)


# Test Cases
print(
    is_valid_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10])
)  # Output: True
print(
    is_valid_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 25, 6, -1, 8, 10])
)  # Output: True
print(
    is_valid_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, 10, -1])
)  # Output: False

# =============================================================================================== #

# Big O:

"""
### Time and Space Complexity

### Time Complexity:
- **O(n)** where `n` is the length of the `array`. We iterate through the array once, and for each element,
we check if it matches the current element of the sequence. Once we've found all elements of the sequence, we stop.

#### **Space Complexity**:
- **O(1)** space because we only use a single integer (`seq_idx`) for tracking the index of the `sequence` and 
no additional space that grows with input size.

"""


# Code Explanation:

"""

This function checks if a sequence is a valid subsequence of an array. A subsequence means that the elements of the
sequence appear in the same order within the array, but not necessarily consecutively. Let's break it down step by step:

### Function Signature:
```
def is_valid_subsequence(array, sequence):
```
- **array**: The main list in which we check if the sequence exists.
- **sequence**: The list we want to verify is a subsequence of the array.

### Initial Setup:
```
seq_idx = 0
```
- **seq_idx**: A variable to track the index of the `sequence` list. We initialize it to 0 because we want to start
from the first element of the `sequence` and check if it's found in the `array`.

### Iterating Through the Array:
```
for value in array:
```
- We loop through each element (`value`) in the `array` list.

### Check if Subsequence is Already Matched:
```
if seq_idx == len(sequence):
    break
```
- This is a quick exit condition. If we've already matched all elements of the `sequence` (i.e., `seq_idx` has reached
the length of the `sequence`), then we break out of the loop early because there's no need to continue checking further.

### Matching Elements Between Array and Sequence:
```
if sequence[seq_idx] == value:
    seq_idx += 1
```
- If the current element in `array` (`value`) matches the current element in `sequence` (i.e., `sequence[seq_idx]`),
we increment `seq_idx` to check the next element in `sequence`.
- This means we've found a match for the current element of `sequence`, and now we're ready to move on to the next element
of `sequence` in the next iteration of the loop.

### Return Result:
```
return seq_idx == len(sequence)
```
- After iterating through the entire array, if `seq_idx` equals the length of the `sequence`, it means we've found
every element in the sequence in the correct order in the array, and the function returns `True`.
- If not, it means the sequence was not found in the correct order, and the function returns `False`.

### Example Walkthrough:

#### Test Case 1:
```
is_valid_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10])
```

- The function checks if `[1, 6, -1, 10]` is a valid subsequence of `[5, 1, 22, 25, 6, -1, 8, 10]`.
- Starting with `seq_idx = 0` (which corresponds to the first element of `sequence`, `1`), it checks the array:
  - First value is `5`, which doesn’t match `1`.
  - Next value is `1`, which matches `1`, so `seq_idx` becomes `1`.
  - The next value is `22`, which doesn’t match `6`.
  - The next value is `25`, which doesn’t match `6`.
  - The next value is `6`, which matches `6`, so `seq_idx` becomes `2`.
  - The next value is `-1`, which matches `-1`, so `seq_idx` becomes `3`.
  - Finally, the next value is `10`, which matches `10`, so `seq_idx` becomes `4`.
- Since `seq_idx` reaches the length of the sequence (`4`), the function returns `True`.

#### Test Case 2:
```
is_valid_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 25, 6, -1, 8, 10])
```
- Here, we check if the entire `array` is a subsequence of itself. The function matches each element in the array
one by one, incrementing `seq_idx` every time a match is found.
- Once `seq_idx` reaches the length of the `sequence`, the function returns `True`.

### Conclusion:
The function effectively checks if a given `sequence` is a subsequence of the `array` by iterating through the
array and matching elements in order. The time complexity is linear - O(n), and the space complexity is constant - O(1).

"""
