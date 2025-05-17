# Problem Description:

"""
                                               Heap Sort

Write a function that takes in an array of integers and returns a `sorted version` of that array. Use the `Heap Sort` algorithm
to sort the array.


## Sample Input:
```
array = [8, 5, 2, 9, 5, 6, 3]
```

## Sample Output:
```
[2, 3, 5, 5, 6, 8, 9]
```

## Optimal Time & Space Complexity:
```
Best: O(n log(n)) time | O(1) space - where n is the length of the input array.
Average: O(n log(n)) time | O(1) space - where n is the length of the input array.
Worst: O(n log(n)) time | O(1) space - where n is the length of the input array.
```

"""

# =========================================================================================================================== #

# Solution:


# Best: O(n log(n)) time | O(1) space
# Average: O(n log(n)) time | O(1) space
# Worst: O(n log(n)) time | O(1) space


# Max-Heap Version (Ascending Order Sort)
def heapify(arr, n, i):
    """
    Heapify a subtree rooted at index i in an array of size n.
    This function ensures the max-heap property is maintained for the subtree.
    """
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child position
    right = 2 * i + 2  # Right child position

    # If left child exists and is greater than current largest
    if left < n and arr[left] > arr[largest]:
        largest = left

    # If right child exists and is greater than current largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)  # Recursively heapify the affected subtree


def heap_sort(arr):
    """
    Main function to perform heap sort on the given array.
    """
    n = len(arr)

    # Build a max-heap (rearrange array)
    # Start from the last non-leaf node (n//2 - 1) and work backwards
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements from the heap
    for i in range(n - 1, 0, -1):
        # Move current root (max element) to the end
        arr[i], arr[0] = arr[0], arr[i]
        # Call heapify on the reduced heap (size = i)
        heapify(arr, i, 0)

    return arr


# Test Cases:

print(heap_sort([8, 5, 2, 9, 5, 6, 3]))
# Output: [2, 3, 5, 5, 6, 8, 9]

print(heap_sort([-4, 5, 10, 8, -10, -6, -4, -2, -5, 3, 5, -4, -5, -1, 1, 6, -7]))
# Output: [-10, -7, -6, -5, -5, -4, -4, -4, -2, -1, 1, 3, 5, 5, 6, 8, 10]

print(heap_sort([2, 1]))
# Output: [1, 2]

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### **Time Complexity Analysis**

#### **1. Building the Heap (Heapify All Non-Leaf Nodes)**
- The first loop in `heap_sort` runs from `n//2 - 1` down to `0`, calling `heapify` for each node.
- **Intuition**: Only non-leaf nodes need to be heapified (since leaves are already valid heaps).

- **Time Complexity**:
  - At each level of the heap, `heapify` takes **O(h)** time, where `h` is the height from the current node to the leaves.
  - The number of nodes at height `h` is roughly `n / 2^{h+1}`.
  - Total time = `Σ (from h=0 to log n) [n / 2^{h+1}] * O(h)` ≈ **O(n)** (using geometric series properties).

#### **2. Extracting Elements One by One**
- The second loop in `heap_sort` runs `n-1` times, swapping the root (max element) with the last unsorted element and calling
`heapify` on the reduced heap.
- **Intuition**: Each `heapify` call takes **O(log k)** time, where `k` is the size of the heap (decreasing from `n` to `1`).

- **Time Complexity**:
  - Total swaps: `n-1` times.
  - Each `heapify` call: **O(log i)** (for `i` from `n` down to `1`).
  - Total = `Σ (from i=1 to n-1) O(log i)` ≈ **O(n log n)** (since `log(n!) ≈ n log n`).

#### **Total Time Complexity**
- **Building the heap**: **O(n)**
- **Extracting elements**: **O(n log n)**
- **Overall**: **O(n log n)** (dominant term is `O(n log n)`).

---

### **Space Complexity Analysis**

- **Heap Sort is In-Place**: It uses only a constant amount of extra space (for swaps and temporary variables).
- **Recursion**: The `heapify` function is recursive, but in the worst case, the recursion depth is **O(log n)**
(height of the heap).
  - If implemented iteratively, the space complexity can be **O(1)** (tail recursion optimization or manual stack simulation).
