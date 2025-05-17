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
