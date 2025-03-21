# Problem Description:

"""

                                                # Min Rewards

Imagine that you're a teacher who's just graded the final exam in a class. You have a list of student scores on the final exam
in a particular order (not necessarily sorted), and you want to reward your students. You decide to do so fairly by giving them
arbitrary rewards following two rules:

    1. All students must receive at least one reward.

    2. Any given student must receive strictly more rewards than an adjacent student (a student immediately to the left or to the
    right) with a lower score and must receive strictly fewer rewards than an adjacent student with a higher score.

Write a function that takes in a list of scores and returns the minimum number of rewards that you must give out to students to
satisfy the two rules.

You can assume that all students have different scores; in other words, the scores are all unique.


## Sample Input:
```
scores = [8, 4, 2, 1, 3, 6, 7, 9, 5]
```

## Sample Output:
```
25 // you would give out the following rewards: [4, 3, 2, 1, 2, 3, 4, 5, 1]
```

## Optimal Time & Space Complexity:
```
O(n) time | O(n) space - where `n` is the length of the input array.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n) time | O(n) space - where `n` is the length of the input array
def min_rewards(scores):
    # Initialize a list of rewards with 1 for each student
    rewards = [1 for _ in scores]

    # First pass: Traverse the scores from left to right
    # If the current student's score is higher than the previous one,
    # give them one more reward than the previous student
    for i in range(1, len(scores)):
        if scores[i] > scores[i - 1]:
            rewards[i] = rewards[i - 1] + 1

    # Second pass: Traverse the scores from right to left
    # If the current student's score is higher than the next one,
    # ensure they have at least one more reward than the next student
    # (but don't reduce their reward if it's already higher)
    for i in reversed(range(len(scores) - 1)):
        if scores[i] > scores[i + 1]:
            rewards[i] = max(rewards[i], rewards[i + 1] + 1)

    # Return the sum of all rewards
    return sum(rewards)


# Test Cases:

print(min_rewards([8, 4, 2, 1, 3, 6, 7, 9, 5]))
# Output: 25

print(min_rewards([0, 4, 2, 1, 3]))
# Output: 9

print(min_rewards([1]))
# Output: 1

# =========================================================================================================================== #
