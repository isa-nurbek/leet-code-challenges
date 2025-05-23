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

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
This Python function `number_of_ways_to_make_change(n, denoms)` calculates how many different ways you can make change for
a given amount `n` using the coin denominations provided in the `denoms` list.

---

### 🔍 Function Signature

```
def number_of_ways_to_make_change(n, denoms):
```

* `n`: the total amount for which we want to make change.
* `denoms`: list of coin denominations available to use.

---

### 🧠 High-Level Idea

This is a classic **Dynamic Programming (DP)** problem.
We solve it by **building up** the number of ways to form each amount from `0` to `n`, using smaller subproblems.

---

### 🧱 Detailed Breakdown

```
ways = [0 for amount in range(n + 1)]
ways[0] = 1
```

* We create a list `ways` of size `n + 1`, initialized with zeros.
* `ways[i]` will eventually contain the number of ways to make change for amount `i`.
* Set `ways[0] = 1` because there's **one way to make change for 0**: use no coins.

---

### 🔁 Loop through each denomination

```
for denom in denoms:
```

* For each coin denomination, we update our `ways` list to reflect how many more ways are possible using this denomination.

```
    for amount in range(1, n + 1):
        if denom <= amount:
            ways[amount] += ways[amount - denom]
```

* We iterate through all amounts from `1` to `n`.
* If the current denomination `denom` is less than or equal to the current `amount`, it means this denomination can be used
to contribute to this amount.

### 🧩 How does the DP update work?

When we do:

```
ways[amount] += ways[amount - denom]
```

We're saying:

* The number of ways to make `amount` increases by however many ways there are to make `amount - denom`.
* Why? Because if you can make `amount - denom`, then by adding one coin of value `denom`, you can make `amount`.

---

### 🧪 Example: `number_of_ways_to_make_change(6, [1, 5])`

We want the number of ways to make 6 using coins of 1 and 5.

#### Step-by-step with DP array (`ways`):

Start:

```
ways = [1, 0, 0, 0, 0, 0, 0]  # ways[0] = 1
```

Use `1`:

```
ways[1] += ways[0] -> 1
ways[2] += ways[1] -> 1
...
ways[6] += ways[5] -> 1

ways = [1, 1, 1, 1, 1, 1, 1]
```

Use `5`:

```
ways[5] += ways[0] -> 1 + 1 = 2
ways[6] += ways[1] -> 1 + 1 = 2

ways = [1, 1, 1, 1, 1, 2, 2]
```

So, final answer: `ways[6] = 2`

➡️ You can make 6 using:

* 6x 1s
* 1x 5 + 1x 1

---

### ✅ Test Cases Explained

```
print(number_of_ways_to_make_change(6, [1, 5]))
# Output: 2
```

As shown above.

```
print(number_of_ways_to_make_change(0, [2, 3, 4, 7]))
# Output: 1
```

Only one way to make change for 0: use no coins.

```
print(number_of_ways_to_make_change(10, [1, 5, 10, 25]))
# Output: 4
```

Ways:

* 10x1
* 5+5
* 10
* 5+1x5

---

### 🧠 Time and Space Complexity

* **Time**: O(n * m), where `n` is the target amount and `m` is the number of denominations.
* **Space**: O(n), for the `ways` list.

---

Let's visualize the **Dynamic Programming table** as it gets filled.

We’ll walk through the example:

```
number_of_ways_to_make_change(6, [1, 5])
```

---

### Initial Setup

* Amount to make: `6`
* Denominations: `[1, 5]`
* DP Array: `ways[0..6]`
* Initially:

```
Index:     0  1  2  3  4  5  6
ways:     [1, 0, 0, 0, 0, 0, 0]
```

We set `ways[0] = 1` because there's **1 way to make 0** (use no coins).

---

### Step 1: Using coin = 1

Now, we update the array for every amount `a` from `1` to `6`.

For each `a`, we add `ways[a - 1]` to `ways[a]`.

```
After using coin 1:
Index:     0  1  2  3  4  5  6
ways:     [1, 1, 1, 1, 1, 1, 1]
```

Why?

* ways[1] = ways[1] + ways[0] → 0 + 1 = 1
* ways[2] = ways[2] + ways[1] → 0 + 1 = 1
* ...
* So you can form each amount `a` in **1 way** using only 1s.

---

### Step 2: Using coin = 5

Now update using `coin = 5`.

For `a = 5 to 6`:

* ways[5] += ways[0] → 1 + 1 = 2
* ways[6] += ways[1] → 1 + 1 = 2

```
After using coin 5:
Index:     0  1  2  3  4  5  6
ways:     [1, 1, 1, 1, 1, 2, 2]
```

---

### 🎉 Final Result

```
ways[6] = 2
```

So, 2 ways to make 6 using [1, 5].

---

### 🧮 Breakdown of the 2 ways:

1. 1 + 1 + 1 + 1 + 1 + 1 (six 1s)
2. 5 + 1

---

Let’s walk through the example:

```
number_of_ways_to_make_change(10, [1, 5, 10])
```

---

### 🏗️ Goal

We want to find how many different combinations of `[1, 5, 10]` can make the total `10`.

We’ll build the `ways` DP array and **visualize its updates** as we include each coin.

---

### 🧾 Initial Setup

```
Index:     0  1  2  3  4  5  6  7  8  9 10
ways:     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```

Set `ways[0] = 1` because there's **1 way to make 0** (use no coins).

---

### 🪙 Step 1: Use coin = 1

We update ways[a] += ways[a - 1] for a from 1 to 10.

```
After using coin 1:
Index:     0  1  2  3  4  5  6  7  8  9 10
ways:     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
```

🟢 Each amount `a` can be made in **1 way** using only 1s.

---

### 🪙 Step 2: Use coin = 5

Now update from `amount = 5` to `10` using:

```
ways[amount] += ways[amount - 5]
```

```
Index:         0  1  2  3  4  5  6  7  8  9 10
Before coin 5: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
After coin 5:  [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3]
```

🟢 Explanation:

* `ways[5] += ways[0]` → 1 + 1 = 2
* `ways[6] += ways[1]` → 1 + 1 = 2
* ...
* `ways[10] += ways[5]` → 1 + 2 = 3

---

### 🪙 Step 3: Use coin = 10

Now update only `amount = 10`:

```
ways[10] += ways[0] → 3 + 1 = 4
```

```
Final table:
Index:         0  1  2  3  4  5  6  7  8  9 10
ways:         [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 4]
```

---

### ✅ Final Answer:

```
ways[10] = 4
```

---

### 🧮 The 4 Ways to Make 10 with [1, 5, 10]:

1. 10x 1
2. 5 + 5
3. 5 + five 1s
4. 10

"""
