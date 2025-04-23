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
