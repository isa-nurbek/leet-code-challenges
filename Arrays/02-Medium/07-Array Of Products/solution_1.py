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

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### Time Complexity Analysis

The given function `array_of_products` calculates the product of all elements in the input array except for the
element at the current index. Let's break down the time complexity:

1. **Outer Loop**: The outer loop runs `n` times, where `n` is the length of the array.
2. **Inner Loop**: For each iteration of the outer loop, the inner loop also runs `n` times.
3. **Operations Inside Inner Loop**: Inside the inner loop, a multiplication operation is performed if `i != j`.

Since the inner loop runs `n` times for each iteration of the outer loop, the total number of operations is:

    n * n = n^2

Thus, the **time complexity** of the function is - O(n^2).

---

### Space Complexity Analysis

The space complexity is determined by the additional space used by the algorithm, excluding the input and output.

1. **Output Array**: The `products` array stores `n` elements, so it requires O(n) space.
2. **Other Variables**: The variables `running_product`, `i`, and `j` use constant space, O(1).

Since the dominant term is the `products` array, the **space complexity** is - O(n).

---

### Summary

- **Time Complexity**: O(n^2)
- **Space Complexity**: O(n)

---

### Optimized Approach

The above solution can be optimized to O(n) time complexity by using a prefix and suffix product approach.
Here's how:

1. Calculate the prefix product for each element (product of all elements to the left of the current element).
2. Calculate the suffix product for each element (product of all elements to the right of the current element).
3. Multiply the prefix and suffix products to get the final result.

This approach avoids the nested loops and reduces the time complexity to O(n).

Next solutions (solution_2, solution_3) will be optimized.

"""

# =========================================================================================================================== #