- **Overall Space Complexity**: **O(1)** (in-place) if optimized, otherwise **O(log n)** due to recursion stack.

---

### **Summary**

| Operation         | Time Complexity  | Space Complexity     |
|-------------------|------------------|----------------------|
| Build Heap        | O(n)             | O(1) or O(log n)     |
| Extract + Heapify | O(n log n)       | O(1) or O(log n)     |
| **Total**         | **O(n log n)**   | **O(1) or O(log n)** |

Heap Sort is **not stable** (does not preserve the order of equal elements) but is **in-place** and has a **guaranteed O(n log n)
time complexity** in all cases (worst, average, and best).

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
Let’s go through your `heap_sort` implementation step-by-step, explain how it works, and break down the core components:

---

## **Overview**

**Heap Sort**, a comparison-based sorting algorithm that uses a **binary heap data structure** — specifically, a **max heap**
in this case.

* A **max heap** ensures that the **largest element is always at the root** (i.e., index `0`).
* Heap sort works in **two phases**:

  1. Build a max heap from the input array.
  2. Repeatedly extract the maximum (root), place it at the end, and re-heapify the reduced heap.

---

## **Function: `heapify(arr, n, i)`**

This function ensures that the subtree rooted at index `i` obeys the max-heap property.

### **Parameters**:

* `arr`: the array representing the heap.
* `n`: the size of the heap.
* `i`: the index of the root of the subtree to heapify.

### **Process**:

```
largest = i
left = 2 * i + 1
right = 2 * i + 2
```

* For a node at index `i`, its **left child** is at `2i + 1` and **right child** is at `2i + 2`.

```
if left < n and arr[left] > arr[largest]:
    largest = left
```

* If the **left child** exists and is **greater than the current largest**, update `largest`.

```
if right < n and arr[right] > arr[largest]:
    largest = right
```

* Same for the **right child**.

```
if largest != i:
    arr[i], arr[largest] = arr[largest], arr[i]  # Swap
    heapify(arr, n, largest)
```

* If `largest` is not the root, **swap the root with the largest child**, and **recursively heapify** the affected subtree.

---

## **Function: `heap_sort(arr)`**

This is the main sorting function.

### **Step 1: Build a Max Heap**

```
for i in range(n // 2 - 1, -1, -1):
    heapify(arr, n, i)
```

* Start from the last non-leaf node (`n // 2 - 1`) and go backward to the root.
* This ensures every subtree becomes a valid max heap.

### **Step 2: Extract Elements from Heap One by One**

```
for i in range(n - 1, 0, -1):
    arr[i], arr[0] = arr[0], arr[i]
    heapify(arr, i, 0)
```

* Swap the **maximum element (root)** with the **last element**.
* Reduce the heap size (`i`), and **heapify the new root** to maintain the heap property.

### **Return**:

```
return arr
```

* The input array is sorted **in-place** in **ascending order**.

---

## **Test Case Explanation**

### Test 1:

```
heap_sort([8, 5, 2, 9, 5, 6, 3])
# Output: [2, 3, 5, 5, 6, 8, 9]
```

* Builds a max heap: `[9, 8, 6, 5, 5, 2, 3]`
* Swaps and heapifies repeatedly: end result is a sorted array.

### Test 2:

```
heap_sort([-4, 5, 10, 8, -10, -6, -4, -2, -5, 3, 5, -4, -5, -1, 1, 6, -7])
# Output: [-10, -7, -6, -5, -5, -4, -4, -4, -2, -1, 1, 3, 5, 5, 6, 8, 10]
```

* Handles both positive and negative numbers.

### Test 3:

```
heap_sort([2, 1])
# Output: [1, 2]
```

* Very small input — still follows heap logic correctly.

---

## **Time and Space Complexity**

### **Time Complexity**:

* **Build Heap**: O(n)
* **Heapify (n times)**: O(log n) each → total O(n log n)
* **Overall**: **O(n log n)**

### **Space Complexity**:

* **In-place sorting**: O(1) auxiliary space

---

## **Summary**

Your implementation:
✅ Uses max-heap to sort in-place
✅ Is efficient (O(n log n)) and stable for large inputs
✅ Handles both small and large test cases well

---

Let’s walk through a visualization of **heap sort using a max heap**, step by step, with **ASCII diagrams**.

---

