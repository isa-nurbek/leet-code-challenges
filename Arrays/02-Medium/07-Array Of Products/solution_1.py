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


# O(n^2) time | O(n) space
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

# Detailed Code Explanation:

"""
### **Explanation of the `array_of_products` Function**

The function `array_of_products` takes an array of integers as input and returns a new array where each element
at index `i` is the product of all elements in the input array *except* the one at index `i`. 

---

### **Step-by-Step Breakdown**

#### **Step 1: Initialize the `products` Array**
```
products = [1 for _ in range(len(array))]
```
- This creates a new list `products` of the same length as `array`, where each element is initially set to `1`. 
- The purpose of this list is to store the final product values.

#### **Step 2: Iterate Over Each Element of `array`**
```
for i in range(len(array)):
    running_product = 1
```
- We iterate over each index `i` of the input `array`.
- A variable `running_product` is initialized to `1`. This will store the cumulative product of all elements except `array[i]`.

#### **Step 3: Compute the Product of All Elements Except `array[i]`**
```
for j in range(len(array)):
    if i != j:
        running_product *= array[j]
```
- A nested loop iterates over every index `j` of `array`.
- If `j` is not equal to `i` (meaning we skip the current element at index `i`), we multiply `running_product` by `array[j]`.
- This effectively calculates the product of all elements in `array` except `array[i]`.

#### **Step 4: Store the Computed Product in `products`**
```
products[i] = running_product
```
- The computed `running_product` (excluding `array[i]`) is stored in `products[i]`.

#### **Step 5: Return the Final `products` Array**
```
return products
```
- After iterating through all elements, the function returns the `products` array.

---

### **Example Walkthrough**

#### **Input:** `[5, 1, 4, 2]`
We need to compute:
- `products[0] = 1 × 4 × 2 = 8`
- `products[1] = 5 × 4 × 2 = 40`
- `products[2] = 5 × 1 × 2 = 10`
- `products[3] = 5 × 1 × 4 = 20`

#### **Output:** `[8, 40, 10, 20]`

---


### **Edge Cases**

1. **Array with Zeroes:**
   ```
   print(array_of_products([0, 0, 0, 0]))
   ```
   - Since multiplication by zero results in zero, every element in the output will be `0`.
   - **Output:** `[0, 0, 0, 0]`

2. **Array with Negative Numbers:**
   ```
   print(array_of_products([-5, 2, -4, 14, -6]))
   ```
   - It correctly computes the products, considering sign changes due to multiplication.

---

### **Optimization Idea**

Instead of using **O(N²)** nested loops, we can optimize it to **O(N)** using:
1. **Left product array**: Stores cumulative product of elements to the left of each index.
2. **Right product array**: Stores cumulative product of elements to the right of each index.
3. Multiply corresponding left and right products to get the final result.

Next 2 solutions are optimized.

"""
