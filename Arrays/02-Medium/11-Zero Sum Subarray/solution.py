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


# O(n) time | O(n) space - where `n` is the length of nums
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
