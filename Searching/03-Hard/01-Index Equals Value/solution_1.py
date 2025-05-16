# Problem Description:

"""
                                             Index Equals Value

Write a function that takes in a sorted array of distinct integers and returns the first index in the array that is equal to the
value at that index. In other words, your function should return the minimum index where `index == array[index]`.

If there is no such index, your function should return `-1`.


## Sample Input:
```
array = [-5, -3, 0, 3, 4, 5, 9]
```

## Sample Output:
```
3

// 3 == array[3]
```

## Optimal Time & Space Complexity:
```
O(log(n)) time | O(1) space - where `n` is the length of the input array.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n) time | O(1) space
def index_equals_value(array):
    """
    Finds the first index in a sorted array where the value equals the index.

    Args:
        array: A sorted list of integers to search through.

    Returns:
        int: The first index where array[index] == index, or -1 if no such index exists.
    """

    # Iterate through each index in the array
    for idx in range(len(array)):
        # Get the value at the current index
        value = array[idx]

        # Check if the value matches the index
        if value == idx:
            # Return the first matching index found
            return idx

    # If no index matches its value, return -1
    return -1


# Test Cases:

print(index_equals_value([-5, -3, 0, 3, 4, 5, 9]))
# Output: 3

print(index_equals_value([-12, 1, 2, 3, 12]))
# Output: 1

print(index_equals_value([-5, -4, -3, -2, -1, 0, 1, 3, 5, 6, 7, 11, 12, 14, 19, 20]))
# Output: 11

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### Time Complexity:

The function iterates through each element of the array exactly once in the worst case (if no element satisfies `array[idx] == idx`). 

- **Best Case**: The first element satisfies the condition (`array[0] == 0`), and the function returns immediately.
Time complexity is \( O(1) \).

- **Worst Case**: No element satisfies the condition, or the matching element is at the end of the array.
The loop runs `n` times (where `n`) is the length of the array).
Time complexity is O(n).

- **Average Case**: On average, the loop may run `n/2` times, but this still simplifies to O(n).

Thus, the **time complexity is O(n)**.

### Space Complexity:

The function uses a constant amount of additional space (variables like `idx` and `value`), regardless of the input size. 

- No extra data structures or recursive calls are used.
- Thus, the **space complexity is O(1)** (constant space).

### Summary:
- **Time Complexity**: O(n) 
- **Space Complexity**: O(1) 

### Optimization Note:

The current implementation is a linear scan, which is optimal in the worst case. However, if the array is **sorted**,
a **binary search** approach could reduce the time complexity to O(log n). But for an unsorted array, O(n) is the best possible.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
Let’s break down the function `index_equals_value` and its test cases in detail.

### 🔍 **Problem Statement:**

Given a **sorted array of integers**, find the **smallest index `i`** such that `array[i] == i`.
If no such index exists, return `-1`.

---

### ✅ **Function Definition**

```
def index_equals_value(array):
    for idx in range(len(array)):
        value = array[idx]

        if value == idx:
            return idx

    return -1
```

---

### 🧠 **Step-by-Step Explanation**

#### 1. **Iterate through the array**

```
for idx in range(len(array)):
```

* This loop goes from index `0` to `len(array) - 1`.
* `idx` is the index of the current element being checked.

#### 2. **Access value at each index**

```
value = array[idx]
```

* Retrieve the element at index `idx`.

#### 3. **Check if value equals index**

```
if value == idx:
    return idx
```

* If the value at index `idx` is equal to `idx`, return that index immediately.
* Since we are going from left to right, this ensures the **first (smallest) matching index** is returned.

#### 4. **If loop completes with no match**

```
return -1
```

* If no such index was found, return `-1`.

---

### 🧪 **Test Case Analysis**

#### Test Case 1:

```
print(index_equals_value([-5, -3, 0, 3, 4, 5, 9]))
```

* Indices:     0   1   2   3   4   5   6
* Values:     -5  -3   0   3   4   5   9
* Check each index:

  * index 0: -5 ≠ 0
  * index 1: -3 ≠ 1
  * index 2:  0 ≠ 2
  * index 3:  3 == 3 ✅ → return 3

**Output: `3`**

---

#### Test Case 2:

```
print(index_equals_value([-12, 1, 2, 3, 12]))
```

* Indices:     0   1   2   3   4
* Values:    -12   1   2   3  12
* index 0: -12 ≠ 0
* index 1:  1 == 1 ✅ → return 1

**Output: `1`**

---

#### Test Case 3:

```
print(index_equals_value([-5, -4, -3, -2, -1, 0, 1, 3, 5, 6, 7, 11, 12, 14, 19, 20]))
```

* Indices:      0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15
* Values:      -5  -4  -3  -2  -1   0   1   3   5   6   7  11  12  14  19  20
* Check:

  * index 0 to 10 → no match
  * index 11: value = 11 == index ✅ → return 11

**Output: `11`**

---

### 🧠 Summary

* The function **returns the smallest index** where `array[index] == index`.
* It **stops as soon as it finds** the first such match — optimal in linear scan.
* **Time complexity**:

  * Worst case: **O(n)** where `n` is the length of the array.
* **Space complexity**:

  * **O(1)** (no extra space used)

---

Let's visualize the function and its behavior using **ASCII diagrams**. We'll walk through one of the test cases step by step.

### 🔍 **Function Visualization (ASCII)**

Let’s take this test case:

```
index_equals_value([-5, -3, 0, 3, 4, 5, 9])
```

---

### 📊 **Step-by-Step Table**

| Index (`i`) | Value (`array[i]`) | `array[i] == i?`  |
| ----------- | ------------------ | ----------------- |
| 0           | -5                 | ❌                |
| 1           | -3                 | ❌                |
| 2           | 0                  | ❌                |
| 3           | 3                  | ✅ ← MATCH!       |
| 4           | 4                  | (not checked)     |
| 5           | 5                  | (not checked)     |
| 6           | 9                  | (not checked)     |

---

### 🔁 **Loop Progress (ASCII visualization)**

```
Array:      [-5, -3,  0,  3,  4,  5,  9]
Index:       0   1   2   3   4   5   6
              ↓   ↓   ↓   ↓
            -5≠0 -3≠1 0≠2  3==3  ✅
                        ↑
           Loop stops and returns index 3
```

---

### 🧠 Final Result:

```
Output: 3
```

"""
