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
