# Problem Description:

"""
                                               Selection Sort

Write a function that takes in an array of integers and returns a `sorted` version of that array. Use the `Selection Sort` algorithm
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
Best: O(n²) time | O(1) space - where `n` is the length of the input array.
Average: O(n²) time | O(1) space - where `n` is the length of the input array.
Worst: O(n²) time | O(1) space - where `n` is the length of the input array.
```

"""

# =========================================================================================================================== #

# Solution:


# Best: O(n²) time | O(1) space
# Average: O(n²) time | O(1)
# Worst: O(n²) time | O(1) space
def selection_sort(array):
    """
    Sorts an array in ascending order using the Selection Sort algorithm.

    Args:
        array: The list to be sorted

    Returns:
        The sorted list in ascending order
    """
    current_idx = 0  # Start with the first element as the initial position to fill

    # Loop through the array until the second-to-last element
    # (the last element will already be sorted when we get to it)
    while current_idx < len(array) - 1:
        smallest_idx = current_idx  # Assume current element is the smallest initially

        # Search the unsorted portion of the array for the smallest element
        for i in range(current_idx + 1, len(array)):
            # If we find a smaller element, update the smallest_idx
            if array[smallest_idx] > array[i]:
                smallest_idx = i

        # Swap the smallest found element with the current position
        swap(current_idx, smallest_idx, array)
        # Move to the next position in the array
        current_idx += 1

    return array


def swap(i, j, array):
    """
    Helper function to swap two elements in an array.

    Args:
        i: Index of first element
        j: Index of second element
        array: The array containing the elements to swap
    """
    array[i], array[j] = array[j], array[i]


# Test Cases:

print(selection_sort([8, 5, 2, 9, 5, 6, 3]))
# Output: [2, 3, 5, 5, 6, 8, 9]

print(selection_sort([-4, 5, 10, 8, -10, -6, -4, -2, -5, 3, 5, -4, -5, -1, 1, 6, -7]))
# Output: [-10, -7, -6, -5, -5, -4, -4, -4, -2, -1, 1, 3, 5, 5, 6, 8, 10]

print(selection_sort([2, 1]))
# Output: [1, 2]

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### Time Complexity Analysis of Selection Sort

1. **Outer Loop (while loop):**  
   The outer loop runs from `current_idx = 0` to `current_idx = len(array) - 2` (i.e., `n - 1` times, where `n` is the length
   of the array).

2. **Inner Loop (for loop):**  
   For each iteration of the outer loop, the inner loop runs from `current_idx + 1` to `len(array) - 1`:
   - 1st iteration: `n - 1` comparisons  
   - 2nd iteration: `n - 2` comparisons  
   - ...  
   - Last iteration: `1` comparison  

   Total comparisons = `(n - 1) + (n - 2) + ... + 1` = `n(n - 1)/2` ≈ `O(n²)`.

3. **Swap Operation:**  
   Each swap takes constant time `O(1)`, and it happens `n - 1` times (once per outer loop iteration). This does not affect the
   overall time complexity since `O(n²)` dominates `O(n)`.

**Final Time Complexity:**  
`O(n²)` in all cases (best, average, and worst) because the algorithm always performs the same number of comparisons regardless
of input order.

---

### Space Complexity Analysis of Selection Sort

Selection Sort is an **in-place** sorting algorithm, meaning it does not use any extra space proportional to the input size.
The only additional space used is for a few variables (`current_idx`, `smallest_idx`, `i`, etc.), which is constant.

**Final Space Complexity:**  
`O(1)` (constant space, in-place sorting).

---

### Summary:

- **Time Complexity**:

  - Best Case: O(n²) 
  - Worst Case: O(n²) 
  - Average Case: O(n²)
  
- **Space Complexity**: O(1) (in-place sorting).

Selection Sort is inefficient for large datasets but can be useful when memory writes are expensive (since it performs at
most `O(n)` swaps).

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
Let's break it down in detail to understand how it works.

---

## 🔍 What is Selection Sort?

Selection sort is a simple comparison-based sorting algorithm. It works by repeatedly finding the minimum element from the unsorted
part of the list and moving it to the front. It operates in-place, so it doesn’t need extra memory.

---

## 🔧 Code Breakdown

### 1. The main function: `selection_sort(array)`

