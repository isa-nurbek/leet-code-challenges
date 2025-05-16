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

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
The provided code implements the **Quick Select** algorithm, which is an efficient algorithm to find the **k-th smallest element**
in an **unsorted array**. It is related to **Quick Sort** and has an **average-case time complexity of O(n)** and a **worst-case
of O(n²)** (though the worst-case is rare with good pivot selection).

---

### ✅ Goal:

Find the **k-th smallest** element in an unsorted array.

Example:

```
quick_select([8, 5, 2, 9, 7, 6, 3], 3)
```

Returns `5`, which is the **3rd smallest** element in the array.

---

## 🔍 Code Breakdown:

---

### 1. `quick_select(array, k)`

```
def quick_select(array, k):
    position = k - 1  # Convert 1-based index to 0-based index
    return quick_select_helper(array, 0, len(array) - 1, position)
```

* `k` is given as **1-based index** (e.g., 1st, 2nd, 3rd smallest).
* Internally, we work with **0-based indexing**, so we adjust `k - 1`.
* Calls a helper to do the recursive/iterative selection.

---

### 2. `quick_select_helper(array, start_idx, end_idx, position)`

```
def quick_select_helper(array, start_idx, end_idx, position):
    while True:
        if start_idx > end_idx:
            raise Exception("Your algorithm should never arrive here!")
```

* This loop runs **until** the element at `position` is found.
* If `start_idx > end_idx`, it's an error in logic.

---

### 3. **Choosing the pivot and partitioning**

```
pivot_idx = start_idx
left_idx = start_idx + 1
right_idx = end_idx
```

* **Pivot** is the first element of the current subarray.
* `left_idx` and `right_idx` are used to **reorder the array** around the pivot.

```
while left_idx <= right_idx:
    if (
        array[left_idx] > array[pivot_idx]
        and array[right_idx] < array[pivot_idx]
    ):
        swap(left_idx, right_idx, array)

    if array[left_idx] <= array[pivot_idx]:
        left_idx += 1

    if array[right_idx] >= array[pivot_idx]:
        right_idx -= 1
```

#### Partitioning Rule:

* Move elements **smaller than pivot to the left**.
* Move elements **greater than pivot to the right**.
* If `array[left_idx] > pivot` and `array[right_idx] < pivot`, swap them.

```
swap(pivot_idx, right_idx, array)
```

* After partitioning, place the pivot into its **final sorted position**.

---

### 4. **Decide next subarray to search**

```
if right_idx == position:
    return array[right_idx]
elif right_idx < position:
    start_idx = right_idx + 1
else:
    end_idx = right_idx - 1
```

* If pivot is at the target `position`, return it.
* If pivot is to the **left** of the desired position, search right half.
* If pivot is to the **right**, search left half.

---

### 5. `swap(one, two, array)`

```
def swap(one, two, array):
    array[one], array[two] = array[two], array[one]
```

* Simple helper to swap two elements in an array.

---

## 🧪 Test Cases:

### Test 1:

```
quick_select([8, 5, 2, 9, 7, 6, 3], 3)
```

* Sorted: `[2, 3, 5, 6, 7, 8, 9]`
* 3rd smallest: `5`

---

### Test 2:

```
quick_select([102, 41, 58, 81, 2, -5, 1000, 10021, 181, -14515, 25, 15], 5)
```

* Sorted: `[-14515, -5, 2, 15, 25, 41, 58, 81, 102, 181, 1000, 10021]`
* 5th smallest: `25`

---

### Test 3:

```
quick_select([43, 24, 37], 2)
```

* Sorted: `[24, 37, 43]`
* 2nd smallest: `37`

---

## 🧠 Summary:

| Feature               | Description                              |
| --------------------- | ---------------------------------------- |
| Algorithm             | Quick Select (like Quick Sort)           |
| Problem Solved        | Find k-th smallest element               |
| Time Complexity Avg   | O(n)                                     |
| Time Complexity Worst | O(n²) (rare)                             |
| Space Complexity      | O(1) (in-place, iterative version)       |
| Pivot Selection       | Always first element (could be improved) |

