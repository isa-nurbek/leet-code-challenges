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


# Best: O(n log(n)) time | O(log(n)) space
# Average: O(n log(n)) time | O(log(n)) space
# Worst: O(n²) time | O(n) space
def quick_sort_inplace(arr, low=0, high=None):
    """
    Sorts the array in-place using quicksort algorithm.

    Args:
        arr: List to be sorted
        low: Starting index of the subarray to be sorted (default 0)
        high: Ending index of the subarray to be sorted (default None, which sets to last index)

    Returns:
        The sorted array (modified in-place)
    """
    if high is None:
        high = len(arr) - 1  # Initialize high to last index if not provided

    # Only proceed if there's more than one element to sort
    if low < high:
        # Partition the array and get the pivot's final index
        pivot_idx = partition(arr, low, high)

        # Recursively sort the elements before and after the pivot
        quick_sort_inplace(arr, low, pivot_idx - 1)  # Sort left subarray
        quick_sort_inplace(arr, pivot_idx + 1, high)  # Sort right subarray

    return arr  # Return the sorted array (modified in-place)


def partition(arr, low, high):
    """
    Partitions the subarray arr[low..high] such that:
    - All elements <= pivot are before it
    - All elements > pivot are after it
    - The pivot is placed in its correct sorted position

    Args:
        arr: The array to partition
        low: Starting index of subarray
        high: Ending index of subarray (pivot is initially arr[high])

    Returns:
        The index of the pivot element after partitioning
    """
    pivot = arr[high]  # Choose last element as pivot

    i = low - 1  # Index of smaller element (starts before the subarray)

    # Iterate through the subarray
    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i += 1  # Increment index of smaller element
            # Swap elements at i and j
            arr[i], arr[j] = arr[j], arr[i]

    # Place the pivot in its correct position
    # (after the last element that was <= pivot)
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1  # Return the pivot's final index


# Test Cases:

print(quick_sort_inplace([8, 5, 2, 9, 5, 6, 3]))
# Output: [2, 3, 5, 5, 6, 8, 9]

print(
    quick_sort_inplace([-4, 5, 10, 8, -10, -6, -4, -2, -5, 3, 5, -4, -5, -1, 1, 6, -7])
)
# Output: [-10, -7, -6, -5, -5, -4, -4, -4, -2, -1, 1, 3, 5, 5, 6, 8, 10]

print(quick_sort_inplace([2, 1]))
# Output: [1, 2]

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### Time Complexity Analysis:

1. **Best Case**:  
   - Occurs when the pivot always divides the array into two nearly equal halves.  
   - Recurrence relation: T(n) = 2T(n/2) + O(n)
   - By the Master Theorem, this solves to O(n log n).

2. **Average Case**:  
   - For random input, the pivot is expected to split the array reasonably well.  
   - The average time complexity is also O(n log n).

3. **Worst Case**:  
   - Occurs when the pivot is always the smallest or largest element (e.g., already sorted/reverse-sorted array).  
   - Recurrence relation: T(n) = T(n-1) + O(n)
   - This leads to O(n²).

### Space Complexity Analysis:

- The space complexity is determined by the recursion stack depth.  
  - **Best/Average Case**: The recursion depth is O(log n).  
  - **Worst Case**: The recursion depth is O(n).  
- Since the sorting is done in-place, no additional space is used apart from the recursion stack.  

### Summary:

| Case       | Time Complexity  | Space Complexity  |
|------------|------------------|-------------------|
| Best       | O(n log n)       | O(log n)          |
| Average    | O(n log n)       | O(log n)          |
| Worst      | O(n²)            | O(n)              |

### Notes:
- The worst case can be avoided by using randomized quicksort (choosing a random pivot).  
- In practice, quicksort is often faster than other O(n log n) algorithms due to smaller constant factors and cache efficiency.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
Let’s walk through it piece by piece to explain how it works.

---

### 🔧 What Is Quick Sort?

Quick Sort is a “divide-and-conquer” sorting algorithm:

* It selects a pivot element.
* Partitions the array into two parts: elements smaller than (or equal to) the pivot go to the left, larger ones go to the right.
* Recursively applies the same logic to the left and right sub-arrays.

This implementation does it in-place, meaning it modifies the array directly and uses no extra memory for copies.

---

### 🔍 Function: `quick_sort_inplace(arr, low=0, high=None)`

This is the main sorting function.

#### Parameters:

* `arr`: the list to be sorted.
* `low`: starting index of the sub-array to sort (default is 0).
* `high`: ending index of the sub-array (default is None, which is replaced with the last index).

#### What It Does:

```
if high is None:
    high = len(arr) - 1
```

