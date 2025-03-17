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
