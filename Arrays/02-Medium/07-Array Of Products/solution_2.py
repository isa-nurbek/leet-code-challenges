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
    # filled with 1s. This will store the final product for each element.
    products = [1 for _ in range(len(array))]

    # Initialize a list called 'left_products' with the same length as the input array,
    # filled with 1s. This will store the product of all elements to the left of each index.
    left_products = [1 for _ in range(len(array))]

    # Initialize a list called 'right_products' with the same length as the input array,
    # filled with 1s. This will store the product of all elements to the right of each index.
    right_products = [1 for _ in range(len(array))]

    # Calculate the product of all elements to the left of each index.
    left_running_product = 1  # Start with a running product of 1.

    for i in range(len(array)):
        # Store the running product in the left_products list.
        left_products[i] = left_running_product
        # Update the running product by multiplying with the current element.
        left_running_product *= array[i]

    # Calculate the product of all elements to the right of each index.
    right_running_product = 1  # Start with a running product of 1.

    # Iterate from the end of the array to the beginning.
    for i in reversed(range(len(array))):
        # Store the running product in the right_products list.
        right_products[i] = right_running_product
        # Update the running product by multiplying with the current element.
        right_running_product *= array[i]

    # Calculate the final product for each element by multiplying the corresponding
    # left and right products.
    for i in range(len(array)):
        products[i] = left_products[i] * right_products[i]

    # Return the final list of products.
    return products


# Test Cases:

print(array_of_products([5, 1, 4, 2]))
# Output: [8, 40, 10, 20]

print(array_of_products([-5, 2, -4, 14, -6]))
# Output: [672, -1680, 840, -240, 560]

print(array_of_products([0, 0, 0, 0]))
# Output: [0, 0, 0, 0]

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### Time Complexity Analysis

1. **Initialization of Arrays**:
   - `products`, `left_products`, and `right_products` are all initialized with a size equal to the length of the input array.
   This takes O(n) time.

2. **Left Products Calculation**:
   - The loop iterates over the array once to compute the left products. This takes O(n) time.

3. **Right Products Calculation**:
   - The loop iterates over the array once in reverse to compute the right products. This also takes O(n) time.

4. **Final Products Calculation**:
   - The loop iterates over the array once to compute the final products by multiplying the corresponding left and right products.
   This takes O(n) time.

**Total Time Complexity**:
- The overall time complexity is the sum of the time complexities of the individual steps:
  
    O(n) + O(n) + O(n) + O(n) = O(n)
  
- Therefore, the time complexity is - O(n).

---

### Space Complexity Analysis

1. **Auxiliary Space**:
   - The algorithm uses three additional arrays (`products`, `left_products`, and `right_products`), each of size `n`.
   This requires O(n) space.

2. **Input Space**:
   - The input array itself is not counted towards the auxiliary space complexity.

**Total Space Complexity**:
- The space complexity is dominated by the auxiliary space used: O(n)
  
- Therefore, the space complexity is - O(n).

---

### Summary

- **Time Complexity**: O(n)
- **Space Complexity**: O(n)

This algorithm efficiently computes the product of all elements in the array except the current element
in linear time and linear space.

"""

# =========================================================================================================================== #
