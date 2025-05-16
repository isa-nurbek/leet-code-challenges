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


# O(log(n)) time | O(log(n)) space
def index_equals_value(array):
    """
    Finds the first index in a sorted array where array[index] == index.
    Uses a helper function to perform binary search recursively.

    Args:
        array: A sorted list of integers where elements are distinct and in increasing order.

    Returns:
        The first index where array[index] == index, or -1 if no such index exists.
    """
    return index_equals_value_helper(array, 0, len(array) - 1)


def index_equals_value_helper(array, left_idx, right_idx):
    """
    Helper function that performs binary search to find the first index where array[index] == index.

    Args:
        array: The sorted list of integers to search
        left_idx: Left boundary of the current search range
        right_idx: Right boundary of the current search range

    Returns:
        The first matching index found, or -1 if none exists in the current range
    """

    # Base case: search range is invalid, meaning no match was found
    if left_idx > right_idx:
        return -1

    # Calculate middle index to split search range
    middle_idx = left_idx + (right_idx - left_idx) // 2
    middle_value = array[middle_idx]

    if middle_value < middle_idx:
        # If value is less than index, all elements to the left must also be smaller
        # because array is strictly increasing. So we search right half.
        return index_equals_value_helper(array, middle_idx + 1, right_idx)
    elif middle_value == middle_idx and middle_idx == 0:
        # Found match at index 0 (can't check left neighbor)
        return middle_idx
    elif middle_value == middle_idx and array[middle_idx - 1] < middle_idx - 1:
        # Found match where previous element doesn't match, so this is first occurrence
        return middle_idx
    else:
        # Either:
        # 1) Value > index, so we need to search left half, or
        # 2) Value == index but there might be earlier matches, so search left half
        return index_equals_value_helper(array, left_idx, middle_idx - 1)


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

The function implements a modified binary search algorithm.

Here's why:

1. **Binary Search Approach**: The helper function divides the search space in half at each recursive call, similar to
standard binary search.

2. **Constant Work per Step**: In each recursive call, it performs a constant amount of work (calculating the middle index,
comparing values, etc.).

3. **Recursive Calls**: The recursion reduces the problem size by approximately half each time.

Since the search space is halved at each step, the time complexity is **O(log n)**, where `n` is the length of the input array.

### Space Complexity:

The space complexity depends on whether the recursion is tail-optimized or not:

1. **Recursive Calls**: The helper function is recursive, and in the worst case, it can make **O(log n)** nested calls before
reaching the base case (since the depth of recursion is logarithmic in the size of the array).

2. **Stack Space**: Each recursive call consumes stack space for parameters and local variables.

Thus, the space complexity is **O(log n)** due to the recursion stack. If this were implemented iteratively instead of recursively,
the space complexity could be reduced to **O(1)**.

### Final Answer:
- **Time Complexity**: **O(log n)**
- **Space Complexity**: **O(log n)** (due to recursion stack; could be O(1) if rewritten iteratively)

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
Let’s go through your code **step by step**, breaking it down into:

1. **Purpose**
2. **Main function overview**
3. **Recursive logic in detail**
4. **How it finds the earliest match**
5. **Examples/walkthrough**
6. **Time and space complexity**

---

### ✅ 1. **Purpose of the Function**

The goal is to **find the smallest index `i`** in a **sorted array** such that:

array[i] = i

If no such index exists, return `-1`.

---

### ✅ 2. **Main Function Overview**

```
def index_equals_value(array):
    return index_equals_value_helper(array, 0, len(array) - 1)
```

This is the main function. It starts a binary search on the full array using a helper function.

---

### ✅ 3. **Recursive Helper Function in Detail**

```
def index_equals_value_helper(array, left_idx, right_idx):
    if left_idx > right_idx:
        return -1
```

* Base case: If the range is invalid, return `-1`.

---

```
middle_idx = left_idx + (right_idx - left_idx) // 2
middle_value = array[middle_idx]
```

* This computes the middle index safely (avoiding overflow in other languages).
* `middle_value` is the element at that index.

---

#### Now we have 3 cases to consider:

```
if middle_value < middle_idx:
    return index_equals_value_helper(array, middle_idx + 1, right_idx)
```

**Case 1:** If the value is **less than** its index, we can **safely discard the left half** and search right.

> Why? Because all values before `middle_idx` will be even **smaller** (array is sorted), so `array[i] < i` will remain true.

---

```
elif middle_value == middle_idx and middle_idx == 0:
    return middle_idx
```

