# Problem Description:

"""
                                                Min Height BST

Write a function that takes in a `non-empty sorted array` of distinct integers, constructs a BST from the integers, and returns
the root of the BST.

The function should minimize the height of the BST.

You've been provided with a `BST` class that you'll have to use to construct the BST.

Each `BST` node has an integer `value`, a `left` child node, and a `right` child node. A node is said to be a valid `BST` node if
and only if it satisfies the `BST` property: its `value` is strictly greater than the values of every node to its left; its `value`
is less than or equal to the values of every node to its right; and its children nodes are either valid BST nodes themselves or `None`.

A `BST` is valid if and only if all of its nodes are valid `BST` nodes.

> Note that the `BST` class already has an `insert` method which you can use if you want.


## Sample Input:
```
array = [1, 2, 5, 7, 10, 13, 14, 15, 22]
```

## Sample Output:
```
         10
       /     \
      2      14
    /   \   /   \
   1     5 13   15
          \       \
           7      22

// This is one example of a BST with min height that you could create from the input array.
// You could create other BSTs with min height from the same array; for example:

         10
       /     \
      5      15
    /   \   /   \
   2     7 13   22
 /           \
1            14
```

## Optimal Time & Space Complexity:
```
O(n) time | O(n) space - where `n` is the length of the array.
```

"""

# =========================================================================================================================== #

# Solution:


# Binary Search Tree (BST) node class
class BST:
    def __init__(self, value):
        # Initialize a BST node with a given value
        # Left and right children are initialized to None
        self.value = value
        self.left = None
        self.right = None


# O(n) time | O(n) space
def min_height_bst(array):
    # Main function to construct a minimum-height BST from a sorted array
    # It calls the helper function with the full array range (start to end indices)
    return construct_min_height_bst(array, 0, len(array) - 1)


def construct_min_height_bst(array, start_idx, end_idx):
    # Helper function to recursively construct the BST
    # Base case: when start index exceeds end index, return None (no node)
    if end_idx < start_idx:
        return None

    # Find the middle index to make it the root of current subtree
    # This ensures the tree will be balanced (minimum height)
    middle_idx = (start_idx + end_idx) // 2

    # Create a new BST node with the middle value
    bst = BST(array[middle_idx])

    # Recursively construct the left subtree using the left half of the array
    bst.left = construct_min_height_bst(array, start_idx, middle_idx - 1)
    # Recursively construct the right subtree using the right half of the array
    bst.right = construct_min_height_bst(array, middle_idx + 1, end_idx)

    # Return the constructed node
    return bst


# Helper function to print the tree in-order for testing
def in_order_traversal(tree):
    # Perform in-order traversal (left, root, right) to print values in sorted order
    if tree is not None:
        in_order_traversal(tree.left)
        print(tree.value, end=" ")
        in_order_traversal(tree.right)


# Test Cases:

tree1 = min_height_bst([1, 2, 5, 7, 10, 13, 14, 15, 22])
in_order_traversal(tree1)
print()

#  Output: 1 2 5 7 10 13 14 15 22

#     10
#    /  \
#   2    14
#  / \   / \
# 1   5 13 15
#      \     \
#       7    22


tree2 = min_height_bst([1, 2, 5, 7, 10, 13, 14, 15, 22, 28, 32, 36])
in_order_traversal(tree2)
print()

# Output: 1 2 5 7 10 13 14 15 22 28 32 36

#           13
#         /    \
#        5      28
#      /  \    /  \
#     2   10  15  32
#    /    / \   \   \
#   1    7  14  22  36

# =========================================================================================================================== #

# Big O Analysis:

