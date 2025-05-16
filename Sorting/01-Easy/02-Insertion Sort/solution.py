# Problem Description:

"""
                                             Insertion Sort

Write a function that takes in an array of integers and returns a `sorted` version of that array. Use the `Insertion Sort` algorithm
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
def insertion_sort(array):
    """
    Sorts an array in ascending order using the Insertion Sort algorithm.

    Insertion Sort works by building a sorted portion of the array one element at a time.
    It takes each element from the unsorted portion and inserts it into its correct position
    in the sorted portion.

    Args:
        array: The list to be sorted

    Returns:
        The sorted list in ascending order
    """
    # Start from the second element (index 1) since the first element is trivially sorted
    for i in range(1, len(array)):
        j = i  # j is the current index of the element we're inserting

        # While we haven't reached the start of the array and the current element
        # is smaller than its left neighbor
        while j > 0 and array[j] < array[j - 1]:
            # Swap the current element with its left neighbor
            swap(j, j - 1, array)
            # Move left one position to check the next pair
            j -= 1

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

print(insertion_sort([8, 5, 2, 9, 5, 6, 3]))
# Output: [2, 3, 5, 5, 6, 8, 9]

print(insertion_sort([-4, 5, 10, 8, -10, -6, -4, -2, -5, 3, 5, -4, -5, -1, 1, 6, -7]))
# Output: [-10, -7, -6, -5, -5, -4, -4, -4, -2, -1, 1, 3, 5, 5, 6, 8, 10]

print(insertion_sort([2, 1]))
# Output: [1, 2]

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### Time Complexity:

1. **Best Case**: When the array is already sorted, the inner `while` loop never executes (since `array[j] < array[j-1]` will
always be false). This results in only the outer loop running, giving us a time complexity of **O(n)**.

2. **Worst Case**: When the array is sorted in reverse order, the inner `while` loop executes maximally. For each element at index
`i`, we need to swap it all the way to the beginning of the array. This results in:
   - 1 swap for the 2nd element,
   - 2 swaps for the 3rd element,
   - ...
   - (n-1) swaps for the nth element.
   The total number of swaps is `1 + 2 + ... + (n-1) = n(n-1)/2`, which is **O(n²)**.

3. **Average Case**: On average, insertion sort also requires **O(n²)** time because, for randomly ordered arrays, each element
may need to be moved about halfway back through the already-sorted portion.

### Space Complexity:

- The algorithm sorts the array **in-place**, meaning it only uses a constant amount of additional space (for variables like `i`,
`j`, and temporary values during swapping). Thus, the space complexity is **O(1)** (constant space).

### Summary:

- **Time Complexity**:

  - Best Case: O(n) (already sorted)
  - Worst Case: O(n²) (reverse sorted)
  - Average Case: O(n²)
  
- **Space Complexity**: O(1) (in-place sorting).

This makes insertion sort efficient for small or nearly sorted datasets but inefficient for large, randomly ordered datasets.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
Let's go step by step to understand how this **Insertion Sort** algorithm works, including both the logic and each part of the code.

---

## ✅ Insertion Sort: Concept

**Insertion Sort** is a simple sorting algorithm that builds the final sorted array one element at a time.

### How It Works:

* Imagine sorting playing cards in your hand.
* You take one card at a time and insert it into its correct position among the already sorted cards.
* The same logic is applied here: you divide the array into a sorted and an unsorted part. Initially, the sorted part has just
the first element.

---

## 🔍 Code Breakdown

### Main Function: `insertion_sort(array)`

```
def insertion_sort(array):
    for i in range(1, len(array)):
        j = i

        while j > 0 and array[j] < array[j - 1]:
            swap(j, j - 1, array)
            j -= 1

    return array
```

### Step-by-Step Explanation:

1. **Start at index 1** (not 0):

   ```
   for i in range(1, len(array)):
   ```

   * Because a single-element subarray (`array[0]`) is already sorted.
   * You’ll insert `array[i]` into the correct position in the sorted part `array[0..i-1]`.

2. **Inner while loop**:

   ```
   while j > 0 and array[j] < array[j - 1]:
   ```

   * Move left while the current element (`array[j]`) is smaller than the one before it (`array[j-1]`).
   * Keep swapping until the correct position is found or `j` becomes 0.

3. **Swap elements**:

   ```
   swap(j, j - 1, array)
   ```

   * This helper function swaps the elements at positions `j` and `j - 1`.

4. **Decrement j**:

   ```
   j -= 1
   ```

   * Move left in the array.

5. **Return the sorted array**:

   ```
   return array
   ```

---

### Helper Function: `swap(i, j, array)`

```
def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
```

* A simple way to exchange two elements in the list using tuple unpacking.

---

## 🧪 Test Cases:

### 1. `[8, 5, 2, 9, 5, 6, 3]`

Sorted: `[2, 3, 5, 5, 6, 8, 9]`

### 2. `[-4, 5, 10, 8, -10, -6, -4, -2, -5, 3, 5, -4, -5, -1, 1, 6, -7]`

Sorted: `[-10, -7, -6, -5, -5, -4, -4, -4, -2, -1, 1, 3, 5, 5, 6, 8, 10]`

### 3. `[2, 1]`

Sorted: `[1, 2]`

---

## ✅ Time and Space Complexity

* **Time Complexity**:

  * Worst-case: `O(n^2)` (e.g., array is in reverse order)
  * Best-case: `O(n)` (already sorted)
  * Average: `O(n^2)`

* **Space Complexity**: `O(1)`

  * It’s an in-place sort (no extra memory used except a few variables).

---

## 🔚 Summary

* Insertion sort is **simple**, **easy to implement**, and efficient for **small datasets**.
* It becomes inefficient on large lists compared to more advanced algorithms like **merge sort** or **quick sort**.
* This code version is clean, readable, and uses a helper function (`swap`) to improve clarity.

---

Let’s visualize how **Insertion Sort** works step by step using an ASCII-style explanation for this array:

```
[8, 5, 2, 9, 5, 6, 3]
```

We will show:

* The **current element** being inserted.
* The **sorted portion** of the array.
* The **swapping** as it happens.

---

### Initial Array:

```
[8, 5, 2, 9, 5, 6, 3]
```

---

### Step 1: i = 1, current = 5

Compare and swap with 8.

```
[8, 5, 2, 9, 5, 6, 3]
 ^  ^
 j  j-1 => 5 < 8 → swap

[5, 8, 2, 9, 5, 6, 3]
       ↑ Sorted: [5, 8]
```

---

### Step 2: i = 2, current = 2

Compare with 8, then 5.

```
[5, 8, 2, 9, 5, 6, 3]
       ^  ^
       j  j-1 => 2 < 8 → swap

[5, 2, 8, 9, 5, 6, 3]
    ^  ^
    j  j-1 => 2 < 5 → swap

[2, 5, 8, 9, 5, 6, 3]
             ↑ Sorted: [2, 5, 8]
```

---

### Step 3: i = 3, current = 9

9 is greater than 8, no swap needed.

```
[2, 5, 8, 9, 5, 6, 3]
                 ↑ Sorted: [2, 5, 8, 9]
```

---

### Step 4: i = 4, current = 5

Compare with 9, then 8, then 5 → stop

```
[2, 5, 8, 9, 5, 6, 3]
                ^  ^ => 5 < 9 → swap

[2, 5, 8, 5, 9, 6, 3]
             ^  ^ => 5 < 8 → swap

[2, 5, 5, 8, 9, 6, 3]
          ^  ^ => 5 == 5 → stop
                     ↑ Sorted: [2, 5, 5, 8, 9]
```

---

### Step 5: i = 5, current = 6

Compare with 9, then 8 → stop at 5

```
[2, 5, 5, 8, 9, 6, 3]
                   ^  ^ => 6 < 9 → swap

[2, 5, 5, 8, 6, 9, 3]
              ^  ^ => 6 < 8 → swap

[2, 5, 5, 6, 8, 9, 3]
         ↑ Sorted: [2, 5, 5, 6, 8, 9]
```

---

### Step 6: i = 6, current = 3

Compare with 9, 8, 6, 5, 5, 2

```
[2, 5, 5, 6, 8, 9, 3]
                      ^  ^ => 3 < 9 → swap

[2, 5, 5, 6, 8, 3, 9]
                 ^  ^ => 3 < 8 → swap

[2, 5, 5, 6, 3, 8, 9]
              ^  ^ => 3 < 6 → swap

[2, 5, 5, 3, 6, 8, 9]
           ^  ^ => 3 < 5 → swap

[2, 5, 3, 5, 6, 8, 9]
        ^  ^ => 3 < 5 → swap

[2, 3, 5, 5, 6, 8, 9]
     ↑ Final Sorted Array
```

---

### ✅ Final Sorted Array:

```
[2, 3, 5, 5, 6, 8, 9]
```

"""
