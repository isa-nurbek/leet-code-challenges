# Problem Description:

"""

                                         # Array Of Products

Write a function that takes in a non-empty array of integers and returns an array of the same length, where
each element in the output array is equal to the product of every other number in the input array.

In other words, the value at `output[i]` is equal to the product of every number in the input array other than `input[i]`.

Note that you're expected to solve this problem without using division.


## Sample Input:
```
array = [5, 1, 4, 2]
```

## Sample Output:
```
[8, 40, 10, 20]
// 8 is equal to 1 x 4 x 2
// 40 is equal to 5 x 4 x 2
// 10 is equal to 5 x 1 x 2
// 20 is equal to 5 x 1 x 4
```

## Optimal Time & Space Complexity:
```
O(n) time | O(n) space - where `n` is the length of the input array.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n) time | O(n) space - where `n` is the length of the input array
def array_of_products(array):
    # Initialize a list called 'products' with the same length as the input array,
    # where each element is set to 1. This will store the final product values.
    products = [1 for _ in range(len(array))]

    # Initialize a variable to keep track of the running product of elements to the left of the current index.
    left_running_product = 1

    # First pass: Traverse the array from left to right.
    # For each element, store the product of all elements to its left in the 'products' array.
    for i in range(len(array)):
        # Set the current position in 'products' to the running product.
        products[i] = left_running_product
        # Update the running product to include the current element.
        left_running_product *= array[i]

    # Reset the running product variable to 1 for the second pass.
    right_running_product = 1

    # Second pass: Traverse the array from right to left.
    # For each element, multiply the existing value in 'products' (which is the product of all elements to its left)
    # by the product of all elements to its right.
    for i in reversed(range(len(array))):
        # Multiply the current value in 'products' by the running product.
        products[i] *= right_running_product
        # Update the running product to include the current element.
        right_running_product *= array[i]

    # Return the final 'products' array, which now contains the product of all elements except the one at each index.
    return products


# Test Cases:

print(array_of_products([5, 1, 4, 2]))
# Output: [8, 40, 10, 20]

print(array_of_products([-5, 2, -4, 14, -6]))
# Output: [672, -1680, 840, -240, 560]

print(array_of_products([0, 0, 0, 0]))
# Output: [0, 0, 0, 0]

# =========================================================================================================================== #
