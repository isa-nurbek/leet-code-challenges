# Problem Description:

"""

                                            Nth Fibonacci

The Fibonacci sequence is defined as follows: the first number of the sequence is `0`, the second number is `1`, and the
nth number is the sum of the (n - 1)th and (n - 2)th numbers. Write a function that takes in an integer `n` and returns
the nth Fibonacci number.

Important note: the Fibonacci sequence is often defined with its first two numbers as `F0 = 0` and `F1 = 1`. For the purpose
of this question, the first Fibonacci number is `F0`; therefore, `get_nth_fib(1)` is equal to `F0`, `get_nth_fib(2)` is
equal to `F1`, etc..


## Sample Input #1
```
n = 2
```

## Sample Output #1
```
1 // 0, 1
```

## Sample Input #2
```
n = 6
```

## Sample Output #2
```
5 // 0, 1, 1, 2, 3, 5
```

## Optimal Time & Space Complexity:
```
O(n) time | O(1) space - where `n` is the input number.
```
"""

# =========================================================================================================================== #

# Solution:


# O(n) time | O(n) space
def get_nth_fib(n, memoize={1: 0, 2: 1}):
    # Base case: if n is in our memoization dictionary, return the stored value
    if n in memoize:
        return memoize[n]
    else:
        # Recursive case: calculate Fibonacci for n by summing previous two values
        # Store the result in memoize before returning to cache it for future calls
        memoize[n] = get_nth_fib(n - 1, memoize) + get_nth_fib(n - 2, memoize)
        return memoize[n]


# Test Cases:

print(get_nth_fib(2))  # Output: 1
print(get_nth_fib(6))  # Output: 5
print(get_nth_fib(8))  # Output: 13

# =========================================================================================================================== #

# Big O Analysis:

"""

## Time and Space Complexity Analysis

### **Time Complexity: O(n)**

- **Explanation**:  
  - The function uses memoization to store previously computed Fibonacci numbers, avoiding redundant calculations.
  - For each `n`, the function computes `get_nth_fib(n)` **only once**, and subsequent calls for the same `n` take **O(1)**
  time (due to the dictionary lookup).
  - Since we compute `fib(3), fib(4), ..., fib(n)` **exactly once**, the total number of operations is **O(n)**.
  - Each addition operation (`memoize[n-1] + memoize[n-2]`) is **O(1)**.

### **Space Complexity: O(n)**

- **Explanation**:  
  - The memoization dictionary stores **O(n)** entries (from `fib(1)` to `fib(n)`).
  - The recursion depth goes up to **O(n)** (since we compute `fib(n)` → `fib(n-1)` → ... → `fib(1)`), leading
  to **O(n)** space on the call stack.
  - If optimized iteratively (instead of recursively), the space complexity can be reduced to **O(1)** 
  (but this implementation uses recursion).

### Summary:
- **Time**: O(n) 
- **Space**: O(n) 

### **Key Observations**:
1. **Memoization eliminates recomputation**, reducing time complexity from exponential (**O(2ⁿ)** in naive recursion) to **O(n)**.
2. **Recursion depth is linear**, contributing to **O(n)** space.
3. **Default argument `memoize` persists across calls**, which can be advantageous (but may cause issues if the function is
called with unexpected side effects).

### **Optimization Note**:
- If we switch to an **iterative approach**, we can achieve:
  - **Time: O(n)**
  - **Space: O(1)** (just storing the last two Fibonacci numbers).

"""
