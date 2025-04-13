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
def get_nth_fib(n, memoize=None):
    # Initialize memoization dictionary if not provided
    # Contains base cases: Fib(1) = 0, Fib(2) = 1
    if memoize is None:
        memoize = {1: 0, 2: 1}

    # If we haven't computed this Fibonacci number yet
    if n not in memoize:
        # Compute it recursively and store the result
        memoize[n] = get_nth_fib(n - 1, memoize) + get_nth_fib(n - 2, memoize)

    # Return the stored or newly computed value
    return memoize[n]


# Test Cases:

print(get_nth_fib(2))  # Output: 1
print(get_nth_fib(6))  # Output: 5
print(get_nth_fib(8))  # Output: 13

# =========================================================================================================================== #

# Big O Analysis:

"""

## Time and Space Complexity Analysis

### Time Complexity:

- **Base Cases Handling**: The function handles base cases (n=1 and n=2) in constant time, O(1).
- **Memoization Check**: For each call to `get_nth_fib(n)`, the function checks if `n` is in `memoize`.
This is an O(1) operation (assuming dictionary lookups are average-case O(1)).
- **Recursive Calls**: For any `n` not in `memoize`, the function makes two recursive calls: `get_nth_fib(n-1)` and
`get_nth_fib(n-2)`. However, due to memoization, each unique `n` is computed only once. After the first computation,
the result is stored and reused.
- **Total Unique Computations**: The function computes values for `n, n-1, n-2, ..., 1`, which is `O(n)` unique computations.

- **Overall Time Complexity**: Since each computation is O(1) (due to memoization), the total time complexity is **O(n)**.

### Space Complexity:

- **Memoization Dictionary**: The `memoize` dictionary stores `O(n)` entries (from `1` to `n`).
- **Recursion Stack**: In the worst case (without tail recursion optimization), the recursion stack can go up to `O(n)`
depth (e.g., for `get_nth_fib(n)`, it calls `get_nth_fib(n-1)`, which calls `get_nth_fib(n-2)`, etc., until it hits the base case).
- **Overall Space Complexity**: The dominant factor is the recursion stack and the memoization dictionary, both of which are `O(n)`.
Thus, the total space complexity is **O(n)**.

### Key Points:
- The memoization ensures that each Fibonacci number is computed only once, leading to linear time complexity.
- The space complexity is linear due to the memoization dictionary and the recursion stack.

### Summary:
Time Complexity: **O(n)**  
Space Complexity: **O(n)**

"""
