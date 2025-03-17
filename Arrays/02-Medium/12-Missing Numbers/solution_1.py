# Problem Description:

"""

                                                # Missing Numbers

You're given an unordered list of unique integers `nums` in the range `[1, n]`, where `n` represents the length of `nums + 2`.
This means that two numbers in this range are missing from the list.

Write a function that takes in this list and returns a new list with the two missing numbers, sorted numerically.


## Sample Input:
```
nums = [1, 4, 3]
```

## Sample Output:
```
[2, 5]  // n is 5, meaning the completed list should be [1, 2, 3, 4, 5]
```

## Optimal Time & Space Complexity:
```
O(n) time | O(1) space - where `n` is the length of the input array.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n) time | O(n) space - where `n` is the length of the input array
def missing_numbers(nums):
    # Create a set of the numbers present in the input list for O(1) look-up time.
    included_nums = set(nums)

    # Initialize an empty list to store the missing numbers.
    solution = []

    # Iterate through the range from 1 to the length of the input list + 2.
    # The reason for adding 2 is that the problem expects exactly two missing numbers.
    for num in range(1, len(nums) + 3):
        # Check if the current number is not in the set of included numbers.
        if not num in included_nums:
            # If the number is missing, append it to the solution list.
            solution.append(num)

    # Return the list of missing numbers.
    return solution


# Test Cases:

print(missing_numbers([1, 4, 3]))
# Output: [2, 5]

print(missing_numbers([1, 2, 7, 5, 4]))
# Output: [3, 6]

print(missing_numbers([2]))
# Output: [1, 3]

print(missing_numbers([]))
# Output: [1, 2]

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### Time Complexity Analysis

1. **Creating the Set (`included_nums`)**:
   - The line `included_nums = set(nums)` converts the input list `nums` into a set. This operation takes O(n) time,
   where `n` is the length of the list `nums`, because each element in the list is inserted into the set.

2. **Iterating Through the Range**:
   - The loop `for num in range(1, len(nums) + 3)` iterates over a range of numbers from 1 to `len(nums) + 2`. The
   length of this range is (n + 2), where `n` is the length of `nums`.
   
   - Inside the loop, the operation `if not num in included_nums` checks if `num` is in the set `included_nums`.
   Checking membership in a set is an O(1) operation on average.
   
   - Therefore, the loop runs in O(n + 2) = O(n) time.

3. **Appending to the Solution List**:
   - Appending to the list `solution` is an O(1) operation, and it happens at most twice (since there are two missing numbers).

**Overall Time Complexity**:
- The dominant operation is the creation of the set and the loop, both of which are O(n). Therefore, the overall
time complexity is - O(n).

---

### Space Complexity Analysis

1. **Set (`included_nums`)**:
   - The set `included_nums` stores all the unique elements from the input list `nums`. In the worst case, this set will
   contain (n) elements, where `n` is the length of `nums`. Thus, the space required for the set is O(n).

2. **Solution List**:
   - The list `solution` stores the missing numbers. Since there are exactly two missing numbers, the space required
   for this list is O(1) (constant space).

3. **Other Variables**:
   - The loop variable `num` and other temporary variables use O(1) space.

**Overall Space Complexity**:
- The dominant space usage is the set `included_nums`, which requires O(n) space. Therefore, the overall
space complexity is - O(n).

---

### Summary

- **Time Complexity**: O(n)
- **Space Complexity**: O(n)

This implementation is efficient for finding the two missing numbers in the given range.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
### **Explanation of the Code**
The function `missing_numbers(nums)` finds the **two missing numbers** from an expected sequence of consecutive numbers
starting from 1 up to (n + 2), where `n` is the length of `nums`. 

#### **Key Observations**
1. The given list `nums` contains `n` unique numbers within the range `[1, n+2]`.
2. Since two numbers are missing from this sequence, our goal is to identify those missing numbers.
3. The function efficiently finds them using a **set-based lookup**.

---

### **Step-by-Step Breakdown**

#### **1. Store Given Numbers in a Set**
```
included_nums = set(nums)
```
- Convert `nums` into a **set** called `included_nums`. This allows for quick lookups when checking which numbers are missing.
- Using a set lookup (`num in included_nums`) is **O(1)** on average.

---

#### **2. Find Missing Numbers**
```
solution = []
for num in range(1, len(nums) + 3):
    if not num in included_nums:
        solution.append(num)
```
- The function iterates over the numbers **from 1 to (n + 2)** (where n = len(nums)).
- If a number is **not** in `included_nums`, it is added to `solution`.
- Since exactly **two numbers** will be missing, the function collects and returns them.

---

#### **3. Return the Missing Numbers**
```
return solution
```
- The function returns the list of **two missing numbers**.

---

### **Example Walkthrough**

#### **Example 1**
```
missing_numbers([1, 4, 3])
```
- Given `nums = [1, 4, 3]`
- Length of `nums` = **3**, so the range to check is **1 to 5**.
- Numbers in the range: `{1, 2, 3, 4, 5}`
- Present numbers: `{1, 3, 4}`
- **Missing numbers:** `{2, 5}`

- **Output:** `[2, 5]`

---

#### **Example 2**
```
missing_numbers([1, 2, 7, 5, 4])
```
- Given `nums = [1, 2, 7, 5, 4]`
- Length of `nums` = **5**, so the range to check is **1 to 7**.
- Numbers in the range: `{1, 2, 3, 4, 5, 6, 7}`
- Present numbers: `{1, 2, 4, 5, 7}`
- **Missing numbers:** `{3, 6}`

- **Output:** `[3, 6]`

---

#### **Example 3**
```
missing_numbers([2])
```
- Given `nums = [2]`
- Length of `nums` = **1**, so the range to check is **1 to 3**.
- Numbers in the range: `{1, 2, 3}`
- Present numbers: `{2}`
- **Missing numbers:** `{1, 3}`

- **Output:** `[1, 3]`

---

#### **Example 4**
```
missing_numbers([])
```
- Given `nums = []` (empty list)
- Length of `nums` = **0**, so the range to check is **1 to 2**.
- Numbers in the range: `{1, 2}`
- Present numbers: `{}` (empty)
- **Missing numbers:** `{1, 2}`

- **Output:** `[1, 2]`

---

### **Conclusion**
- The function correctly identifies the two missing numbers in a **range from 1 to (n+2)**.
- Uses a **set for fast lookups**, making it efficient.
- Runs in **O(n) time**, making it scalable for large lists.

"""
