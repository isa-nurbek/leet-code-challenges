# Problem Description:

"""

                                            Permutations

Write a function that takes in an array of unique integers and returns an array of all `permutations` of those integers in
no particular order.

If the input array is empty, the function should return an empty array.


## Sample Input
```
array = [1, 2, 3]
```

## Sample Output
```
[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
```

## Optimal Time & Space Complexity:
```
O(n * n!) time | O(n * n!) space - where `n` is the length of the input array.
```
"""

# =========================================================================================================================== #

# Solution:


# O(n * n!) time | O(n * n!) space
def get_permutations(array):
    """Main function to generate all permutations of an array.

    Args:
        array: The input array to generate permutations for

    Returns:
        A list containing all possible permutations of the input array
    """
    permutations = []  # This will store all the permutations we generate
    permutations_helper(0, array, permutations)  # Start the recursive process
    return permutations


def permutations_helper(i, array, permutations):
    """Recursive helper function to generate permutations.

    This works by swapping elements to generate all possible orderings.

    Args:
        i: Current index we're fixing in the permutation
        array: The array we're generating permutations for
        permutations: List to store the resulting permutations
    """
    # Base case: If we've reached the last element, we have a complete permutation
    if i == len(array) - 1:
        permutations.append(array[:])  # Add a copy of the current array state
    else:
        # Recursive case: Generate permutations for remaining elements
        for j in range(i, len(array)):
            # Swap current element with element at index j
            swap(array, i, j)
            # Recursively generate permutations for the remaining positions
            permutations_helper(i + 1, array, permutations)
            # Swap back (backtrack) to restore original array for next iteration
            swap(array, i, j)


def swap(array, i, j):
    """Helper function to swap two elements in an array in-place.

    Args:
        array: The array containing elements to swap
        i: Index of first element
        j: Index of second element
    """
    array[i], array[j] = array[j], array[i]


# Test Cases:

print(get_permutations([1, 2, 3]))
# Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

print(get_permutations([1]))
# Output: [[1]]

print(get_permutations([]))
# Output: []

# =========================================================================================================================== #

# Big O Analysis:

