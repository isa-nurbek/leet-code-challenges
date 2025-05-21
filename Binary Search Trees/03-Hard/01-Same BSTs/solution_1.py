# Problem Description:

"""
                                                Same BSTs

An array of integers is said to represent the `Binary Search Tree (BST)` obtained by inserting each integer in the array, from left
to right, into the `BST`.

Write a function that takes in two arrays of integers and determines whether these arrays represent the same `BST`.

Note that you're not allowed to construct any `BST`s in your code.

A `BST` is a `Binary Tree` that consists only of `BST` nodes. A node is said to be a valid `BST` node if and only if it satisfies
the `BST` property: its value is strictly greater than the values of every node to its left; its value is less than or equal to the
values of every node to its right; and its children nodes are either valid `BST` nodes themselves or `None`.


## Sample Input:
```
array_one = [10, 15, 8, 12, 94, 81, 5, 2, 11]
array_two = [10, 8, 5, 15, 2, 12, 11, 94, 81]
```

## Sample Output:
```
True 
// Both arrays represent the BST below

          10
       /     \
      8      15
    /       /   \
   5      12    94
 /       /     /
2       11    81
```

## Optimal Time & Space Complexity:
```
O(n²) time | O(d) space - where `n` is the number of nodes in each array, respectively, and `d` is the depth
of the BST that they represent.
```

"""

# =========================================================================================================================== #

# Solution:


# Binary Search Tree (BST) node class
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n²) time | O(d) space
def same_bsts(array_one, array_two):
    """
    Determines if two arrays represent the same Binary Search Tree (BST).

    Args:
        array_one: First array representing BST nodes in insertion order
        array_two: Second array representing BST nodes in insertion order

    Returns:
        bool: True if both arrays represent the same BST, False otherwise
    """

    # First check: if arrays have different lengths, they can't represent same BST
    if len(array_one) != len(array_two):
        return False

    # Base case: empty arrays are considered same BSTs
    if len(array_one) == 0 and len(array_two) == 0:
        return True

    # Root values must be equal for BSTs to be same
    if array_one[0] != array_two[0]:
        return False

    # Get all elements less than root (left subtree) for both arrays
    left_one = get_smaller(array_one)
    left_two = get_smaller(array_two)

    # Get all elements greater than or equal to root (right subtree) for both arrays
    right_one = get_bigger_or_equal(array_one)
    right_two = get_bigger_or_equal(array_two)

    # Recursively check if both left and right subtrees are same BSTs
    return same_bsts(left_one, left_two) and same_bsts(right_one, right_two)


def get_smaller(array):
    """
    Helper function to get all elements smaller than the first element (root).

    Args:
        array: Input array representing a BST

    Returns:
        list: Elements smaller than root (left subtree elements)
    """
    smaller = []
    # Start from index 1 since index 0 is the root
    for i in range(1, len(array)):
        if array[i] < array[0]:
            smaller.append(array[i])

    return smaller


def get_bigger_or_equal(array):
    """
    Helper function to get all elements greater than or equal to the first element (root).

    Args:
        array: Input array representing a BST

    Returns:
        list: Elements greater than or equal to root (right subtree elements)
    """
    bigger_or_equal = []
    # Start from index 1 since index 0 is the root
    for i in range(1, len(array)):
        if array[i] >= array[0]:
            bigger_or_equal.append(array[i])

    return bigger_or_equal


# Test Case:

array_one = [10, 15, 8, 12, 94, 81, 5, 2, 11]
array_two = [10, 8, 5, 15, 2, 12, 11, 94, 81]

print(same_bsts(array_one, array_two))  # Output: True

# Both arrays represent the BST below
#           10
#        /     \
#       8      15
#     /       /   \
#    5      12    94
#  /       /     /
# 2       11    81

# =========================================================================================================================== #

# Big O Analysis:

