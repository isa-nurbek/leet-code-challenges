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
