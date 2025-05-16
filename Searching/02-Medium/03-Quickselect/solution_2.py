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


import random


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
            raise Exception("This should never happen.")

        # Choose a random pivot and swap it to the start
        pivot_idx = random.randint(start_idx, end_idx)
        swap(start_idx, pivot_idx, array)

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

### Time Complexity:

The `quick_select` algorithm is a selection algorithm to find the k-th smallest element in an unordered list.
It's based on the QuickSort algorithm but only recurses into one partition.

1. **Best Case**:  
   - The best case occurs when the randomly chosen pivot is the k-th element.  
   - This results in a single partitioning step, giving a time complexity of **O(n)**.

2. **Average Case**:  
   - On average, the pivot will divide the array into two roughly equal parts.  
   - The recurrence relation is:  
     
    T(n) = T(n/2) + O(n)
    
   - Solving this using the Master Theorem gives **O(n)** time complexity.

3. **Worst Case**:  
   - The worst case occurs when the pivot is always the smallest or largest element (e.g., if the array is already sorted and
   we pick the first/last element as the pivot).  
   - The recurrence relation becomes:  
    
    T(n) = T(n-1) + O(n)
    
   - This results in **O(n²)** time complexity.  
   - However, since we are using **randomized pivot selection**, the probability of worst-case behavior is extremely low.

### Space Complexity:

- The algorithm is **iterative** (using a `while True` loop instead of recursion), so it does not use additional call stack space.  
- All operations are performed **in-place** (only constant extra space is used for variables like `pivot_idx`, `left_idx`, `right_idx`, etc.).  
- Thus, the space complexity is **O(1)** (constant space).

### Summary:

| Case      | Time Complexity | Space Complexity  |
|-----------|-----------------|-------------------|
| Best      | O(n)            | O(1)              |
| Average   | O(n)            | O(1)              |
| Worst     | O(n²)           | O(1)              |

The randomized pivot selection ensures that the **average case O(n)** is the expected runtime, making this an efficient algorithm
for selection problems.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
The provided code implements the **QuickSelect** algorithm, which is an efficient algorithm to find the **k-th smallest element**
in an unsorted array (in linear average time). Let's break down and explain how this code works in detail.

---

## 🧠 **QuickSelect Algorithm - Concept**

QuickSelect is similar to QuickSort. Instead of sorting the whole array, it partially sorts the array such that we can find the
**k-th smallest** (or largest) element.
It uses a **pivot-based partitioning** strategy to narrow down the part of the array that contains the desired element.

---

## 🔍 **Function-by-Function Breakdown**

### ✅ `quick_select(array, k)`

This is the entry point to the algorithm.

```
def quick_select(array, k):
    position = k - 1  # convert to 0-based index
    return quick_select_helper(array, 0, len(array) - 1, position)
```

* Converts the user-specified 1-based `k` to 0-based (`k-1`) because Python uses 0-based indexing.
* Calls the recursive helper with the full array range.

---

### ✅ `quick_select_helper(array, start_idx, end_idx, position)`

This function **recursively partitions** the array to find the element at the `position` index.

#### Steps:

1. **Pivot Selection & Swap to Start**:

   ```
   pivot_idx = random.randint(start_idx, end_idx)
   swap(start_idx, pivot_idx, array)
   ```

   * Chooses a **random pivot** index between `start_idx` and `end_idx`.
   * Swaps the pivot with the first element to simplify partitioning.

2. **Partitioning Logic**:

   ```
   left_idx = start_idx + 1
   right_idx = end_idx
   ```

   * `left_idx` and `right_idx` are pointers used to rearrange elements:

     * Elements **less than or equal to** the pivot move to the left.
     * Elements **greater than** the pivot move to the right.

3. **While Loop for Swapping**:

   ```
   while left_idx <= right_idx:
       if array[left_idx] > array[pivot_idx] and array[right_idx] < array[pivot_idx]:
           swap(left_idx, right_idx, array)

       if array[left_idx] <= array[pivot_idx]:
           left_idx += 1

       if array[right_idx] >= array[pivot_idx]:
           right_idx -= 1
   ```

   * If an element on the left is **too big** and an element on the right is **too small**, they are **swapped**.
   * Adjusts the pointers after checking if they are already in the correct partition.

4. **Final Swap**:

   ```
   swap(pivot_idx, right_idx, array)
   ```

   * Puts the pivot in its **correct sorted position** (`right_idx`).

5. **Check Position**:

   ```
   if right_idx == position:
       return array[right_idx]
   elif right_idx < position:
       start_idx = right_idx + 1
   else:
       end_idx = right_idx - 1
   ```

   * If the pivot is at the correct `position`, return it.
   * Otherwise, continue searching in the half where the k-th element must lie.

---

### 🔁 `swap(one, two, array)`

A helper function to swap two elements in an array.

```
def swap(one, two, array):
    array[one], array[two] = array[two], array[one]
```

---

## 🧪 Test Cases

```
print(quick_select([8, 5, 2, 9, 7, 6, 3], 3))  
# Output: 5
```

* Sorted array: [2, 3, 5, 6, 7, 8, 9]
* 3rd smallest = 5

```
print(quick_select([102, 41, 58, 81, 2, -5, 1000, 10021, 181, -14515, 25, 15], 5))  
# Output: 25
```

* Sorted: [-14515, -5, 2, 15, 25, 41, 58, 81, 102, 181, 1000, 10021]
* 5th smallest = 25

