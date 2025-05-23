# Problem Description:

"""
                                                Min Number Of Coins For Change

Given an array of `positive` integers representing coin denominations and a single `non-negative` integer `n` representing a target
amount of money, write a function that returns the `smallest number of coins` needed to make change for (to sum up to) that target
amount using the given coin denominations.

> Note that you have access to an unlimited amount of coins. In other words, if the denominations are `[1, 5, 10]`, you have access
to an unlimited amount of `1`s, `5`s, and `10`s.

If it's impossible to make change for the target amount, return `-1`.


## Sample Input:
```
n = 7
denoms = [1, 5, 10]
```

## Sample Output:
```
3

// 2x1 + 1x5
```

## Optimal Time & Space Complexity:
```
O(n * d) time | O(n) space - where `n` is the target amount and `d` is the number of coin denominations.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n * d) time | O(n) space
def min_number_of_coins_for_change(n, denoms):
    # Initialize a list to store the minimum number of coins needed for each amount from 0 to n
    # We use infinity as the initial value to represent that those amounts are initially unreachable
    num_of_coins = [float("inf") for amount in range(n + 1)]

    # Base case: 0 coins are needed to make change for 0 amount
    num_of_coins[0] = 0

    # Iterate through each coin denomination
    for denom in denoms:
        # For each denomination, iterate through all amounts from 0 to n
        for amount in range(len(num_of_coins)):
            # If the current denomination can be used to make change for the current amount
            if denom <= amount:
                # Update the minimum number of coins needed for this amount by either:
                # - Keeping the existing minimum, or
                # - Using one of the current denomination plus the minimum for (amount - denom)
                num_of_coins[amount] = min(
                    num_of_coins[amount], num_of_coins[amount - denom] + 1
                )

    # Return the result for amount n, or -1 if it's not possible to make change
    return num_of_coins[n] if num_of_coins[n] != float("inf") else -1


# Test Cases:

print(min_number_of_coins_for_change(7, [1, 5, 10]))
# Output: 3

print(min_number_of_coins_for_change(0, [1, 2, 3]))
# Output: 0

print(min_number_of_coins_for_change(9, [3, 4, 5]))
# Output: 2
