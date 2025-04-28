# Problem Description:

"""

                                        Three Number Sum

Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. The
function should find all triplets in the array that sum up to the target sum and return a two-dimensional array of
all these triplets. The numbers in each triplet should be ordered in ascending order, and the triplets themselves
should be ordered in ascending order with respect to the numbers they hold.

If no three numbers sum up to the target sum, the function should return an empty array.


## Sample Input:
```
array = [12, 3, 1, 2, -6, 5, -8, 6]
target_sum = 0
```

## Sample Output:
```
[[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
```

## Optimal Time & Space Complexity:
```
O(n^2) time | O(n) space - where `n`  is the length of the input array.
```

"""

# =========================================================================================================================== #

# Solution:


# `O(n²)` time | `O(n)` space
def three_number_sum(array, target_sum):
    # Sort the array to make it easier to find the triplets
    array.sort()
    triplets = []

    # Iterate through the array, leaving room for the left and right pointers
    for i in range(len(array) - 2):
        # Initialize the left and right pointers
        left = i + 1
        right = len(array) - 1

        # Use a while loop to find all possible triplets for the current i
        while left < right:
            # Calculate the current sum of the three numbers
            current_sum = array[i] + array[left] + array[right]

            # If the current sum matches the target sum, add the triplet to the list
            if current_sum == target_sum:
                triplets.append([array[i], array[left], array[right]])
                # Move both pointers to find other possible triplets
                left += 1
                right -= 1
            # If the current sum is less than the target, move the left pointer to the right
            elif current_sum < target_sum:
                left += 1
            # If the current sum is greater than the target, move the right pointer to the left
            elif current_sum > target_sum:
                right -= 1

    # Return the list of triplets that sum up to the target
    return triplets


# Test cases
print(three_number_sum([12, 3, 1, 2, -6, 5, -8, 6], 0))
# Output: [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]

print(three_number_sum([1, 2, 3], 6))
# Output: [[1, 2, 3]]

print(three_number_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 18))
#   Output: [
#       [1, 2, 15], [1, 8, 9],
#       [2, 7, 9], [3, 6, 9],
#       [3, 7, 8], [4, 5, 9],
#       [4, 6, 8], [5, 6, 7],
#   ]

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### Time Complexity:

The time complexity of the `three_number_sum` function is **O(n^2)**, where `n` is the length of the input array.

Here's why:

1. **Sorting the array**: The initial sorting step takes **O(n log n)** time.
2. **Nested loops**:
   - The outer loop runs **O(n)** times (from `i = 0` to `i = len(array) - 2`).
   - The inner `while` loop runs in **O(n)** time in the worst case (since `left` and `right` pointers traverse the array).
   - Together, the nested loops contribute **O(n^2)** time complexity.

Since **O(n^2)** dominates **O(n log n)**, the overall time complexity is **O(n^2)**.

---

### Space Complexity:

The space complexity is **O(n)** in the worst case, where `n` is the length of the input array. Here's why:

1. **Sorting**: Sorting typically uses **O(log n)** space (for the sorting algorithm's internal stack).

2. **Output storage**: The `triplets` list can store up to **O(n)** triplets in the worst case (e.g., if all triplets
sum to the target).

Thus, the space complexity is **O(n)** due to the output storage.

---

### Summary:
- **Time Complexity**: **O(n^2)**
- **Space Complexity**: **O(n)** (due to the output storage)

This algorithm is efficient for finding all triplets that sum to the target value.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
The `three_number_sum` function is designed to find all unique triplets in an array that sum up to a given target value.
Here's a detailed explanation of how the code works:

---

### **Step-by-Step Explanation**

#### **1. Input Parameters**
- `array`: The input list of integers.
- `target_sum`: The target sum that the triplets should add up to.

#### **2. Sorting the Array**
```
array.sort()
```
- The array is sorted in ascending order. Sorting is crucial because it allows us to use the **two-pointer technique**
to efficiently find triplets.

#### **3. Initialize the Result List**
```
triplets = []
```
- This list will store all the valid triplets that sum up to the `target_sum`.

#### **4. Outer Loop: Fixing the First Number**
```
for i in range(len(array) - 2):
```
- The outer loop iterates through the array, fixing the first number of the triplet (`array[i]`).
- The loop runs up to `len(array) - 2` because we need at least two more numbers to form a triplet.

#### **5. Two-Pointer Technique**
```
left = i + 1
right = len(array) - 1
```
- For each fixed number (`array[i]`), we initialize two pointers:
  - `left`: Starts just after the fixed number (`i + 1`).
  - `right`: Starts at the end of the array.

#### **6. Inner Loop: Finding Triplets**
```
while left < right:
    current_sum = array[i] + array[left] + array[right]
```
- The inner loop uses the two-pointer technique to find pairs (`array[left]` and `array[right]`) that, when
added to `array[i]`, equal the `target_sum`.

#### **7. Checking the Current Sum**
- **Case 1: `current_sum == target_sum`**
  ```
  if current_sum == target_sum:
      triplets.append([array[i], array[left], array[right]])
      left += 1
      right -= 1
  ```
  - If the sum of the three numbers equals the `target_sum`, we add the triplet `[array[i], array[left], array[right]]`
  to the `triplets` list.
  - Move both pointers (`left` and `right`) to find other possible triplets.

- **Case 2: `current_sum < target_sum`**
  ```
  elif current_sum < target_sum:
      left += 1
  ```
  - If the sum is less than the `target_sum`, move the `left` pointer to the right to increase the sum.

- **Case 3: `current_sum > target_sum`**
  ```
  elif current_sum > target_sum:
      right -= 1
  ```
  - If the sum is greater than the `target_sum`, move the `right` pointer to the left to decrease the sum.

#### **8. Returning the Result**
```
return triplets
```
- After the loops complete, the function returns the list of all valid triplets.

---

### **Example Walkthrough**

#### **Example 1**
```
print(three_number_sum([12, 3, 1, 2, -6, 5, -8, 6], 0))
```
- **Sorted Array**: `[-8, -6, 1, 2, 3, 5, 6, 12]`
- **Triplets Found**:
  1. `[-8, 2, 6]` (sum = 0)
  2. `[-8, 3, 5]` (sum = 0)
  3. `[-6, 1, 5]` (sum = 0)
- **Output**: `[[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]`

#### **Example 2**
```
print(three_number_sum([1, 2, 3], 6))
```
- **Sorted Array**: `[1, 2, 3]`
- **Triplets Found**:
  1. `[1, 2, 3]` (sum = 6)
- **Output**: `[[1, 2, 3]]`

#### **Example 3**
```
print(three_number_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 18))
```
- **Sorted Array**: `[1, 2, 3, 4, 5, 6, 7, 8, 9, 15]`
- **Triplets Found**:
  1. `[1, 2, 15]` (sum = 18)
  2. `[1, 8, 9]` (sum = 18)
  3. `[2, 7, 9]` (sum = 18)
  4. `[3, 6, 9]` (sum = 18)
  5. `[3, 7, 8]` (sum = 18)
  6. `[4, 5, 9]` (sum = 18)
  7. `[4, 6, 8]` (sum = 18)
  8. `[5, 6, 7]` (sum = 18)
- **Output**: `[[1, 2, 15], [1, 8, 9], [2, 7, 9], [3, 6, 9], [3, 7, 8], [4, 5, 9], [4, 6, 8], [5, 6, 7]]`

---

### **Key Points**
- Sorting the array enables the use of the two-pointer technique.
- The two-pointer technique reduces the problem from `O(n^3)` to `O(n^2)`.
- The function efficiently finds all unique triplets that sum to the target value.

"""
