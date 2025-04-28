# Problem Description:

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
target_sum = 10
```

## Sample Output:
```
[-1, 11] 

// The numbers could be in reverse order
```

## Optimal Time & Space Complexity:
```
O(n) time | O(n) space - where `n` is the length of the input array
```

"""

# =========================================================================================================================== #

# Solution:


# O (n) time | O(n) space
def two_number_sum(array, target_sum):
    # Create a dictionary to keep track of the numbers we've seen so far
    nums = {}

    # Iterate through each number in the array
    for num in array:
        # Calculate the potential match that would add up to the target sum
        potential_match = target_sum - num

        # Check if the potential match is already in the dictionary
        if potential_match in nums:
            # If it is, return the pair of numbers that add up to the target sum
            return [potential_match, num]
        else:
            # If not, add the current number to the dictionary and continue
            nums[num] = True

    # If no pair is found, return an empty list
    return []


# Test Cases
print(two_number_sum([4, 6, 1, -3, 7], 3))  # Output: [6, -3]
print(two_number_sum([3, 5, -4, 8, 11, 1, -1, 6], 10))  # Output: [11, -1]
print(two_number_sum([5, 1, 4, 7, 9], 10))  # Output: [1, 9]
print(two_number_sum([7], 7))  # Output: []

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### Time Complexity:
- **O(n)**: The function iterates through the array once, where `n` is the number of elements in the array.
For each element, it performs a constant-time operation (checking if `potential_match` exists in the `nums`
dictionary and inserting the current number into the dictionary). Since dictionary lookups and insertions
are on average O(1), the overall time complexity is O(n).

### Space Complexity:
- **O(n)**: In the worst case, the function stores all elements of the array in the `nums` dictionary if no pair
is found until the last element. Therefore, the space complexity is O(n).

### Summary:
- **Time Complexity**: O(n)
- **Space Complexity**: O(n)

This implementation is efficient for finding two numbers that sum to the target value in linear time and space.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""

The provided Python code implements an efficient algorithm to solve the **Two Number Sum** problem, where the task
is to find two numbers in an array that add up to a given `target_sum`. Here's a detailed explanation of the code:

---

### Code Breakdown

#### Function Definition:
```
def two_number_sum(array, target_sum):
```
- This function takes two inputs:
  1. **`array`**: A list of integers to search through.
  2. **`target_sum`**: The target sum we want two numbers in the array to add up to.
- It returns a list containing the two numbers that sum up to `target_sum`, or an empty list if no such numbers exist.

---

#### Step 1: Create a Dictionary to Store Seen Numbers
```
nums = {}
```
- `nums` is a dictionary (hash table) that will store numbers we have already seen in the array. This allows
constant-time lookup for previously seen numbers.

---

#### Step 2: Loop Through the Array
```
for num in array:
```
- The algorithm iterates through each number in the array.

---

#### Step 3: Calculate the Potential Match
```
potential_match = target_sum - num
```
- For the current number `num`, calculate the `potential_match` such that:

    potential_match + num = target_sum

- For example, if `target_sum = 10` and `num = 3`, then `potential_match = 10 - 3 = 7`.

---

#### Step 4: Check If the Potential Match Exists
```
if potential_match in nums:
    return [potential_match, num]
```
- Check if `potential_match` is already in the `nums` dictionary:
  - If it exists, it means the two numbers (`potential_match` and `num`) sum up to the `target_sum`.
  The function immediately returns these two numbers as a list.

---

#### Step 5: Add the Current Number to the Dictionary
```
else:
    nums[num] = True
```
- If the `potential_match` is not in the dictionary, store the current number `num` in `nums` to mark it as seen.

---

#### Step 6: Return an Empty List if No Match is Found
```
return []
```
- If the loop completes without finding a pair of numbers that sum to `target_sum`, return an empty list.

---

### Example Outputs:

#### Example 1: `two_number_sum([4, 6, 1, -3, 7], 3)`

1. Initial array: `[4, 6, 1, -3, 7]`, target_sum = 3.
2. Dictionary `nums` starts empty: `{}`.
3. Iteration:
   - **4**: `potential_match = 3 - 4 = -1`. Not in `nums`. Add 4 to `nums`: `{4: True}`.
   - **6**: `potential_match = 3 - 6 = -3`. Not in `nums`. Add 6 to `nums`: `{4: True, 6: True}`.
   - **1**: `potential_match = 3 - 1 = 2`. Not in `nums`. Add 1 to `nums`: `{4: True, 6: True, 1: True}`.
   - **-3**: `potential_match = 3 - (-3) = 6`. Found in `nums`. Return `[6, -3]`.

**Output**: `[6, -3]`.

---

#### Example 2: `two_number_sum([3, 5, -4, 8, 11, 1, -1, 6], 10)`

1. Initial array: `[3, 5, -4, 8, 11, 1, -1, 6]`, target_sum = 10.
2. Dictionary `nums` starts empty: `{}`.
3. Iteration:
   - **3**: `potential_match = 10 - 3 = 7`. Not in `nums`. Add 3: `{3: True}`.
   - **5**: `potential_match = 10 - 5 = 5`. Not in `nums`. Add 5: `{3: True, 5: True}`.
   - **-4**: `potential_match = 10 - (-4) = 14`. Not in `nums`. Add -4: `{3: True, 5: True, -4: True}`.
   - **8**: `potential_match = 10 - 8 = 2`. Not in `nums`. Add 8: `{3: True, 5: True, -4: True, 8: True}`.
   - **11**: `potential_match = 10 - 11 = -1`. Not in `nums`. Add 11: `{3: True, 5: True, -4: True, 8: True, 11: True}`.
   - **1**: `potential_match = 10 - 1 = 9`. Not in `nums`. Add 1: `{3: True, 5: True, -4: True, 8: True, 11: True, 1: True}`.
   - **-1**: `potential_match = 10 - (-1) = 11`. Found in `nums`. Return `[11, -1]`.

**Output**: `[11, -1]`.

---

#### Example 3: `two_number_sum([5, 1, 4, 7, 9], 10)`

1. Initial array: `[5, 1, 4, 7, 9]`, target_sum = 10.
2. Dictionary `nums` starts empty: `{}`.
3. Iteration:
   - **5**: `potential_match = 10 - 5 = 5`. Not in `nums`. Add 5: `{5: True}`.
   - **1**: `potential_match = 10 - 1 = 9`. Not in `nums`. Add 1: `{5: True, 1: True}`.
   - **4**: `potential_match = 10 - 4 = 6`. Not in `nums`. Add 4: `{5: True, 1: True, 4: True}`.
   - **7**: `potential_match = 10 - 7 = 3`. Not in `nums`. Add 7: `{5: True, 1: True, 4: True, 7: True}`.
   - **9**: `potential_match = 10 - 9 = 1`. Found in `nums`. Return `[1, 9]`.

**Output**: `[1, 9]`.

---

#### Example 4: `two_number_sum([7], 7)`

1. Initial array: `[7]`, target_sum = 7.
2. Dictionary `nums` starts empty: `{}`.
3. Iteration:
   - **7**: `potential_match = 7 - 7 = 0`. Not in `nums`. Add 7: `{7: True}`.
4. End of loop. No pair found.

**Output**: `[]`.

---

### Key Notes:

- **Efficiency**: The use of a dictionary for lookups ensures optimal performance compared to nested loops.

"""
