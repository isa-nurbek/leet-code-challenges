# Problem Description:

"""

                                                # Four Number Sum

Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. The function
should find all quadruplets in the array that sum up to the target sum and return a two-dimensional array of all these
quadruplets in no particular order.

If no four numbers sum up to the target sum, the function should return an empty array.


## Sample Input:
```
array = [7, 6, 4, -1, 1, 2]
targetSum = 16
```

## Sample Output:
```
[[7, 6, 4, -1], [7, 6, 1, 2]] // the quadruplets could be ordered differently
```

## Optimal Time & Space Complexity:
```
Average: O(n^2) time | O(n^2) space - where `n` is the length of the input array.
Worst: O(n^3) time | O(n^2) space - where `n` is the length of the input array.
```

"""

# =========================================================================================================================== #

# Solution:


# Average: O(n^2) time | O(n^2) space
# Worst: O(n^3) time | O(1) space
def four_number_sum_sorted(array, target_sum):
    # Sort the array to make it easier to find quadruplets and avoid duplicates
    array.sort()

    # Initialize an empty list to store the quadruplets that sum up to the target
    quadruplets = []

    # Iterate through the array, leaving room for the other three numbers in the quadruplet
    for i in range(len(array) - 3):
        # Iterate through the array starting from the next element after i
        for j in range(i + 1, len(array) - 2):
            # Initialize two pointers, one at the start (left) and one at the end (right) of the remaining array
            left, right = j + 1, len(array) - 1

            # Use a two-pointer approach to find pairs that, along with array[i] and array[j], sum to the target
            while left < right:
                # Calculate the current sum of the four numbers
                current_sum = array[i] + array[j] + array[left] + array[right]

                # If the current sum matches the target, add the quadruplet to the list
                if current_sum == target_sum:
                    quadruplets.append([array[i], array[j], array[left], array[right]])
                    # Move both pointers to find other possible quadruplets
                    left += 1
                    right -= 1
                # If the current sum is less than the target, move the left pointer to the right to increase the sum
                elif current_sum < target_sum:
                    left += 1
                # If the current sum is greater than the target, move the right pointer to the left to decrease the sum
                else:
                    right -= 1

    # Return the list of quadruplets that sum up to the target
    return quadruplets


# Test Cases:

array = [7, 6, 4, -1, 1, 2]
target_sum = 16

array_2 = [1, 2, 3, 4, 5, 6, 7]
target_sum_2 = 10

array_3 = [1, 2, 3, 4, 5]
target_sum_3 = 100

print(four_number_sum_sorted(array, target_sum))
# Output: [[7, 6, 4, -1], [7, 6, 1, 2]]

print(four_number_sum_sorted(array_2, target_sum_2))
# Output: [[1, 2, 3, 4]]

print(four_number_sum_sorted(array_3, target_sum_3))
# Output: []

# =========================================================================================================================== #
