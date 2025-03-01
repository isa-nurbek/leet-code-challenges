# Description:

"""

                                        Two Number Sum

Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. If any two
numbers in the input array sum up to the target sum, the function should return them in an array, in any order. If no two
numbers sum up to the target sum, the function should return an empty array.

Note that the target sum has to be obtained by summing two different integers in the array; you can't add a single integer
to itself in order to obtain the target sum.

You can assume that there will be at most one pair of numbers summing up to the target sum.

## Sample Input:

```
array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10
```

## Sample Output:

```
[-1, 11] // the numbers could be in reverse order
```

## Optimal Space & Time Complexity:

```
`O(n)` time | `O(n)` space - where `n` is the length of the input array
```

"""

# =============================================================================================== #

# Solution:


# O (n^2) time | O(1) space
def two_number_sum(array, target_sum):
    for i in range(len(array) - 1):
        first_num = array[i]
        for j in range(i + 1, len(array)):
            second_num = array[j]

            if first_num + second_num == target_sum:
                return [first_num, second_num]
    return []


# Test Cases
print(two_number_sum([3, 5, -4, 8, 11, 1, -1, 6], 10))  # Output: [11, -1]
print(two_number_sum([4, 6, 1, -3, 7], 3))  # Output: [6, -3]
print(two_number_sum([5, 1, 4, 7, 9], 10))  # Output: [1, 9]
print(two_number_sum([7], 7))  # Output: []

# =============================================================================================== #

# Big O:

"""

### Complexity Analysis:
1. **Time Complexity: O(n²)**:
   - The outer loop runs `n - 1` iterations, and the inner loop runs approximately `n / 2` iterations on average.
   - This leads to an approximate total of `n² / 2` iterations, which simplifies to O(n²).
   
2. **Space Complexity: O(1)**:
   - The function uses a constant amount of additional space (two variables `first_num` and `second_num`)
   regardless of the input size.

"""


# Code Explanation:

"""

The `two_number_sum` function is designed to find two numbers in a given array whose sum equals a specified `target_sum`.
If such a pair exists, the function returns the two numbers as a list. If no such pair exists, it returns an empty list.

### Code Explanation:

#### Function Definition and Input:
```
def two_number_sum(array, target_sum):
```
- `array`: A list of integers to search for the pair.
- `target_sum`: An integer representing the desired sum of two numbers.

---

#### Outer Loop:
```
for i in range(len(array) - 1):
    first_num = array[i]
```
- The **outer loop** iterates through the array using index `i`.
- `first_num` is set to the current element at index `i`.

---

#### Inner Loop:
```
for j in range(i + 1, len(array)):
    second_num = array[j]
```
- The **inner loop** starts from `i + 1`, which ensures that each pair of numbers is checked exactly once
(avoiding duplicates like `array[i]` and `array[j]` vs. `array[j]` and `array[i]`).
- `second_num` is set to the current element at index `j`.

---

#### Sum Check:
```
if first_num + second_num == target_sum:
    return [first_num, second_num]
```
- For each pair `(first_num, second_num)`, the function checks if their sum equals `target_sum`.
- If the condition is satisfied, the pair is returned as a list.

---

#### Default Return:
```
return []
```
- If no pair is found after iterating through all possible pairs, the function returns an empty list.

---

### Example Walkthrough:

#### Input: `array = [3, 5, -4, 8, 11, 1, -1, 6]`, `target_sum = 10`
1. Outer loop starts with `i = 0`, `first_num = 3`.
   - Inner loop checks pairs:
     - `3 + 5 = 8` (not 10)
     - `3 + (-4) = -1` (not 10)
     - `3 + 8 = 11` (not 10)
     - `3 + 11 = 14` (not 10)
     - `3 + 1 = 4` (not 10)
     - `3 + (-1) = 2` (not 10)
     - `3 + 6 = 9` (not 10)

2. Outer loop continues with `i = 1`, `first_num = 5`.
   - Inner loop checks pairs:
     - `5 + (-4) = 1` (not 10)
     - `5 + 8 = 13` (not 10)
     - `5 + 11 = 16` (not 10)
     - `5 + 1 = 6` (not 10)
     - `5 + (-1) = 4` (not 10)
     - `5 + 6 = 11` (not 10)

3. Outer loop continues with `i = 2`, `first_num = -4`.
   - Inner loop checks pairs:
     - `-4 + 8 = 4` (not 10)
     - `-4 + 11 = 7` (not 10)
     - `-4 + 1 = -3` (not 10)
     - `-4 + (-1) = -5` (not 10)
     - `-4 + 6 = 2` (not 10)

4. Outer loop continues with `i = 3`, `first_num = 8`.
   - Inner loop checks pairs:
     - `8 + 11 = 19` (not 10)
     - `8 + 1 = 9` (not 10)
     - `8 + (-1) = 7` (not 10)
     - `8 + 6 = 10` (match found!)

   - Function returns `[8, 6]`.

---

#### Other Test Cases:

1. **Input**: `[4, 6, 1, -3, 7]`, `target_sum = 3`
   - Pair `(6, -3)` matches. Output: `[6, -3]`.

2. **Input**: `[5, 1, 4, 7, 9]`, `target_sum = 10`
   - Pair `(1, 9)` matches. Output: `[1, 9]`.

3. **Input**: `[7]`, `target_sum = 7`
   - No pairs exist since the array has only one element. Output: `[]`.

"""
