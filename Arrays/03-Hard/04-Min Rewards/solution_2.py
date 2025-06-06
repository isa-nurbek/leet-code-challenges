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
25 

// You would give out the following rewards: [4, 3, 2, 1, 2, 3, 4, 5, 1]
```

## Optimal Time & Space Complexity:
```
O(n) time | O(n) space - where `n` is the length of the input array.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n^2) time | O(n) space
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

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### Time Complexity Analysis

1. **`get_local_min_idxs(array)`**:
   - This function iterates through the entire array once to find local minima.
   
   - **Time Complexity**: O(n), where `n` is the length of the array.

2. **`expand_from_local_min_idx(local_min_idx, scores, rewards)`**:
   - This function expands from a local minimum to the left and right, updating the rewards.
   - In the worst case, it could traverse the entire array (e.g., if the array is strictly increasing or decreasing).
   
   - **Time Complexity**: O(n) for each local minimum.

3. **`min_rewards(scores)`**:
   - The function first initializes the `rewards` array, which takes O(n) time.
   - It then calls `get_local_min_idxs`, which takes O(n) time.
   - For each local minimum, it calls `expand_from_local_min_idx`, which takes O(n) time.
   - If there are `k` local minima, the total time complexity for this part is O(k * n).

   - In the worst case, the number of local minima `k` could be proportional to `n` (e.g., alternating peaks and valleys), 
   so the total time complexity becomes O(n^2).

---

### Space Complexity Analysis

1. **`get_local_min_idxs(array)`**:
   - This function uses a list to store the indices of local minima.
   - **Space Complexity**: O(n) in the worst case (if every element is a local minimum).

2. **`expand_from_local_min_idx(local_min_idx, scores, rewards)`**:
   - This function uses a constant amount of extra space (for indices and temporary variables).
   - **Space Complexity**: O(1).

3. **`min_rewards(scores)`**:
   - The function uses an additional `rewards` array of size `n`.
   - **Space Complexity**: O(n).

### Summary

- **Time Complexity**: O(n^2) in the worst case.
- **Space Complexity**: O(n).

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
This code is an implementation of the **Minimum Rewards Problem**, where students are given a score, and we need to assign
rewards based on the given conditions:

- Every student must get at least **one** reward.
- A student with a **higher** score than an adjacent student must receive **more** rewards.

### **Code Breakdown**

#### **1. `min_rewards(scores)` Function**

This is the main function that calculates the minimum total rewards required.

- **Step 1**: Initialize a `rewards` list, where each student starts with **one reward**.
- **Step 2**: Find the **local minima** (students with scores lower than their adjacent students).
- **Step 3**: Expand from each local minimum to adjust the reward distribution.
- **Step 4**: Return the total sum of rewards.

---

#### **2. `get_local_min_idxs(array)` Function**

This function identifies the **local minima** in the given `scores` array.

- **Local Minimum**: A student is a local minimum if their score is lower than their adjacent students.
- **Edge Cases**:
  - If there is only **one** student, they are a local minimum.
  - The first element is a local minimum if it is smaller than the second element.
  - The last element is a local minimum if it is smaller than the second-last element.
  - Any other element is a local minimum if it is **smaller than both its neighbors**.

Example:
```
scores = [8, 4, 2, 1, 3, 6, 7, 9, 5]
```
Local minima are:
- `1` at index `3`
- `5` at index `8`

---

#### **3. `expand_from_local_min_idx(local_min_idx, scores, rewards)` Function**

This function ensures that all students get the correct number of rewards.

- **Left Expansion**: It moves leftward from the `local_min_idx` and ensures students with higher scores than
their right neighbors receive more rewards.

- **Right Expansion**: It moves rightward from the `local_min_idx` and ensures students with higher scores than
their left neighbors receive more rewards.

**Example Walkthrough:**

Let’s consider the input:
```
scores = [8, 4, 2, 1, 3, 6, 7, 9, 5]
```
1. Initially, `rewards = [1, 1, 1, 1, 1, 1, 1, 1, 1]`.
2. **Identify Local Minima:** `{3, 8}`.
3. **Expanding from index `3` (score 1):**
   - Right expansion updates: `[1, 1, 1, 1, 2, 3, 4, 5, 1]`
   - Left expansion updates: `[3, 2, 2, 1, 2, 3, 4, 5, 1]`
4. **Expanding from index `8` (score 5):**
   - No left expansion needed.
   - Right expansion not needed as it’s the last element.

Final rewards:
```
[3, 2, 2, 1, 2, 3, 4, 5, 1]
```
Sum: `25`

---

### **Test Cases**

#### **Test Case 1**
```
print(min_rewards([8, 4, 2, 1, 3, 6, 7, 9, 5]))
```
**Output**:
```
25
```
---

#### **Test Case 2**
```
print(min_rewards([0, 4, 2, 1, 3]))
```
**Explanation**:
- Local minima: `{0, 3}`
- Expanding rewards: `[1, 2, 1, 1, 2]`
- Total: `9`

**Output**:
```
9
```
---

#### **Test Case 3**
```
print(min_rewards([1]))
```
**Explanation**:
- Only one student, so the minimum reward is `1`.

**Output**:
```
1
```
"""