```
def selection_sort(array):
    current_idx = 0

    while current_idx < len(array) - 1:
        smallest_idx = current_idx
```

* `current_idx`: This is the index where we want to place the smallest remaining value.
* We loop through the array starting from `current_idx` to the end to find the smallest value.

### 2. Finding the smallest value in the unsorted part

```
for i in range(current_idx + 1, len(array)):
    if array[smallest_idx] > array[i]:
        smallest_idx = i
```

* This loop compares the current smallest element with the rest of the array.
* If a smaller value is found, `smallest_idx` is updated.

### 3. Swapping elements

```
swap(current_idx, smallest_idx, array)
current_idx += 1
```

* Once the smallest element in the unsorted part is found, it is swapped with the element at `current_idx`.
* Then we move the boundary of the sorted part one step forward.

### 4. The swap helper function

```
def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
```

* This function swaps the values at positions `i` and `j` in the array using tuple unpacking.

---

## 🔁 Step-by-Step Example

For `selection_sort([8, 5, 2, 9, 5, 6, 3])`

* Iteration 1: Find smallest → 2 → swap with 8 → [2, 5, 8, 9, 5, 6, 3]
* Iteration 2: Find next smallest → 3 → swap with 5 → [2, 3, 8, 9, 5, 6, 5]
* Continue until fully sorted → [2, 3, 5, 5, 6, 8, 9]

---

## ✅ Time and Space Complexity

* 🕒 Time: O(n²) in all cases (worst, average, and best).
* 🧠 Space: O(1) — it sorts in-place.

---

## 🧪 Test Outputs

Test cases output as expected:

```
print(selection_sort([8, 5, 2, 9, 5, 6, 3]))
# Output: [2, 3, 5, 5, 6, 8, 9]

print(selection_sort([-4, 5, 10, 8, -10, -6, -4, -2, -5, 3, 5, -4, -5, -1, 1, 6, -7]))
# Output: [-10, -7, -6, -5, -5, -4, -4, -4, -2, -1, 1, 3, 5, 5, 6, 8, 10]

print(selection_sort([2, 1]))
# Output: [1, 2]
```

---

Here's a detailed ASCII visualization showing how Selection Sort works on the array:

📦 Input: [8, 5, 2, 9, 5, 6, 3]

Legend:

* ⬅️ current index being sorted
* 🔍 scanning unsorted portion
* ✅ sorted portion
* ⭐ smallest found in unsorted portion

We’ll show each step of the algorithm:

Initial:
[8, 5, 2, 9, 5, 6, 3]

───────────────────────────────
Pass 1 (current_idx = 0):

[8⬅️, 5🔍, 2⭐, 9🔍, 5🔍, 6🔍, 3🔍] → Swap 8 and 2
[2✅, 5, 8, 9, 5, 6, 3]

───────────────────────────────
Pass 2 (current_idx = 1):

[2✅, 5⬅️, 8🔍, 9🔍, 5🔍, 6🔍, 3⭐] → Swap 5 and 3
[2✅, 3✅, 8, 9, 5, 6, 5]

───────────────────────────────
Pass 3 (current_idx = 2):

[2✅, 3✅, 8⬅️, 9🔍, 5⭐, 6🔍, 5🔍] → Swap 8 and 5
[2✅, 3✅, 5✅, 9, 8, 6, 5]

───────────────────────────────
Pass 4 (current_idx = 3):

[2✅, 3✅, 5✅, 9⬅️, 8🔍, 6🔍, 5⭐] → Swap 9 and 5
[2✅, 3✅, 5✅, 5✅, 8, 6, 9]

───────────────────────────────
Pass 5 (current_idx = 4):

[2✅, 3✅, 5✅, 5✅, 8⬅️, 6⭐, 9🔍] → Swap 8 and 6
[2✅, 3✅, 5✅, 5✅, 6✅, 8, 9]

───────────────────────────────
Pass 6 (current_idx = 5):

[2✅, 3✅, 5✅, 5✅, 6✅, 8⬅️, 9🔍] → Already sorted
[2✅, 3✅, 5✅, 5✅, 6✅, 8✅, 9]

───────────────────────────────
✅ Final Sorted Array:
[2, 3, 5, 5, 6, 8, 9]

"""
