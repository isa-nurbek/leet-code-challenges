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
1 

// Sequence: 0, 1
```

## Sample Input #2
```
n = 6
```

## Sample Output #2
```
5 

// Sequence: 0, 1, 1, 2, 3, 5
```

## Optimal Time & Space Complexity:
```
O(n) time | O(1) space - where `n` is the input number.
```
"""

# =========================================================================================================================== #

# Solution:


# O(n) time | O(1) space
def get_nth_fib(n):
    # Returns the nth Fibonacci number (0-based index)

    # Handle the base case where n is 1
    # The first Fibonacci number is defined as 0
    if n == 1:
        return 0

    # Initialize the first two Fibonacci numbers:
    # a represents F(1) = 0
    # b represents F(2) = 1
    a, b = 0, 1

    # Iterate from 3 to n (inclusive) to calculate subsequent numbers
    # We start at 3 because we already have F(1) and F(2)
    for _ in range(3, n + 1):
        # Update the Fibonacci numbers:
        # a becomes the previous b (F(n-1))
        # b becomes the sum of previous a and b (F(n) = F(n-1) + F(n-2))
        a, b = b, a + b

    # Return the nth Fibonacci number
    # After the loop, b holds the value of F(n)
    return b


# Test Cases:

print(get_nth_fib(2))  # Output: 1
print(get_nth_fib(6))  # Output: 5
print(get_nth_fib(8))  # Output: 13

# =========================================================================================================================== #

# Big O Analysis:

"""

## Time and Space Complexity Analysis

### Time Complexity:

1. **Base Case (n == 1):** 
   - The function returns 0 immediately. This is an O(1) operation.
2. **Iterative Calculation (n > 1):**
   - The function initializes `a` and `b` to 0 and 1, respectively.
   - Then, it runs a loop from 3 to n (inclusive), performing constant-time operations (addition and assignment) in each iteration.
   - The loop runs for `n - 2` iterations (since it starts at 3 and goes up to n).
   
   - Thus, the time complexity is O(n).

### Space Complexity:

1. The function uses a constant amount of additional space:
   - Variables `a` and `b` to store the last two Fibonacci numbers.
   - No additional data structures or recursive calls are used.
   
   - Thus, the space complexity is O(1) (constant space).

### Summary:
- **Time Complexity:** O(n) (linear time).
- **Space Complexity:** O(1) (constant space).

### Note:
If the input `n` is 1 or 2, the function returns immediately (O(1) time), but in the worst case (n > 2),
the time complexity is O(n). The space complexity is always O(1).

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
Let's break down the function `get_nth_fib(n)` and explain exactly how it works, step by step.

### 🚀 Purpose of the Function:
This function calculates the **n-th Fibonacci number**, using an **iterative approach**.

### 🔢 What is the Fibonacci Sequence?
The Fibonacci sequence is a series of numbers where:
```
F(1) = 0
F(2) = 1
F(3) = 1  => F(1) + F(2)
F(4) = 2  => F(2) + F(3)
F(5) = 3  => F(3) + F(4)
F(6) = 5  => F(4) + F(5)
...
```

Each number is the sum of the **two preceding ones**.

---

### 🧠 Function Breakdown

```
def get_nth_fib(n):
```
- This defines a function that takes one argument `n`, which represents the position in the Fibonacci sequence.

---

```
if n == 1:
    return 0
```
- If the input is `1`, it returns `0` immediately, because `F(1)` is `0`.

---

```
a, b = 0, 1
```
- Initializes two variables:
  - `a` is the first Fibonacci number → F(1) = 0
  - `b` is the second Fibonacci number → F(2) = 1

These two variables will keep track of the last two Fibonacci numbers.

---

```
for _ in range(3, n + 1):
    a, b = b, a + b
```
- This `for` loop starts from `3` and goes up to `n` (inclusive). Why start at 3?
  - Because we already defined `F(1)` and `F(2)` in the previous step.

**What happens in the loop?**
- `a, b = b, a + b` is a **simultaneous update**:
  - Set `a` to the old `b`
  - Set `b` to the sum of the old `a + b`
  - This is effectively sliding forward in the sequence.

Let’s take an example: `n = 6`

| Iteration | a   | b   | Explanation                   |
|-----------|-----|-----|-------------------------------|
| Start     | 0   | 1   | Initial values                |
| i = 3     | 1   | 1   | a=1, b=0+1                    |
| i = 4     | 1   | 2   | a=1, b=1+1                    |
| i = 5     | 2   | 3   | a=2, b=1+2                    |
| i = 6     | 3   | 5   | a=3, b=2+3                    |

So for `n = 6`, it returns `5` — correct!

---

```
return b
```
- After the loop, `b` will be the n-th Fibonacci number, so it returns that.

---

### ✅ Test Cases

```
print(get_nth_fib(2))  # Output: 1
```
- F(2) = 1 ✅

```
print(get_nth_fib(6))  # Output: 5
```
- F(6) = 5 ✅

```
print(get_nth_fib(8))  # Output: 13
```
- F(8) = 13 ✅

---

### 🧪 Summary

- Efficient: O(n) time, O(1) space.
- Uses iteration instead of recursion to save memory.
- Handles base case (n == 1) correctly.
- Great for computing Fibonacci numbers even for large `n`.

"""
