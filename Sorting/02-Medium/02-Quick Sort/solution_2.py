# Problem Description:

"""
                                               Quick Sort

Write a function that takes in an array of integers and returns a `sorted` version of that array. Use the `Quick Sort` algorithm
to sort the array.

To avoid `O(n²)` worst-case time complexity you can:

- Choose a `random pivot` or `median-of-three pivot`.
- Use an `in-place partitioning` scheme to reduce space usage.

1. **Avoiding O(n²) worst-case**: Quick Sort can degrade to `O(n²)` time complexity if poorly chosen pivots (e.g., always picking
the `first/last` element in an already sorted array) lead to highly unbalanced partitions. The suggestions address this:
   - **Random pivot**: Randomization makes worst-case behavior unlikely.
   - **Median-of-three pivot**: Choosing the median of the first, middle, and last elements helps avoid bad pivots.

2. **In-place partitioning**: This reduces space complexity from O(log n) (due to recursion stack) to O(1) auxiliary space
(excluding the stack), making it more memory-efficient.


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
Best: O(n log(n)) time | O(log(n)) space - where n is the length of the input array.
Average: O(n log(n)) time | O(log(n)) space - where n is the length of the input array.
Worst: O(n²) time | O(log(n)) space - where n is the length of the input array.
```

"""

# =========================================================================================================================== #

# Solution:

import random  # Import the random module for selecting random pivot


# Best: O(n log(n)) time | O(log(n)) space
# Average: O(n log(n)) time | O(log(n)) space
# Worst: O(n²) time | O(n²) space
def randomized_quick_sort(arr):
    """
    Sorts an array using the randomized quicksort algorithm.
    This version creates new lists for partitions rather than sorting in-place.

    Args:
        arr: List of comparable elements to be sorted

    Returns:
        A new list containing all elements from arr in sorted order
    """

    # Base case: arrays of length 0 or 1 are already sorted
    if len(arr) <= 1:
        return arr.copy()  # Return a copy to maintain consistency in return types

    # Randomly select a pivot index to help avoid worst-case O(n^2) performance
    pivot_idx = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_idx]

    # Partition the array into three parts:
    # - left: elements smaller than pivot
    # - middle: elements equal to pivot (handles duplicate values)
    # - right: elements larger than pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Recursively sort the left and right partitions, then combine with middle
    # Note: middle doesn't need sorting as all elements are equal
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)


# Test Cases:

print(randomized_quick_sort([8, 5, 2, 9, 5, 6, 3]))
# Output: [2, 3, 5, 5, 6, 8, 9]

print(
    randomized_quick_sort(
        [-4, 5, 10, 8, -10, -6, -4, -2, -5, 3, 5, -4, -5, -1, 1, 6, -7]
    )
)
# Output: [-10, -7, -6, -5, -5, -4, -4, -4, -2, -1, 1, 3, 5, 5, 6, 8, 10]

print(randomized_quick_sort([2, 1]))
# Output: [1, 2]

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### Time Complexity Analysis

1. **Best Case**: 
   - The pivot chosen divides the array into two nearly equal parts every time.
   - The recurrence relation is: T(n) = 2T(n/2) + O(n).
   - By the Master Theorem, this solves to O(n log n).

2. **Average Case**:
   - In randomized quicksort, the probability of choosing a "good" pivot (one that splits the array roughly in half) is high.
   - The average-case time complexity is also O(n log n).

3. **Worst Case**:
   - The worst case occurs when the pivot is consistently the smallest or largest element, leading to highly unbalanced partitions.
   - The recurrence relation becomes: T(n) = T(n-1) + O(n), which solves to O(n²).
   - However, the probability of this happening in randomized quicksort is very low (especially as the input size grows).

### Space Complexity Analysis

The space complexity is determined by the additional memory used during the sorting process:

1. **Auxiliary Space for Partitions**:
   - In each recursive call, we create new lists `left`, `middle`, and `right`. In the worst case (unbalanced partitions),
   this can lead to O(n) space per recursive call, and the recursion depth can be O(n), leading to O(n²) space.
   - In the average case (balanced partitions), the recursion depth is O(log n), and the total space used is O(n log n)
   (since each level of recursion requires O(n) space).

