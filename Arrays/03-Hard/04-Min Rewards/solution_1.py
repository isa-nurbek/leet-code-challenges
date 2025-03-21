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


# O(n^2) time | O(n) space - where `n` is the length of the input array
def min_rewards(scores):
    # Initialize a list of rewards with 1 for each student
    rewards = [1 for _ in scores]

    # Traverse the scores from left to right
    for i in range(1, len(scores)):
        j = i - 1  # j is the index of the previous student

        # If the current student's score is higher than the previous one,
        # they should get more rewards than the previous student
        if scores[i] > scores[j]:
            rewards[i] = rewards[j] + 1
        else:
            # If the current student's score is not higher, we need to adjust
            # the rewards of previous students to ensure the rules are followed
            while j >= 0 and scores[j] > scores[j + 1]:
                # Update the reward of the previous student to be at least
                # one more than the next student
                rewards[j] = max(rewards[j], rewards[j + 1] + 1)
                j -= 1  # Move to the previous student

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

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### Time Complexity Analysis

The time complexity of the `min_rewards` function can be analyzed as follows:

1. **Initialization**: The initialization of the `rewards` array takes O(n) time, where `n` is the number of elements
in the `scores` array.

2. **First Pass (Left to Right)**:
   - The first loop iterates through the `scores` array once, comparing each element with its previous element.
   - This loop runs in O(n) time.

3. **Second Pass (Right to Left)**:
   - The second loop (inside the `else` block) iterates backward from the current index `i` to the start of the array.
   - In the worst case, this inner loop could run O(n) times for each element, leading to a total time complexity of O(n^2).

Thus, the **worst-case time complexity** of the function is O(n^2).

---

### Space Complexity Analysis

1. **Auxiliary Space**:
   - The `rewards` array is the only additional space used, which requires O(n) space.

Thus, the **space complexity** of the function is O(n).

---

### Summary

- **Time Complexity:** O(n^2)
- **Space Complexity:** O(n)

This is inefficient solution.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
### **Explanation of the `min_rewards` Function**

The `min_rewards` function calculates the minimum number of rewards to distribute among students based on their scores.
The rule is that students with higher scores must receive more rewards than their immediate neighbors with lower scores.

---

## **Step-by-Step Breakdown of the Code**

### **1. Initialization**
```
rewards = [1 for _ in scores]
```
- The `rewards` list is initialized with `1` for each student, meaning each student gets at least **one** reward.
- This ensures that no student is left without a reward.

---

### **2. First Pass (Left to Right)**
```
for i in range(1, len(scores)):
    j = i - 1

    if scores[i] > scores[j]:
        rewards[i] = rewards[j] + 1
```
- This loop **iterates from left to right**.
- If the **current score is greater than the previous score**, the current student must get **more** rewards than the previous one.
- So, the reward at index `i` is updated to `rewards[j] + 1`.

#### **Example of First Pass**

For `scores = [8, 4, 2, 1, 3, 6, 7, 9, 5]`, after this step:

| Index  | Scores | Rewards (after left-to-right pass) |
|--------|--------|------------------------------------|
| 0      | 8      | 1                                  |
| 1      | 4      | 1                                  |
| 2      | 2      | 1                                  |
| 3      | 1      | 1                                  |
| 4      | 3      | 2                                  |
| 5      | 6      | 3                                  |
| 6      | 7      | 4                                  |
| 7      | 9      | 5                                  |
| 8      | 5      | 1                                  |

Notice that we **only** increase the rewards when moving upwards (higher scores than previous ones).

---

### **3. Second Pass (Right to Left)**
```
else:
    while j >= 0 and scores[j] > scores[j + 1]:
        rewards[j] = max(rewards[j], rewards[j + 1] + 1)
        j -= 1
```
- When the **current score is not greater** than the previous one (indicating a descending slope), we need to adjust rewards.
- This ensures that **students in descending order get more rewards** than their right neighbor if needed.
- The `while` loop **iterates backward** and adjusts the rewards to **maintain the correct ordering**.

#### **Example of Second Pass**

After adjusting in descending order:

| Index  | Scores | Rewards (after right-to-left pass) |
|--------|--------|------------------------------------|
| 0      | 8      | 4                                  |
| 1      | 4      | 3                                  |
| 2      | 2      | 2                                  |
| 3      | 1      | 1                                  |
| 4      | 3      | 2                                  |
| 5      | 6      | 3                                  |
| 6      | 7      | 4                                  |
| 7      | 9      | 5                                  |
| 8      | 5      | 1                                  |

---

### **4. Final Step: Summing Rewards**
```
return sum(rewards)
```
- Finally, the function returns the **sum of all rewards**, which gives the minimum number of rewards required.

---

## **Test Cases Walkthrough**

### **1st Test Case**
```
print(min_rewards([8, 4, 2, 1, 3, 6, 7, 9, 5]))
```
- Minimum rewards required: **25**

### **2nd Test Case**
```
print(min_rewards([0, 4, 2, 1, 3]))
```
- Minimum rewards required: **9**

### **3rd Test Case**
```
print(min_rewards([1]))
```
- Only **one student**, so **only one reward** is needed.
- Output: **1**

---

## **Issues with This Implementation**

1. **The Right-to-Left Adjustment is Inefficient**
   - The while loop runs for **every** decreasing segment.
   - Instead of a `while` loop, a **single right-to-left pass** could be used, reducing redundant checks.

### **Optimized Approach**

A **better approach** would be:
1. **Left-to-right pass:** Increase rewards for increasing sequences.
2. **Right-to-left pass:** Adjust rewards for decreasing sequences.

We will do efficient approach in the next solution.

"""
