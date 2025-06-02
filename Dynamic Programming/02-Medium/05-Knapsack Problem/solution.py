# Problem Description:

"""
                                            Knapsack Problem

You're given an array of arrays where each subarray holds two integer values and represents an item; the first integer is the
item's value, and the second integer is the item's weight. You're also given an integer representing the maximum capacity of a
knapsack that you have.

Your goal is to fit items in your knapsack without having the sum of their weights exceed the knapsack's capacity, all the while
maximizing their combined value.

> Note that you only have one of each item at your disposal.

Write a function that returns the maximized combined value of the items that you should pick as well as an array of the indices
of each item picked.

If there are multiple combinations of items that maximize the total value in the knapsack, your function can return any of them.


## Sample Input:
```
items = [[1, 2], [4, 3], [5, 6], [6, 7]]
capacity = 10
```

## Sample Output:
```
[10, [1, 3]]

// items [4, 3] and [6, 7]
```

## Optimal Time & Space Complexity:
```
O(n * c) time | O(n * c) space - where `n` is the number of items and `c` is the capacity.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n * c) time | O(n * c) space
def knapsack_problem(items, capacity):
    """
    Solves the 0/1 knapsack problem using dynamic programming.

    Args:
        items: List of tuples where each tuple represents (value, weight) of an item
        capacity: Maximum weight capacity of the knapsack

    Returns:
        List containing [max_value, selected_items] where:
            max_value: Maximum achievable value
            selected_items: Indices of selected items in the original list
    """

    n = len(items)
    # Create a DP table with (n+1) rows (items) and (capacity+1) columns (weights)
    # dp[i][w] will store the max value for first i items with capacity w
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build DP table bottom-up
    for i in range(1, n + 1):
        value, weight = items[i - 1]  # Current item's value and weight

        for w in range(capacity + 1):
            if weight <= w:
                # If current item can fit, choose max between:
                # 1. Not taking the item (previous value for same weight)
                # 2. Taking the item (value + best value for remaining weight)
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)
            else:
                # If item doesn't fit, carry forward previous value
                dp[i][w] = dp[i - 1][w]

    # The maximum value is in the bottom-right cell of the table
    max_value = dp[n][capacity]

    # Backtrack to find which items were selected
    w = capacity
    selected_items = []

    for i in range(n, 0, -1):
        # If the value changed from the row above, this item was selected
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)  # Add item index (converting to 0-based)
            w -= items[i - 1][1]  # Reduce remaining capacity by item's weight

    # Reverse to maintain original order (since we backtracked)
    selected_items.reverse()

    return [max_value, selected_items]


# Test Cases:

print(knapsack_problem([[1, 2], [4, 3], [5, 6], [6, 7]], 10))
# Output: [10, [1, 3]]

print(knapsack_problem([[2, 1], [70, 70], [30, 30], [69, 69], [100, 100]], 100))
# Output: [101, [0, 2, 3]]

print(knapsack_problem([[1, 2], [70, 70], [30, 30], [69, 69], [100, 100]], 0))
# Output: [0, []]

# =========================================================================================================================== #

# Big O Analysis:

"""
# Time and Space Complexity Analysis:

Let's analyze the time and space complexity of the given knapsack problem solution:

## Time Complexity:

1. **Initialization of DP table**: Creating a 2D array of size (n+1) x (capacity+1) takes O(n * capacity) time.
2. **Filling the DP table**:
   - Outer loop runs `n` times (for each item)
   - Inner loop runs `capacity + 1` times (for each possible weight from 0 to capacity)
   - Inside the inner loop, we do constant-time operations (comparisons and max calculation)
   - Total for this part: O(n * capacity)
3. **Backtracking to find selected items**:
   - We iterate through the `n` items once in reverse
   - Each iteration does constant-time work
   - Total for this part: O(n)

**Overall Time Complexity**: O(n * capacity) (the dominant term)

## Space Complexity:

1. **DP table storage**: The 2D array consumes O(n * capacity) space.
2. **Selected items list**: This requires O(n) space in the worst case (if all items are selected), but this is dominated by
the DP table.

**Overall Space Complexity**: O(n * capacity)

### **Final Answer**
- **Time Complexity**: O(n * capacity)
- **Space Complexity**: O(n * capacity)

### Notes:
- This is the standard dynamic programming solution for the 0/1 knapsack problem with pseudo-polynomial time complexity.
- The complexity is called "pseudo-polynomial" because it's polynomial in terms of the numerical value of `capacity`,
but not polynomial in terms of the input size (since encoding `capacity` takes only log(capacity) bits).
- If `capacity` is large (e.g., exponential in `n`), this solution becomes impractical.

"""