"""
# Time and Space Complexity Analysis:

Let's analyze the time and space complexity of the `same_bsts` function.

### Time Complexity:

1. **Base Cases**: The base cases (checking lengths and root values) are all O(1) operations.
2. **Splitting Arrays**: The `get_smaller` and `get_bigger_or_equal` functions both iterate over the array
(excluding the first element) to partition the elements into left and right subtrees. This is O(n) for each call,
where `n` is the length of the current array.
3. **Recursive Calls**: The function makes two recursive calls, one for the left subtrees and one for the right subtrees.
In the worst case, the array could be split unevenly (e.g., all elements are smaller or all are bigger than the root),
leading to a depth of recursion of `n` (degenerate tree). However, on average, for balanced BSTs, the depth is log(n).

- **Worst Case (Unbalanced Trees)**: O(n²)  
  - Each level of recursion processes a subarray of size `n-1`, `n-2`, ..., `1`, leading to a total of O(n²) operations.
- **Average Case (Balanced Trees)**: O(n log n)  
  - The array is split roughly in half at each level, leading to log(n) levels, each doing O(n) work (for partitioning).

### Space Complexity:

1. **Auxiliary Arrays**: The `get_smaller` and `get_bigger_or_equal` functions create new arrays for the left and right subtrees,
which requires O(n) space per recursive call.
2. **Recursion Stack**: The depth of the recursion stack depends on the height of the tree.
   - **Worst Case (Unbalanced Trees)**: O(n) space for the recursion stack.
   - **Average Case (Balanced Trees)**: O(log n) space for the recursion stack.

- **Worst Case (Unbalanced Trees)**: O(n²)  
  - Each recursive call creates O(n) space, and there are O(n) such calls.
- **Average Case (Balanced Trees)**: O(n log n)  
  - Each level of recursion requires O(n) space (sum of all subarrays at that level), and there are O(log n) levels.

### Final Answer:

- **Time Complexity**: O(n²) in the worst case, O(n log n) on average.
- **Space Complexity**: O(n²) in the worst case, O(n log n) on average (due to auxiliary arrays).  
  (Can be optimized to O(n) worst-case and O(log n) average space complexity with an index-based approach.)

### Optimizations:

The current approach uses extra space for creating subarrays. An optimized approach could use indices to represent subarrays
in the original array, reducing space complexity to O(d) (where `d` is the depth of recursion) for the recursion stack, without
creating new arrays. This would make the space complexity O(n) in the worst case and O(log n) on average, while the time
complexity remains the same.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
This code defines a function `same_bsts` that checks whether two arrays represent the **same Binary Search Tree (BST)** structure,
without building the actual BSTs. Let’s break it down step-by-step:

---

## 🌲 What is the problem being solved?

Given two arrays (like pre-order traversals), determine if they could represent the **same BST** — that is, whether **inserting the
elements from each array (in order)** into a BST would result in the **same tree structure**.

---

## 🔍 Code Explanation

### 1. **BST Class (Unused in this code)**

```
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
```

This is a basic BST node class, but it’s **not used** in the algorithm. It's likely provided for context.

---

### 2. **Main Function: `same_bsts(array_one, array_two)`**

This is the recursive function that compares the two arrays.

#### Step-by-step:

```
if len(array_one) != len(array_two):
    return False
```

* If the arrays have different lengths, they can't represent the same BST.

```
if len(array_one) == 0 and len(array_two) == 0:
    return True
```

* If both arrays are empty, they represent empty trees → return `True`.

```
if array_one[0] != array_two[0]:
    return False
```

* The root of both trees must be the same (first element of the array). If not, they are different trees.

---

### 3. **Split Arrays into Left and Right Subtrees**

```
left_one = get_smaller(array_one)
left_two = get_smaller(array_two)

right_one = get_bigger_or_equal(array_one)
right_two = get_bigger_or_equal(array_two)
```

These helper functions break each array into:

* `left`: all values less than the root (array[0])
* `right`: all values **greater than or equal to** the root

#### Example:

If `array = [10, 15, 8, 12]`

* `get_smaller(array)` → `[8]` (left subtree)
* `get_bigger_or_equal(array)` → `[15, 12]` (right subtree)

---

### 4. **Recursive Comparison**

```
return same_bsts(left_one, left_two) and same_bsts(right_one, right_two)
```

* Recursively check if the left and right subtrees match.

---

## 🔧 Helper Functions

### `get_smaller(array)`

Returns all elements in the array **less than** the root (array[0]):

```
def get_smaller(array):
    smaller = []
    for i in range(1, len(array)):
        if array[i] < array[0]:
            smaller.append(array[i])
    return smaller
```

### `get_bigger_or_equal(array)`

Returns all elements in the array **greater than or equal to** the root:

```
def get_bigger_or_equal(array):
    bigger_or_equal = []
    for i in range(1, len(array)):
        if array[i] >= array[0]:
            bigger_or_equal.append(array[i])
    return bigger_or_equal
```

---

## 🧪 Test Case Breakdown

```
array_one = [10, 15, 8, 12, 94, 81, 5, 2, 11]
array_two = [10, 8, 5, 15, 2, 12, 11, 94, 81]
```

Both arrays represent this BST:

```
           10
        /     \
       8      15
     /       /   \
    5      12    94
  /       /     /
 2       11    81
```

So the function will return `True`.

---

## ✅ Summary

### What makes two arrays represent the same BST?

* Same root
* Same elements in left and right subtree (order can differ, but structure must match)

### Algorithm Strategy:

* Recursively divide both arrays into left/right based on the root
* Compare those sub-arrays recursively

### Efficiency:

* **Time complexity:** Worst case: O(n²) due to slicing and recursion on each subarray
* **Space complexity:** O(n) for recursive stack and sublists

---

Here’s an ASCII visualization of the BST represented by both arrays:

### 🔢 Arrays:

```python
array_one = [10, 15, 8, 12, 94, 81, 5, 2, 11]
array_two = [10, 8, 5, 15, 2, 12, 11, 94, 81]
```

### 🌳 BST Structure:

```
           10
         /    \
       8       15
      /       /   \
     5      12     94
    /      /      /
   2     11     81
```

### 📌 Node Descriptions:

* `10` is the root.
* `8` is less than `10`, goes to the left.
* `15` is greater than `10`, goes to the right.
* `5` is less than `8`, so it goes to `8`'s left.
* `2` is less than `5`, goes further left.
* `12` is less than `15`, goes left of `15`.
* `11` is less than `12`, so it becomes `12`'s left child.
* `94` is greater than `15`, goes to its right.
* `81` is less than `94`, becomes `94`'s left child.

Both arrays result in this exact structure — though their insertion order differs — which is why `same_bsts` returns `True`.

---

Let’s walk through the **step-by-step insertion** of both arrays into a BST and see how they build the **same structure**
despite the different order.

---

## 🔢 `array_one = [10, 15, 8, 12, 94, 81, 5, 2, 11]`

### Step-by-Step Insertion:

1. **Insert 10**

```
10
```

2. **Insert 15** → right of 10

```
   10
     \
     15
```

3. **Insert 8** → left of 10

```
   10
  /  \
 8    15
```

4. **Insert 12** → right of 10 → left of 15

```
   10
  /  \
 8    15
      /
    12
```

5. **Insert 94** → right of 10 → right of 15

```
   10
  /  \
 8    15
      / \
    12  94
```

6. **Insert 81** → right of 10 → right of 15 → left of 94

```
   10
  /  \
 8    15
      / \
    12  94
         /
       81
```

7. **Insert 5** → left of 10 → left of 8

```
     10
    /  \
   8    15
  /     / \
 5    12  94
           /
         81
```

8. **Insert 2** → left of 10 → left of 8 → left of 5

```
     10
    /  \
   8    15
  /     / \
 5    12  94
 /        /
2        81
```

9. **Insert 11** → right of 10 → left of 15 → left of 12

```
     10
    /  \
   8    15
  /     / \
 5    12  94
 /    /   /
2   11   81
```

✅ Final Tree (from `array_one`):

```
           10
         /    \
       8       15
      /       /   \
     5      12     94
    /      /      /
   2     11     81
```

---

## 🔢 `array_two = [10, 8, 5, 15, 2, 12, 11, 94, 81]`

### Step-by-Step Insertion:

1. **Insert 10**

```
10
```

2. **Insert 8** → left of 10

```
  10
 /
8
```

3. **Insert 5** → left of 10 → left of 8

```
   10
  /
 8
/
5
```

4. **Insert 15** → right of 10

```
   10
  /  \
 8    15
/
5
```

5. **Insert 2** → left of 10 → left of 8 → left of 5

```
     10
    /  \
   8    15
  /
 5
/
2
```

6. **Insert 12** → right of 10 → left of 15

```
     10
    /  \
   8    15
  /     /
 5     12
/
2
```

7. **Insert 11** → right of 10 → left of 15 → left of 12

```
     10
    /  \
   8    15
  /     /
 5     12
/     /
2    11
```

8. **Insert 94** → right of 10 → right of 15

```
     10
    /  \
   8    15
  /     / \
 5    12  94
/     /
2    11
```

9. **Insert 81** → right of 10 → right of 15 → left of 94

```
     10
    /  \
   8    15
  /     / \
 5    12  94
/     /   /
2    11  81
```

✅ Final Tree (from `array_two`):

```
           10
         /    \
       8       15
      /       /   \
     5      12     94
    /      /      /
   2     11     81
```

---

### ✅ Result:

Both arrays produce the **exact same BST structure**, which confirms why `same_bsts(array_one, array_two)` returns `True`.

"""
