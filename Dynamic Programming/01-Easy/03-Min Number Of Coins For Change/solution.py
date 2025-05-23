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

# =========================================================================================================================== #

# Big O Analysis:

"""
# Time and Space Complexity Analysis:

Let's analyze the time and space complexity of the given `min_number_of_coins_for_change` function.

### **Time Complexity:**

The time complexity is determined by the nested loops in the function:
1. The outer loop iterates over each denomination in `denoms`.
2. The inner loop iterates over each amount from `0` to `n`.

- Let `m` = number of denominations (`len(denoms)`).
- Let `n` = the target amount.

Since the inner loop runs for each denomination, the total time complexity is: O(m * n)

### **Space Complexity:**

The function uses an array `num_of_coins` of size `n + 1` to store intermediate results.

Thus, the space complexity is: O(n)

### **Summary:**
- **Time Complexity:** O(m * n)
- **Space Complexity:** O(n)

### **Explanation:**
- The algorithm is a classic **Dynamic Programming (DP)** approach to the **Unbounded Knapsack Problem** (Coin Change problem).
- The DP table (`num_of_coins`) keeps track of the minimum coins needed for each amount up to `n`.
- For each denomination, we update the DP table by considering whether using that denomination leads to a better (smaller)
coin count for a given amount.

This approach efficiently computes the minimum coins required while avoiding the exponential time complexity of a brute-force
recursive solution.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
Here's a detailed explanation of how the `min_number_of_coins_for_change` function works:

---

### **Problem Statement:**

You are given:

* An integer `n` — the **target amount** you want to make.
* A list `denoms` — a list of coin denominations.

**Goal:**
Return the **minimum number of coins** required to make the amount `n` using the given denominations.
If it's **not possible**, return `-1`.

---

### **Code Breakdown:**

```
def min_number_of_coins_for_change(n, denoms):
```

This function takes:

* `n`: the target amount
* `denoms`: a list of available coin denominations

---

#### Step 1: Initialization

```
num_of_coins = [float("inf") for amount in range(n + 1)]
num_of_coins[0] = 0
```

* Create a list `num_of_coins` of size `n+1`.

  * Each index `i` in this list will store the **minimum number of coins needed** to make the amount `i`.
* Initially, we set all values to `infinity` (`float("inf")`) because we haven't computed them yet.
* Set `num_of_coins[0] = 0`, because **zero coins are needed to make amount 0**.

---

#### Step 2: Dynamic Programming (Bottom-Up)

```
for denom in denoms:
    for amount in range(len(num_of_coins)):
        if denom <= amount:
            num_of_coins[amount] = min(
                num_of_coins[amount], num_of_coins[amount - denom] + 1
            )
```

* Loop through each **coin denomination**.

* For each amount from `0` to `n`:

  * If the current coin (`denom`) can be used (i.e., `denom <= amount`):

    * Update the minimum number of coins for this `amount`:

      ```python
      num_of_coins[amount] = min(
          num_of_coins[amount],        # current known min
          num_of_coins[amount - denom] + 1  # if we use this coin
      )
      ```

* This uses the idea:
  To make amount `A`, if you know the minimum coins needed to make `A - d`,
  then you can make `A` with one extra coin of denomination `d`.

---

#### Step 3: Return the Result

```
return num_of_coins[n] if num_of_coins[n] != float("inf") else -1
```

* If `num_of_coins[n]` is still `inf`, it means there's **no combination of coins** that sums up to `n`.
* Otherwise, return the computed minimum number of coins.

---

### **Examples:**

#### Example 1:

```
min_number_of_coins_for_change(7, [1, 5, 10])
```

* We want to make 7 using coins `[1, 5, 10]`.
* Optimal way: `5 + 1 + 1` → 3 coins
* **Output: `3`**

---

#### Example 2:

```
min_number_of_coins_for_change(0, [1, 2, 3])
```

* We want to make 0 → use 0 coins
* **Output: `0`**

---

#### Example 3:

```
min_number_of_coins_for_change(9, [3, 4, 5])
```

* Try combinations like:

  * `4 + 5` = 9 (2 coins)
  * `3 + 3 + 3` = 9 (3 coins)
* Best is `4 + 5`
* **Output: `2`**

---

### **Summary:**

This is a classic **Dynamic Programming** problem:

* Subproblem: What's the minimum number of coins to make amount `x`?
* Build up solutions from `0` to `n`.
* Time complexity: `O(n * m)` where `n` is the target amount and `m` is number of denominations.
* Space complexity: `O(n)`

---

Let’s visualize the algorithm step-by-step using **ASCII** graphics for the example:

### Example: `min_number_of_coins_for_change(7, [1, 5, 10])`

We want the **minimum number of coins** to make `7` using coins of `[1, 5, 10]`.

---

### STEP 1: Initialize DP Table

```
Amount (index):    0  1  2  3  4  5  6  7
Initial values:    0  ∞  ∞  ∞  ∞  ∞  ∞  ∞
```

> `0` coins needed for amount 0.
> `∞` (infinity) means we haven't found a way to make that amount yet.

---

### STEP 2: Process Denomination = 1

We try to use coin `1` to build up to 7.

```
Amount (index):    0  1  2  3  4  5  6  7
Using 1 coin:      0  1  2  3  4  5  6  7
Explanation:       - 0+1 1+1 2+1 3+1 ...
```

We update each `amount` if `amount >= 1`, using:

```
num_of_coins[amount] = min(current, num_of_coins[amount - 1] + 1)
```

---

### STEP 3: Process Denomination = 5

Now we try to use coin `5`:

```
Amount (index):    0  1  2  3  4  5  6  7
Before 5 coin:     0  1  2  3  4  5  6  7
Using 5 coin:      -  -  -  -  -  1  2  3
                             ^  ^  ^
                            (0+1)(1+1)(2+1)
```

Update values if:

```
num_of_coins[amount] > num_of_coins[amount - 5] + 1
```

Resulting table:

```
Updated table:     0  1  2  3  4  1  2  3
```

---

### STEP 4: Process Denomination = 10

Nothing changes, because we can’t use coin `10` to build amounts ≤ 7.

```
Final table:       0  1  2  3  4  1  2  3
```

---

### Final Result

We look at the value at index `7`:

```
min_number_of_coins_for_change(7, [1, 5, 10]) = 3
```

**Explanation:**

* Best way to make 7 is: `5 + 1 + 1` → 3 coins

"""