"""
# Time and Space Complexity Analysis:

### Time Complexity Analysis

The time complexity of constructing a minimum height BST from a sorted array using the provided algorithm is **O(n)**,
where **n** is the number of elements in the array.

#### Explanation:

1. **Divide and Conquer Approach**: The algorithm recursively splits the array into two halves around the middle element.
This middle element becomes the root of the current subtree, ensuring the BST is balanced (and thus of minimum height).

2. **Visiting Each Element Once**: Each element in the array is processed exactly once to become a node in the BST.
The work done per element is constant time (calculating the middle index and creating a node).

3. **Recurrence Relation**: The recurrence relation for the algorithm is:
   
   T(n) = 2T(n/2) + O(1)
   
   This solves to **O(n)** using the Master Theorem or by recognizing that the algorithm performs a constant amount of work
   for each of the **n** nodes.

### Space Complexity Analysis

The space complexity is **O(n)** for the output BST (to store all the nodes), and the additional space used by the recursion
stack is **O(log n)** in the average case for a balanced BST.

#### Explanation:

1. **Output Space**: The BST itself requires **O(n)** space to store all the nodes.

2. **Recursion Stack**: The recursion depth is equal to the height of the BST. Since the BST is balanced, the height is **log n**,
leading to **O(log n)** space for the recursion stack.
   - In the worst case (which doesn't happen here because the tree is balanced), the recursion stack could be **O(n)** for a
   completely unbalanced tree.
   
3. **Total Space Complexity**: Dominated by the output BST, so **O(n)**.

### Summary:
- **Time Complexity**: **O(n)** (each element is processed once).
- **Space Complexity**: **O(n)** (for the BST) + **O(log n)** (recursion stack) = **O(n)** overall.

This is optimal for constructing a balanced BST from a sorted array.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
Let's walk through your **`min_height_bst`** implementation step by step, explaining how it works and why it builds a
**Binary Search Tree (BST) with minimal height** from a **sorted array**.

---

### ✅ Objective:

Build a **Binary Search Tree (BST)** such that it has **minimum possible height** from a given **sorted array** (in ascending order).

---

## 🔧 Code Explanation

### 1. **BST Class Definition**

```
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
```

* This is a basic class to represent each **node** in a BST.
* It has:

  * `value`: the integer value of the node.
  * `left`: pointer to the left subtree.
  * `right`: pointer to the right subtree.

---

### 2. **Main Function: `min_height_bst`**

```
def min_height_bst(array):
    return construct_min_height_bst(array, 0, len(array) - 1)
```

* Takes a **sorted array** as input.
* Calls a **recursive helper function** `construct_min_height_bst` with start and end indexes.

---

### 3. **Recursive Function: `construct_min_height_bst`**

```
def construct_min_height_bst(array, start_idx, end_idx):
    if end_idx < start_idx:
        return None
```

* **Base Case**: if `start_idx > end_idx`, it means there's no element to process; return `None`.

---

```
    middle_idx = (start_idx + end_idx) // 2
    bst = BST(array[middle_idx])
```

* Select the **middle element** as the root of the current subtree.
* Why?

  * Choosing the middle ensures that the left and right subtrees are **balanced**, leading to **minimal height**.
  * For a sorted array, left side will have smaller elements, right side will have larger ones — perfect for BST.

---

```
    bst.left = construct_min_height_bst(array, start_idx, middle_idx - 1)
    bst.right = construct_min_height_bst(array, middle_idx + 1, end_idx)

    return bst
```

* Recursively build the **left** subtree with the **left half** of the array.
* Recursively build the **right** subtree with the **right half**.
* Return the root of the constructed tree.

---

## 🧪 Testing: In-Order Traversal

```
def in_order_traversal(tree):
    if tree is not None:
        in_order_traversal(tree.left)
        print(tree.value, end=" ")
        in_order_traversal(tree.right)
```

* This prints the BST in **sorted (ascending)** order.
* **In-order traversal** of a BST always yields sorted output.

---

### 🧠 Example Breakdown:

#### Input: `[1, 2, 5, 7, 10, 13, 14, 15, 22]`

* Middle element: `10` → becomes root.
* Left subarray: `[1, 2, 5, 7]` → `2` becomes left child of `10`
* Right subarray: `[13, 14, 15, 22]` → `14` becomes right child of `10`
* Continue recursively...

Structure:

```
       10
     /    \
    2      14
   / \    /  \
  1   5  13  15
        \     \
         7    22
```

* **Balanced** — height is minimized.

---

## ⏱️ Time and Space Complexity

### ✅ Time Complexity: **O(n)**

* Every element is visited once and inserted once → linear time.

### ✅ Space Complexity:

* **O(n)** for storing the tree nodes.
* **O(log n)** average recursion stack height (for balanced tree),
* **O(n)** worst case (stack) if recursion depth is counted as space.

---

## ✅ Summary

* The approach works by **recursively picking the middle element** of the array (or subarray) to ensure the BST remains **as
balanced as possible**.
* This results in a tree with **minimum height**, where operations like search and insert will be most efficient (logarithmic
time in the best case).
* The `in_order_traversal` confirms that the BST structure is correct by printing the values in order.

---

Let's visualize your BST using ASCII diagrams for both examples you gave.

### 🌳 Example 1: Input `[1, 2, 5, 7, 10, 13, 14, 15, 22]`

```
              10
            /    \
          2        14
        /   \     /   \
      1      5   13    15
                 \      \
                  7      22
```

#### How this structure forms:

* Middle of entire array: `10` → root
* Left of `10`: `[1, 2, 5, 7]`, middle = `2` → left child of 10
* Right of `10`: `[13, 14, 15, 22]`, middle = `14` → right child
* Then continue breaking down subarrays recursively:

  * `1` and `5` become children of `2`
  * `13` and `15` become children of `14`
  * `7` is the right child of `5`
  * `22` is right child of `15`

---

### 🌳 Example 2: Input `[1, 2, 5, 7, 10, 13, 14, 15, 22, 28, 32, 36]`

```
                    13
                 /      \
              5           28
            /   \        /   \
          2     10     15     32
         /     /  \      \      \
       1     7   14      22     36
```

#### Formation breakdown:

* Middle of array: `13` → root
* Left: `[1, 2, 5, 7, 10]` → middle = `5`
* Right: `[14, 15, 22, 28, 32, 36]` → middle = `28`
* Keep dividing subarrays:

  * `2` becomes left of `5`; `10` becomes right
  * `1` is left of `2`, `7` and `14` are children of `10`
  * `15` and `32` are children of `28`
  * `22` is right of `15`, `36` is right of `32`

---

Let's walk through a **step-by-step recursive call tree** for the first example:

---

### 🧪 Input: `[1, 2, 5, 7, 10, 13, 14, 15, 22]`

We’ll walk through how the recursive function `construct_min_height_bst(array, start_idx, end_idx)` builds the BST.

---

### 🧩 Step-by-step Recursive Construction

#### **Step 1**:

```
construct_min_height_bst(array, 0, 8)  → middle = 4 → array[4] = 10
```

Create node `10`, this is the root.

#### **Step 2 (Left Subtree of 10)**:

```
construct_min_height_bst(array, 0, 3)  → middle = 1 → array[1] = 2
```

Create node `2` (left child of 10)

#### **Step 3 (Left Subtree of 2)**:

```
construct_min_height_bst(array, 0, 0)  → middle = 0 → array[0] = 1
```

Create node `1` (left child of 2)

```
construct_min_height_bst(array, 0, -1) → returns None (left of 1)
construct_min_height_bst(array, 1, 0)  → returns None (right of 1)
```

#### **Step 4 (Right Subtree of 2)**:

```
construct_min_height_bst(array, 2, 3)  → middle = 2 → array[2] = 5
```

Create node `5` (right child of 2)

```
construct_min_height_bst(array, 2, 1) → returns None (left of 5)
construct_min_height_bst(array, 3, 3) → middle = 3 → array[3] = 7
```

Create node `7` (right child of 5)

```
construct_min_height_bst(array, 3, 2) → returns None (left of 7)
construct_min_height_bst(array, 4, 3) → returns None (right of 7)
```

#### **Step 5 (Right Subtree of 10)**:

```
construct_min_height_bst(array, 5, 8)  → middle = 6 → array[6] = 14
```

Create node `14` (right child of 10)

#### **Step 6 (Left Subtree of 14)**:

```
construct_min_height_bst(array, 5, 5) → middle = 5 → array[5] = 13
```

Create node `13` (left child of 14)

```
construct_min_height_bst(array, 5, 4) → returns None (left of 13)
construct_min_height_bst(array, 6, 5) → returns None (right of 13)
```

#### **Step 7 (Right Subtree of 14)**:

```
construct_min_height_bst(array, 7, 8) → middle = 7 → array[7] = 15
```

Create node `15` (right child of 14)

```
construct_min_height_bst(array, 7, 6) → returns None (left of 15)
construct_min_height_bst(array, 8, 8) → middle = 8 → array[8] = 22
```

Create node `22` (right child of 15)

```
construct_min_height_bst(array, 8, 7) → returns None (left of 22)
construct_min_height_bst(array, 9, 8) → returns None (right of 22)
```

---

### 🧱 Recursive Call Tree (Indented View)

```
construct(0, 8) → 10
├── construct(0, 3) → 2
│   ├── construct(0, 0) → 1
│   └── construct(2, 3) → 5
│       └── construct(3, 3) → 7
├── construct(5, 8) → 14
│   ├── construct(5, 5) → 13
│   └── construct(7, 8) → 15
│       └── construct(8, 8) → 22
```

---

### ✅ Final Tree Structure (Visual Recap)

```
              10
            /    \
          2        14
        /   \     /   \
      1      5   13    15
                 \      \
                  7      22
```

"""
