# Problem Description:

"""
                                             Find Three Largest Numbers

Write a function that takes in an array of at least `three integers` and, without sorting the input array, returns a sorted array
of the three largest integers in the input array.

The function should return duplicate integers if necessary; for example, it should return `[10, 10, 12]` for an input array of
`[10, 5, 9, 10, 12]`.


## Sample Input:
```
array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
```

## Sample Output:
```
[18, 141, 541]
```

## Optimal Time & Space Complexity:
```
O(n) time | O(1) space - where `n` is the length of the input array.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n) time | O(1) space
def find_three_largest_numbers(array):
    """
    Finds the three largest numbers in the input array in sorted order.

    Args:
        array: List of numbers to search through

    Returns:
        List of three largest numbers in ascending order [smallest, middle, largest]
    """
    # Initialize a list to hold our three largest numbers, starting with None values
    three_largest = [None, None, None]

    # Iterate through each number in the input array
    for num in array:
        # For each number, update our three_largest list if needed
        update_largest(three_largest, num)

    # Return the three largest numbers found
    return three_largest


def update_largest(three_largest, num):
    """
    Updates the three_largest list with the current number if it belongs in the top three.

    Args:
        three_largest: Current list of three largest numbers
        num: Number to potentially insert into the three_largest list
    """
    # Check if we should update the third position (largest number)
    if three_largest[2] is None or num > three_largest[2]:
        shift_and_update(three_largest, num, 2)
    # Else check if we should update the second position
    elif three_largest[1] is None or num > three_largest[1]:
        shift_and_update(three_largest, num, 1)
    # Else check if we should update the first position (smallest of top three)
    elif three_largest[0] is None or num > three_largest[0]:
        shift_and_update(three_largest, num, 0)


def shift_and_update(array, num, idx):
    """
    Shifts numbers to the left in the array and inserts the new number at the specified index.

    For example, if array is [a, b, c] and we insert at index 1 (for number x):
    - a gets discarded
    - b shifts to a's position
    - x is inserted at b's position
    - c remains unchanged

    Args:
        array: The array to modify
        num: The number to insert
        idx: The position where the number should be inserted
    """
    # Iterate through the array up to the specified index
    for i in range(idx + 1):
        if i == idx:
            # At the target index, insert the new number
            array[i] = num
        else:
            # For indices before the target, shift the next value left
            array[i] = array[i + 1]


# Test Cases:

print(find_three_largest_numbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]))
# Output: [18, 141, 541]

print(find_three_largest_numbers([55, 43, 11, 3, -3, 10]))
# Output: [11, 43, 55]

print(find_three_largest_numbers([7, 7, 7, 7, 7, 7, 8, 7, 7, 7, 7]))
# Output: [7, 7, 8]

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### **Time Complexity:**

1. **`find_three_largest_numbers(array)`**:
   - This function iterates over each element in the input array once (`O(n)` time, where `n` is the size of the array).
   - For each element, it calls `update_largest()`, which performs comparisons and possibly calls `shift_and_update()`.

2. **`update_largest(three_largest, num)`**:
   - This function performs at most 3 comparisons (`O(1)` time per call).

3. **`shift_and_update(array, num, idx)`**:
   - This function shifts elements in the `three_largest` array up to index `idx`. The worst case is when `idx = 2`, which
   requires shifting 3 elements (`O(1)` time since the array size is fixed at 3).

**Overall Time Complexity**:
- Since each element in the input array is processed in `O(1)` time (due to fixed-size operations),
the total time complexity is: O(n) where `n` is the number of elements in the input array.

---

### **Space Complexity:**

1. The algorithm uses an auxiliary array `three_largest` of size 3, which is **constant space**.
2. No additional space is used that scales with the input size.

**Overall Space Complexity**: O(1)

### **Summary:**
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
Let's break down each part in detail.

---

### ✅ High-Level Overview

The goal is to:

* Traverse the array once.
* Keep track of the **three largest elements** seen so far.
* Return them **in ascending order**.

---

### 🔍 Function Breakdown

---

#### 1. `find_three_largest_numbers(array)`

```
def find_three_largest_numbers(array):
    three_largest = [None, None, None]
    for num in array:
        update_largest(three_largest, num)
    return three_largest
```

**Purpose:**

* Initializes a list `three_largest` of size 3 with `None` (i.e., empty slots for the top 3 numbers).
* Iterates through each number in the input array.
* Calls `update_largest` to insert that number into the correct position **if it belongs in the top 3**.

---

#### 2. `update_largest(three_largest, num)`

```
def update_largest(three_largest, num):
    if three_largest[2] is None or num > three_largest[2]:
        shift_and_update(three_largest, num, 2)
    elif three_largest[1] is None or num > three_largest[1]:
        shift_and_update(three_largest, num, 1)
    elif three_largest[0] is None or num > three_largest[0]:
        shift_and_update(three_largest, num, 0)
```

**Purpose:**

* Decides **where** the current number fits in the `three_largest` list.
* The list is in ascending order: `three_largest[0] < [1] < [2]`
* If `num` is greater than the largest so far (`three_largest[2]`), it becomes the new largest, and the others are pushed down.
* If not, check if it's the second or third largest.

---

#### 3. `shift_and_update(array, num, idx)`

```
def shift_and_update(array, num, idx):
    for i in range(idx + 1):
        if i == idx:
            array[i] = num
        else:
            array[i] = array[i + 1]
```

**Purpose:**

* Shifts smaller elements to the left to make room for the new number at the correct index (`idx`).
* Example:
  Suppose `array = [10, 30, 50]` and `num = 60` needs to go at index 2 (the largest).
  Then:

  * `array[0] = array[1]` → 30
  * `array[1] = array[2]` → 50
  * `array[2] = 60`

This ensures that all values move **down one spot** and the new value is inserted in the right position.

---

### 🧪 Test Case Breakdown

#### Input:

```
find_three_largest_numbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7])
```

**Step-by-step:**

* Start with `[None, None, None]`
* After processing:

  * `141` → `[None, None, 141]`
  * `1` → `[None, 1, 141]`
  * `17` → `[1, 17, 141]`
  * `-7`, `-17`, `-27` → ignored
  * `18` → `[17, 18, 141]`
  * `541` → `[18, 141, 541]`
  * others (`8`, `7`, `7`) → ignored

✅ Final output: `[18, 141, 541]`

---

### 🧠 Why This Works Well

* **Time Complexity**: `O(n)` — only one pass through the array.
* **Space Complexity**: `O(1)` — fixed-size list (length 3).
* Handles **negative numbers**, **duplicates**, and **any array size ≥ 3**.

---

### 📝 Summary

* `three_largest = [small, medium, large]`
* Traverse array once.
* Use a helper to insert numbers in the right place.
* Maintain the list in **sorted order** as you go.

This is an **efficient and clean** way to solve the problem of finding the top 3 largest numbers in a list.

---

Let's walk through an **ASCII visualization** of how the algorithm works on this input:

```
find_three_largest_numbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7])
```

We will track the internal `three_largest` array at each step.

---

### 🧱 Initial State

```
three_largest = [ None, None, None ]
```

---

### 🔁 Step-by-Step Processing

#### → num = 141

```
141 > None → becomes largest

[ None, None, 141 ]
```

---

#### → num = 1

```
1 < 141 → becomes second largest

[ None, 1, 141 ]
```

---

#### → num = 17

```
17 > 1 → becomes second largest, shift 1 to the left

Before: [ None, 1, 141 ]
After:  [ 1, 17, 141 ]
```

---

#### → num = -7

```
-7 < 1 → ignored
```

#### → num = -17

```
-17 < 1 → ignored
```

#### → num = -27

```
-27 < 1 → ignored
```

---

#### → num = 18

```
18 > 17 → becomes second largest, shift 17 to the left

Before: [ 1, 17, 141 ]
After:  [ 17, 18, 141 ]
```

---

#### → num = 541

```
541 > 141 → becomes largest, shift 141 & 18 to the left

Before: [ 17, 18, 141 ]
After:  [ 18, 141, 541 ]
```

---

#### → num = 8

```
8 < 18 → ignored
```

#### → num = 7

```
7 < 18 → ignored
```

#### → num = 7

```
7 < 18 → ignored
```

---

### ✅ Final Result

```
three_largest = [ 18, 141, 541 ]
```

---

### 🎯 Summary in Table Form

| Step | Current Num  | Action                         | Resulting `three_largest` |
| ---- | ------------ | ------------------------------ | ------------------------- |
| 1    | 141          | Insert at position 2 (largest) |  [None, None, 141]        |
| 2    | 1            | Insert at position 1           |  [None, 1, 141]           |
| 3    | 17           | Insert at position 1, shift    |  [1, 17, 141]             |
| 4-6  | -7, -17, -27 | Ignored                        |  [1, 17, 141]             |
| 7    | 18           | Insert at position 1, shift    |  [17, 18, 141]            |
| 8    | 541          | Insert at position 2, shift    |  [18, 141, 541]           |
| 9-11 | 8, 7, 7      | Ignored                        |  [18, 141, 541]           |

"""