2. **Optimization**:
   - This implementation is not in-place, so it uses more space than an in-place version of quicksort (which would have O(log n))
   space for recursion stack in the average case).

### Summary:

- **Time Complexity**:

  - Best Case: O(n log n)
  - Average Case: O(n log n)
  - Worst Case: O(n²) (unlikely with randomization).
  
- **Space Complexity**:

  - Best Case: O(n log n)
  - Average Case: O(n log n)
  - Worst Case: O(n²)

### Note:
The space complexity can be improved to O(n) in the worst case (or O(log n)) for in-place versions), but this implementation
trades space for clarity and simplicity.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
Let’s break down the code for the function randomized\_quick\_sort step-by-step:

### Overview

This is a Python implementation of the Quick Sort algorithm using a randomized pivot selection strategy. Quick Sort is a
divide-and-conquer sorting algorithm with average time complexity O(n log n).

---

### Code Explanation

```
import random
```

* Imports the `random` module, used to randomly select a pivot element to improve performance on already sorted or nearly sorted arrays.

---

```
    def randomized_quick_sort(arr):
```

* Defines the function that takes a list arr and returns a sorted version of it.

---

```
if len(arr) <= 1:
    return arr.copy()
```

* Base case: if the array has 0 or 1 element, it's already sorted.
* `arr.copy()` ensures that the original array isn’t affected if the user modifies the result.

---

```
    pivot_idx = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_idx]
```

* Picks a random index as the pivot.
* The pivot is the value at that index. This randomization helps to avoid the worst-case performance of Quick Sort O(n²)
for sorted or patterned input.

---

```
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
```

* The array is partitioned into three sublists:

  * `left`: elements less than pivot
  * `middle`: elements equal to pivot (important for handling duplicates)
  * `right`: elements greater than pivot

---

```
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)
```

* Recursive calls:

  * Sort `left` and `right` partitions independently.
  * Combine the sorted parts with `middle` to get the full sorted array.

---

### Example

For the input:

```
randomized_quick_sort([8, 5, 2, 9, 5, 6, 3])
```

Let’s say the randomly chosen pivot is 5:

* `left`: [2, 3]
* `middle`: [5, 5]
* `right`: [8, 9, 6]

Then, it recursively sorts [2, 3] and [8, 9, 6], combines all, and returns the sorted list:

```
[2, 3] + [5, 5] + [6, 8, 9] → [2, 3, 5, 5, 6, 8, 9]
```

---

### Key Points

* ✅ Efficient average-case performance: O(n log n)
* ✅ Handles duplicates properly
* ✅ Random pivot helps avoid worst-case scenarios
* ❌ Not in-place (creates new lists for each partition, so uses extra memory)

---

Here's a step-by-step ASCII visualization of how randomized_quick_sort works using this example:

🧪 Input:

```
[8, 5, 2, 9, 5, 6, 3]
```

Let’s walk through it, assuming the randomly chosen pivots are as follows at each step.

---

### Step 1: Pick pivot = 5

Split:

```
Left   = [2, 3]
Middle = [5, 5]
Right  = [8, 9, 6]
```

Recursive calls:

```
randomized_quick_sort([2, 3])
randomized_quick_sort([8, 9, 6])
```

---

### Step 2a: Sort [2, 3] — Pick pivot = 3

Split:

```
Left   = [2]
Middle = [3]
Right  = []
```

Return:

```
[2] + [3] + [] = [2, 3]
```

---

### Step 2b: Sort [8, 9, 6] — Pick pivot = 8

Split:

```
Left   = [6]
Middle = [8]
Right  = [9]
```

Return:

```
[6] + [8] + [9] = [6, 8, 9]
```

---

### Final Assembly

Now combine everything:

```
Left   = [2, 3]
Middle = [5, 5]
Right  = [6, 8, 9]

Final = [2, 3] + [5, 5] + [6, 8, 9]
      = [2, 3, 5, 5, 6, 8, 9]
```

---

🎉 Final Sorted Output:

```
[2, 3, 5, 5, 6, 8, 9]
```

"""
