# Problem Description:

"""

                                          Blackjack Probability

In the game of Blackjack, the dealer must draw cards until the sum of the values of their cards is greater than or equal to a
`target` value minus 4. For example, traditional Blackjack uses a `target` value of 21, so the dealer must draw cards until their
total is greater than or equal to 17, at which point they stop drawing cards (they "stand"). If the dealer draws a card that
brings their total above the `target` (above 21 in traditional Blackjack), they lose (they "bust").

Naturally, when a dealer is drawing cards, they can either end up standing or busting, and this is entirely up to the luck of
their draw.

Write a function that takes in a `target` value as well as a dealer's `starting_hand` value and returns the probability that the
dealer will bust (go over the `target` value before standing). The `target` value will always be a positive integer, and the
`starting_hand` value will always be a positive integer that's smaller than or equal to the `target` value.

For simplicity, you can assume that the dealer has an infinite deck of cards and that each card has a value between 1 and 10
inclusive. The likelihood of drawing a card of any value is always the same, regardless of previous draws.

Your solution should be rounded to 3 decimal places and to the nearest value. For example, a probability of `0.314159` would
be rounded to `0.314`, while a probability of `0.1337` would be rounded to `0.134`.


## Sample Input
```
target = 21
starting_hand = 15
```

## Sample Output
```
0.45 // Drawing a 2-6 would result in the dealer standing.
// Drawing a 7-10 would result in the dealer busting.
// Drawing a 1 would result in a 16, meaning the dealer keeps drawing.
// Drawing with a 16 results in a 0.5 probability of busting (6-10 all result in busts).
// The overall probability of busting is 0.4 + (0.1 * 0.5)
// (the probability of busting on the first draw + the probability of busting on the second).
```

## Optimal Time & Space Complexity:
```
O(t - s) time | O(t - s) space - where `t` is the target, and `s` is the starting hand.
```
"""

# =========================================================================================================================== #

# Solution:


# O(t - s) time | O(t - s) space
def blackjack_probability(target, starting_hand):
    """Calculate the probability of going over the target value in Blackjack.

    Args:
        target (int): The target value (typically 21 in Blackjack)
        starting_hand (int): The current hand value to start from

    Returns:
        float: The probability of busting, rounded to 3 decimal places
    """
    # Initialize memoization dictionary to store already computed probabilities
    memo = {}
    # Calculate and return the probability rounded to 3 decimal places
    return round(calculate_probability(starting_hand, target, memo), 3)


def calculate_probability(current_hand, target, memo):
    """Recursive helper function to calculate bust probability with memoization.

    Args:
        current_hand (int): Current hand value in the recursive calculation
        target (int): The target value we're trying not to exceed
        memo (dict): Dictionary to store computed probabilities for efficiency

    Returns:
        float: Probability of busting from the current hand state
    """
    # If we've already computed this hand value, return stored result
    if current_hand in memo:
        return memo[current_hand]

    # Base case: current hand already exceeds target (bust)
    if current_hand > target:
        return 1  # 100% probability we're busted

    # Base case: current hand is close enough to target that any card will cause bust
    # (Since highest card value is 10, if current_hand + 4 >= target, then a 10 would bust)
    if current_hand + 4 >= target:
        return 0  # 0% probability of busting from this state

    # Initialize total probability for this hand state
    total_probability = 0

    # Consider all possible card draws (1 through 10)
    for drawn_card in range(1, 11):
        # Each card has 10% chance (1/10 probability)
        # Recursively calculate probability for the new hand state
        total_probability += 0.1 * calculate_probability(
            current_hand + drawn_card, target, memo
        )

    # Store computed probability in memo before returning
    memo[current_hand] = total_probability
    return total_probability


# Test Cases:

print(blackjack_probability(21, 15))  #  Output: 0.45
print(blackjack_probability(21, 21))  #  Output: 0
print(blackjack_probability(10, 3))  #  Output: 0.395

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis


### **Time Complexity**

Let **`S`** be the maximum possible `current_hand` value where we perform computations.  
- The worst case is when `starting_hand` is small, and we compute probabilities for all possible hands up to `target + 10`
(since the maximum card is `10`).
- The recursion branches into **10** possibilities at each step (for cards `1` to `10`).
- However, memoization ensures that each subproblem (`current_hand`) is computed only once.

