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

`O(n)` time | `O(n)` space - where `n` is the length of the input array

"""


# O (n log(n)) time | O(1) space
def two_number_sum(array, target_sum):
    array.sort()
    left = 0
    right = len(array) - 1

    while left < right:
        current_sum = array[left] + array[right]
        if current_sum == target_sum:
            return [array[left], array[right]]
        elif current_sum < target_sum:
            left += 1
        elif current_sum > target_sum:
            right -= 1
    return []


print(two_number_sum([5, 1, 4, 7, 9], 10))  # Output: [1, 9]
print(two_number_sum([4, 6, 1, -3, 7], 3))  # Output: [6, -3]
print(two_number_sum([3, 5, -4, 8, 11, 1, -1, 6], 10))  # Output: [11, -1]
print(two_number_sum([7], 7))  # Output: []

# Big O:

"""

1. **Time Complexity**:
   - Sorting: O(n log(n)).
   - Two-pointer traversal: O(n).
   - Overall: O(n log(n)).

2. **Space Complexity**:
   - Sorting is in-place, so it uses O(1) additional space.

"""


# Code Explanation:

"""

The `two_number_sum` function is designed to find two numbers in an array that add up to a given `target_sum`.
It uses a two-pointer technique to achieve an efficient **O(n log(n))** time complexity and **O(1)** space complexity.
Here's a step-by-step breakdown of how it works:

---

### 1. **Input Parameters**
- **array**: A list of integers.
- **target_sum**: The desired sum of two numbers.

Example:
- Input array: `[5, 1, 4, 7, 9]`
- Target sum: `10`

---

### 2. **Sorting the Array**
```
array.sort()
```
The array is sorted in ascending order to enable the two-pointer technique. Sorting takes O(n log(n)) time.

Example:
- Original array: `[5, 1, 4, 7, 9]`
- Sorted array: `[1, 4, 5, 7, 9]`

---

### 3. **Initializing Two Pointers**
```
left = 0
right = len(array) - 1
```
- **`left` pointer**: Starts at the smallest element (index 0).
- **`right` pointer**: Starts at the largest element (last index).

For the sorted array `[1, 4, 5, 7, 9]`:
- `left` = `0` (value: `1`)
- `right` = `4` (value: `9`)

---

### 4. **Iterative Process (While Loop)**
```
while left < right:
```
The loop continues until the two pointers meet. This ensures every pair of numbers is checked without repetition.

---

### 5. **Calculate Current Sum**
```
current_sum = array[left] + array[right]
```
- Adds the elements pointed to by `left` and `right`.
- Compares `current_sum` with `target_sum`.

---

### 6. **Check Conditions**
```
if current_sum == target_sum:
    return [array[left], array[right]]
```
- If the sum matches `target_sum`, the function returns the pair.

```
elif current_sum < target_sum:
    left += 1
```
- If the sum is smaller, increment `left` to increase the sum.

```
elif current_sum > target_sum:
    right -= 1
```
- If the sum is larger, decrement `right` to decrease the sum.

---

### 7. **Return Statement**
If no pair is found after the loop ends, return an empty list:
```
return []
```

---

### Examples Walkthrough

#### **Example 1**
```
print(two_number_sum([5, 1, 4, 7, 9], 10))
```
1. Sorted array: `[1, 4, 5, 7, 9]`
2. Initial pointers: `left = 0` (1), `right = 4` (9).
3. Iteration:
   - **Current sum**: `1 + 9 = 10`. Match found!
4. Output: `[1, 9]`.

---

#### **Example 2**
```
print(two_number_sum([4, 6, 1, -3, 7], 3))
```
1. Sorted array: `[-3, 1, 4, 6, 7]`
2. Initial pointers: `left = 0` (-3), `right = 4` (7).
3. Iteration:
   - **Current sum**: `-3 + 7 = 4`. Too large; move `right`.
   - **Current sum**: `-3 + 6 = 3`. Match found!
4. Output: `[6, -3]`.

---

#### **Example 3**
```
print(two_number_sum([3, 5, -4, 8, 11, 1, -1, 6], 10))
```
1. Sorted array: `[-4, -1, 1, 3, 5, 6, 8, 11]`
2. Iteration:
   - Check pairs: `[-4, 11]`, `[-1, 11]`, `[1, 11]`, `[3, 11]`.
   - Match found: `11 + (-1) = 10`.
3. Output: `[11, -1]`.

---

#### **Example 4**
```
print(two_number_sum([7], 7))
```
1. Sorted array: `[7]`.
2. Loop does not start because `left` is not less than `right`.
3. Output: `[]` (no pair exists).

---

### Key Points

1. **Two-Pointer Technique**:
   - Efficient for sorted arrays.
   - Adjusts pointers based on comparison with `target_sum`.

2. **Edge Cases**:
   - Single element: No pair exists.
   - Empty array: Returns an empty list.
   - Multiple valid pairs: Returns the first found.

"""
