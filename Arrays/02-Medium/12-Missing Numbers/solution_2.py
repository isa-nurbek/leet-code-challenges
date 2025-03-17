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