Thus:
- **Number of subproblems**: `O(T)`, where `T = target - starting_hand + 10` (since we compute up to `target + 10` in the
worst case).
- **Work per subproblem**: `O(10) = O(1)` (since we loop over 10 cards and perform constant-time operations).

**Total time complexity**: `O(T)`, where `T` is the range of possible `current_hand` values we compute.

In the worst case, if `starting_hand = 0` and `target` is large, `T = O(target)`.


### **Space Complexity**

- The space is dominated by:
  1. The **memoization dictionary (`memo`)** which stores `O(T)` entries.
  2. The **recursion stack depth**, which is `O(T)` in the worst case (if we draw `1`s repeatedly until we reach
  `current_hand > target`).

**Total space complexity**: `O(T)`.

### **Final Answer**

- **Time Complexity**: `O(T)`, where `T = target - starting_hand + 10` (or `O(target)` in the worst case).
- **Space Complexity**: `O(T)` (due to memoization and recursion stack).

This is efficient due to memoization, avoiding exponential recomputation.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
This code calculates the **probability of busting (going over a target number)** in a simplified version of blackjack, where
the player repeatedly draws cards (valued 1 through 10, each with equal probability) until they either bust or reach a point
where drawing again has too much risk.

---

### 🔢 **Function Signature Overview**

```
def blackjack_probability(target, starting_hand):
```
- `target`: the maximum value the player wants to **avoid exceeding** (typically 21).
- `starting_hand`: current hand total before drawing more cards.

---

## 🔁 Main Workflow

### Step 1: `blackjack_probability()`

```
memo = {}
return round(calculate_probability(starting_hand, target, memo), 3)
```

- Initializes a `memo` dictionary for **memoization** (caching results to avoid recomputation).
- Calls the recursive helper `calculate_probability()` with the current hand and target.
- Rounds the result to 3 decimal places.

---

### Step 2: `calculate_probability(current_hand, target, memo)`

This is a **recursive function** that computes the probability of **busting** from a given hand total.

```
if current_hand in memo:
    return memo[current_hand]
```
- **Memoization check**: If we’ve already calculated the probability from this hand value, reuse it.

---

### 📌 Base Cases

```
if current_hand > target:
    return 1
```
- **Busted**: If the current hand exceeds the target, return `1` (100% probability of busting — already busted).

```
if current_hand + 4 >= target:
    return 0
```
- **Stop drawing**: If the maximum average draw (`+4`) brings us to or past the target, we **should not draw** — risk is too high.
- This is a **heuristic**: since average draw is ~5.5, checking with +4 is a safety margin to stop drawing.

---

### 🔄 Recursive Calculation

```
total_probability = 0
for drawn_card in range(1, 11):
    total_probability += 0.1 * calculate_probability(current_hand + drawn_card, target, memo)
```
- For each card value `1 to 10`:
  - Add the probability of busting if you draw that card.
  - Since all cards are equally likely, each has a probability of `0.1`.

```
memo[current_hand] = total_probability
return total_probability
```
- Cache the result for this hand total.
- Return the probability of busting from this hand.

---

## 📊 Example: `blackjack_probability(21, 15)`

- Start with 15.
- Drawing cards 1–6 won’t bust you; 7+ will.
- Recursively compute the risk of busting for each possible draw:
  - E.g., if you draw 3, your new hand is 18, so you compute bust probability starting from 18.

---

### ✅ Test Cases

```
print(blackjack_probability(21, 15))  # 0.45
```
- There's a 45% chance you'll bust eventually if you keep drawing from 15 toward 21.

```
print(blackjack_probability(21, 21))  # 0
```
- You’re at the target. You won’t draw. No chance of busting.

```
print(blackjack_probability(10, 3))  # 0.395
```
- You start low, but target is also low — must stop early to avoid going over 10. Hence, some bust risk.

---

## 🧠 Summary

This algorithm uses:
- **Recursion with memoization** to avoid recomputing probabilities for the same hand.
- A **probabilistic model** assuming equal chance (10%) for drawing cards from 1 to 10.
- A **cutoff heuristic (`+4`)** to decide when to stop drawing.

"""
