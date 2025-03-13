# Problem Description:

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

## Optimal Time & Space Complexity:
```
O(n log n) time | O(1) space - where `n` is the number of coins.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n log n) time | O(1) space - where `n` is the number of coins
def non_constructible_change(coins):
    # Sort the coins in ascending order to process them from smallest to largest
    coins.sort()

    # Initialize a variable to keep track of the maximum change we can create so far
    current_change_created = 0

    # Iterate through each coin in the sorted list
    for coin in coins:
        # If the current coin is greater than the maximum change we can create + 1,
        # then we cannot create the amount `current_change_created + 1`
        if coin > current_change_created + 1:
            return current_change_created + 1

        # Otherwise, add the current coin to the maximum change we can create
        current_change_created += coin

    # If we can create all amounts up to the sum of all coins,
    # then the smallest amount we cannot create is the sum of all coins + 1
    return current_change_created + 1


# Test Cases
print(non_constructible_change([5, 7, 1, 1, 2, 3, 22]))  # Output: 20
print(non_constructible_change([1, 1, 1, 1, 1]))  # Output: 6
print(non_constructible_change([1, 5, 1, 1, 1, 10, 15, 20, 100]))  # Output: 55
print(non_constructible_change([]))  # Output: 1

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### **Time Complexity**

1. **Sorting**: The function starts by sorting the `coins` array. Sorting typically takes O(n log n) time,
where `n` is the number of coins.

2. **Iteration**: After sorting, the function iterates through the sorted array once. This iteration takes O(n) time.

Thus, the overall time complexity is dominated by the sorting step:

    O(n log n) + O(n) = O(n log n)

---

### **Space Complexity**

1. The function uses a constant amount of extra space (e.g., `current_change_created`). It does not use any additional
data structures that grow with the input size.

2. Sorting is typically done in-place, so no extra space is required for sorting.

Thus, the space complexity is: O(1)

---

### **Summary**
- **Time Complexity**: O(n log n)
- **Space Complexity**: O(1)

This is an efficient solution for the problem.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

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