"""

## Time and Space Complexity Analysis

### Time Complexity:

The algorithm generates all permutations of the input array. For an array of length `n`, there are `n!` (n factorial) permutations.

1. **Base Case**: When `i == len(array) - 1`, it copies the current array (O(n) time) and appends it to `permutations`.
2. **Recursive Case**: For each index `i`, the algorithm swaps `array[i]` with `array[j]` for `j` from `i` to `n-1`, and 
recursively generates permutations for `i+1`.

- The recursion tree has `n!` leaves (one for each permutation).
- Each leaf involves an O(n) operation (copying the array).
- The total number of nodes in the recursion tree is roughly `n! + n!/1! + n!/2! + ... + n!/(n-1!)`, which is still O(n!).
- Each recursive call does O(1) work (apart from the recursive calls and the base case).

Thus, the total time complexity is **O(n! * n)**.

### Space Complexity:

1. **Output Space**: The `permutations` list stores `n!` permutations, each of size `n`, so this contributes O(n! * n) space.
2. **Recursion Stack**: The recursion depth is `n` (since `i` goes from `0` to `n-1`), and each stack frame uses O(1) space
(just storing `i`, `j`, and some pointers). Thus, the recursion stack contributes O(n) space.

The dominant term is the output space, so the total space complexity is **O(n! * n)**.

### Summary:
- **Time Complexity**: O(n! * n)
- **Space Complexity**: O(n! * n) (due to the output storage)

This is optimal for generating all permutations because you can't do better than O(n!) time (since there are n! permutations)
or O(n! * n) space (since you need to store n! permutations, each of size n).

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
Let's go through this Python code step by step to understand how it generates all permutations of an array.
This is a classic backtracking algorithm.

---

### ✅ Goal:
Generate **all permutations** of a list (e.g., `[1, 2, 3]`), which means all possible ways to arrange its elements.

---

### 🔧 Code Breakdown:

#### 1. **`get_permutations(array)`**
This is the **main function** that the user calls.

```
def get_permutations(array):
    permutations = []
    permutations_helper(0, array, permutations)
    return permutations
```

- **Input**: an array (e.g., `[1, 2, 3]`)
- **`permutations`**: a list that will store all the result permutations.
- **It calls `permutations_helper()`**, starting from index `0`.

---

#### 2. **`permutations_helper(i, array, permutations)`**
This is the **recursive backtracking function**.

```
def permutations_helper(i, array, permutations):
    if i == len(array) - 1:
        permutations.append(array[:])
    else:
        for j in range(i, len(array)):
            swap(array, i, j)
            permutations_helper(i + 1, array, permutations)
            swap(array, i, j)
```

##### 📌 Let's explain each part:
- `i`: current index (the position we are "fixing").
- **Base case**:
  ```
  if i == len(array) - 1:
      permutations.append(array[:])
  ```
  - If we've reached the last index, it means the array is a complete permutation. So we add a **copy** of it to the result list (`array[:]` makes a shallow copy).
  
- **Recursive case**:
  ```
  for j in range(i, len(array)):
      swap(array, i, j)
      permutations_helper(i + 1, array, permutations)
      swap(array, i, j)
  ```
  - For each index `j` from `i` to end:
    - Swap elements at `i` and `j` (this "fixes" one element at position `i`).
    - Recursively call `permutations_helper(i + 1, ...)` to generate permutations of the remaining elements.
    - **Swap back** (backtrack) to restore the original order for the next loop iteration.

---

#### 3. **`swap(array, i, j)`**
A simple helper function to swap two elements in the array:

```
def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
```

---

### 🔁 Example Walkthrough: `get_permutations([1, 2, 3])`

Let’s look at the process:

```
Initial call: permutations_helper(0, [1, 2, 3])

i = 0:
  j = 0: swap(0,0) => [1,2,3]
    i = 1:
      j = 1: swap(1,1) => [1,2,3]
        i = 2: add [1,2,3]
      j = 2: swap(1,2) => [1,3,2]
        i = 2: add [1,3,2]
      backtrack
  j = 1: swap(0,1) => [2,1,3]
    i = 1:
      j = 1: swap(1,1) => [2,1,3]
        i = 2: add [2,1,3]
      j = 2: swap(1,2) => [2,3,1]
        i = 2: add [2,3,1]
      backtrack
  j = 2: swap(0,2) => [3,2,1]
    i = 1:
      j = 1: swap(1,1) => [3,2,1]
        i = 2: add [3,2,1]
      j = 2: swap(1,2) => [3,1,2]
        i = 2: add [3,1,2]
```

So the output will be:
```
[[1, 2, 3],
 [1, 3, 2],
 [2, 1, 3],
 [2, 3, 1],
 [3, 2, 1],
 [3, 1, 2]]
```

---

### 🧠 Key Concepts Used:
- **Recursion**: to explore each path of permutations.
- **Backtracking**: after trying a swap, it "undoes" it to try another path.
- **Swapping**: used to rearrange elements in-place (no extra space needed for subarrays).

---

### 📎 Edge Cases:
```
print(get_permutations([]))       # Output: []
print(get_permutations([1]))      # Output: [[1]]
```

These are handled correctly because:
- If array is empty → the recursive function doesn't run.
- If array has 1 element → base case is triggered immediately.

---

Here's a **visual diagram** to help you see how the recursion tree and backtracking work for:

### 🔄 `get_permutations([1, 2, 3])`

We'll represent the **recursive tree** where each level is a deeper recursive call, and we use indentation to show the depth.
Each arrow `→` means a swap happened.

---

```
Start: [1, 2, 3]
|
|-- swap(0,0) → [1, 2, 3]
|   |
|   |-- swap(1,1) → [1, 2, 3]
|   |   |
|   |   |-- swap(2,2) → [1, 2, 3] ✅
|   |
|   |-- swap(1,2) → [1, 3, 2]
|       |
|       |-- swap(2,2) → [1, 3, 2] ✅
|
|-- swap(0,1) → [2, 1, 3]
|   |
|   |-- swap(1,1) → [2, 1, 3]
|   |   |
|   |   |-- swap(2,2) → [2, 1, 3] ✅
|   |
|   |-- swap(1,2) → [2, 3, 1]
|       |
|       |-- swap(2,2) → [2, 3, 1] ✅
|
|-- swap(0,2) → [3, 2, 1]
    |
    |-- swap(1,1) → [3, 2, 1]
    |   |
    |   |-- swap(2,2) → [3, 2, 1] ✅
    |
    |-- swap(1,2) → [3, 1, 2]
        |
        |-- swap(2,2) → [3, 1, 2] ✅
```

---

### ✅ Final Permutations Collected:
```
[1, 2, 3]
[1, 3, 2]
[2, 1, 3]
[2, 3, 1]
[3, 2, 1]
[3, 1, 2]
```

---

### 🔁 Why swap back?

After each recursive call, we **swap back** to undo the last change, so the next iteration can start from the original
state of the array. That’s the **backtracking** part.

"""
