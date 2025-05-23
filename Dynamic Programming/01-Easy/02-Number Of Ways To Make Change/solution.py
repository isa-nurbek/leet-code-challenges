# Problem Description:

"""
                                                Number Of Ways To Make Change

Given an array of distinct `positive` integers representing coin denominations and a single `non-negative` integer `n` representing
a target amount of money, write a function that returns the number of ways to make change for that target amount using the given
coin denominations.

> Note that an unlimited amount of coins is at your disposal.


## Sample Input:
```
n = 6
denoms = [1, 5]
```

## Sample Output:
```
2

// 1x1 + 1x5 and 6x1
```

## Optimal Time & Space Complexity:
```
O(n * d) time | O(n) space - where `n` is the target amount and `d` is the number of coin denominations.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n * d) time | O(n) space
def number_of_ways_to_make_change(n, denoms):
    """
    Calculate the number of ways to make change for a given amount using dynamic programming.

    Args:
    n (int): The target amount to make change for
    denoms (list): List of available coin denominations

    Returns:
    int: Number of ways to make change for amount n using given denominations
    """

    # Initialize a DP array where ways[amount] will store the number of ways
    # to make change for that amount. We include 0 to n amounts.
    ways = [0 for amount in range(n + 1)]

    # Base case: There's exactly 1 way to make change for amount 0 - by using no coins
    ways[0] = 1

    # Iterate through each coin denomination
    for denom in denoms:
        # For each denomination, update the ways array for all amounts from 1 to n
        for amount in range(1, n + 1):
            # If the current denomination can be used for this amount
            if denom <= amount:
                # The number of ways to make 'amount' is increased by the number of ways
                # to make (amount - denom), since we can add this coin to those combinations
                ways[amount] += ways[amount - denom]

    # Return the number of ways to make change for the target amount n
    return ways[n]


# Test Cases:

print(number_of_ways_to_make_change(6, [1, 5]))
# Output: 2

print(number_of_ways_to_make_change(0, [2, 3, 4, 7]))
# Output: 1

print(number_of_ways_to_make_change(10, [1, 5, 10, 25]))
# Output: 4

# =========================================================================================================================== #

# Big O Analysis:

"""
# Time and Space Complexity Analysis:

### **Space Complexity:**

- The function uses an array `ways` of size `n + 1` to store intermediate results.
- No other significant additional space is used.
- Thus, the **space complexity is `O(n)`**, where `n` is the target amount.

### **Time Complexity:**

1. **Initialization:**
   - `ways = [0 for amount in range(n + 1)]` takes `O(n)` time.
   - `ways[0] = 1` is a constant-time operation.

2. **Nested Loops:**
   - The outer loop runs once for each denomination in `denoms`. Let `d` be the number of denominations (`d = len(denoms)`).
   - The inner loop runs for each `amount` from `1` to `n` (i.e., `n` iterations).
   - Inside the inner loop, the operation `ways[amount] += ways[amount - denom]` is `O(1)`.

Thus, the total time complexity is:
- **`O(d * n)`**, where:
  - `d` = number of denominations.
  - `n` = target amount.

### **Final Complexity:**

- **Time Complexity:** `O(d * n)`
- **Space Complexity:** `O(n)`

### **Explanation of the Approach:**

The dynamic programming approach works by:
1. **Initializing** `ways[0] = 1` because there is exactly 1 way to make change for `0` (using no coins).
2. **Iterating over each denomination** and updating the `ways` array:
   - For each `denom`, and for each `amount` from `1` to `n`, if `denom <= amount`, then the number of ways to make `amount` is
   increased by `ways[amount - denom]` (since we can add `denom` to all those ways).
3. **Returning** `ways[n]`, which now contains the total number of ways to make change for `n`.

This approach efficiently computes the solution by breaking the problem into smaller subproblems.

"""
