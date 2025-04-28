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
    # Calculate the total sum of numbers from 1 to n+2, where n is the length of the input list.
    # Since there are two missing numbers, the range should be 1 to len(nums) + 2.
    total = sum(range(1, len(nums) + 3))

    # Subtract each number in the input list from the total.
    # The remaining value will be the sum of the two missing numbers.
    for num in nums:
        total -= num

    # Find the average of the two missing numbers.
    # This helps in dividing the problem into two halves: one half for numbers less than or equal to the average,
    # and the other half for numbers greater than the average.
    average_missing_value = total // 2

    # Initialize variables to store the sum of numbers in the first half (<= average) and the second half (> average).
    found_first_half = 0
    found_second_half = 0

    # Iterate through the input list and sum the numbers in the first half and the second half.
    for num in nums:
        if num <= average_missing_value:
            found_first_half += num
        else:
            found_second_half += num

    # Calculate the expected sum of numbers in the first half (1 to average_missing_value).
    expected_first_half = sum(range(1, average_missing_value + 1))

    # Calculate the expected sum of numbers in the second half (average_missing_value + 1 to len(nums) + 2).
    expected_second_half = sum(range(average_missing_value + 1, len(nums) + 3))

    # The difference between the expected sum and the found sum in each half will give the two missing numbers.
    return [
        expected_first_half - found_first_half,
        expected_second_half - found_second_half,
    ]


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

1. **Sum Calculation**:
   - `total = sum(range(1, len(nums) + 3))`: This operation sums all numbers from 1 to `len(nums) + 2`. The sum of the 
   first `n` natural numbers is `n (n + 1) / 2`, so this operation is - O(n), where `n` is the length of `nums`.

2. **Subtracting Elements**:
   - `for num in nums: total -= num`: This loop iterates over each element in `nums` and subtracts it from `total`.
   This is also - O(n).

3. **Finding the Average Missing Value**:
   - `average_missing_value = total // 2`: This is a constant-time operation, O(1).

4. **Summing First and Second Halves**:
   - The loop `for num in nums:` iterates over each element in `nums` and adds it to either `found_first_half` or
   `found_second_half` based on the condition `if num <= average_missing_value`. This is - O(n).

5. **Expected Sum Calculation**:
   - `expected_first_half = sum(range(1, average_missing_value + 1))`: This sums numbers from 1 to `average_missing_value`,
   which is - O(n).
   
   - `expected_second_half = sum(range(average_missing_value + 1, len(nums) + 3))`: This sums numbers from
   `average_missing_value + 1` to `len(nums) + 2`, which is also - O(n).

6. **Returning the Result**:
   - The final return statement is - O(1).

---

### Space Complexity Analysis

1. **Variables**:
   - The variables `total`, `average_missing_value`, `found_first_half`, `found_second_half`, `expected_first_half`, and
   `expected_second_half` all use constant space, O(1).

2. **Input and Output**:
   - The input list `nums` is not modified, and the output is a list of two integers. The space used by the input and
   output is - O(n) for the input and O(1) for the output.

---

### Summary

- **Time Complexity**: O(n)
  - The dominant operations are the loops and sum calculations, all of which are linear in terms of the input size `n`.

- **Space Complexity**: O(1)
  - The algorithm uses a constant amount of extra space regardless of the input size.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
### **Explanation of the Code**

The function `missing_numbers(nums)` is designed to find the **two missing numbers** from a sequence of consecutive
numbers ranging from **1 to (n+2)**, where `n` is the length of the input list `nums`. Instead of using a set, 
it **calculates the missing numbers using arithmetic properties**.

---

### **Step-by-Step Breakdown**

#### **1. Compute the Total Sum of the Expected Range**
```
total = sum(range(1, len(nums) + 3))
```
- This calculates the sum of the first `(n + 2)` natural numbers.
- The sum of the first `m` natural numbers is given by the formula:
  
    S = m (m + 1) / 2
  
- Since two numbers are missing, the difference between this total and the sum of `nums` will give the
**sum of the two missing numbers**.

---

#### **2. Subtract the Given Numbers from the Total Sum**
```
for num in nums:
    total -= num
```
- This reduces `total` by removing all the numbers that are present in `nums`.
- Now, `total` contains the sum of the **two missing numbers**.

---

#### **3. Find the Average of the Two Missing Numbers**
```
average_missing_value = total // 2
```
- Since the two missing numbers add up to `total`, they must be **split into two groups**:
  - One group contains numbers **≤ `average_missing_value`**.
  - The other group contains numbers **> `average_missing_value`**.
- This helps in breaking the problem into two halves.

---