If the user doesn't specify `high`, it uses the full array.

```
if low < high:
    pivot_idx = partition(arr, low, high)
```

If the sub-array has more than one element, it partitions the array and gets the index where the pivot element ended up.

```
quick_sort_inplace(arr, low, pivot_idx - 1)
quick_sort_inplace(arr, pivot_idx + 1, high)
```

Then it recursively sorts the left and right sub-arrays.

---

### 🔍 Function: `partition(arr, low, high)`

This function does the actual partitioning.

#### Steps:

```
pivot = arr[high]
```

It picks the last element as the pivot.

```
i = low - 1
```

`i` tracks the boundary of the "less than or equal to pivot" region.

```
for j in range(low, high):
    if arr[j] <= pivot:
        i += 1
        arr[i], arr[j] = arr[j], arr[i]
```

If an element is ≤ pivot, it is moved to the "less than" side by swapping with the element at index `i + 1`.

```
arr[i + 1], arr[high] = arr[high], arr[i + 1]
```

Finally, the pivot is moved to its correct sorted position.

```
return i + 1
```

The index of the pivot is returned so the array can be split into two parts.

---

### ✅ Test Cases and Expected Outputs:

```
quick_sort_inplace([8, 5, 2, 9, 5, 6, 3])
# Output: [2, 3, 5, 5, 6, 8, 9]
```

```
quick_sort_inplace([-4, 5, 10, 8, -10, -6, -4, -2, -5, 3, 5, -4, -5, -1, 1, 6, -7])
# Output: [-10, -7, -6, -5, -5, -4, -4, -4, -2, -1, 1, 3, 5, 5, 6, 8, 10]
```

```
quick_sort_inplace([2, 1])
# Output: [1, 2]
```

Each list is sorted in-place.

---

### 🔁 Summary of Key Concepts

* Quick Sort is recursive.
* The partition function rearranges elements based on a pivot.
* This version sorts the array in-place, so no extra memory is used.
* It performs well on average: O(n log n) time, but worst-case is O(n²) (e.g., sorted arrays without pivot optimization).

---

Here's a step-by-step ASCII visualization of how in-place Quick Sort works using this array:

📦 Input:

```
[8, 5, 2, 9, 5, 6, 3]
```

We’ll walk through the first few recursive steps.

---

## Step 1: Initial call

```
quick_sort_inplace([8, 5, 2, 9, 5, 6, 3], low=0, high=6)
```

🎯 Pivot = 3 (last element)

Initial array:

```
[8, 5, 2, 9, 5, 6, 3]
                   ↑
                pivot
```

Now we partition the array around 3.

We want to move all elements ≤ 3 to the left.

Swaps during partitioning:

* Compare 8 > 3 → do nothing
* Compare 5 > 3 → do nothing
* Compare 2 ≤ 3 → swap 2 with 8

  → [2, 5, 8, 9, 5, 6, 3]
  
* Compare 9 > 3 → do nothing
* Compare 5 > 3 → do nothing
* Compare 6 > 3 → do nothing

Then place pivot (3) between smaller and larger elements:

Swap 3 with element after last smaller one (5):
→ [2, 3, 8, 9, 5, 6, 5]

🎉 Pivot (3) placed at index 1

```
Final after partitioning:
[2, 3, 8, 9, 5, 6, 5]
    ↑
  pivot index
```

---

## Step 2: Left subarray [2] (index 0 to 0)

It has only one element — already sorted.

---

## Step 3: Right subarray [8, 9, 5, 6, 5] (index 2 to 6)

```
quick_sort_inplace([2, 3, 8, 9, 5, 6, 5], low=2, high=6)
```

🎯 Pivot = 5

Initial:

```
[2, 3, 8, 9, 5, 6, 5]
                  ↑
               pivot
```

Partitioning:

* Compare 8 > 5 → nothing
* Compare 9 > 5 → nothing
* Compare 5 ≤ 5 → swap with 8
  → [2, 3, 5, 9, 8, 6, 5]
* Compare 6 > 5 → nothing

Place pivot between smaller and larger:
→ Swap 5 with 9 → [2, 3, 5, 5, 8, 6, 9]

🎉 Pivot (5) placed at index 3

```
[2, 3, 5, 5, 8, 6, 9]
             ↑
         pivot index
```

---

From here it continues recursively:

* Sorts [5] (index 2–2): one element
* Sorts [8, 6, 9] (index 4–6)
  → Pivot = 9
  → Swap 8 and 6 to get [2, 3, 5, 5, 6, 8, 9]

---

## ✅ Final Sorted Array:

```
[2, 3, 5, 5, 6, 8, 9]
```

"""
