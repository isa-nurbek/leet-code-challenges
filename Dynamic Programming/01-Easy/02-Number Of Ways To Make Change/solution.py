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
    ways = [0 for amount in range(n + 1)]
    ways[0] = 1

    for denom in denoms:
        for amount in range(1, n + 1):
            if denom <= amount:
                ways[amount] += ways[amount - denom]

    return ways[n]


# Test Cases:

print(number_of_ways_to_make_change(6, [1, 5]))
# Output: 2

print(number_of_ways_to_make_change(0, [2, 3, 4, 7]))
# Output: 1

print(number_of_ways_to_make_change(10, [1, 5, 10, 25]))
# Output: 4