---

Let's walk through an ASCII **step-by-step visualization** of the Quick Select algorithm for this example:

```
quick_select([8, 5, 2, 9, 7, 6, 3], 3)
```

Goal: Find the **3rd smallest element** ⇒ **`k = 3`, position = 2** (0-based)

---

### Initial Array

```
Index:     0   1   2   3   4   5   6
Array:    [8,  5,  2,  9,  7,  6,  3]
            ^
         pivot_idx (start)
```

We start with:

* `pivot = 8`
* `left = 1`, `right = 6`

---

### Step 1: Partitioning round

We now move `left` and `right` toward each other:

#### Compare:

* `array[left] = 5` (≤ 8) → ✅ move `left` right
* `array[right] = 3` (≤ 8) → ❌ move `right` left

Do this until:

```
        [8, 5, 2, 9, 7, 6, 3]
            ↑           ↑
         left=1     right=6
```

After scanning:

```
        [8, 5, 2, 9, 7, 6, 3]
                    ↑   ↑
                 left=6 right=6
```

Then:

```
swap(pivot_idx, right_idx)
```

Now pivot 8 swaps with 3:

```
After swapping pivot with right_idx:
        [3, 5, 2, 9, 7, 6, 8]
```

Pivot `8` is now at **index 6**.

---

### Step 2: Check pivot position

* `right_idx = 6` vs `position = 2`
* Since `6 > 2`, search **left side**: `start = 0`, `end = 5`

---

### Next Partition:

```
Subarray: [3, 5, 2, 9, 7, 6]
Index:     0  1  2  3  4  5
           ^
         pivot_idx = 0
pivot = 3
left = 1, right = 5
```

Keep moving:

* `array[left] = 5 (> 3)` and `array[right] = 6 (> 3)` → move `right` left
* `array[right] = 7 (> 3)` → move `right` left
* `array[right] = 9 (> 3)` → move `right` left
* `array[right] = 2 (< 3)` → Now: `array[left]=5`, `array[right]=2` → swap them

#### Swap 1:

```
Before: [3, 5, 2, 9, 7, 6]
Swap(1, 2): [3, 2, 5, 9, 7, 6]
```

Now:

```
left = 2, right = 1 → done
swap pivot (index 0) with right (1)
```

#### Swap 2:

```
Swap(0,1): [2, 3, 5, 9, 7, 6, 8]
```

---

### Check pivot position:

* `right_idx = 1` vs `position = 2`
* Since `1 < 2`, search right: `start = 2`, `end = 5`

---

### Next Partition:

Subarray:

```
[5, 9, 7, 6]
Index: 2 3 4 5
        ^
      pivot_idx = 2
pivot = 5
left = 3, right = 5
```

* `array[left]=9 > 5`, `array[right]=6 > 5` → move right to 4
* `array[right]=7 > 5` → move right to 3
* `array[right]=9 > 5` → move right to 2

Now:

```
left = 3, right = 2 → done
swap(pivot_idx=2, right_idx=2) → no actual swap

Array: [2, 3, 5, 9, 7, 6, 8]
```

---

### Final Check:

* `right_idx = 2` == `position = 2` → 🎉 Found the 3rd smallest!

---

### ✅ Final Result:

```
3rd smallest element = 5
```

---

## 📌 Summary in ASCII:

```
Initial:      [8, 5, 2, 9, 7, 6, 3]      pivot=8
Partitioned:  [3, 5, 2, 9, 7, 6, 8]

Search left:  [3, 5, 2, 9, 7, 6]         pivot=3
Partitioned:  [2, 3, 5, 9, 7, 6, 8]

Search right: [5, 9, 7, 6]               pivot=5
Partitioned:  [2, 3, 5, 9, 7, 6, 8]

Final Answer: 5
```

"""
