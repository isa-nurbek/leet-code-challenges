# Problem Description:

"""

                                                # Zero Sum Subarray

You're given a list of integers `nums`. Write a function that returns a boolean representing whether there exists a zero-sum
subarray of `nums`.

A zero-sum subarray is any subarray where all of the values add up to zero. A subarray is any contiguous section of the array.
For the purposes of this problem, a subarray can be as small as one element and as long as the original array.


## Sample Input:
```
nums = [-5, -5, 2, 3, -2]
```

## Sample Output:
```
True // The subarray [-5, 2, 3] has a sum of 0
```

## Optimal Time & Space Complexity:
```
O(n) time | O(n) space - where `n` is the length of nums.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n) time | O(n) space
def zero_sum_subarray(nums):
    # Create a set to store all the cumulative sums encountered so far.
    # Initialize it with 0 because a sum of 0 is needed to detect a subarray
    # that starts from the beginning of the array.
    sums = set([0])

    # Initialize a variable to keep track of the cumulative sum as we iterate through the array.
    current_sum = 0

    # Iterate through each number in the input array.
    for num in nums:
        # Add the current number to the cumulative sum.
        current_sum += num

        # Check if the current cumulative sum has been seen before.
        # If it has, it means there is a subarray whose sum is zero.
        if current_sum in sums:
            return True

        # If the current cumulative sum hasn't been seen before, add it to the set.
        sums.add(current_sum)

    # If no zero-sum subarray is found after iterating through the entire array, return False.
    return False


# Test Cases:

print(zero_sum_subarray([-5, -5, 2, 3, -2]))
# Output: True

print(zero_sum_subarray([1]))
# Output: False

print(zero_sum_subarray([1, 2, 3]))
# Output: False

print(zero_sum_subarray([2, 3, 4, -5, -3, 4, 5]))
# Output: True

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### Time Complexity Analysis

The time complexity of the `zero_sum_subarray` function is **O(n)**, where **n** is the number of elements in the 
input list `nums`.

Here's why:

1. **Initialization**: The `sums` set is initialized with `{0}`, which is a constant-time operation.
2. **Loop through `nums`**: The function iterates through the list `nums` exactly once. For each element:
   - It updates `current_sum` (an O(1) operation).
   - It checks if `current_sum` exists in the `sums` set (an O(1) operation on average for a set in Python).
   - It adds `current_sum` to the `sums` set (an O(1) operation on average for a set in Python).

Since all operations inside the loop are O(1), the total time complexity is **O(n)**.

---

### Space Complexity Analysis

The space complexity of the `zero_sum_subarray` function is **O(n)**, where **n** is the number of elements in the
input list `nums`.

Here's why:

1. **Set `sums`**: The `sums` set can grow up to the size of `n` in the worst case. For example:
   - If there are no zero-sum subarrays, all prefix sums (`current_sum`) will be unique, and the set will store all `n` prefix sums.
   - If there is a zero-sum subarray, the function will return early, but the worst-case space usage is still **O(n)**.

Thus, the space complexity is **O(n)**.

---

### Summary

- **Time Complexity**: **O(n)**
- **Space Complexity**: **O(n)**

This algorithm is efficient for finding whether a zero-sum subarray exists in a given list of numbers.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
### **Explanation of the Code**

The function `zero_sum_subarray(nums)` determines whether a contiguous subarray exists within the given list `nums` such that the
sum of the subarray is zero. It does this efficiently using a **prefix sum** approach and a **set** to store previously seen sums.

---

### **Step-by-Step Breakdown**

#### **1. Initialize Data Structures**
```
sums = set([0])
current_sum = 0
```
- `sums` is a **set** that stores prefix sums encountered so far, initialized with `{0}`.
- `current_sum` keeps track of the running sum of elements as we iterate through `nums`.

---

#### **2. Iterate Over the List**
```
for num in nums:
    current_sum += num
```
- We iterate over the array `nums` and maintain a cumulative sum (`current_sum`).

---

#### **3. Check for Zero-Sum Subarray**
```
if current_sum in sums:
    return True
```
- If `current_sum` has been seen before in `sums`, it means that some subarray sums to zero.
- Why? Because if at two different indices, the running sum is the same, then the elements between those indices must sum to zero.

---

#### **4. Store the Current Prefix Sum**
```
sums.add(current_sum)
```
- If `current_sum` is not found in `sums`, we add it to `sums` for future reference.

---

#### **5. Return False if No Zero-Sum Subarray is Found**
```
return False
```
- If we finish iterating without finding a repeated prefix sum, return `False`.

---

### **Example Walkthrough**

#### **Example 1**
```
zero_sum_subarray([-5, -5, 2, 3, -2])
```

**Steps:**

| Index  | Num  | `current_sum` | `sums` Set       | Found in Set?           |
|--------|------|---------------|------------------|-------------------------|
| 0      | -5   | -5            | {0}              | No                      |
| 1      | -5   | -10           | {0, -5}          | No                      |
| 2      | 2    | -8            | {0, -5, -10}     | No                      |
| 3      | 3    | -5            | {0, -5, -10, -8} | **Yes** (Return `True`) |

Since `-5` appeared twice, the subarray `[-5, -5, 2, 3]` sums to zero.

**Output:** `True`

---

#### **Example 2**
```
zero_sum_subarray([1])

```
| Index  | Num  | `current_sum` | `sums` Set   | Found in Set?  |
|--------|------|---------------|--------------|----------------|
| 0      | 1    | 1             | {0}          | No             |

**Output:** `False` (No subarray sums to zero)

---

#### **Example 3**
```
zero_sum_subarray([1, 2, 3])
```

| Index  | Num  | `current_sum` | `sums` Set   | Found in Set?  |
|--------|------|---------------|--------------|----------------|
| 0      | 1    | 1             | {0}          | No             |
| 1      | 2    | 3             | {0, 1}       | No             |
| 2      | 3    | 6             | {0, 1, 3}    | No             |

**Output:** `False` (No subarray sums to zero)

---

#### **Example 4**
```
zero_sum_subarray([2, 3, 4, -5, -3, 4, 5])
```

| Index  | Num  | `current_sum` | `sums` Set         | Found in Set?           |
|--------|------|---------------|--------------------|-------------------------|
| 0      | 2    | 2             | {0}                | No                      |
| 1      | 3    | 5             | {0, 2}             | No                      |
| 2      | 4    | 9             | {0, 2, 5}          | No                      |
| 3      | -5   | 4             | {0, 2, 5, 9}       | No                      |
| 4      | -3   | 1             | {0, 2, 5, 9, 4}    | No                      |
| 5      | 4    | 5             | {0, 2, 5, 9, 4, 1} | **Yes** (Return `True`) |

Since `5` appeared twice, the subarray `[4, -5, -3, 4]` sums to zero.

**Output:** `True`

---

### **Conclusion**
- This approach efficiently detects whether a zero-sum subarray exists.
- The key idea is using **prefix sums** and checking for duplicates.
- If a prefix sum repeats, the subarray between those occurrences sums to zero.

"""
