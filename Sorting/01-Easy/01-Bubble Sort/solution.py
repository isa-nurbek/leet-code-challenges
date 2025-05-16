# Problem Description:

"""
                                             Bubble Sort

Write a function that takes in an array of integers and returns a `sorted` version of that array. Use the `Bubble Sort` algorithm
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
Best: O(n) time | O(1) space - where `n` is the length of the input array.
Average: O(n²) time | O(1) space - where `n` is the length of the input array.
Worst: O(n²) time | O(1) space - where `n` is the length of the input array.
```

"""

# =========================================================================================================================== #

# Solution:


# Best: O(n) time | O(1) space
# Average: O(n²) time | O(1)
# Worst: O(n²) time | O(1) space
def bubble_sort(array):
    # Initialize a flag to track if the array is sorted
    is_sorted = False
    # Initialize a counter to keep track of how many elements have been sorted
    counter = 0

    # Continue looping until the array is sorted
    while not is_sorted:
        # Assume the array is sorted unless we find elements to swap
        is_sorted = True

        # Iterate through the unsorted portion of the array
        # The sorted portion grows by 1 each iteration (hence len(array) - 1 - counter)
        for i in range(len(array) - 1 - counter):
            # If current element is greater than the next element
            if array[i] > array[i + 1]:
                # Swap the elements
                swap(i, i + 1, array)
                # Since we found elements to swap, array wasn't fully sorted
                is_sorted = False

        # Increment the counter as the largest element has bubbled to the end
        counter += 1

    # Return the sorted array
    return array


def swap(i, j, array):
    # Swap two elements in the array
    array[i], array[j] = array[j], array[i]


# Test Cases:

print(bubble_sort([8, 5, 2, 9, 5, 6, 3]))
# Output: [2, 3, 5, 5, 6, 8, 9]

print(bubble_sort([-4, 5, 10, 8, -10, -6, -4, -2, -5, 3, 5, -4, -5, -1, 1, 6, -7]))
# Output: [-10, -7, -6, -5, -5, -4, -4, -4, -2, -1, 1, 3, 5, 5, 6, 8, 10]

print(bubble_sort([2, 1]))
# Output: [1, 2]

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### Time Complexity Analysis:

The time complexity of the Bubble Sort algorithm can be analyzed as follows:

1. **Worst-case time complexity**: 
   - In the worst case (when the array is in reverse order), the algorithm will perform the maximum number of comparisons and swaps.
   - For each pass through the array, the largest unsorted element "bubbles up" to its correct position.
   - The number of comparisons in the first pass is `(n-1)`, then `(n-2)`, and so on, down to `1` in the last pass.
   - Total comparisons = `(n-1) + (n-2) + ... + 1 = n(n-1)/2`, which is `O(n²)`.

2. **Best-case time complexity**:
   - In the best case (when the array is already sorted), the algorithm will still perform `(n-1)` comparisons in the first pass
   but will not perform any swaps.
   - Due to the `is_sorted` flag, the algorithm will terminate after the first pass.
   - Thus, the best-case time complexity is `O(n)`.

3. **Average-case time complexity**:
   - On average, Bubble Sort performs `O(n²)` comparisons and swaps because it typically requires multiple passes through the array.

### Space Complexity Analysis:

1. **Space complexity**:
   - Bubble Sort is an in-place sorting algorithm, meaning it does not require additional space proportional to the input size.
   - The only extra space used is for variables like `is_sorted`, `counter`, `i`, and temporary variables in the `swap` function,
   which are all constant space O(1).
   - Thus, the space complexity is `O(1)`.

### Summary:

- **Time Complexity**:

  - Worst-case: `O(n²)`
  - Best-case: `O(n)` (with `is_sorted` optimization)
  - Average-case: `O(n²)`
  
- **Space Complexity**: `O(1)` (in-place sorting).

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
Let's break down the code step by step. You're looking at an implementation of the Bubble Sort algorithm in Python:

### 🔁 Bubble Sort – How It Works

Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them
if they are in the wrong order. The largest unsorted element "bubbles" up to its correct position on each pass.

---

### 📌 Explanation of Each Part

#### 1. `is_sorted = False`

* We use this variable to check if the array is sorted.
* It starts as `False`, meaning we assume the array is not sorted at the beginning.

#### 2. `counter = 0`

* Tracks how many elements from the end are already sorted.
* With each full pass, the largest element gets to the correct position, so we don’t need to check those again.

---

#### 3. `while not is_sorted:`

* Runs as long as the array is not sorted.

##### Inside the loop:

```
is_sorted = True
```

* Assume it's sorted at the beginning of each pass.
* If any swap is made, we know it's not sorted, and set `is_sorted` to `False` again.

---

#### 4. The `for` loop:

```
for i in range(len(array) - 1 - counter):
```

* Iterates through the unsorted part of the array.
* `len(array) - 1 - counter` ensures we don’t touch the sorted part at the end.

---

#### 5. The `if` condition:

```
if array[i] > array[i + 1]:
    swap(i, i + 1, array)
    is_sorted = False
```

* If the current element is greater than the next, they are in the wrong order.
* Swap them and mark `is_sorted = False` to keep sorting.

---

#### 6. The `swap` function:

```
def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
```

* Swaps the two elements at positions `i` and `j`.

---

#### 7. `counter += 1`

* After each pass, increment `counter` because the largest item is now correctly placed at the end.

---

### ✅ Sample Walkthrough

Take `[8, 5, 2, 9]` as an example:

1st pass: Compare and swap → `[5, 2, 8, 9]`
2nd pass: Compare and swap → `[2, 5, 8, 9]`
3rd pass: Nothing changes → `is_sorted` remains `True`, so we stop.

---

### 🧪 Output Results

```
print(bubble_sort([8, 5, 2, 9, 5, 6, 3]))
# Output: [2, 3, 5, 5, 6, 8, 9]
```

This shows that the algorithm correctly sorts the array in ascending order.

---

### 💡 Summary

* Bubble Sort has average and worst-case time complexity of O(n²), but it's simple and easy to implement.
* Best case is O(n) when the array is already sorted (because of the `is_sorted` optimization).

---

Let's walk through an ASCII visualization of Bubble Sort using this sample input:

```
[8, 5, 2, 9]
```

We’ll show each pass of the algorithm, with swaps highlighted.

---

### 🔁 Pass 1:

Compare each adjacent pair and swap if needed.

Initial array:

```
[8, 5, 2, 9]
```

Compare 8 > 5 → Swap:

```
[5, 8, 2, 9]   ← swapped (8,5)
```

Compare 8 > 2 → Swap:

```
[5, 2, 8, 9]   ← swapped (8,2)
```

Compare 8 < 9 → No swap:

```
[5, 2, 8, 9]
```

✅ Largest element 9 is now in the correct place.

---

### 🔁 Pass 2:

We don’t include the last element (9) because it’s already sorted.

Start:

```
[5, 2, 8, 9]
```

Compare 5 > 2 → Swap:

```
[2, 5, 8, 9]   ← swapped (5,2)
```

Compare 5 < 8 → No swap:

```
[2, 5, 8, 9]
```

✅ Second largest element 8 is now in the correct place.

---

### 🔁 Pass 3:

Only the first two elements need checking.

Compare 2 < 5 → No swap:

```
[2, 5, 8, 9]
```

✅ Everything is in order. No swaps → array is sorted.

---

### ✅ Final Result:

```
[2, 5, 8, 9]
```

"""
