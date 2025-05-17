# Problem Description:

"""
                                               Heap Sort

Write a function that takes in an array of integers and returns a `sorted version` of that array. Use the `Heap Sort` algorithm
to sort the array.

You can make 2 versions:

- Max-Heap Version (Ascending Order Sort)
- Min-Heap Version (Descending Order Sort)


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


# Min-Heap Version (Descending Order Sort)
def min_heapify(arr, n, i):
    """
    Converts an array into a min-heap structure starting from index i.
    A min-heap is a binary tree where each parent node is smaller than its children.

    Args:
        arr: The array to be heapified
        n: Size of the heap (can be smaller than array length)
        i: Index of the root node to start heapification from
    """
    smallest = i  # Initialize smallest as root
    left = 2 * i + 1  # Left child index
    right = 2 * i + 2  # Right child index

    # If left child exists and is smaller than current smallest
    if left < n and arr[left] < arr[smallest]:
        smallest = left

    # If right child exists and is smaller than current smallest
    if right < n and arr[right] < arr[smallest]:
        smallest = right

    # If smallest is not the root, swap and continue heapifying
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]  # Swap
        min_heapify(arr, n, smallest)  # Recursively heapify the affected subtree


def heap_sort_descending(arr):
    """
    Sorts an array in descending order using a min-heap approach.
    The process involves:
    1. Building a min-heap from the array
    2. Repeatedly extracting the smallest element and rebuilding the heap

    Args:
        arr: The array to be sorted

    Returns:
        The sorted array in descending order
    """
    n = len(arr)

    # Build the min-heap (rearrange array)
    # Start from the last non-leaf node (n//2 - 1) and work up to the root
    for i in range(n // 2 - 1, -1, -1):
        min_heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        # Move current root (smallest) to end
        arr[0], arr[i] = arr[i], arr[0]
        # Heapify the reduced heap (size i)
        min_heapify(arr, i, 0)

    return arr


# Test Cases:

print(heap_sort_descending([8, 5, 2, 9, 5, 6, 3]))
# Output: [9, 8, 6, 5, 5, 3, 2]

print(
    heap_sort_descending(
        [-4, 5, 10, 8, -10, -6, -4, -2, -5, 3, 5, -4, -5, -1, 1, 6, -7]
    )
)
# Output: [10, 8, 6, 5, 5, 3, 1, -1, -2, -4, -4, -4, -5, -5, -6, -7, -10]

print(heap_sort_descending([2, 1]))
# Output: [2, 1]

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

Let's analyze the time and space complexity of the given `heap_sort_descending` function, which uses a min-heap to sort
an array in descending order.

### Time Complexity:

1. **Building the Min-Heap (Heapify all non-leaf nodes):**
   - The loop runs from `n//2 - 1` down to `0`, so it performs `O(n)` calls to `min_heapify`.
   - Each `min_heapify` operation takes `O(log n)` time in the worst case (since the height of the heap is `log n`).
   - However, the tighter analysis for building the heap is actually `O(n)` (not `O(n log n)`), because most of the `heapify`
   operations work on smaller subtrees. This is a well-known result in heap construction.

   ⇒ Building the heap: **O(n)** time.

2. **Extracting elements and re-heapifying:**
   - The loop runs `n-1` times (from `n-1` down to `1`).
   - In each iteration, we swap the root (smallest element) with the last element and call `min_heapify` on the new root.
   - Each `min_heapify` call takes `O(log i)` time (where `i` is the current size of the heap, decreasing from `n-1` to `1`).
   - The total time for this phase is:
     
        Total = `Σ (from i=1 to n-1) O(log i)` ≈ **O(n log n)** (since `log(n!) ≈ n log n`).

   ⇒ Extracting and re-heapifying: **O(n log n)** time.

**Total Time Complexity:**  
The dominant term is `O(n log n)` (from the extraction phase), so the overall time complexity is: **O(n log n)**.

---

### Space Complexity:

- The `min_heapify` function is recursive, but its maximum depth is `O(log n)` (the height of the heap). Thus, the recursion
stack uses **O(log n)** space.
- Apart from this, the algorithm sorts the array in-place, using only a constant amount of additional space (for variables like
`smallest`, `left`, `right`, etc.).

**Total Space Complexity:**  
**O(1)** (if we ignore recursion stack, otherwise **O(log n)** for recursion).  
In practice, for large `n`, the recursive `min_heapify` could be rewritten iteratively to achieve **O(1)** space.

---

### Summary:
- **Time Complexity:** **O(n log n)** (best, average, and worst case).
- **Space Complexity:** **O(1)** (if using iterative heapify) or **O(log n)** (due to recursion stack).

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
This code implements **heap sort in descending order** using a **min-heap** structure. Let's break it down step by step to
understand how it works and why it gives a sorted array in descending order.

---

## 🔧 Key Concepts

* **Min-Heap**: A binary tree where the value at the root is **less than or equal** to its children.
* **Heapify**: A process to maintain the heap property (min-heap in this case) at a given node.
* **Heap Sort Using Min-Heap**: We build a min-heap and then repeatedly remove the smallest element (the root), placing it
at the end of the array. This gives us a **descending** sorted array.

---

## ✅ Code Breakdown

### 1. `min_heapify(arr, n, i)`

```
def min_heapify(arr, n, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] < arr[smallest]:
        smallest = left

    if right < n and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        min_heapify(arr, n, smallest)
```

This function maintains the **min-heap** property at index `i`:

* It calculates indices of the **left** and **right** children of node `i`.
* If either child is **smaller** than the current node, it updates `smallest`.
* If the smallest is not the current node, it **swaps** the values and **recursively heapifies** the subtree rooted
at the new smallest index.

---

### 2. `heap_sort_descending(arr)`

```
def heap_sort_descending(arr):
    n = len(arr)

    # Step 1: Build the min-heap
    for i in range(n // 2 - 1, -1, -1):
        min_heapify(arr, n, i)
```

This loop **builds a min-heap** from the unsorted array by starting from the last non-leaf node and calling `min_heapify` bottom-up.

```
    # Step 2: Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # move smallest to end
        min_heapify(arr, i, 0)          # re-heapify the reduced heap
```

* After the min-heap is built, we **extract the smallest element** (at index `0`) and swap it with the last element.
* We then **reduce the heap size by 1** and **heapify the root again** to maintain the min-heap.
* This process continues, pushing smaller elements toward the end of the array.

Finally, return the modified array.

---

## 🔄 Example Walkthrough: `[8, 5, 2, 9, 5, 6, 3]`

### Step 1: Build Min-Heap

The min-heap version of `[8, 5, 2, 9, 5, 6, 3]` becomes something like:

```
       2
     /   \
    5     3
   / \   / \
  9  5  6  8
```

Heap array: `[2, 5, 3, 9, 5, 6, 8]`

### Step 2: Sorting (swap and re-heapify)

* Swap `2` with `8` → `[8, 5, 3, 9, 5, 6, 2]` → Heapify → `[3, 5, 8, 9, 5, 6, 2]`
* Swap `3` with `6` → `[6, 5, 8, 9, 5, 3, 2]` → Heapify → ...
* Keep doing this...

Eventually, you'll get `[9, 8, 6, 5, 5, 3, 2]`.

---

## ✅ Final Outputs

```
print(heap_sort_descending([8, 5, 2, 9, 5, 6, 3]))
# Output: [9, 8, 6, 5, 5, 3, 2]

print(heap_sort_descending([-4, 5, 10, 8, -10, -6, -4, -2, -5, 3, 5, -4, -5, -1, 1, 6, -7]))
# Output: [10, 8, 6, 5, 5, 3, 1, -1, -2, -4, -4, -4, -5, -5, -6, -7, -10]

print(heap_sort_descending([2, 1]))
# Output: [2, 1]
```

---

## 🧠 Summary

| Step                    | Description                                                               |
| ----------------------- | ------------------------------------------------------------------------- |
| **1. Build Min-Heap**   | Transform the array into a min-heap.                                      |
| **2. Swap and Heapify** | Repeatedly move the smallest element to the end and rebuild the min-heap. |
| **Result**              | Array is sorted in **descending order**.                                  |

---

Let's visualize the **heap sort in descending order using a min-heap** in **ASCII art**, using the input:

```
arr = [8, 5, 2, 9, 5, 6, 3]
```

---

## 🏁 Original Array (Index view):

```
Index:     0   1   2   3   4   5   6
Array:    [8,  5,  2,  9,  5,  6,  3]
```

---

## 🧱 Step 1: Build Min-Heap

We start heapifying from the last non-leaf node (`n//2 - 1 = 2`) up to the root.

### Final Min-Heap Representation (as array):

```
[2, 5, 3, 9, 5, 6, 8]
```

### Min-Heap Tree (Visual):

```
        2
      /   \
     5     3
    / \   / \
   9   5 6   8
```

---

## 🔁 Step 2: Heap Sort (Swap root with last, re-heapify)

### ⬇ Swap 2 (min) with last: 8

```
[8, 5, 3, 9, 5, 6, 2]  ← size reduced to 6
```

### Heapify Index 0 → Result:

```
[3, 5, 8, 9, 5, 6]
```

```
        3
      /   \
     5     8
    / \   /
   9   5 6
```

---

### ⬇ Swap 3 with 6:

```
[6, 5, 8, 9, 5, 3, 2]
```

Heapify → `[5, 6, 8, 9, 5]` ...

Repeat this process...

---

## ✅ Final Sorted Array (Descending):

```
[9, 8, 6, 5, 5, 3, 2]
```

---

## 🔚 Final Visualization

Heap process in stages (partial):

### Initial:

```
        2
      /   \
     5     3
    / \   / \
   9   5 6   8
```

### After first extraction (2 swapped with 8):

```
        3
      /   \
     5     8
    / \   /
   9   5 6
```

### After second extraction (3 swapped with 6):

```
        5
      /   \
     5     6
    / \
   9   8
```

"""
