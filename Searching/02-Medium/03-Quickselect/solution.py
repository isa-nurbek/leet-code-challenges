# Problem Description:

"""
                                             Quickselect

Write a function that takes in an array of distinct integers as well as an integer `k` and that returns the `k`th smallest integer
in that array.

The function should do this in `linear time`, on average.


## Sample Input:
```
array = [8, 5, 2, 9, 7, 6, 3]
k = 3
```

## Sample Output:
```
5
```

## Optimal Time & Space Complexity:
```
Best: O(n) time | O(1) space - where `n` is the length of the input array.
Average: O(n) time | O(1) space - where `n` is the length of the input array.
Worst: O(n²) time | O(1) space - where `n` is the length of the input array.
```

"""

# =========================================================================================================================== #

# Solution:


# Best: O(n) time | O(1) space
# Average: O(n) time | O(1) space
# Worst: O(n²) time | O(1)
def quick_select(array, k):
    """
    Finds the kth smallest element in an unsorted array using QuickSelect algorithm.

    Args:
        array: The unsorted list of elements
        k: The position of the element to find (1-based index)

    Returns:
        The kth smallest element in the array

    Note:
        This is a wrapper function that sets up the initial parameters for the helper function.
    """
    position = k - 1  # Convert to 0-based index

    return quick_select_helper(array, 0, len(array) - 1, position)


def quick_select_helper(array, start_idx, end_idx, position):
    """
    Helper function that performs the actual QuickSelect algorithm recursively (using iteration).

    Args:
        array: The unsorted list of elements
        start_idx: The starting index of the current subarray
        end_idx: The ending index of the current subarray
        position: The target position (0-based) we're searching for

    Returns:
        The element at the target position when the array would be sorted

    Note:
        Uses a while loop with tail recursion elimination for better performance.
    """
    while True:
        # Base case that should theoretically never be reached if inputs are valid
        if start_idx > end_idx:
            raise Exception("Your algorithm should never arrive here!")

        # Initialize pointers for partitioning
        pivot_idx = start_idx  # Choose first element as pivot
        left_idx = start_idx + 1
        right_idx = end_idx

        # Partitioning step (similar to QuickSort)
        while left_idx <= right_idx:
            # If left element is greater than pivot and right is smaller, swap them
            if (
                array[left_idx] > array[pivot_idx]
                and array[right_idx] < array[pivot_idx]
            ):
                swap(left_idx, right_idx, array)

            # Move left pointer if element is <= pivot
            if array[left_idx] <= array[pivot_idx]:
                left_idx += 1

            # Move right pointer if element is >= pivot
            if array[right_idx] >= array[pivot_idx]:
                right_idx -= 1

        # After partitioning, swap pivot with right_idx (final pivot position)
        swap(pivot_idx, right_idx, array)

        # Check if we've found our target element
        if right_idx == position:
            return array[right_idx]
        # If pivot is left of target, search right subarray
        elif right_idx < position:
            start_idx = right_idx + 1
        # If pivot is right of target, search left subarray
        else:
            end_idx = right_idx - 1


def swap(one, two, array):
    """
    Swaps two elements in an array.

    Args:
        one: Index of first element
        two: Index of second element
        array: The array containing the elements to swap
    """
    array[one], array[two] = array[two], array[one]


# Test Cases:

print(quick_select([8, 5, 2, 9, 7, 6, 3], 3))
# Output: 5

print(quick_select([102, 41, 58, 81, 2, -5, 1000, 10021, 181, -14515, 25, 15], 5))
# Output: 25

print(quick_select([43, 24, 37], 2))
# Output: 37

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### Time Complexity Analysis of Quickselect

The **quickselect** algorithm is used to find the k-th smallest (or largest) element in an unsorted list. It's a selection
algorithm that is based on the **quicksort** algorithm but only recurses into one side of the partition (the side where the
desired element lies).

#### Best-case Time Complexity: **O(n)**

- This occurs when the pivot chosen at every step divides the array into roughly equal parts. However, since we only recurse
into one partition, the total work is:
  - First pass: O(n) (partitioning the entire array)
  - Second pass: O(n/2) (partitioning half the array)
  - Third pass: O(n/4)
  - ...
  - Total: O(n + n/2 + n/4 + ...) = O(2n) = O(n)

#### Average-case Time Complexity: **O(n)**

- On average, the pivot will divide the array into two parts where one part is a constant fraction of the original array
(e.g., 1/4 and 3/4). The series still sums to O(n).

#### Worst-case Time Complexity: **O(n²)**

- This happens when the pivot is always the smallest or largest element (e.g., already sorted array and choosing the first/last
element as the pivot). In this case:
  - First pass: O(n)
  - Second pass: O(n-1)
  - Third pass: O(n-2)
  - ...
  - Total: O(n + (n-1) + (n-2) + ... + 1) = O(n²)

#### Improving Worst-case to O(n) with Median-of-Medians

- If we use a **deterministic pivot selection** strategy like the "median of medians" algorithm (which guarantees a "good" pivot),
the worst-case time complexity can be improved to O(n). However, this adds significant constant overhead and is rarely used in practice.

---

### Space Complexity Analysis of Quickselect

Quickselect is an **in-place** algorithm, meaning it doesn't use additional space proportional to the input size.

#### Best/Average-case Space Complexity: **O(1) (Iterative) or O(log n) (Recursive)**

- The **iterative version** (like the one implemented above) uses **constant space** (O(1)) because it only modifies the array
in-place and uses a loop (no recursion stack).
- The **recursive version** would use **O(log n)** space in the average case (due to recursion depth), but the worst case would
be O(n) (if the pivot is unbalanced).

#### Worst-case Space Complexity (Recursive): **O(n)**

- If the pivot is always the smallest/largest element, the recursion depth is O(n), leading to O(n) space usage.

The provided implementation is **iterative**, so its space complexity is **O(1)** in all cases.

---

### Summary

| Case          | Time Complexity | Space Complexity (Iterative) |
|---------------|-----------------|------------------------------|
| Best-case     | O(n)            | O(1)                         |
| Average-case  | O(n)            | O(1)                         |
| Worst-case    | O(n²)           | O(1)                         |

### Notes
1. The **worst-case O(n²)** can be avoided by using **randomized pivot selection** (choosing a random pivot instead of always
`start_idx`), which makes the worst-case extremely unlikely in practice.
2. The **median-of-medians** method guarantees O(n) worst-case time but is slower in practice due to high constant factors.
3. The **iterative implementation** is better for space complexity (O(1)) compared to a recursive one (O(log n) avg / O(n) worst).

"""
