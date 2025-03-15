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


# O(n^2) time | O(n) space - where `n` is the length of the input array
def array_of_products(array):
    # Initialize a list called 'products' with the same length as the input array.
    # Each element is set to 1 initially because we will be multiplying values.
    products = [1 for _ in range(len(array))]

    # Iterate over each element in the input array using index 'i'.
    for i in range(len(array)):
        # Initialize a variable 'running_product' to 1.
        # This will hold the product of all elements except the one at index 'i'.
        running_product = 1

        # Iterate over each element in the input array again using index 'j'.
        for j in range(len(array)):
            # If the current index 'j' is not equal to 'i', multiply the running_product
            # by the element at index 'j'. This skips the element at index 'i'.
            if i != j:
                running_product *= array[j]

        # After the inner loop completes, assign the computed running_product
        # to the corresponding position in the 'products' list.
        products[i] = running_product

    # Return the final 'products' list, which now contains the product of all elements
    # except the one at the corresponding index in the input array.
    return products


# Test Cases:

print(array_of_products([5, 1, 4, 2]))
# Output: [8, 40, 10, 20]

print(array_of_products([-5, 2, -4, 14, -6]))
# Output: [672, -1680, 840, -240, 560]

print(array_of_products([0, 0, 0, 0]))
# Output: [0, 0, 0, 0]

# =========================================================================================================================== #