**Case 2:** If a match is found at index `0`, immediately return it (this is the earliest possible match).

---

```
elif middle_value == middle_idx and array[middle_idx - 1] < middle_idx - 1:
    return middle_idx
```

**Case 3:** If a match is found, and the **previous element** does not satisfy the condition (`array[i-1] < i-1`),
then this is the **first valid match**, so we return `middle_idx`.

---

```
else:
    return index_equals_value_helper(array, left_idx, middle_idx - 1)
```

**Case 4:** Otherwise, search **left** for a smaller index match.

---

### ✅ 4. **How It Finds the Earliest Match**

Even though a match is found (`array[i] == i`), the algorithm checks whether it's the **first** such match by examining the
**left side** unless it's sure this is the earliest.

The condition:

```
array[middle_idx - 1] < middle_idx - 1
```

means the left side doesn't contain a match (`array[i] = i`), so current index is the first one.

---

### ✅ 5. **Test Case Walkthrough**

Example:

```
print(index_equals_value([-5, -3, 0, 3, 4, 5, 9]))
```

**Step-by-step:**

* Input array: `[-5, -3, 0, 3, 4, 5, 9]`
* Start: `left = 0`, `right = 6`
* Middle: `middle = 3`, `array[3] = 3`

  * Match found! Check `array[2] = 0 < 2` → ✅, so return `3`

---

### ✅ 6. **Time and Space Complexity**

#### **Time Complexity:**

* Since you're using **binary search**, each step cuts the search space in half.
* Worst-case time: **O(log n)**

#### **Space Complexity:**

* The function is **recursive**, so it uses the call stack.
* Max depth = **log n**, so space: **O(log n)**

---

### ✅ Summary

| Feature               | Description                                   |
| --------------------- | --------------------------------------------- |
| Purpose               | Find smallest index `i` where `array[i] == i` |
| Approach              | Modified binary search                        |
| Early Match Detection | By checking left neighbor                     |
| Time Complexity       | `O(log n)`                                    |
| Space Complexity      | `O(log n)` due to recursion                   |
| Edge Case Handling    | Ensures earliest match is returned            |

---

Let's visualize how the binary search works step-by-step using ASCII art. We'll use this example:

```
index_equals_value([-5, -3, 0, 3, 4, 5, 9])
```

We want to find the **smallest index** `i` such that:

array[i] == i

---

### 🔢 Step-by-step Binary Search (ASCII)

#### Initial Array:

```
Index :     0    1    2    3    4    5    6
Array :   [-5,  -3,   0,   3,   4,   5,   9]
```

### 🔍 Step 1:

```
Left: 0, Right: 6
Middle = (0 + 6) // 2 = 3
Check: array[3] = 3

✅ Match found! array[3] == 3
Now check: array[2] = 0 < 2 ➜ So no earlier match exists.
Return 3.
```

We visualize the decision as:

```
         Search Range: [0 ----------- 6]
         Middle Index:           3
                         ^ Match: array[3] == 3
                         Check array[2] < 2 → true
                         => Return 3
```

---

### 📦 Another Example

```
index_equals_value([-12, 1, 2, 3, 12])
```

```
Index :     0     1     2     3     4
Array :  [-12,   1,    2,    3,   12]
```

### 🔍 Step 1:

```
Left: 0, Right: 4
Middle = (0 + 4) // 2 = 2
Check: array[2] = 2

✅ Match found! array[2] == 2
Check: array[1] = 1 == 1 ❌
So go left and try to find smaller match.
```

### 🔍 Step 2 (Left half):

```
Left: 0, Right: 1
Middle = (0 + 1) // 2 = 0
array[0] = -12 ≠ 0 ➜ go right
```

### 🔍 Step 3:

```
Left: 1, Right: 1
Middle = 1
array[1] = 1 ✅ Match!
Check: array[0] = -12 < 0 ✅
Return 1
```

Visual Summary:

```
Initial Range:     [0 --------------- 4]
                          ^
                      Middle: 2 (Match)
                      Go left for smaller

Search Left:        [0 --- 1]
                      ^
                   array[1] == 1
                   array[0] < 0
                   => Return 1
```

---

### ✅ ASCII Flow Summary of Search

```
While left <= right:
    middle = (left + right) // 2

             [left ------------ right]
                    ^
                 middle

    If array[middle] < middle:
        Discard left half → left = middle + 1

    Else if array[middle] == middle:
        Check if it's the first such match
        If yes: return
        Else: search left

    Else:
        Discard right half → right = middle - 1
```

"""