```
print(quick_select([43, 24, 37], 2))  
# Output: 37
```

* Sorted: [24, 37, 43]
* 2nd smallest = 37

---

## ⏱️ Time Complexity

* **Average case**: **O(n)** — because each partition ideally reduces the problem size by half.
* **Worst case**: **O(n²)** — if the pivot is always the largest or smallest element (unbalanced partitions).

  * The use of a **random pivot** mitigates this.

---

## 🧩 Summary

| Part                    | Purpose                                                              |
| ----------------------- | -------------------------------------------------------------------- |
| `quick_select()`        | Starts the algorithm and converts k to 0-based                       |
| `quick_select_helper()` | Core logic to partition the array and find the k-th smallest element |
| `swap()`                | Utility function for swapping elements                               |
| Random pivot            | Prevents worst-case time complexity                                  |

This is a powerful algorithm used when you want the k-th smallest (or largest) element without fully sorting the array.

---

Let’s visualize how the **QuickSelect algorithm** works on an example using **ASCII diagrams**. We'll walk through:

### 🧪 Example:

```
quick_select([8, 5, 2, 9, 7, 6, 3], 3)
```

> Goal: Find the **3rd smallest** element
> Target index = `k - 1 = 2` (0-based)

---

## 🔁 Step-by-Step ASCII Visualization

### Step 1: Initial Array

```
[8, 5, 2, 9, 7, 6, 3]
           ^       ^
       start=0   end=6
```

### Step 2: Choose a random pivot (e.g. pivot=3 at index 6), swap with start

```
Swap index 0 and 6 (pivot 3 moved to front)
[3, 5, 2, 9, 7, 6, 8]
 ^
pivot
```

### Step 3: Partitioning Loop

We’ll now move elements around so that:

* Elements ≤ 3 go left of pivot
* Elements > 3 go right

Pointers start here:

```
[3, 5, 2, 9, 7, 6, 8]
    ^           ^
  left        right
```

Check conditions:

* `5 > 3` and `8 > 3` → only decrement right:

```
[3, 5, 2, 9, 7, 6, 8]
    ^        ^
  left     right
```

* `5 > 3` and `6 > 3` → right--
* `5 > 3` and `7 > 3` → right--
* `5 > 3` and `9 > 3` → right--

```
[3, 5, 2, 9, 7, 6, 8]
    ^  ^
  left right
```

Now:

* `5 > 3`, `2 < 3` → swap left and right (1 and 2):

```
[3, 2, 5, 9, 7, 6, 8]
    ^  ^
  left right
```

* `2 <= 3`, move left++
* `5 >= 3`, move right--

```
[3, 2, 5, 9, 7, 6, 8]
       ^  ^
     left right
```

`left > right`, so exit loop.

Now swap pivot (0) with `right` (1):

```
Swap 0 and 1 → pivot placed at correct position
[2, 3, 5, 9, 7, 6, 8]
    ^
  pivot @ index 1
```

### Step 4: Check position

We want position 2 (k=3):

* `pivot @ 1 < 2`, so recurse on right subarray

---

### Step 5: Second Call on Subarray

Call on:

```
[2, 3, 5, 9, 7, 6, 8]
           ^        ^
         start=2   end=6
```

Pick random pivot, say index 3 (pivot = 9), swap with index 2:

```
[2, 3, 9, 5, 7, 6, 8]
           ^
         pivot=9
```

Partition:

```
[2, 3, 9, 5, 7, 6, 8]
               ^    ^
             left right
```

Loop swaps nothing since all elements < pivot.
Final state after swapping pivot with right (index 6):

```
[2, 3, 8, 5, 7, 6, 9]
                   ^
               pivot @ index 6
```

### Step 6: Check position

We want index 2. Pivot is at 6 → recurse left

---

### Step 7: Third Call on:

```
[2, 3, 8, 5, 7, 6, 9]
           ^     ^
         start=2 end=5
```

Pick pivot (say index 3 → 5), swap with index 2:

```
[2, 3, 5, 8, 7, 6, 9]
           ^
         pivot=5
```

Partition:

```
[2, 3, 5, 8, 7, 6, 9]
               ^  ^
             left right
```

All > 5, so no swaps

Final swap:

```
[2, 3, 6, 8, 7, 5, 9]
                   ^
               pivot @ index 5
```

Still too far → continue in left part

---

### Step 8: Final Call on:

```
[2, 3, 6, 8, 7, 5, 9]
           ^  ^
         s=2  e=4
```

Choose pivot = 6, partition...

Eventually, pivot lands at index 2 — match found!

---

## ✅ Final Answer:

```
The 3rd smallest element is: 5
```

---

## 🔚 Summary Diagram

```
Initial:     [8, 5, 2, 9, 7, 6, 3]
Step 1:      [3, 5, 2, 9, 7, 6, 8]
After part:  [2, 3, 5, 9, 7, 6, 8]
Call 2:      [2, 3, 9, 5, 7, 6, 8]
After part:  [2, 3, 8, 5, 7, 6, 9]
Call 3:      [2, 3, 5, 8, 7, 6, 9]
After part:  [2, 3, 6, 8, 7, 5, 9]
...
Final array: [2, 3, 5, 6, 7, 8, 9]
```

You **didn't sort the full array**, just enough to find the k-th element. That’s the power of **QuickSelect**!

"""