### 🔢 Input Array:

We’ll use this example for clarity:

```
arr = [8, 5, 2, 9, 5, 6, 3]
```

---

## ✅ Step 1: Build Max Heap

We start heapifying from the last non-leaf node (index `n//2 - 1 = 2`).

### Initial Array as Tree:

```
         8
       /   \
      5     2
     / \   / \
    9   5 6   3
```

We heapify from bottom-up: indices 2, 1, 0.

---

### 🔁 heapify at index 2:

```
Subtree rooted at 2: left = 6, right = 7 → only left exists: arr[6] = 3

arr[2] = 2 < arr[6] = 3 → swap

Result:
         8
       /   \
      5     3
     / \   / \
    9   5 6   2
```

New array: `[8, 5, 3, 9, 5, 6, 2]`

---

### 🔁 heapify at index 1:

```
Subtree rooted at 5: children = 9, 5 → 9 is largest → swap

         8
       /   \
      9     3
     / \   / \
    5   5 6   2
```

New array: `[8, 9, 3, 5, 5, 6, 2]`

---

### 🔁 heapify at index 0:

```
Subtree rooted at 8: children = 9, 3 → 9 is largest → swap

         9
       /   \
      8     3
     / \   / \
    5   5 6   2
```

New array: `[9, 8, 3, 5, 5, 6, 2]`

---

## 🎯 Max Heap Built!

```
         9
       /   \
      8     3
     / \   / \
    5   5 6   2
```

---

## ✅ Step 2: Extract Max One by One

Each time:

* Swap root with last element
* Reduce heap size
* Heapify root

---

### 🧮 Iteration 1:

Swap `arr[0]` and `arr[6]`: `[2, 8, 3, 5, 5, 6, 9]`

Heapify index 0 (size = 6):

```
         8
       /   \
      5     3
     / \   /
    2   5 6
```

New heap: `[8, 5, 6, 2, 5, 3, 9]`

---

### 🧮 Iteration 2:

Swap `arr[0]` and `arr[5]`: `[3, 5, 6, 2, 5, 8, 9]`

Heapify index 0 (size = 5):

```
         6
       /   \
      5     3
     / \
    2   5
```

New heap: `[6, 5, 3, 2, 5, 8, 9]`

---

### 🧮 Iteration 3:

Swap `arr[0]` and `arr[4]`: `[5, 5, 3, 2, 6, 8, 9]`

Heapify index 0 (size = 4):

```
         5
       /   \
      5     3
     /
    2
```

New heap: `[5, 5, 3, 2, 6, 8, 9]`

---

### 🧮 Iteration 4:

Swap `arr[0]` and `arr[3]`: `[2, 5, 3, 5, 6, 8, 9]`

Heapify index 0 (size = 3):

```
         5
       /   \
      2     3
```

Heapified: `[5, 2, 3, 5, 6, 8, 9]`

---

### 🧮 Iteration 5:

Swap `arr[0]` and `arr[2]`: `[3, 2, 5, 5, 6, 8, 9]`

Heapify index 0 (size = 2): `[3, 2, 5, 5, 6, 8, 9]`

---

### 🧮 Iteration 6:

Swap `arr[0]` and `arr[1]`: `[2, 3, 5, 5, 6, 8, 9]`

---

## ✅ Final Sorted Array:

```
[2, 3, 5, 5, 6, 8, 9]
```

---

### 📝 Summary Table of Key Steps:

| Step       | Array                   | Heap Tree (Root) |
| ---------- | ----------------------- | ---------------- |
| Original   | `[8, 5, 2, 9, 5, 6, 3]` | 8                |
| Build Heap | `[9, 8, 3, 5, 5, 6, 2]` | 9                |
| Extract #1 | `[8, 5, 6, 2, 5, 3, 9]` | 8                |
| Extract #2 | `[6, 5, 3, 2, 5, 8, 9]` | 6                |
| Extract #3 | `[5, 5, 3, 2, 6, 8, 9]` | 5                |
| Extract #4 | `[5, 2, 3, 5, 6, 8, 9]` | 5                |
| Extract #5 | `[3, 2, 5, 5, 6, 8, 9]` | 3                |
| Extract #6 | `[2, 3, 5, 5, 6, 8, 9]` | 2                |


"""
