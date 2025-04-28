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
[2, 5]  

// n is 5, meaning the completed list should be [1, 2, 3, 4, 5]
```

## Optimal Time & Space Complexity:
```
O(n) time | O(1) space - where `n` is the length of the input array.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n) time | O(1) space
def missing_numbers(nums):
    # Initialize the XOR variable to store the result of XOR operations
    solution_XOR = 0

    # Iterate through the range of numbers from 0 to len(nums) + 2
    # We add 3 because the array is missing two numbers, so the range should be len(nums) + 2
    for i in range(0, len(nums) + 3):
        # XOR the current index with solution_XOR
        solution_XOR ^= i

        # If the current index is within the bounds of the nums array, XOR the element at that index
        if i < len(nums):
            solution_XOR ^= nums[i]

    # At this point, solution_XOR will be the XOR of the two missing numbers
    # Now, we need to find the two missing numbers using the XOR result

    # Initialize a list to store the two missing numbers
    solution = [0, 0]

    # Find the rightmost set bit in solution_XOR
    # This bit will be different between the two missing numbers
    set_bit = solution_XOR & -solution_XOR

    # Iterate through the range again to separate the numbers into two groups based on the set_bit
    for i in range(0, len(nums) + 3):
        # If the current index has the set_bit not set, XOR it with solution[0]
        if i & set_bit == 0:
            solution[0] ^= i
        # Otherwise, XOR it with solution[1]
        else:
            solution[1] ^= i

        # If the current index is within the bounds of the nums array, do the same for the elements in nums
        if i < len(nums):
            if nums[i] & set_bit == 0:
                solution[0] ^= nums[i]
            else:
                solution[1] ^= nums[i]

    # Return the sorted list of the two missing numbers
    return sorted(solution)


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

The function `missing_numbers` can be broken down into the following steps:

1. **First Loop (XOR Calculation):**
   - This loop runs from `0` to `len(nums) + 2` (inclusive).
   - The loop performs a constant number of operations (XOR) per iteration.
   - The loop runs `len(nums) + 3` times.
   
   - Time complexity: **O(N)**, where `N` is the length of `nums`.

2. **Second Loop (Partitioning and XOR Calculation):**
   - This loop also runs from `0` to `len(nums) + 2` (inclusive).
   - The loop performs a constant number of operations (XOR and bitwise AND) per iteration.
   - The loop runs `len(nums) + 3` times.
   
   - Time complexity: **O(N)**, where `N` is the length of `nums`.

3. **Sorting the Result:**
   - The final step sorts the `solution` array, which contains exactly 2 elements.
   - Sorting 2 elements is a constant-time operation.
   
   - Time complexity: **O(1)**.

### Overall Time Complexity:
- The dominant part of the algorithm is the two loops, each running in **O(N)** time.

- Therefore, the overall time complexity is **O(N)**.

---

### Space Complexity Analysis

1. **Variables:**
   - `solution_XOR`, `set_bit`, and `solution` are the main variables used.
   - These variables use a constant amount of space.
   
   - Space complexity: **O(1)**.

2. **Input:**
   - The input `nums` is not modified, so it does not contribute to additional space usage.

### Overall Space Complexity:
- The algorithm uses a constant amount of extra space.

- Therefore, the space complexity is **O(1)**.

---

### Summary:
- **Time Complexity:** **O(N)**
- **Space Complexity:** **O(1)**

This algorithm is efficient for finding the two missing numbers in a sequence of integers.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
### **Explanation of the Code**
This function finds the **two missing numbers** in an array of distinct numbers ranging from `1` to `n+2` using **XOR operations**.
It follows an optimized approach with **O(n) time complexity** and **O(1) space complexity**.

---

### **Step-by-Step Breakdown**
The function leverages **bitwise XOR properties** to efficiently determine the two missing numbers.

#### **1. Compute XOR of all numbers (Expected and Given)**
```
solution_XOR = 0

for i in range(0, len(nums) + 3):
    solution_XOR ^= i

    if i < len(nums):
        solution_XOR ^= nums[i]
```
- This initializes `solution_XOR = 0`.
- The loop runs from `0` to `(n+2)`, where `n = len(nums)`.
- It XORs **all numbers in the full expected range**.
- Then, it XORs **all numbers present in `nums`**.
- The result `solution_XOR` will be the XOR of the two missing numbers.

#### **Key XOR Property Used**
- `a ^ a = 0` (same numbers cancel out)
- `a ^ 0 = a` (XOR with zero leaves the number unchanged)

Thus, after XORing everything, `solution_XOR = missing1 ^ missing2`.

---

#### **2. Find a Set Bit to Differentiate the Two Missing Numbers**
```
set_bit = solution_XOR & -solution_XOR
```
- `solution_XOR` contains `missing1 ^ missing2`.
- The expression `solution_XOR & -solution_XOR` isolates the **rightmost set bit** in `solution_XOR`.
- This helps differentiate the two missing numbers.

