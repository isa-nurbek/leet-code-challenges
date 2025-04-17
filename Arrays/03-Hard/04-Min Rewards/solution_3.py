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


# O(n) time | O(n) space
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

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### Time Complexity Analysis

1. **Initialization of `rewards` array**: 
   - This step involves creating an array of size `n` (where `n` is the length of the `scores` array) and initializing
   each element to 1. This operation takes O(n) time.

2. **First pass (left to right)**:
   - This loop iterates through the `scores` array from the second element to the last element. For each element, it
   compares the current score with the previous one and updates the `rewards` array accordingly. This loop runs in O(n) time.

3. **Second pass (right to left)**:
   - This loop iterates through the `scores` array from the second-to-last element to the first element. For each element, it
   compares the current score with the next one and updates the `rewards` array accordingly. This loop also runs in O(n) time.

4. **Summing the `rewards` array**:
   - This step involves summing all the elements in the `rewards` array, which takes O(n) time.

**Overall Time Complexity**:
- The time complexity is dominated by the three O(n) operations, so the total time complexity is O(n).

---

### Space Complexity Analysis

1. **`rewards` array**:
   - The `rewards` array is the only additional space used that scales with the input size. It requires O(n) space.

**Overall Space Complexity**:
- The space complexity is O(n) due to the `rewards` array.

### Summary

- **Time Complexity**: O(n)
- **Space Complexity**: O(n)

This algorithm efficiently computes the minimum number of rewards required in O(n) time and O(n) space.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
### **Explanation of the `min_rewards` function**

This function calculates the minimum number of rewards that should be distributed to students based on their scores.
The main constraint is that a student with a higher score than their adjacent student should receive more rewards.

---

### **Approach Used**

1. **Initialize Rewards**:  
   - Every student gets at least **one** reward initially.
   - We create a `rewards` array of the same length as `scores` and initialize all elements to `1`.

2. **Left-to-Right Pass**:  
   - We iterate **from left to right** (i.e., from index `1` to `n-1`).
   - If the **current score** is greater than the **previous score**, the current student should get more rewards
   than the previous student.
   
   - So, `rewards[i] = rewards[i - 1] + 1`.

3. **Right-to-Left Pass**:  
   - We iterate **from right to left** (i.e., from index `n-2` to `0`).
   - If the **current score** is greater than the **next score**, the current student should get more rewards than the next student.
   - To ensure correctness, we take the maximum of the existing reward and `rewards[i + 1] + 1`.
   
   - `rewards[i] = max(rewards[i], rewards[i + 1] + 1)`.

4. **Summing Up Rewards**:  
   - Finally, we return the sum of all elements in the `rewards` array.

---

### **Step-by-Step Execution**

#### **Example 1: `scores = [8, 4, 2, 1, 3, 6, 7, 9, 5]`**
1. **Initialize `rewards`**  
   ```
   scores:  [8, 4, 2, 1, 3, 6, 7, 9, 5]
   rewards: [1, 1, 1, 1, 1, 1, 1, 1, 1]  (All initialized to 1)
   ```

2. **Left-to-Right Pass**
   - If `scores[i] > scores[i-1]`, increase reward.
   ```
   scores:  [8, 4, 2, 1, 3, 6, 7, 9, 5]
   rewards: [1, 1, 1, 1, 2, 3, 4, 5, 1]  (Increasing rewards for rising values)
   ```

3. **Right-to-Left Pass**
   - If `scores[i] > scores[i+1]`, adjust reward.
   ```
   scores:  [8, 4, 2, 1, 3, 6, 7, 9, 5]
   rewards: [4, 3, 2, 1, 2, 3, 4, 5, 1]  (Ensuring fairness for decreasing values)
   ```

4. **Final Sum**  
   ```
   4 + 3 + 2 + 1 + 2 + 3 + 4 + 5 + 1 = 25
   ```
   **Output: `25`**

---

### **Edge Cases**

1. **Single Element (`scores = [1]`)**
   - Output: `1` (only one student, gets one reward)

2. **Already Increasing (`scores = [1, 2, 3, 4]`)**
   - Output: `1 + 2 + 3 + 4 = 10`

3. **Already Decreasing (`scores = [4, 3, 2, 1]`)**
   - Output: `4 + 3 + 2 + 1 = 10`

4. **All Equal Scores (`scores = [3, 3, 3, 3]`)**
   - Output: `1 + 1 + 1 + 1 = 4`

---

### **Conclusion**

- The function ensures fairness by making two passes over the `scores` array.
- It guarantees the **minimum rewards** distribution while satisfying the given constraints.

"""
