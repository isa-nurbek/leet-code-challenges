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


# O(n) time | O(1) space - where `n` is the length of the input array
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
