# Problem Description:

"""
                                             Binary Search

Write a function that takes in a `sorted array` of integers as well as a `target integer`. The function should use the `Binary
Search` algorithm to determine if the target integer is contained in the array and should return its `index` if it is, otherwise `-1`.


## Sample Input:
```
array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
target = 33
```

## Sample Output:
```
3
```

## Optimal Time & Space Complexity:
```
O(log(n)) time | O(1) space - where `n` is the length of the input array.
```

"""

# =========================================================================================================================== #

# Solution:


# O(log(n)) time | O(log(n)) space
def binary_search(array, target):
    """Performs binary search on a sorted array to find the target value.

    Args:
        array: A sorted list of elements to search through
        target: The value to search for in the array

    Returns:
        The index of the target in the array, or -1 if not found
    """
    # Start the search with the full range of the array
    return binary_search_helper(array, target, 0, len(array) - 1)


def binary_search_helper(array, target, left, right):
    """Helper function that performs binary search recursively on a subarray.

    Args:
        array: The sorted list to search through
        target: The value to search for
        left: The left boundary of the current search range
        right: The right boundary of the current search range

    Returns:
        The index of the target in the array, or -1 if not found
    """
    # Base case: search range is invalid (target not found)
    if left > right:
        return -1

    # Calculate the middle point of the current search range
    middle = (left + right) // 2
    potential_match = array[middle]

    # Check if we've found the target
    if target == potential_match:
        return middle
    # If target is smaller, search the left half
    elif target < potential_match:
        return binary_search_helper(array, target, left, middle - 1)
    # If target is larger, search the right half
    else:
        return binary_search_helper(array, target, middle + 1, right)


# Test Cases:

print(binary_search([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33))
# Output: 3

print(binary_search([1, 5, 23, 111], 5))
# Output: 1

print(binary_search([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 0))
# Output: 0

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### Time Complexity:

Binary search works by repeatedly dividing the search interval in half. At each step, the algorithm compares the middle element
of the current interval with the target value and eliminates half of the remaining elements from consideration.

- **Best Case**: O(1) - when the target is the middle element of the array.
- **Worst Case**: O(log n) - when the target is at one of the ends or not present in the array.
- **Average Case**: O(log n)

Each recursive call processes half of the remaining elements, leading to a logarithmic number of operations with respect to the
input size.

### Space Complexity:

This is a recursive implementation, so we need to consider the call stack:
- In each recursive call, we only pass constant space (the array reference and a few indices).
- The maximum depth of the recursion is the number of times we can divide the array in half, which is log₂n.

Therefore:
- **Space Complexity**: O(log n) for the recursive call stack.

### Summary:
- Time Complexity: O(log n)
- Space Complexity: O(log n) (due to recursion)

### Comparison with Iterative Binary Search:
An iterative implementation would have O(1) space complexity since it doesn't use the call stack. This recursive version uses
more space (O(log n)) due to the recursive calls, but both have the same O(log n) time complexity.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
Let's go through the code **step-by-step** to understand how it works.

---

## 🔍 **What is Binary Search?**

**Binary Search** is an efficient algorithm for finding an item from a **sorted list**. It works by repeatedly dividing the
search interval in half:

* If the value of the search key is **less** than the item in the middle, search in the **left half**.
* If it's **greater**, search in the **right half**.
* If it's **equal**, return the position.

---

## ✅ Code Explanation

```
def binary_search(array, target):
    return binary_search_helper(array, target, 0, len(array) - 1)
```

### 📌 `binary_search`

* This is the **main function** that takes:

  * `array`: a **sorted list**.
  * `target`: the value you want to find.
* It calls a **helper function**, `binary_search_helper`, with:

  * `left = 0` → start index.
  * `right = len(array) - 1` → end index.

---

```
def binary_search_helper(array, target, left, right):
    if left > right:
        return -1
```

### 🧠 Base Case (Recursion Ends)

* If `left > right`, that means the subarray is empty.
* So, **target doesn't exist** in the array → return `-1`.

---

```
middle = (left + right) // 2
potential_match = array[middle]
```

### 🎯 Find the Middle Element

* `middle` is the index halfway between `left` and `right`.
* `potential_match` is the value at that middle index.

---

```
if target == potential_match:
    return middle
```

### ✅ Case 1: Target Found

* If the target equals the middle element, return `middle` index.

---

```
elif target < potential_match:
    return binary_search_helper(array, target, left, middle - 1)
```

### 🔁 Case 2: Search Left Half

* If target is **less** than the middle value, search the **left half**:

  * Adjust the `right` boundary to `middle - 1`.

---

```
else:
    return binary_search_helper(array, target, middle + 1, right)
```

### 🔁 Case 3: Search Right Half

* If target is **greater**, search the **right half**:

  * Adjust the `left` boundary to `middle + 1`.

---

## 🧪 Test Case Walkthrough

```
print(binary_search([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33))
```

* `left = 0`, `right = 9`
* `middle = (0 + 9) // 2 = 4` → value = 45
* `33 < 45` → search left: `left = 0`, `right = 3`
* `middle = (0 + 3) // 2 = 1` → value = 1
* `33 > 1` → search right: `left = 2`, `right = 3`
* `middle = (2 + 3) // 2 = 2` → value = 21
* `33 > 21` → search right: `left = 3`, `right = 3`
* `middle = 3` → value = 33 → **match found at index 3**

---

## 🧠 Time and Space Complexity

* **Time Complexity:** `O(log n)` – the array is halved every time.
* **Space Complexity:** `O(log n)` – due to recursion call stack (can be made `O(1)` if done iteratively).

---

## ✅ Summary

This recursive binary search:

* Efficiently finds an element in a sorted list.
* Returns the index of the target or `-1` if not found.
* Demonstrates classic **divide and conquer** strategy.

---

Let's visualize how the **binary search algorithm** works using ASCII art.

We’ll use this example:

```
array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
target = 33
```

---

## 🔍 **Step-by-Step Visualization**

**Initial array:**

```
Index:    0   1   2   3   4   5   6   7   8   9
Array:   [0,  1, 21, 33, 45, 45, 61, 71, 72, 73]
                      ↑
                   middle = 4 (value = 45)
```

* `left = 0`, `right = 9`
* `target < 45` → search **left half**

---

**Next Step:**

```
Index:    0   1   2   3
Array:   [0,  1, 21, 33]
                  ↑
               middle = 1 (value = 1)
```

* `left = 0`, `right = 3`
* `target > 1` → search **right half**

---

**Next Step:**

```
Index:        2   3
Array:       [21, 33]
                    ↑
                 middle = 2 (value = 21)
```

* `left = 2`, `right = 3`
* `target > 21` → search **right half**

---

**Final Step:**

```
Index:           3
Array:          [33]
                   ↑
                middle = 3 (value = 33)
```

* `left = 3`, `right = 3`
* `target == 33` → 🎯 **FOUND at index 3**

---

## ✅ Summary Table

| Step | Left | Right | Middle | Value at Middle | Action           |
| ---- | ---- | ----- | ------ | --------------- | ---------------- |
| 1    | 0    | 9     | 4      | 45              | Go Left          |
| 2    | 0    | 3     | 1      | 1               | Go Right         |
| 3    | 2    | 3     | 2      | 21              | Go Right         |
| 4    | 3    | 3     | 3      | 33              | 🎯 Found Target  |

"""