Example:
- Suppose `solution_XOR = 6` (binary: `110`).
- `-solution_XOR` in two's complement is `010`.
- `solution_XOR & -solution_XOR` gives `010` (i.e., the rightmost set bit).

---

#### **3. Separate Numbers into Two Groups**
```
solution = [0, 0]

for i in range(0, len(nums) + 3):
    if i & set_bit == 0:
        solution[0] ^= i
    else:
        solution[1] ^= i

    if i < len(nums):
        if nums[i] & set_bit == 0:
            solution[0] ^= nums[i]
        else:
            solution[1] ^= nums[i]
```
- We use `set_bit` to divide numbers into **two separate groups**:
  - **Group 1:** Numbers where the rightmost set bit is **0**.
  - **Group 2:** Numbers where the rightmost set bit is **1**.
- Each group XORs all numbers within it.
- Since each group is missing exactly **one number**, XORing cancels out all duplicates, leaving the missing numbers.

---

#### **4. Return Sorted Missing Numbers**
```
return sorted(solution)
```
- Sorting ensures a consistent output format.

---

### **Example Walkthrough**

#### **Example 1: `missing_numbers([1, 4, 3])`**

1. Expected range: `[1, 2, 3, 4, 5]`
2. Given `nums = [1, 4, 3]`
3. Compute XOR of all numbers:
   ```
   solution_XOR = 1 ^ 2 ^ 3 ^ 4 ^ 5 ^ 1 ^ 4 ^ 3
                = (1 ^ 1) ^ (3 ^ 3) ^ (4 ^ 4) ^ 2 ^ 5
                = 0 ^ 0 ^ 0 ^ 2 ^ 5
                = 2 ^ 5 = 7
   ```
4. Find rightmost set bit:
   ```
   set_bit = 7 & -7 = 1  (binary: 011 & 101 = 001)
   ```
5. Separate into two groups:
   - **Group 1 (bit = 0):** `[2]`
   - **Group 2 (bit = 1):** `[5]`
6. Missing numbers: `[2, 5]`

**Output:** `[2, 5]`

---

#### **Example 2: `missing_numbers([1, 2, 7, 5, 4])`**

1. Expected range: `[1, 2, 3, 4, 5, 6, 7]`
2. Given `nums = [1, 2, 7, 5, 4]`
3. Compute XOR of all numbers:
   ```
   solution_XOR = 1 ^ 2 ^ 3 ^ 4 ^ 5 ^ 6 ^ 7 ^ 1 ^ 2 ^ 7 ^ 5 ^ 4
                = (1 ^ 1) ^ (2 ^ 2) ^ (4 ^ 4) ^ (5 ^ 5) ^ (7 ^ 7) ^ 3 ^ 6
                = 0 ^ 0 ^ 0 ^ 0 ^ 0 ^ 3 ^ 6
                = 3 ^ 6 = 5
   ```
4. Find rightmost set bit:
   ```
   set_bit = 5 & -5 = 1  (binary: 101 & 011 = 001)
   ```
5. Separate into two groups:
   - **Group 1 (bit = 0):** `[3]`
   - **Group 2 (bit = 1):** `[6]`
6. Missing numbers: `[3, 6]`

**Output:** `[3, 6]`

---

#### **Example 3: `missing_numbers([2])`**

1. Expected range: `[1, 2, 3]`
2. Given `nums = [2]`
3. Compute XOR of all numbers:
   ```
   solution_XOR = 1 ^ 2 ^ 3 ^ 2
                = (2 ^ 2) ^ 1 ^ 3
                = 0 ^ 1 ^ 3
                = 1 ^ 3 = 2
   ```
4. Find rightmost set bit:
   ```
   set_bit = 2 & -2 = 2  (binary: 010 & 110 = 010)
   ```
5. Separate into two groups:
   - **Group 1 (bit = 0):** `[1]`
   - **Group 2 (bit = 1):** `[3]`
6. Missing numbers: `[1, 3]`

**Output:** `[1, 3]`

---

#### **Example 4: `missing_numbers([])`**

1. Expected range: `[1, 2]`
2. Given `nums = []`
3. Compute XOR of all numbers:
   ```
   solution_XOR = 1 ^ 2 = 3
   ```
4. Find rightmost set bit:
   ```
   set_bit = 3 & -3 = 1  (binary: 011 & 101 = 001)
   ```
5. Separate into two groups:
   - **Group 1 (bit = 0):** `[2]`
   - **Group 2 (bit = 1):** `[1]`
6. Missing numbers: `[1, 2]`

**Output:** `[1, 2]`

---

### **Conclusion**
- Uses **XOR operations** for an efficient O(n) solution.
- Avoids extra space, making it better than set-based approaches.
- Ensures correctness by leveraging **bitwise separation**.

This is an **optimal and clever** way to solve the missing numbers problem.

"""
