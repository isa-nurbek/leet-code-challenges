# Problem Description:

"""
                                               Three Number Sort

You're given an array of integers and another array of three distinct integers. The first array is guaranteed to only contain
integers that are in the second array, and the second array represents a desired order for the integers in the first array. For
example, a second array of `[x, y, z]` represents a desired order of `[x, x, ..., x, y, y, ..., y, z, z, ..., z]` in the first array.

Write a function that sorts the first array according to the desired order in the second array.

The function should perform this in place (i.e., it should mutate the input array), and it shouldn't use any auxiliary space
(i.e., it should run with constant space: `O(1)` space).

> Note that the desired order won't necessarily be ascending or descending and that the first array won't necessarily contain all
three integers found in the second array—it might only contain one or two.


## Sample Input:
```
array = [1, 0, 0, -1, -1, 0, 1, 1]
order = [0, 1, -1]
```

## Sample Output:
```
[0, 0, 0, 1, 1, 1, -1, -1]
```

## Optimal Time & Space Complexity:
```
O(n) time | O(1) space - where `n` is the length of the array.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n) time | O(1) space
def three_number_sort(array, order):
    # The order array contains the desired order of values: [first_value, second_value, third_value]
    first_value = order[0]
    second_value = order[1]
    # The third_value isn't needed explicitly since it's whatever remains

    # Initialize three pointers:
    # first_idx: boundary of where first_value elements end (starts at 0)
    # second_idx: current element being examined (starts at 0)
    # third_idx: boundary of where third_value elements begin (starts at end of array)
    first_idx, second_idx, third_idx = 0, 0, len(array) - 1

    # Iterate while the current pointer hasn't passed the third_value boundary
    while second_idx <= third_idx:
        value = array[second_idx]

        if value == first_value:
            # If current value belongs in the first group, swap it with the element at first_idx
            array[second_idx], array[first_idx] = array[first_idx], array[second_idx]
            # Move both first and second pointers forward
            first_idx += 1
            second_idx += 1
        elif value == second_value:
            # If current value belongs in the middle group, just move the second pointer forward
            second_idx += 1
        else:
            # If current value belongs in the third group, swap it with the element at third_idx
            array[second_idx], array[third_idx] = array[third_idx], array[second_idx]
            # Move the third pointer backward (we don't move second_idx because the swapped
            # element needs to be examined in the next iteration)
            third_idx -= 1

    return array


# Test Cases:

print(three_number_sort([1, 0, 0, -1, -1, 0, 1, 1], [0, 1, -1]))
# Output: [0, 0, 0, 1, 1, 1, -1, -1]

print(three_number_sort([7, 8, 9, 7, 8, 9, 9, 9, 9, 9, 9, 9], [8, 7, 9]))
# Output: [8, 8, 7, 7, 9, 9, 9, 9, 9, 9, 9, 9]

print(three_number_sort([], [0, 7, 9]))
# Output: []

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### Time Complexity Analysis:

The algorithm processes each element in the array exactly once using the `second_idx` and `third_idx` pointers. The `while`
loop runs until `second_idx` crosses `third_idx`, which means it processes each element in the array at most once. 

- **Comparisons and swaps**: For each element, the algorithm performs a constant amount of work (comparisons and swaps). 
- **Number of operations**: Since there are `n` elements in the array, the total number of operations is proportional to `n`.

Thus, the **time complexity is O(n)**, where `n` is the length of the array.

---

### Space Complexity Analysis:

The algorithm sorts the array in place by swapping elements and using a few extra variables (`first_idx`, `second_idx`,
`third_idx`, `first_value`, `second_value`, `value`). 

- No additional data structures (like extra arrays or hash tables) are used.
- The space used does not grow with the input size.

Thus, the **space complexity is O(1)** (constant space).

---

### Summary:
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)

This is similar to the Dutch National Flag problem, where we partition the array into three sections in a single pass.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
The function `three_number_sort` is designed to sort an array that contains **only three distinct values** in a specific **custom
order** provided by the user. This is a variation of the **Dutch National Flag Problem**, which is commonly solved using a
**three-pointer approach**.

---

### 🔍 Function Definition

```
def three_number_sort(array, order):
```

* `array`: The list of integers to be sorted.
* `order`: A list containing exactly **three unique integers**. It defines the required order of elements in the sorted array.

---

### ⚙️ Variables Initialization

```
first_value = order[0]
second_value = order[1]

first_idx, second_idx, third_idx = 0, 0, len(array) - 1
```

* `first_value`: The first element in `order` – should go to the **beginning** of the array.

* `second_value`: The second element in `order` – should be in the **middle** of the array.

* The third element in `order` is **implicitly** handled as anything that is neither `first_value` nor `second_value`.

* `first_idx`: Index where the next `first_value` should be placed.

* `second_idx`: Current element being inspected.

* `third_idx`: Index where the next third value (i.e., not in first or second position) should go, starting from the end.

---

### 🔁 While Loop – 3-Way Partitioning

```
while second_idx <= third_idx:
    value = array[second_idx]
```

Iterates through the array once, using `second_idx` as the main pointer.

#### ▶️ Case 1: `value == first_value`

```
if value == first_value:
    array[second_idx], array[first_idx] = array[first_idx], array[second_idx]
    first_idx += 1
    second_idx += 1
```

* Swap `value` to the front.
* Move both `first_idx` and `second_idx` forward.

#### ▶️ Case 2: `value == second_value`

```
elif value == second_value:
    second_idx += 1
```

* It is in the correct "middle" group. Just continue.

#### ▶️ Case 3: `value == third_value` (implicitly)

```
else:
    array[second_idx], array[third_idx] = array[third_idx], array[second_idx]
    third_idx -= 1
```

* Swap the current value to the end.
* Do **not** increment `second_idx` yet, since the swapped-in element hasn't been checked.

---

### ✅ Return Sorted Array

```
return array
```

---

### 📊 Example Walkthrough

```
three_number_sort([1, 0, 0, -1, -1, 0, 1, 1], [0, 1, -1])
```

* Goal: Sort so `0`s come first, then `1`s, then `-1`s.
* Algorithm:

  * Moves all `0`s to the front (`first_value`)
  * Leaves all `1`s in the middle (`second_value`)
  * Moves all `-1`s to the end (implicitly `third_value`)
* Result: `[0, 0, 0, 1, 1, 1, -1, -1]`

---

### 🧠 Time and Space Complexity

* **Time Complexity**: `O(n)` — Single pass through the array.
* **Space Complexity**: `O(1)` — In-place sorting.

---

### ✅ Summary

* Efficient one-pass algorithm for sorting arrays with **three distinct values**.
* Uses **three pointers**: beginning (`first_idx`), middle (`second_idx`), and end (`third_idx`).
* Similar to the **Dutch National Flag** algorithm, tailored for a custom order of three values.

---

Let's visualize how the algorithm works step-by-step using ASCII art.

---

### 🎯 Example Input:

```
array = [1, 0, 0, -1, -1, 0, 1, 1]
order = [0, 1, -1]
```

So we want:

* `0` → front
* `1` → middle
* `-1` → end

---

### 📍 Pointer Legend

* `F` → `first_idx`
* `S` → `second_idx`
* `T` → `third_idx`

We'll show array states and the pointer positions at each step.

---

### 🧮 Initial State

```
Array:     [1, 0, 0, -1, -1, 0, 1, 1]
Pointers:   F S               T
Values:     0 0               7
```

---

### 🔁 Step-by-step Process

---

#### Step 1: `value = 1` (second\_value)

No change, just move `S` forward.

```
Array:     [1, 0, 0, -1, -1, 0, 1, 1]
Pointers:   F   S             T
```

---

#### Step 2: `value = 0` (first\_value)

Swap with `F`, move `F` and `S`.

```
Swap index 1 and 0 → [0, 1, 0, -1, -1, 0, 1, 1]
Array:     [0, 1, 0, -1, -1, 0, 1, 1]
Pointers:     F   S           T
```

---

#### Step 3: `value = 0` (first\_value)

Swap with `F`, move both `F`, `S`.

```
Swap index 2 and 1 → [0, 0, 1, -1, -1, 0, 1, 1]
Array:     [0, 0, 1, -1, -1, 0, 1, 1]
Pointers:       F   S         T
```

---

#### Step 4: `value = 1` (second\_value)

Just move `S`.

```
Array:     [0, 0, 1, -1, -1, 0, 1, 1]
Pointers:       F     S       T
```

---

#### Step 5: `value = -1` (third\_value)

Swap with `T`, move `T`.

```
Swap index 3 and 7 → [0, 0, 1, 1, -1, 0, 1, -1]
Array:     [0, 0, 1, 1, -1, 0, 1, -1]
Pointers:       F     S     T
```

Still `value = 1`, so move `S`.

---

#### Step 6: `value = -1` (third\_value)

Swap with `T`, move `T`.

```
Swap index 4 and 6 → [0, 0, 1, 1, 1, 0, -1, -1]
Array:     [0, 0, 1, 1, 1, 0, -1, -1]
Pointers:       F       S   T
```

---

#### Step 7: `value = 0` (first\_value)

Swap with `F`.

```
Swap index 5 and 2 → [0, 0, 0, 1, 1, 1, -1, -1]
Array:     [0, 0, 0, 1, 1, 1, -1, -1]
Pointers:           F   S T
```

Now `S > T`, so we stop.

---

### ✅ Final Sorted Array

```
[0, 0, 0, 1, 1, 1, -1, -1]
```

"""
