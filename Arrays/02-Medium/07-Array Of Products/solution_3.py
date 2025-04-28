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


# O(n) time | O(n) space
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

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### **Time Complexity: O(n)**
- The function iterates through the array twice:

  1. **First pass (left to right):** This pass calculates the running product of all elements to the left of each index.
  It takes **O(n)** time.
  
  2. **Second pass (right to left):** This pass calculates the running product of all elements to the right of each index
  and multiplies it with the previously computed left product. It also takes **O(n)** time.
  
- Since both passes are sequential and independent, the total time complexity is **O(n)**.

---

### **Space Complexity: O(n)**

- The function uses an additional array `products` of size `n` to store the results. This array is the only significant
extra space used.

- Apart from this, a few variables (`left_running_product`, `right_running_product`, and loop counters) are used,
but they occupy constant space (**O(1)**).

- Therefore, the total space complexity is **O(n)** due to the `products` array.

---

### **Summary**
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

This is an optimal solution for the problem, as it avoids using nested loops (which would result in O(n²) time complexity)
and achieves the result in linear time and space.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
### **Explanation of the Code**

The function `array_of_products(array)` computes a new array such that each element at index `i` is the product of all 
elements in the input array **except** the one at index `i`. This is done **without** using division. The approach
optimally solves the problem in **O(n) time complexity** and **O(n) space complexity**.

---

### **Step-by-Step Breakdown**
#### **Step 1: Initialize an Output Array**
```
products = [1 for _ in range(len(array))]
```
- We create an array `products` of the same length as the input array, initializing every element to `1`.
- This array will store the final result.

---

#### **Step 2: Compute Left Running Products**
```
left_running_product = 1
for i in range(len(array)):
    products[i] = left_running_product
    left_running_product *= array[i]
```
- `left_running_product` keeps track of the cumulative product of all elements to the **left** of `i`.
- We iterate through `array` from left to right.
- At each index `i`, we set `products[i]` to `left_running_product`.
- Then, we update `left_running_product` by multiplying it by `array[i]`.

✅ **Example Execution for Input `[5, 1, 4, 2]`**

| `i`  | `left_running_product` (Before Update) | `products[i]` | `left_running_product` (After Update) |
|------|----------------------------------------|---------------|---------------------------------------|
| 0    | 1                                      | 1             | 1 × 5 = 5                             |
| 1    | 5                                      | 5             | 5 × 1 = 5                             |
| 2    | 5                                      | 5             | 5 × 4 = 20                            |
| 3    | 20                                     | 20            | 20 × 2 = 40                           |

After this step, `products = [1, 5, 5, 20]`.

---

#### **Step 3: Compute Right Running Products and Final Result**
```
right_running_product = 1
for i in reversed(range(len(array))):
    products[i] *= right_running_product
    right_running_product *= array[i]
```
- `right_running_product` keeps track of the cumulative product of all elements to the **right** of `i`.
- We iterate through `array` from right to left.
- At each index `i`, we multiply `products[i]` by `right_running_product`.
- Then, we update `right_running_product` by multiplying it by `array[i]`.

✅ **Example Execution for Input `[5, 1, 4, 2]`**

| `i`  | `right_running_product` (Before Update) | `products[i]` (Updated) | `right_running_product` (After Update) |
|------|-----------------------------------------|-------------------------|----------------------------------------|
| 3    | 1                                       | 20 × 1 = 20             | 1 × 2 = 2                              |
| 2    | 2                                       | 5 × 2 = 10              | 2 × 4 = 8                              |
| 1    | 8                                       | 5 × 8 = 40              | 8 × 1 = 8                              |
| 0    | 8                                       | 1 × 8 = 8               | 8 × 5 = 40                             |

Final `products` array: **`[8, 40, 10, 20]`** ✅

---

### **Example Walkthroughs**

#### **Example 1: `[5, 1, 4, 2]`**

**Expected Output:** `[8, 40, 10, 20]`

| Index  | Left Products   | Right Products | Final Products |
|--------|-----------------|----------------|----------------|
| 0      | `1`             | `8`            | `1 × 8 = 8`    |
| 1      | `5`             | `8`            | `5 × 8 = 40`   |
| 2      | `5`             | `2`            | `5 × 2 = 10`   |
| 3      | `20`            | `1`            | `20 × 1 = 20`  |


#### **Example 2: `[-5, 2, -4, 14, -6]`**

**Expected Output:** `[672, -1680, 840, -240, 560]`

| Index  | Left Products   | Right Products | Final Products     |
|--------|-----------------|----------------|--------------------|
| 0      | `1`             | `672`          | `1 × 672 = 672`    |
| 1      | `-5`            | `336`          | `-5 × 336 = -1680` |
| 2      | `-10`           | `-84`          | `-10 × -84 = 840`  |
| 3      | `40`            | `-6`           | `40 × -6 = -240`   |
| 4      | `560`           | `1`            | `560 × 1 = 560`    |


#### **Example 3: `[0, 0, 0, 0]`**

**Expected Output:** `[0, 0, 0, 0]`
- Since all elements are zero, all products will be zero.

---

### **Key Takeaways**

1. **Avoids division**: Unlike a naive approach that first computes the total product and then divides by `array[i]`,
this method avoids division entirely.

2. **Efficient**: Runs in **O(n) time** and uses **O(n) space**.
3. **Uses two passes**:
   - **First pass (left products)**
   - **Second pass (right products)**

"""

# =========================================================================================================================== #

# Optimized Code (O(1) Extra Space)


# O(n) time | O(1) space - where `n` is the length of the input array
def array_of_products(array):
    n = len(array)
    products = [1] * n

    # Compute left products directly in the result array
    left_running_product = 1
    for i in range(n):
        products[i] = left_running_product
        left_running_product *= array[i]

    # Compute right products directly in the result array
    right_running_product = 1
    for i in reversed(range(n)):
        products[i] *= right_running_product
        right_running_product *= array[i]

    return products


# Test Cases:
print(array_of_products([5, 1, 4, 2]))  # Output: [8, 40, 10, 20]
print(array_of_products([-5, 2, -4, 14, -6]))  # Output: [672, -1680, 840, -240, 560]
print(array_of_products([0, 0, 0, 0]))  # Output: [0, 0, 0, 0]


"""
To optimize the space complexity from **O(n) to O(1)** (excluding the output array), we can modify the approach
so that we **reuse the output array** instead of maintaining separate arrays for left and right products.

---

## **Explanation of Optimization**

### **What Changed?**
- Previously, we used an extra array to store left products separately.
- Now, we compute **left products directly in the `products` array**.
- We then update `products` in place by multiplying with **right products**, removing the need for extra space.

### **Time and Space Complexity**
- **Time Complexity:** **O(n)** (Same as before)
- **Space Complexity:** **O(1)** (excluding the output array, since no extra storage is used)

This approach makes the function more memory-efficient while maintaining the same performance! 

"""
