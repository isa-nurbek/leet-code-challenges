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


# O(n²) time | O(n) space
def min_number_of_jumps(array):
    # Initialize a jumps array to store the minimum number of jumps needed to reach each position
    # Start with infinity for all positions except the first one (which takes 0 jumps to reach)
    jumps = [float("inf") for x in array]
    jumps[0] = 0  # Base case: no jumps needed to reach first element

    # Iterate through each position in the array starting from the second element
    for i in range(1, len(array)):
        # For each position i, check all previous positions j (0 to i-1)
        for j in range(0, i):
            # Check if from position j, we can jump to position i
            # This is possible if the value at j (array[j]) is >= the distance between j and i
            if array[j] >= i - j:
                # If we can jump from j to i, update jumps[i] to be the minimum between:
                # - its current value
                # - jumps[j] + 1 (jumps to reach j plus this one jump)
                jumps[i] = min(jumps[j] + 1, jumps[i])

    # The last element of jumps array contains the minimum jumps needed to reach the end
    return jumps[-1]


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

## Time Complexity:

1. **Initialization**: The `jumps` array is initialized in O(n) time, where n is the length of the input array.
2. **Nested Loops**:
   - The outer loop runs from `i = 1` to `i = n-1` (n-1 iterations).
   - The inner loop runs from `j = 0` to `j = i-1` (i iterations for each i).
   - For each `i`, the inner loop runs `i` times.
   So, the total number of operations is roughly `1 + 2 + 3 + ... + (n-1) = (n-1)*n/2 = O(n²)`.
3. **Operations Inside Inner Loop**:
   - The `if` condition and the `min` operation are O(1) per iteration.

Thus, the **total time complexity is O(n²)**.

## Space Complexity:

1. The `jumps` array uses O(n) additional space.
2. No other significant space is used (only a few variables like `i`, `j`).

Thus, the **space complexity is O(n)**.

### Summary:
- **Time Complexity**: O(n²) (due to nested loops).
- **Space Complexity**: O(n) (for the `jumps` array).

### Note:
This is a dynamic programming approach with a quadratic time complexity. There is a more efficient O(n) greedy solution for this
problem, but this implementation follows the DP approach.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
Let's walk through the function `min_number_of_jumps` step by step, along with what it does and how it solves the problem.

---

## 🔍 **Problem Description**

Given an array of **positive integers**, where each element represents the **maximum number of steps** you can jump forward from
that position, your goal is to compute the **minimum number of jumps** needed to reach the **end of the array** (last index),
starting at index 0.

### Example:

Input: `[3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]`
Output: `4`

This means you can reach the end in **4 jumps**.

---

## ✅ **Function Definition**

```
def min_number_of_jumps(array):
```

### 📌 Edge Case:

* The array will always have at least one element.
* The value at each index tells you how far you can jump.

---

## 🛠️ **Initialization**

```
    jumps = [float("inf") for x in array]
    jumps[0] = 0
```

### What this does:

* `jumps[i]` stores the **minimum number of jumps needed to reach index `i`**.
* Initially, you cannot reach any index, so all entries are set to infinity (`inf`) — a placeholder for "unreachable".
* You start at index `0`, so the number of jumps to reach it is `0`.

---

## 🔁 **Nested Loop**

```
    for i in range(1, len(array)):
        for j in range(0, i):
            if array[j] >= i - j:
                jumps[i] = min(jumps[j] + 1, jumps[i])
```

### Outer loop (`i`):

Goes from 1 to the end of the array — for each position `i`, we want to find out the minimum number of jumps to get there.

### Inner loop (`j`):

For each `i`, we look at **all previous indices `j`** and check:

* Can we jump from `j` to `i`?
  This is true if `array[j] >= i - j`.

### If yes:

Then:

```
jumps[i] = min(jumps[j] + 1, jumps[i])
```

* `jumps[j] + 1` means: if you can get to index `j` in `jumps[j]` jumps, and can jump from `j` to `i`, then it takes
`jumps[j] + 1` to get to `i`.

* We take the minimum among all such possible values to find the **least number of jumps**.

---

## 🏁 Return Final Result

```
    return jumps[-1]
```

