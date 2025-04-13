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
