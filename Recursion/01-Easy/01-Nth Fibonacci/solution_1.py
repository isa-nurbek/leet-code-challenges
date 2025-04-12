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


# O(2ⁿ) time | O(n) space
def get_nth_fib(n):
    # Base case: when n is 2, return 1 (2nd Fibonacci number is 1)
    if n == 2:
        return 1
    # Base case: when n is 1, return 0 (1st Fibonacci number is 0)
    elif n == 1:
        return 0
    else:
        # Recursive case: Fibonacci number is sum of previous two Fibonacci numbers
        return get_nth_fib(n - 1) + get_nth_fib(n - 2)


# Test Cases
print(get_nth_fib(2))  # Output: 1
print(get_nth_fib(6))  # Output: 5
print(get_nth_fib(8))  # Output: 13

# =========================================================================================================================== #

# Big O Analysis:

"""

## Time and Space Complexity Analysis

### Time Complexity: O(2ⁿ)

This is because each call to `get_nth_fib` makes two more recursive calls (to `n-1` and `n-2`), leading to an exponential
growth in the number of function calls. 

- For `n`, the number of calls roughly doubles with each increase in `n`, forming a binary tree of calls with depth `n`.
- The exact number of operations is actually O(ϕⁿ), where ϕ (phi) is the golden ratio (~1.618), but we simplify this
to O(2ⁿ) in Big-O notation since exponential growth dominates.

### Space Complexity: O(n)

This is due to the maximum depth of the recursion stack.

- Each recursive call adds a new frame to the call stack, and the deepest the stack gets is `n` levels
(e.g., `get_nth_fib(n)` → `get_nth_fib(n-1)` → ... → `get_nth_fib(1)`).
- No additional space is used beyond the call stack, so the space complexity is linear with respect to `n`.

### Why Not O(2^n) Space?

You might wonder why the space complexity isn't also exponential. This is because the recursion stack only keeps track
of one path from the root to a leaf in the call tree at any given time. Once a branch is fully resolved, its stack frames
are popped off, and new ones are added for the next branch.

### Example for `n = 5`:

The call tree looks like this:
```
                     fib(5)
                   /        \
              fib(4)         fib(3)
             /      \        /     \
        fib(3)     fib(2)  fib(2)  fib(1)
       /     \
   fib(2)   fib(1)
```
- The longest path is `fib(5) → fib(4) → fib(3) → fib(2) → fib(1)`, which has a depth of 4 (or `n-1`). Hence,
the space complexity is O(n).

### Key Takeaway:
- **Time**: O(2ⁿ) (exponential time, very inefficient for large `n`).
- **Space**: O(n) (linear space due to recursion stack depth).

### Better Approaches:

This recursive approach is highly inefficient. You can improve it using:
1. **Memoization (Top-Down DP)**: Store computed values to avoid redundant calls. Reduces time to O(n) and space to O(n).
2. **Iterative (Bottom-Up DP)**: Compute Fibonacci numbers iteratively. Time O(n), space O(1) (if optimized).
3. **Matrix Exponentiation or Binet's Formula**: O(log n) time (advanced methods).

"""

# Detailed Code Explanation:

"""
Let’s break down the function `get_nth_fib(n)` step by step and understand how it works, especially for a few test
cases like `get_nth_fib(6)` and `get_nth_fib(8)`.

### 🔢 **What is the Fibonacci Sequence?**

The **Fibonacci sequence** is a series of numbers where:

```
F(1) = 0
F(2) = 1
F(3) = 1
F(4) = 2
F(5) = 3
F(6) = 5
F(7) = 8
F(8) = 13
F(9) = 21
...
```

Each number is the **sum of the two preceding ones**:
```
F(n) = F(n - 1) + F(n - 2)
```

### 🧠 **Code Explanation:**

```
def get_nth_fib(n):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return get_nth_fib(n - 1) + get_nth_fib(n - 2)
```

#### 🔍 How it works:

- This is a **recursive function**, meaning it calls itself to solve smaller parts of the problem.
- It has **base cases** to stop recursion:
  - `if n == 2: return 1` → the second Fibonacci number is 1.
  - `elif n == 1: return 0` → the first Fibonacci number is 0.
- Otherwise, it uses:
  - `get_nth_fib(n - 1) + get_nth_fib(n - 2)`
  - This adds the previous two Fibonacci numbers, just like the mathematical formula.

---

### 🧪 Test Case: `get_nth_fib(6)`

To find the 6th Fibonacci number:

```
get_nth_fib(6)
= get_nth_fib(5) + get_nth_fib(4)
= (get_nth_fib(4) + get_nth_fib(3)) + (get_nth_fib(3) + get_nth_fib(2))
= ...
```

This continues breaking down recursively until it hits the base cases (`n == 1` or `n == 2`).

Here’s what actually gets calculated:

```
get_nth_fib(6)
= get_nth_fib(5) + get_nth_fib(4)
= (get_nth_fib(4) + get_nth_fib(3)) + (get_nth_fib(3) + get_nth_fib(2))
= ((get_nth_fib(3) + get_nth_fib(2)) + (get_nth_fib(2) + get_nth_fib(1))) + ((get_nth_fib(2) + get_nth_fib(1)) + 1)
= ((1 + 1) + (1 + 0)) + ((1 + 0) + 1)
= (2 + 1) + (1 + 1)
= 3 + 2
= 5
```

✅ So, `get_nth_fib(6)` returns `5`.

---

### 🧪 Test Case: `get_nth_fib(8)`

```
F(1) = 0  
F(2) = 1  
F(3) = 1  
F(4) = 2  
F(5) = 3  
F(6) = 5  
F(7) = 8  
F(8) = 13
```

So the function will compute all the way down recursively until it reaches the base cases and adds them up.

✅ So, `get_nth_fib(8)` returns `13`.

---

### ⚠️ **Performance Warning**

This recursive solution is **inefficient for large `n`** because it **repeats the same calculations many times**.
This is called **exponential time complexity**:  
Time Complexity: **O(2ⁿ)**  
Space Complexity: **O(n)** (due to call stack)

---

✅ More Efficient Version (Using Memoization).
Memoization version stores already computed results to avoid recomputation.

"""
