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


# O(log(n)) time | O(1) space
def binary_search(array, target):
    """
    Performs binary search on a sorted array to find the target value.

    Args:
        array: A sorted list of elements to search through
        target: The value to search for in the array

    Returns:
        int: The index of the target in the array, or -1 if not found
    """
    # Start the search with the full range of the array
    return binary_search_helper(array, target, 0, len(array) - 1)


def binary_search_helper(array, target, left, right):
    """
    Helper function that performs the actual binary search recursively.

    Args:
        array: The sorted list to search through
        target: The value to search for
        left: The leftmost index of the current search range
        right: The rightmost index of the current search range

    Returns:
        int: Index of the target if found, -1 otherwise
    """
    # Continue searching while the search range is valid (left hasn't passed right)
    while left <= right:
        # Calculate the middle index of the current search range
        middle = (left + right) // 2
        potential_match = array[middle]

        # Check if we've found the target
        if target == potential_match:
            return middle  # Target found, return its index
        # If target is smaller, search the left half
        elif target < potential_match:
            right = middle - 1
        # If target is larger, search the right half
        else:
            left = middle + 1

    # If we exit the loop, the target wasn't found
    return -1


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

### Time Complexity Analysis:

The time complexity of binary search is **O(log n)**, where **n** is the number of elements in the array.

#### Explanation:
1. **Divide and Conquer Approach**: In each iteration, the search space is halved. 
   - Initially, the search space is the entire array (size `n`).
   - After the first comparison, it reduces to `n/2`.
   - After the second comparison, it reduces to `n/4`, and so on.
   
2. **Number of Steps**: The algorithm continues dividing the search space until it either finds the target or the search space is
empty. The maximum number of steps required is the number of times you can divide `n` by 2 until you get to 1, which is `log₂ n`.

#### Example:
- For an array of size `8`, the worst-case number of steps is `log₂ 8 = 3`.
- For an array of size `1024`, the worst-case number of steps is `log₂ 1024 = 10`.

### Space Complexity Analysis:

The space complexity is **O(1)** (constant space).

#### Explanation:
1. **Iterative Approach**: The algorithm uses a loop and only a few extra variables (`left`, `right`, `middle`, `potential_match`),
regardless of the input size.
2. **No Recursion**: Unlike the recursive version of binary search (which would have `O(log n)` space due to the call stack), this
implementation is iterative and does not use additional space for recursive calls.

### Summary:
- **Time Complexity**: **O(log n)**
- **Space Complexity**: **O(1)** (constant space)

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
This code is an implementation of the **binary search** algorithm in Python. Binary search is a highly efficient algorithm for
finding an element in a **sorted array**. It works by **repeatedly dividing the search interval in half**.

---

## 🔍 Core Idea of Binary Search

* Start with the entire array.
* Find the **middle element**.
* If the middle element equals the target, return its index.
* If the target is **less** than the middle element, search the **left half**.
* If the target is **greater**, search the **right half**.
* Repeat until the element is found or the search space is empty.

---

## ✅ Code Breakdown

### `binary_search(array, target)`

This is the main function that is called by the user. It serves as a **wrapper** to call a helper function with the initial
search boundaries:

```
return binary_search_helper(array, target, 0, len(array) - 1)
```

* `array`: the sorted list of elements
* `target`: the value to find
* `0`: left boundary (start of array)
* `len(array) - 1`: right boundary (end of array)

---

### `binary_search_helper(array, target, left, right)`

This is the **actual binary search logic**, implemented using a `while` loop.

```
while left <= right:
```

This loop continues as long as the search space is valid. When `left > right`, it means the target is not found.

---

### Step-by-Step Execution Inside the Loop:

```
middle = (left + right) // 2
```

* Calculates the **midpoint index** of the current search range.

```
potential_match = array[middle]
```

* Retrieves the value at the middle index.

---

### Decision Making:

```
if target == potential_match:
    return middle
```

* Found the target! Return the index.

```
elif target < potential_match:
    right = middle - 1
```

* Target must be in the **left half**, so adjust the right boundary.

```
else:
    left = middle + 1
```

* Target must be in the **right half**, so adjust the left boundary.

---

### If Not Found:

```
return -1
```

* If the loop exits without finding the target, return `-1` to indicate "not found".

---

## 🧪 Test Cases

### Test 1:

```
print(binary_search([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33))
# Output: 3
```

* 33 is found at index `3`.

### Test 2:

```
print(binary_search([1, 5, 23, 111], 5))
# Output: 1
```

* 5 is at index `1`.

### Test 3:

```
print(binary_search([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 0))
# Output: 0
```

* 0 is at the beginning, index `0`.

---

## ⏱️ Time and Space Complexity

* **Time Complexity**: O(log n)

  * Because the search space is halved on each iteration.
* **Space Complexity**: O(1)

  * It uses constant space (iterative version). A recursive version would use O(log n) space due to the call stack.

---

## ✅ Summary

* Efficient search for sorted arrays.
* Works by dividing the array in half repeatedly.
* Implemented iteratively here.
* Returns the index if the element is found, otherwise `-1`.

---

Let's walk through a **visual ASCII step-by-step trace** of the binary search using this example:

### 🔍 Example:

```
binary_search([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33)
```

We are searching for **33** in a sorted array.

---

### 🧠 Step-by-Step ASCII Visualization

#### Initial array:

```
Index :   0   1   2   3   4   5   6   7   8   9
Array : [ 0,  1, 21, 33, 45, 45, 61, 71, 72, 73]
Target: 33
```

---

#### 🔁 Iteration 1:

```
left = 0
right = 9
middle = (0 + 9) // 2 = 4

[ 0,  1, 21, 33, 45, 45, 61, 71, 72, 73]
                   ↑
                 middle = 4
                 value  = 45
```

* `target (33) < 45` → search **left half**.
* Update: `right = middle - 1 = 3`

---

#### 🔁 Iteration 2:

```
left = 0
right = 3
middle = (0 + 3) // 2 = 1

[ 0,  1, 21, 33, 45, 45, 61, 71, 72, 73]
       ↑
     middle = 1
     value  = 1
```

* `target (33) > 1` → search **right half**.
* Update: `left = middle + 1 = 2`

---

#### 🔁 Iteration 3:

```
left = 2
right = 3
middle = (2 + 3) // 2 = 2

[ 0,  1, 21, 33, 45, 45, 61, 71, 72, 73]
           ↑
         middle = 2
         value  = 21
```

* `target (33) > 21` → search **right half**.
* Update: `left = middle + 1 = 3`

---

#### 🔁 Iteration 4:

```
left = 3
right = 3
middle = (3 + 3) // 2 = 3

[ 0,  1, 21, 33, 45, 45, 61, 71, 72, 73]
               ↑
             middle = 3
             value  = 33
```

✅ Target found at index **3**!

---

## ✅ Final Result:

```
Return 3
```

"""
