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


# O(log(n)) time | O(1) space
def index_equals_value(array):
    # Initialize left and right pointers for binary search
    left = 0
    right = len(array) - 1
    # Initialize result to -1 (no match found case)
    result = -1

    # Binary search loop
    while left <= right:
        # Calculate middle index to avoid potential overflow
        middle = left + (right - left) // 2
        middle_value = array[middle]

        if middle_value == middle:
            # Found a match, store the result
            result = middle
            # Continue searching left half to find a smaller matching index
            # since we want the smallest index where array[i] == i
            right = middle - 1
        elif middle_value < middle:
            # If value is less than index, all elements to the left must also be
            # smaller than their indices (since array is sorted)
            # So we search the right half
            left = middle + 1
        else:  # middle_value > middle
            # If value is greater than index, all elements to the right must also be
            # larger than their indices (since array is sorted)
            # So we search the left half
            right = middle - 1

    # Return the smallest found index where array[i] == i, or -1 if none exists
    return result


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

### Time Complexity Analysis:

1. **Binary Search**: The algorithm uses binary search, which halves the search space in each iteration. 
   - In each iteration, the algorithm checks the middle element and adjusts the `left` or `right` pointer accordingly.
   - The number of iterations is proportional to the number of times you can halve the search space until it becomes empty.
   For an array of size `n`, this is `O(log n)`.

2. **Operations per Iteration**: In each iteration, the algorithm performs a constant amount of work (calculating `middle`,
accessing `array[middle]`, comparisons, and updating pointers). Thus, the work per iteration is `O(1)`.

Combining these, the total time complexity is: O(log n) 

### Space Complexity Analysis:

The space complexity is determined by the additional memory used by the algorithm beyond the input:

1. **Variables**: The algorithm uses a few extra variables (`left`, `right`, `middle`, `middle_value`, `result`), all of which
occupy constant space O(1).
2. **Input**: The input array is not counted towards the space complexity of the function itself (it's part of the input space).

Thus, the space complexity is: O(1) 

### Summary:
- **Time Complexity**: `O(log n)`
- **Space Complexity**: `O(1)`

### Additional Notes:
- The algorithm is efficient because it leverages the sorted nature of the array (implied by the problem constraints, since binary
search is used) to eliminate half of the remaining elements in each step.

- The early termination when `middle_value == middle` (by setting `right = middle - 1`) ensures that we find the smallest such
index, if it exists. If no such index exists, the function returns `-1`.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
This function, `index_equals_value`, searches for the **smallest index `i`** in a **sorted array** such that:

```
array[i] == i
```

It uses a **modified binary search** to efficiently find this index.

---

### 🔍 Problem Goal

Find the smallest index `i` such that `array[i] == i`.
If no such index exists, return `-1`.

---

## 🔁 Code Breakdown

### Initialization:

```
left = 0
right = len(array) - 1
result = -1
```

* `left` and `right` define the current bounds of the binary search.
* `result` will store the **smallest matching index** found (if any).

---

### While Loop (Binary Search):

```
while left <= right:
    middle = left + (right - left) // 2
    middle_value = array[middle]
```

* Calculates the middle index safely to avoid integer overflow.
* Retrieves the value at that index.

---

### Three Cases:

#### ✅ Case 1: Match Found

```
if middle_value == middle:
    result = middle
    right = middle - 1  # Continue to search left for smaller match
```

* A match is found (`array[middle] == middle`), so store it in `result`.
* Instead of stopping, we continue searching the **left side** (`right = middle - 1`) to find **smaller** matching indices.

#### ➡️ Case 2: Value Less Than Index

```
elif middle_value < middle:
    left = middle + 1
```

* If `array[middle] < middle`, then for all elements on the **left**, `array[i]` will be even **smaller** than `i`.
* So we **discard the left half** and search in the **right half**.

#### ⬅️ Case 3: Value Greater Than Index

```
else:  # middle_value > middle
    right = middle - 1
```

* If `array[middle] > middle`, all elements on the **right** will also have `array[i] > i`.
* So we **discard the right half** and search in the **left half**.

---

### Return

```
return result
```

* Returns the smallest index `i` such that `array[i] == i`.
* If no match is found, `result` remains `-1`.

---

## 🧪 Test Case Analysis

### Test 1:

```
print(index_equals_value([-5, -3, 0, 3, 4, 5, 9]))
```

* Index 3 → `array[3] = 3` ✅
* Output: `3`

---

### Test 2:

```
print(index_equals_value([-12, 1, 2, 3, 12]))
```

* Index 1 → `array[1] = 1` ✅
* Index 2 → `array[2] = 2` ✅, but we want the **smallest**, so return `1`.

---

### Test 3:

```
print(index_equals_value([-5, -4, -3, -2, -1, 0, 1, 3, 5, 6, 7, 11, 12, 14, 19, 20]))
```

* Index 11 → `array[11] = 11` ✅
* Output: `11`

---

## 🧠 Time Complexity

* Binary search ⇒ **O(log n)** time
* Much faster than linear search (**O(n)**), especially for large arrays.

---

## ✅ Summary

* This is a clever variant of binary search to find a "fixed point": `array[i] == i`.
* It returns the **smallest such index**, not just any match.
* Efficient, elegant, and widely used in algorithmic interview problems.

---

Here’s a step-by-step **ASCII visualization** of how the `index_equals_value()` function works, using the example:

```
index_equals_value([-5, -3, 0, 3, 4, 5, 9])
```

---

## 🧠 Array Layout:

```
Index:      0   1   2   3   4   5   6
Values:    -5  -3   0   3   4   5   9
```

We are looking for `array[i] == i`.

---

### 🔍 Step-by-Step Binary Search

#### Step 1: Initial bounds

```
left = 0, right = 6
middle = (0 + 6) // 2 = 3
array[3] = 3

=> Match found! array[3] == 3
=> Store result = 3
=> Move right to middle - 1 to find smaller match
```

#### Step 2:

```
left = 0, right = 2
middle = (0 + 2) // 2 = 1
array[1] = -3

=> array[1] < 1
=> Move left to middle + 1
```

#### Step 3:

```
left = 2, right = 2
middle = (2 + 2) // 2 = 2
array[2] = 0

=> array[2] < 2
=> Move left to middle + 1
```

Now `left = 3`, `right = 2` → loop ends.

---

### ✅ Final Result:

The smallest index where `array[i] == i` is:

```
Result: 3
```

---

## 🔠 ASCII Diagram (Horizontal)

```
Indexes:      0   1   2   3   4   5   6
Array:       -5  -3   0   3   4   5   9
              ↑       ↑
            Left     Mid (3 == 3 ✅)
```

After storing result = 3, we search the left side:

```
Indexes:      0   1   2   3
Array:       -5  -3   0   3
              ↑   ↑
            Left Mid (array[1] = -3 < 1)
```

```
Indexes:      0   1   2
Array:       -5  -3   0
                  ↑   ↑
                Left Mid (array[2] = 0 < 2)
```

---

### ⛳️ ASCII Summary

```
Search 1 → middle = 3 → array[3] = 3 ✅
Search left → middle = 1 → array[1] = -3 ❌
Search right → middle = 2 → array[2] = 0 ❌
Loop ends → return result = 3
```

"""
