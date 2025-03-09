# Description:

"""

                                        Non-Constructible Change

Given an array of positive integers representing the values of coins in your possession, write a function that returns
the minimum amount of change (the minimum sum of money) that you cannot create. The given coins can have any positive 
integer value and aren't necessarily unique (i.e., you can have multiple coins of the same value).

For example, if you're given `coins = [1, 2, 5]`, the minimum amount of change that you can't create is `4`. If you're given
no coins, the minimum amount of change that you can't create is `1`.

## Sample Input:

```
coins = [5, 7, 1, 1, 2, 3, 22]
```

## Sample Output:

```
20
```

## Optimal Space & Time Complexity:

```
`O(n log n)` time | `O(1)` space - where `n` is the number of coins
```

"""

# =============================================================================================== #

# Solution:


# O(n log n) time | O(1) space - where `n` is the number of coins
def non_constructible_change(coins):
    coins.sort()

    current_change_created = 0

    for coin in coins:
        if coin > current_change_created + 1:
            return current_change_created + 1

        current_change_created += coin

    return current_change_created + 1


# Test Cases
print(non_constructible_change([5, 7, 1, 1, 2, 3, 22]))  # 20
print(non_constructible_change([1, 1, 1, 1, 1]))  # 6
print(non_constructible_change([1, 5, 1, 1, 1, 10, 15, 20, 100]))  # 55
print(non_constructible_change([]))  # 1

# =============================================================================================== #

# Big O:

"""

## Time and Space Complexity:

The function `non_constructible_change` is designed to find the smallest amount of change that cannot be created using
the given coins. Let's break down the function and analyze its time and space complexity.

### Function Explanation:
1. **Sorting**: The function starts by sorting the list of coins in ascending order.
2. **Iterating through coins**: It then iterates through the sorted list, maintaining a running total of the change that
can be created so far (`current_change_created`).
3. **Check for the smallest non-constructible change**: For each coin, it checks if the coin's value is greater than
`current_change_created + 1`. If it is, then `current_change_created + 1` is the smallest amount of change that cannot be created.
4. **Update the running total**: If the coin's value is not greater than `current_change_created + 1`, it adds the coin's
value to `current_change_created`.
5. **Return the result**: If the loop completes without finding a non-constructible change, the function returns
`current_change_created + 1`.

### Time Complexity:
- **Sorting**: The sorting step takes `O(n log n)` time, where `n` is the number of coins.
- **Iterating through the list**: The iteration through the list takes `O(n)` time.

Therefore, the overall time complexity is dominated by the sorting step, which is - O`(n log n)`.

### Space Complexity:
- **Sorting**: The space complexity of the sorting step depends on the sorting algorithm used. Python's built-in `sort()`
method uses Timsort, which has a space complexity of `O(n)` in the worst case.
- **Other variables**: The function uses a constant amount of additional space (e.g., `current_change_created`).

Therefore, the overall space complexity is `O(n)` due to the sorting step.

### Edge Case:
- **Empty list**: If the list of coins is empty, the function returns `1`, which is the smallest amount of change
that cannot be created with no coins.

### Summary:
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)`

"""

# Code Explanation:

"""
### Explanation of the Code

The function `non_constructible_change` is designed to find the smallest amount of change that **cannot** be created
using the given coins. Here's a detailed breakdown of how it works:

---

### Key Idea
The algorithm relies on the fact that if you have already created all amounts of change up to a certain value (say `current_change_created`), and the next coin is greater than `current_change_created + 1`, then `current_change_created + 1`
is the smallest amount of change that cannot be created.

---

### Step-by-Step Explanation

1. **Sort the Coins**:
   ```
   coins.sort()
   ```
   - The coins are sorted in ascending order to ensure that we process them from the smallest to the largest. This allows
   us to build up the possible amounts of change incrementally.

2. **Initialize `current_change_created`**:
   ```
   current_change_created = 0
   ```
   - This variable keeps track of the maximum amount of change that can be created so far using the coins processed up to
   the current point.

3. **Iterate Through the Coins**:
   ```
   for coin in coins:
   ```
   - We loop through each coin in the sorted list.

4. **Check if the Current Coin Breaks the Sequence**:
   ```
   if coin > current_change_created + 1:
       return current_change_created + 1
   ```
   - If the current coin is greater than `current_change_created + 1`, it means we cannot create the amount
   `current_change_created + 1` using the coins processed so far. Hence, `current_change_created + 1` is the
   smallest amount of change that cannot be created.

5. **Update `current_change_created`**:
   ```
   current_change_created += coin
   ```
   - If the current coin does not break the sequence, we add its value to `current_change_created`. This means we can
   now create all amounts of change up to `current_change_created`.

6. **Return the Result**:
   ```
   return current_change_created + 1
   ```
   - If the loop completes without finding a gap, the smallest amount of change that cannot be created is
   `current_change_created + 1`.

---

### Example Walkthroughs

#### Example 1:
```
coins = [5, 7, 1, 1, 2, 3, 22]
```
- Sorted coins: `[1, 1, 2, 3, 5, 7, 22]`
- Iteration:
  - Coin = 1: `current_change_created = 1` (can create 1)
  - Coin = 1: `current_change_created = 2` (can create 1, 2)
  - Coin = 2: `current_change_created = 4` (can create 1, 2, 3, 4)
  - Coin = 3: `current_change_created = 7` (can create 1, 2, 3, 4, 5, 6, 7)
  - Coin = 5: `current_change_created = 12` (can create 1 to 12)
  - Coin = 7: `current_change_created = 19` (can create 1 to 19)
  - Coin = 22: `22 > 19 + 1`, so the smallest amount that cannot be created is `20`.

#### Example 2:
```
coins = [1, 1, 1, 1, 1]
```
- Sorted coins: `[1, 1, 1, 1, 1]`
- Iteration:
  - Coin = 1: `current_change_created = 1` (can create 1)
  - Coin = 1: `current_change_created = 2` (can create 1, 2)
  - Coin = 1: `current_change_created = 3` (can create 1, 2, 3)
  - Coin = 1: `current_change_created = 4` (can create 1, 2, 3, 4)
  - Coin = 1: `current_change_created = 5` (can create 1, 2, 3, 4, 5)
- After the loop, the smallest amount that cannot be created is `6`.

#### Example 3:
```
coins = [1, 5, 1, 1, 1, 10, 15, 20, 100]
```
- Sorted coins: `[1, 1, 1, 1, 5, 10, 15, 20, 100]`
- Iteration:
  - Coin = 1: `current_change_created = 1` (can create 1)
  - Coin = 1: `current_change_created = 2` (can create 1, 2)
  - Coin = 1: `current_change_created = 3` (can create 1, 2, 3)
  - Coin = 1: `current_change_created = 4` (can create 1, 2, 3, 4)
  - Coin = 5: `current_change_created = 9` (can create 1 to 9)
  - Coin = 10: `current_change_created = 19` (can create 1 to 19)
  - Coin = 15: `current_change_created = 34` (can create 1 to 34)
  - Coin = 20: `current_change_created = 54` (can create 1 to 54)
  - Coin = 100: `100 > 54 + 1`, so the smallest amount that cannot be created is `55`.

#### Example 4:
```
coins = []
```
- No coins are provided.
- The smallest amount that cannot be created is `1`.

---

### Summary
The function efficiently finds the smallest amount of change that cannot be created by sorting the coins and iteratively
building up the possible amounts of change. It leverages the sorted order to detect gaps in the sequence of possible amounts.

"""
