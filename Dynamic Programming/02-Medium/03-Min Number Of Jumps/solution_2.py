# Problem Description:

"""
                                            Min Number Of Jumps

You're given a `non-empty` array of positive integers where each integer represents the maximum number of steps you can take
forward in the array. For example, if the element at index `1` is `3`, you can go from index `1` to index `2`, `3`, or `4`.

Write a function that returns the minimum number of jumps needed to reach the final index.

> Note that jumping from index `i` to index `i + x` always constitutes one jump, no matter how large `x` is.


## Sample Input:
```
array = [3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]
```

## Sample Output:
```
4

// 3 --> (4 or 2) --> (2 or 3) --> 7 --> 3
```

## Optimal Time & Space Complexity:
```
O(n) time | O(1) space - where `n` is the length of the input array.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n) time | O(1) space
def min_number_of_jumps(array):
    # If the array has 0 or 1 elements, no jumps are needed
    if len(array) <= 1:
        return 0

    jumps = 0  # Counts the number of jumps made
    max_reach = array[0]  # The farthest index that can be reached with current jumps
    current_end = array[0]  # The end of the current jump's range

    # Iterate through the array (excluding the last element)
    for i in range(1, len(array) - 1):
        # Update the maximum reachable index from the current position
        max_reach = max(max_reach, i + array[i])

        # When we reach the end of the current jump's range,
        # we need to make another jump
        if i == current_end:
            jumps += 1
            # The new jump's range extends to the max_reach
            current_end = max_reach

    # We need one more jump to reach the end from the last position
    return jumps + 1


# Test Cases:

print(min_number_of_jumps([3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]))
# Output: 4

print(min_number_of_jumps([2, 1, 2, 3, 1]))
# Output: 2

print(min_number_of_jumps([1]))
# Output: 0

# =========================================================================================================================== #

# Big O Analysis:

"""
# Time and Space Complexity Analysis:

Let's analyze the time and space complexity of the given `min_number_of_jumps` function.

## **Time Complexity: O(n)**

- The function iterates through the `array` once with a single loop from index `1` to `len(array) - 2`.
This results in **O(n)** time, where `n` is the length of the array.
- Inside the loop, each operation (comparison, arithmetic, assignment) is **O(1)**, so the overall complexity remains linear.

## **Space Complexity: O(1)**

- The function uses a constant amount of extra space (`jumps`, `max_reach`, `current_end`), regardless of input size.
Thus, the space complexity is **O(1)** (constant space).

### Summary:
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
Here's a detailed breakdown of how the `min_number_of_jumps` function works:

---

### ✅ **Problem Summary**

You are given an array where each element represents the maximum number of steps you can jump forward from that position.

> Your goal is to find the **minimum number of jumps** needed to reach the **end of the array**, starting at index `0`.

---

### 🔍 **Function Definition**

```
def min_number_of_jumps(array):
```

This function receives an input list `array`, which contains integers representing jump lengths from each index.

---

### 🧪 **Edge Case: Array of Length 0 or 1**

```
    if len(array) <= 1:
        return 0
```

* If the array has only one element (or none), you're already at the end.
* **0 jumps needed**.

---

### 🧮 **Initial Setup**

```
    jumps = 0
    max_reach = array[0]
    current_end = array[0]
```

* `jumps`: Counts how many jumps have been made.
* `max_reach`: The farthest index we **can** reach with the current or next jump.
* `current_end`: The end of the range for the **current** jump. When the loop index `i` reaches this point, we **must jump** again.

---

### 🔁 **Main Loop**

```
    for i in range(1, len(array) - 1):
```

* Start from index 1 and go up to the second-to-last index (`len(array) - 2`).
* Why not include the last index? Because you can reach it with the last jump — no need to "jump" from the last index.

---

### 🔧 **Update max_reach**

```
    max_reach = max(max_reach, i + array[i])
```

* We keep track of the **farthest point** we can reach from all indices seen so far.
* `i + array[i]` = how far we can jump from index `i`.

---

### 🚀 **Time to Jump?**

```
    if i == current_end:
        jumps += 1
        current_end = max_reach
```

* If we've reached the end of the range of the **current jump**, we:

  * Increment the `jumps` counter.
  * Update `current_end` to `max_reach`, meaning the next jump's reach.

---

### 🔚 **Final Return**

```
    return jumps + 1
```

* At the end of the loop, we add **1 more jump** to reach the final destination.
* Why? Because the last jump to get **into the final segment** happens **after** the last `i == current_end` condition.

---

### 📌 **Test Cases Explanation**

---

#### 🧪 Test 1:

```
print(min_number_of_jumps([3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]))
# Output: 4
```

* Path: Jump from index 0 → 1 → 5 → 6 → 10
* Jump values: `3 → 4 → 3 → 7 → 3`

---

#### 🧪 Test 2:

```
print(min_number_of_jumps([2, 1, 2, 3, 1]))
# Output: 2
```

* Path: 0 → 2 → 4

---

#### 🧪 Test 3:

```
print(min_number_of_jumps([1]))
# Output: 0
```

* Already at the end, no jumps required.

---

### 📈 Time and Space Complexity

* **Time Complexity**: `O(n)` — Single loop through the array.
* **Space Complexity**: `O(1)` — No extra space used.

---

Let’s walk through an ASCII **visualization** of how `min_number_of_jumps` works — using the first test case:

---

### 🔢 Input:

```
array = [3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]
```

### 🎯 Goal:

Find the **minimum number of jumps** to reach the end (index 10).

---

## 📊 Step-by-Step ASCII Visualization

```
Index:    0   1   2   3   4   5   6   7   8   9   10
Value:    3   4   2   1   2   3   7   1   1   1   3
           ^   ^                       ^           ^
           |   |                       |           |
       Start  1st Jump           3rd Jump       End Goal
```

---

### 🔁 Loop Execution

Let’s simulate what the algorithm does in each step:

| i | `array[i]` | `max_reach` | `current_end` | `jumps` | Description                                             |
| - | ---------- | ----------- | ------------- | ------- | ------------------------------------------------------- |
| 0 | 3          | 3           | 3             | 0       | Initial setup                                           |
| 1 | 4          | 5 (`1+4`)   | 3             | 0       | Can reach index 5 now                                   |
| 2 | 2          | 5           | 3             | 0       | Still within current jump                               |
| 3 | 1          | 5           | 3             | **1**   | Reached `current_end`, jump → update `current_end = 5`  |
| 4 | 2          | 6 (`4+2`)   | 5             | 1       | Can now reach index 6                                   |
| 5 | 3          | 8 (`5+3`)   | 5             | **2**   | Reached `current_end`, jump → update `current_end = 8`  |
| 6 | 7          | 13 (`6+7`)  | 8             | 2       | Can reach beyond end                                    |
| 7 | 1          | 13          | 8             | 2       | Still within current jump                               |
| 8 | 1          | 13          | 8             | **3**   | Reached `current_end`, jump → update `current_end = 13` |

### 🏁 Finish

We finish loop at index 9. One more jump will land us at or past the last index (10), so:

```
return jumps + 1  # 3 + 1 = 4
```

---

### ✅ Final Result: **4 jumps**

---

## 💡 ASCII Timeline of Jumps

```
[3]---\
       [4, 2, 1]---\
                    [2, 3]---\
                              [7, 1, 1, 1, 3]
Jump1       Jump2       Jump3       Jump4 (into final segment)
```

"""