#### **4. Compute the Sum of Found Numbers in Each Half**
```
found_first_half = 0
found_second_half = 0

for num in nums:
    if num <= average_missing_value:
        found_first_half += num
    else:
        found_second_half += num
```
- The numbers in `nums` are split into two categories:
  - `found_first_half`: Sum of numbers **≤ `average_missing_value`**.
  - `found_second_half`: Sum of numbers **> `average_missing_value`**.

---

#### **5. Compute the Expected Sums for Each Half**
```
expected_first_half = sum(range(1, average_missing_value + 1))
expected_second_half = sum(range(average_missing_value + 1, len(nums) + 3))
```
- These are the expected sums **if no numbers were missing**.
- `expected_first_half`: The sum of all numbers **≤ `average_missing_value`**.
- `expected_second_half`: The sum of all numbers **> `average_missing_value`**.

---

#### **6. Find the Two Missing Numbers**
```
return [
    expected_first_half - found_first_half,
    expected_second_half - found_second_half,
]
```
- The missing numbers are found by subtracting the **sum of found numbers** from the **expected sums**.
- This gives the two missing numbers.

---

### **Example Walkthrough**

#### **Example 1**
```
missing_numbers([1, 4, 3])
```
1. Compute total sum:
   ```
   total = sum([1, 2, 3, 4, 5]) = 15
   total -= (1 + 4 + 3) → total = 15 - 8 = 7
   ```
   - The missing numbers add up to **7**.
   
2. Compute `average_missing_value`:
   ```
   average_missing_value = 7 // 2 = 3
   ```
   
3. Split `nums` into two groups:
   - Numbers ≤ 3: `{1, 3}`, sum = `4`
   - Numbers > 3: `{4}`, sum = `4`
   
4. Compute expected sums:
   ```
   expected_first_half = sum([1, 2, 3]) = 6
   expected_second_half = sum([4, 5]) = 9
   ```
   
5. Find missing numbers:
   ```
   missing_1 = 6 - 4 = 2
   missing_2 = 9 - 4 = 5
   ```

**Output:** `[2, 5]`

---

#### **Example 2**
```
missing_numbers([1, 2, 7, 5, 4])
```
1. Compute total sum:
   ```
   total = sum([1, 2, 3, 4, 5, 6, 7]) = 28
   total -= (1 + 2 + 7 + 5 + 4) → total = 28 - 19 = 9
   ```
   - The missing numbers add up to **9**.

2. Compute `average_missing_value`:
   ```
   average_missing_value = 9 // 2 = 4
   ```
   
3. Split `nums` into two groups:
   - Numbers ≤ 4: `{1, 2, 4}`, sum = `7`
   - Numbers > 4: `{5, 7}`, sum = `12`
   
4. Compute expected sums:
   ```
   expected_first_half = sum([1, 2, 3, 4]) = 10
   expected_second_half = sum([5, 6, 7]) = 18
   ```
   
5. Find missing numbers:
   ```
   missing_1 = 10 - 7 = 3
   missing_2 = 18 - 12 = 6
   ```

**Output:** `[3, 6]`

---

#### **Example 3**
```
missing_numbers([2])
```
1. Compute total sum:
   ```
   total = sum([1, 2, 3]) = 6
   total -= 2 → total = 6 - 2 = 4
   ```
   - The missing numbers add up to **4**.

2. Compute `average_missing_value`:
   ```
   average_missing_value = 4 // 2 = 2
   ```
   
3. Split `nums` into two groups:
   - Numbers ≤ 2: `{2}`, sum = `2`
   - No numbers > 2.
   
4. Compute expected sums:
   ```
   expected_first_half = sum([1, 2]) = 3
   expected_second_half = sum([3]) = 3
   ```
   
5. Find missing numbers:
   ```
   missing_1 = 3 - 2 = 1
   missing_2 = 3 - 0 = 3
   ```

**Output:** `[1, 3]`

---

#### **Example 4**
```
missing_numbers([])
```
1. Compute total sum:
   ```
   total = sum([1, 2]) = 3
   ```
   - The missing numbers add up to **3**.

2. Compute `average_missing_value`:
   ```
   average_missing_value = 3 // 2 = 1
   ```
   
3. Compute expected sums:
   ```
   expected_first_half = sum([1]) = 1
   expected_second_half = sum([2]) = 2
   ```
   
4. Find missing numbers:
   ```
   missing_1 = 1 - 0 = 1
   missing_2 = 2 - 0 = 2
   ```

**Output:** `[1, 2]`

---

### **Conclusion**
- The function efficiently finds the two missing numbers in **O(n) time**.
- It uses **arithmetic properties** to calculate missing numbers instead of a set.
- It correctly divides the numbers into two halves to determine the missing values.

"""
