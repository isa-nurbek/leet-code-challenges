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

# Detailed Code Explanation:

"""
### **Explanation of `array_of_products` Function**

The `array_of_products` function computes a new array where each element at index `i` is the product of all numbers in the input
array **except** the number at index `i`. The function does **not** use division to avoid issues with zero division errors.

---

### **Step-by-Step Breakdown**

#### **1. Initializing Arrays**
```
products = [1 for _ in range(len(array))]
left_products = [1 for _ in range(len(array))]
right_products = [1 for _ in range(len(array))]
```
- The function first initializes three lists of the same length as `array`:
  - `products`: Stores the final result.
  - `left_products`: Stores the product of all elements **to the left** of index `i`.
  - `right_products`: Stores the product of all elements **to the right** of index `i`.

Example for `array = [5, 1, 4, 2]`:
```
products       = [1, 1, 1, 1]
left_products  = [1, 1, 1, 1]
right_products = [1, 1, 1, 1]
```

---

#### **2. Filling `left_products`**
```
left_running_product = 1
for i in range(len(array)):
    left_products[i] = left_running_product
    left_running_product *= array[i]
```
- This loop iterates over the array from **left to right**.
- It maintains `left_running_product`, which stores the cumulative product of elements before index `i`.

##### **Step-by-step for `[5, 1, 4, 2]`**

| Index  | `left_running_product` (before update) | `left_products[i]` | `left_running_product` (after update) |
|--------|----------------------------------------|--------------------|---------------------------------------|
| 0      | 1                                      | 1                  | 1 × 5 = 5                             |
| 1      | 5                                      | 5                  | 5 × 1 = 5                             |
| 2      | 5                                      | 5                  | 5 × 4 = 20                            |
| 3      | 20                                     | 20                 | 20 × 2 = 40                           |

After this step, `left_products` becomes:
```
[1, 5, 5, 20]
```

---

#### **3. Filling `right_products`**
```
right_running_product = 1
for i in reversed(range(len(array))):
    right_products[i] = right_running_product
    right_running_product *= array[i]
```
- This loop iterates from **right to left**.
- It maintains `right_running_product`, which stores the cumulative product of elements after index `i`.

##### **Step-by-step for `[5, 1, 4, 2]`**

| Index  | `right_running_product` (before update) | `right_products[i]` | `right_running_product` (after update) |
|--------|-----------------------------------------|---------------------|----------------------------------------|
| 3      | 1                                       | 1                   | 1 × 2 = 2                              |
| 2      | 2                                       | 2                   | 2 × 4 = 8                              |
| 1      | 8                                       | 8                   | 8 × 1 = 8                              |
| 0      | 8                                       | 8                   | 8 × 5 = 40                             |

After this step, `right_products` becomes:
```
[8, 8, 2, 1]
```

---

#### **4. Computing Final `products`**
```
for i in range(len(array)):
    products[i] = left_products[i] * right_products[i]
```
- Each element at index `i` in `products` is calculated as:
  products[i] = left_products[i] * right_products[i]

##### **Final Computation for `[5, 1, 4, 2]`**

| Index  | `left_products[i]` | `right_products[i]` | `products[i]` |
|--------|--------------------|---------------------|---------------|
| 0      | 1                  | 8                   | 1 × 8  = 8    |
| 1      | 5                  | 8                   | 5 × 8  = 40   |
| 2      | 5                  | 2                   | 5 × 2  = 10   |
| 3      | 20                 | 1                   | 20 × 1 = 20   |

Final `products` array:
```
[8, 40, 10, 20]
```

---

### **Test Cases & Explanation**

#### **Test Case 1: `[5, 1, 4, 2]`**
Output:
```
[8, 40, 10, 20]
```
(Explained above)

#### **Test Case 2: `[-5, 2, -4, 14, -6]`**

##### **Step-by-step**
1. `left_products`: `[1, -5, -10, 40, 560]`
2. `right_products`: `[-672, 336, -84, -6, 1]`
3. `products`: `left_products[i] * right_products[i]`
   ```
   [672, -1680, 840, -240, 560]
   ```

#### **Test Case 3: `[0, 0, 0, 0]`**

- Any product that includes a zero is zero.
- Every element has at least one zero in the array.
- The output is:
  ```
  [0, 0, 0, 0]
  ```

---

### **Alternative Optimization (Space Efficient)**
Instead of using `left_products` and `right_products`, we can compute `products` in two passes using a single array:

1. Compute **left running product** directly into `products`.
2. Multiply it with a **right running product** in a second pass.

```
def optimized_array_of_products(array):
    n = len(array)
    products = [1] * n

    left_running_product = 1
    for i in range(n):
        products[i] = left_running_product
        left_running_product *= array[i]

    right_running_product = 1
    for i in reversed(range(n)):
        products[i] *= right_running_product
        right_running_product *= array[i]

    return products
```

- **Space Complexity:** O(1) auxiliary space (excluding output array)
- **Time Complexity:** O(n)

---

### **Conclusion**
- The function effectively computes the product of all elements except the current one **without using division**.
- It uses **left and right product arrays** to store intermediate values.
- The optimized version reduces space usage to **O(1)**.

"""
