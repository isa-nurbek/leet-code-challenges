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

`O(n)` time | `O(1)` space - where `n` is the length of the array

"""


# O (n) time | O(1) space
def is_valid_subsequence(array, sequence):
    arr_idx = 0
    seq_idx = 0

    while arr_idx < len(array) and seq_idx < len(sequence):
        if array[arr_idx] == sequence[seq_idx]:
            seq_idx += 1
        arr_idx += 1
    return seq_idx == len(sequence)


print(
    is_valid_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10])
)  # Output: True
print(
    is_valid_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 25, 6, -1, 8, 10])
)  # Output: True
print(
    is_valid_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, 10, -1])
)  # Output: False


# Big O:

"""

### Time and Space Complexity

#### **Time Complexity**:
- O(n): The function processes each element of `array` at most once, where `n` is the length of `array`.

#### **Space Complexity**:
- O(1): The function uses constant space (only two pointers).

"""


# Code Explanation:

"""

The provided code is a Python function that determines whether a given `sequence` is a subsequence of an `array`.
It operates in O(n) time complexity and O(1) space complexity.

---

### How the Code Works

#### 1. **Inputs**:
- `array`: A list of integers where we check for the presence of the sequence.
- `sequence`: A list of integers to check if it exists as a subsequence in `array`.

#### 2. **Output**:
The function returns `True` if `sequence` is a subsequence of `array`, otherwise it returns `False`.

#### 3. **Definitions**:
A **subsequence** is a set of elements that appear in the same order in another sequence, but not necessarily consecutively.

For example:
- `[1, 6, -1, 10]` is a subsequence of `[5, 1, 22, 25, 6, -1, 8, 10]`.
- `[5, 1, 22, 25, 6, -1, 8, 10]` is a subsequence of itself.

---

### Code Walkthrough

#### Initialization:
```
arr_idx = 0
seq_idx = 0
```
- `arr_idx`: Index pointer for iterating through `array`.
- `seq_idx`: Index pointer for iterating through `sequence`.

---

#### While Loop:
```
while arr_idx < len(array) and seq_idx < len(sequence):
```
- The loop runs until one of these conditions is met:
  1. `arr_idx` reaches the end of `array` (all elements of `array` are processed).
  2. `seq_idx` reaches the end of `sequence` (all elements of `sequence` have been matched).

---

#### Inside the Loop:
```
if array[arr_idx] == sequence[seq_idx]:
    seq_idx += 1
```
- **Comparison**: Compares the current element of `array` (`array[arr_idx]`) with the current element
of `sequence` (`sequence[seq_idx]`).
- **Match**: If they match:
  - Increment `seq_idx` to move to the next element in the `sequence`.
- **No Match**: If they don’t match:
  - Do nothing and just continue iterating through `array`.

```
arr_idx += 1
```
- Increment `arr_idx` in every iteration to process the next element in `array`.

---

#### End of Loop:
```
return seq_idx == len(sequence)
```
- **Check Completion**:
  - If `seq_idx` equals the length of `sequence`, it means all elements in `sequence` have been matched in the correct
  order in `array`, and the function returns `True`.
  - Otherwise, it returns `False`.

---

### Example Runs:

#### Example 1:
```
is_valid_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10])
```
1. Initial values: `arr_idx = 0`, `seq_idx = 0`.
2. Iteration:
   - `array[1] == sequence[0]`: Match, `seq_idx = 1`.
   - `array[4] == sequence[1]`: Match, `seq_idx = 2`.
   - `array[5] == sequence[2]`: Match, `seq_idx = 3`.
   - `array[7] == sequence[3]`: Match, `seq_idx = 4`.
3. `seq_idx == len(sequence)`: **True**.

#### Example 2:
```
is_valid_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 25, 6, -1, 8, 10])
```
1. Initial values: `arr_idx = 0`, `seq_idx = 0`.
2. Iteration:
   - All elements of `sequence` are matched in order with `array`.
3. `seq_idx == len(sequence)`: **True**.


Here's an example that returns `False`:

### Example 3:
```
is_valid_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, 10, -1])
```

1. Initial values: `arr_idx = 0`, `seq_idx = 0`.

2. Iteration:
   - `array[1] == sequence[0]`: Match, `seq_idx = 1`.
   - `array[4] == sequence[1]`: Match, `seq_idx = 2`.
   - `array[7] == sequence[2]`: Match, `seq_idx = 3`.
   - No match for `sequence[3] = -1` after `sequence[2] = 10`.

3. Loop ends: `seq_idx != len(sequence)`. **Output: False**.

### Why This Fails:
The order in the `sequence` ([1, 6, 10, -1]) does not match the order in the `array`.
Specifically, `-1` appears **before** `10` in the `array`. This violates the subsequence rule.

---

### Key Points:
- The function relies on two pointers (`arr_idx` and `seq_idx`) to track progress in `array` and `sequence`.
- It ensures the order of elements in `sequence` matches their appearance in `array`.
- Skips over elements in `array` that don't match the current element in `sequence`.

This efficient approach ensures the function works for long arrays and sequences with minimal overhead.

"""
