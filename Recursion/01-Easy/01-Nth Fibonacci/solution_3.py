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