* This returns the minimum number of jumps required to get to the **last index**.

---

## 🧪 Test Case Walkthrough

### Test Case 1:

```
min_number_of_jumps([3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3])
```

#### Visualizing Jumps:

* Start at index 0 → can jump up to 3 steps: `[1, 2, 3]`.
* From index 1 (value 4) → can jump up to 4 steps.
* Best path:

  * Jump from 0 → 1
  * Jump from 1 → 4
  * Jump from 4 → 6
  * Jump from 6 → end

✅ Minimum jumps: `4`

---

## 🧠 Time and Space Complexity

### ⏱ Time Complexity: `O(n²)`

* Nested loops: for each `i`, you may check up to `i` previous values.

### 💾 Space Complexity: `O(n)`

* Due to the `jumps[]` list storing min jumps to each index.

---

## 🔄 Optimization

There exists a **greedy O(n)** solution to this problem (not shown here) that keeps track of the current farthest reach, jumps left,
and number of jumps — more efficient for large inputs.

---

Let's visualize the execution of the `min_number_of_jumps` function with ASCII diagrams, using this input:

```
min_number_of_jumps([3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3])
```

---

## 🔢 Array and Indices

Let's label the array with indices and values:

```
Index:   0   1   2   3   4   5   6   7   8   9  10
Value:   3   4   2   1   2   3   7   1   1   1   3
```

Each number shows how far you can jump forward from that position.

---

## 🔄 Step-by-Step Jumps with Explanation

We want to find a **path from 0 to 10 (last index)** using the fewest jumps.

### Step 1: From Index 0 (Value = 3)

From index 0, we can jump to:

```
0 --→ 1
   --→ 2
   --→ 3
```

Jumps array:
`[0, 1, 1, 1, ∞, ∞, ∞, ∞, ∞, ∞, ∞]`

---

### Step 2: From Index 1 (Value = 4)

From index 1, jump range is:

```
1 --→ 2
   --→ 3
   --→ 4
   --→ 5
```

We update the jumps array where possible:

* 4 can be reached from 1 with 2 jumps
* 5 can be reached from 1 with 2 jumps

Jumps array:
`[0, 1, 1, 1, 2, 2, ∞, ∞, ∞, ∞, ∞]`

---

### Step 3: From Index 2 (Value = 2)

Jump to:

```
2 --→ 3
   --→ 4
```

`jumps[4] = min(2, jumps[2]+1 = 2)` → already 2
No update needed.

---

### Step 4: From Index 3 (Value = 1)

Jump to:

```
3 --→ 4
```

No improvement → skip.

---

### Step 5: From Index 4 (Value = 2)

```
4 --→ 5
   --→ 6
```

Update:

* `jumps[6] = jumps[4] + 1 = 3`

Jumps array:
`[0, 1, 1, 1, 2, 2, 3, ∞, ∞, ∞, ∞]`

---

### Step 6: From Index 5 (Value = 3)

```
5 --→ 6
   --→ 7
   --→ 8
```

Update:

* `jumps[7] = jumps[5] + 1 = 3`
* `jumps[8] = jumps[5] + 1 = 3`

Jumps array:
`[0, 1, 1, 1, 2, 2, 3, 3, 3, ∞, ∞]`

---

### Step 7: From Index 6 (Value = 7)

```
6 --→ 7
   --→ 8
   --→ 9
   --→ 10
```

Update:

* `jumps[9] = 4`
* `jumps[10] = 4`

Jumps array:
`[0, 1, 1, 1, 2, 2, 3, 3, 3, 4, 4]`

---

## ✅ Final Jumps Array

```
Index:   0   1   2   3   4   5   6   7   8   9  10
Jumps:   0   1   1   1   2   2   3   3   3   4   4
```

### 🔚 Minimum number of jumps to reach the end: **4**

---

## 📈 ASCII Flow of Jump Path (One of the optimal paths)

```
Start
  |
  v
[0] --3→ [1] --4→ [4] --2→ [6] --7→ [10]
```

**Explanation:**

* From 0, jump 1 step to 1
* From 1, jump 3 steps to 4
* From 4, jump 2 steps to 6
* From 6, jump 4 steps to 10

Total Jumps: **4**

"""
