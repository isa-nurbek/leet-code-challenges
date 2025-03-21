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
    # Initialize rewards array with 1 for each student
    rewards = [1 for _ in scores]

    # Find the indices of local minimums in the scores array
    local_min_idxs = get_local_min_idxs(scores)

    # For each local minimum, expand left and right to assign rewards
    for local_min_idx in local_min_idxs:
        expand_from_local_min_idx(local_min_idx, scores, rewards)

    # Return the sum of all rewards
    return sum(rewards)


def get_local_min_idxs(array):
    # If the array has only one element, it's the only local minimum
    if len(array) == 1:
        return [0]

    local_min_idxs = []

    # Iterate through the array to find local minimums
    for i in range(len(array)):
        # Check if the first element is a local minimum
        if i == 0 and array[i] < array[i + 1]:
            local_min_idxs.append(i)

        # Check if the last element is a local minimum
        if i == len(array) - 1 and array[i] < array[i - 1]:
            local_min_idxs.append(i)

        # Skip the first and last elements since they are already handled
        if i == 0 or i == len(array) - 1:
            continue

        # Check if the current element is a local minimum
        if array[i] < array[i + 1] and array[i] < array[i - 1]:
            local_min_idxs.append(i)

    return local_min_idxs


def expand_from_local_min_idx(local_min_idx, scores, rewards):
    # Expand to the left of the local minimum
    left_idx = local_min_idx - 1

    while left_idx >= 0 and scores[left_idx] > scores[left_idx + 1]:
        # Ensure the reward is at least one more than the right neighbor
        rewards[left_idx] = max(rewards[left_idx], rewards[left_idx + 1] + 1)
        left_idx -= 1

    # Expand to the right of the local minimum
    right_idx = local_min_idx + 1

    while right_idx < len(scores) and scores[right_idx] > scores[right_idx - 1]:
        # Assign one more than the left neighbor
        rewards[right_idx] = rewards[right_idx - 1] + 1
        right_idx += 1


# Test Cases:

print(min_rewards([8, 4, 2, 1, 3, 6, 7, 9, 5]))
# Output: 25

print(min_rewards([0, 4, 2, 1, 3]))
# Output: 9

print(min_rewards([1]))
# Output: 1

# =========================================================================================================================== #
