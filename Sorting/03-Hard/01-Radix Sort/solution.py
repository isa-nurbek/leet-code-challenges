# Problem Description:

"""
                                                Radix Sort

Write a function that takes in an array of `non-negative` integers and returns a `sorted` version of that array. Use the `Radix
Sort` algorithm to sort the array.


## Sample Input:
```
array = [8762, 654, 3008, 345, 87, 65, 234, 12, 2]
```

## Sample Output:
```
[2, 12, 65, 87, 234, 345, 654, 3008, 8762]
```

## Optimal Time & Space Complexity:
```
O(d * (n + b)) time | O(n + b) space - where `n` is the length of the input array, `d` is the max number of digits,
and `b` is the base of the numbering system used.
```

"""

# =========================================================================================================================== #

# Solution:


# O(d * (n + b)) time | O(n + b) space
def radix_sort(arr):
    """Sorts an array of integers using the radix sort algorithm."""
    # Handle empty array case
    if not arr:
        return arr

    # Find the maximum number to know the number of digits
    max_num = max(arr)

    # Start with the least significant digit (rightmost)
    exp = 1
    while max_num // exp > 0:
        # Sort the array based on the current digit (exp place)
        counting_sort(arr, exp)
        # Move to the next significant digit (left)
        exp *= 10

    return arr


def counting_sort(arr, exp):
    """Performs counting sort on the given array based on a specific digit place.

    Args:
        arr: The array to be sorted
        exp: The current digit place (1 for units, 10 for tens, etc.)
    """
    n = len(arr)
    # Initialize output array that will have sorted numbers
    output = [0] * n
    # Initialize count array to store count of occurrences for each digit (0-9)
    count = [0] * 10

    # Store count of occurrences for each digit in count[]
    for i in range(n):
        # Extract the digit at the current exp place
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Change count[i] so it contains the actual position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array in sorted order
    i = n - 1  # Start from the end to maintain stability
    while i >= 0:
        # Get the digit at current exp place
        index = (arr[i] // exp) % 10
        # Place the element at its correct position in output[]
        output[count[index] - 1] = arr[i]
        # Decrease the count for this digit
        count[index] -= 1
        # Move to the previous element
        i -= 1

    # Copy the sorted output back to the original array
    for i in range(n):
        arr[i] = output[i]


# Test Cases:

print(radix_sort([8762, 654, 3008, 345, 87, 65, 234, 12, 2]))
# Output: [2, 12, 65, 87, 234, 345, 654, 3008, 8762]

print(radix_sort([111, 11, 11, 1, 0]))
# Output: [0, 1, 11, 11, 111]

print(radix_sort([4, 44, 444, 888, 88, 33, 3, 22, 2222, 1111, 1234]))
# Output: [3, 4, 22, 33, 44, 88, 444, 888, 1111, 1234, 2222]

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### **Radix Sort Analysis**

#### **Time Complexity**

- **Overall Time Complexity**: **O(d * (n + k))**
  - **d**: Number of digits in the largest number (`max_num`).
  - **n**: Number of elements in the array.
  - **k**: Base of the numbering system (here, base 10 ⇒ `k = 10`).

**Breakdown:**
1. **Finding `max_num`**: `O(n)` (one pass over the array).
2. **Loop over each digit (`d` times)**:
   - Each iteration calls **Counting Sort**, which runs in `O(n + k)` time.
   - Since `k = 10` (constant), Counting Sort is `O(n)` per digit.
3. **Total time**: `O(d * n)` (since `k` is constant).

**Best/Worst/Average Case**:  

Radix Sort is **non-comparative**, so its time complexity remains **O(d * n)** regardless of input distribution.

---

#### **Space Complexity**

- **Overall Space Complexity**: **O(n + k)**
  - **Output array**: `O(n)` (to store sorted elements per digit).
  - **Count array**: `O(k)` (here, `k = 10` ⇒ constant `O(1)`).
  - **Total space**: `O(n)` (since `k` is negligible).

**Notes**:
- **In-place?** No, Radix Sort uses extra space for `output` and `count` arrays.
- **Stable?** Yes, because Counting Sort is stable (preserves order of equal keys).

---

### **Key Takeaways**
| Complexity     | Value      |
|----------------|------------|
| **Time**       | O(d * n)   |
| **Space**      | O(n)       |
| **Stable?**    | Yes        |
| **In-place?**  | No         |

- **Efficiency**: Excellent for integers with a fixed number of digits (e.g., sorting 32-bit integers where `d = 10`).
- **Limitation**: Not ideal for floating-point numbers or variable-length strings (unless padded).

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
**Radix Sort**, a non-comparative, digit-by-digit sorting algorithm ideal for sorting integers.

Let’s walk through it in detail.

---

## 🔍 Overview

**Radix Sort** processes integers digit-by-digit starting from the **least significant digit (LSD)** to the **most significant
digit (MSD)**. It repeatedly applies a **stable sort** (like **Counting Sort**) on each digit position.

---

## 🔢 High-Level Idea

For example, consider the list `[345, 87, 65]`. We sort:

* first by **units digit**: 5 (345), 7 (87), 5 (65)
* then by **tens digit**: 4 (345), 8 (87), 6 (65)
* then by **hundreds digit**: 3 (345), 0 (87), 0 (65)

This step-by-step sorting yields a fully sorted list.

---

## 🧠 Code Explanation

### 1. `radix_sort(arr)`

```
def radix_sort(arr):
    if not arr:
        return arr
```

* If the list is empty, return it as is.

```
    max_num = max(arr)
```

* Find the **maximum number** to determine how many digit positions we need to sort.

```
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
```

* `exp` starts at 1 (units place), then 10 (tens), 100 (hundreds), etc.
* We keep sorting the array with increasing digit position until all digits of the largest number are covered.

---

### 2. `counting_sort(arr, exp)`

This is a helper to sort numbers based on the digit at the current `exp` position.

```
    n = len(arr)
    output = [0] * n
    count = [0] * 10
```

* `output`: a temporary list for sorted values.
* `count`: counts the occurrences of digits (0–9).

#### 2.1 Count digit frequencies at `exp` position:

```
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
```

* Extract the digit at position `exp` using `(arr[i] // exp) % 10`.
* Count how many times each digit appears.

#### 2.2 Accumulate counts (for stable sorting):

```
    for i in range(1, 10):
        count[i] += count[i - 1]
```

* Transforms count array into cumulative positions — tells us where to place digits.

#### 2.3 Build `output` array (in reverse for stability):

```
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1
```

* Place each element in its correct sorted position in `output` using the cumulative count.
* We iterate from right to left to maintain **stability** (important for Radix Sort).

#### 2.4 Copy sorted values back to original array:

```
    for i in range(n):
        arr[i] = output[i]
```

* Copies the sorted result for this digit back to the original array.

---

## ✅ Test Cases Explained

### 1.

```
print(radix_sort([8762, 654, 3008, 345, 87, 65, 234, 12, 2]))
```

* Multi-digit numbers, includes all digit lengths.
* **Output**: `[2, 12, 65, 87, 234, 345, 654, 3008, 8762]` — correctly sorted.

### 2.

```
print(radix_sort([111, 11, 11, 1, 0]))
```

* Handles duplicates and 0.
* **Output**: `[0, 1, 11, 11, 111]` — correct.

### 3.

```
print(radix_sort([4, 44, 444, 888, 88, 33, 3, 22, 2222, 1111, 1234]))
```

* Mixed length numbers with similar digits.
* **Output**: `[3, 4, 22, 33, 44, 88, 444, 888, 1111, 1234, 2222]`

---

## 📈 Time and Space Complexity

### ⏱ Time Complexity:

* **Best / Avg / Worst**: `O(d * (n + k))`

  * `n`: number of elements
  * `d`: number of digits in the max number
  * `k`: range of digit values (0–9, so `k = 10`)
* Since `k = 10`, this simplifies to `O(d * n)`

### 🧠 Space Complexity:

* `O(n + k)` for `output` and `count` arrays

---

## ⚠ Limitations

* Works only with **non-negative integers**.
* Needs adaptation to handle **negative numbers** or **floating-point numbers**.

---

Let's visualize the **Radix Sort process** step-by-step on the input:

```
[8762, 654, 3008, 345, 87, 65, 234, 12, 2]
```

---

### Step 1: Sort by **units digit** (exp = 1)

Look at the units digit of each number:

| Number | Units digit |
| ------ | ----------- |
| 8762   | 2           |
| 654    | 4           |
| 3008   | 8           |
| 345    | 5           |
| 87     | 7           |
| 65     | 5           |
| 234    | 4           |
| 12     | 2           |
| 2      | 2           |

**Buckets (0 to 9):**

```
0: []
1: []
2: [8762, 12, 2]
3: []
4: [654, 234]
5: [345, 65]
6: []
7: [87]
8: [3008]
9: []
```

Concatenate buckets:

```
[8762, 12, 2, 654, 234, 345, 65, 87, 3008]
```

---

### Step 2: Sort by **tens digit** (exp = 10)

Look at the tens digit of each number in the updated array:

| Number | Tens digit |
| ------ | ---------- |
| 8762   | 6          |
| 12     | 1          |
| 2      | 0          |
| 654    | 5          |
| 234    | 3          |
| 345    | 4          |
| 65     | 6          |
| 87     | 8          |
| 3008   | 0          |

**Buckets:**

```
0: [2, 3008]
1: [12]
2: []
3: [234]
4: [345]
5: [654]
6: [8762, 65]
7: []
8: [87]
9: []
```

Concatenate buckets:

```
[2, 3008, 12, 234, 345, 654, 8762, 65, 87]
```

---

### Step 3: Sort by **hundreds digit** (exp = 100)

Look at the hundreds digit:

| Number | Hundreds digit |
| ------ | -------------- |
| 2      | 0              |
| 3008   | 0              |
| 12     | 0              |
| 234    | 2              |
| 345    | 3              |
| 654    | 6              |
| 8762   | 7              |
| 65     | 0              |
| 87     | 0              |

**Buckets:**

```
0: [2, 3008, 12, 65, 87]
1: []
2: [234]
3: [345]
4: []
5: []
6: [654]
7: [8762]
8: []
9: []
```

Concatenate buckets:

```
[2, 3008, 12, 65, 87, 234, 345, 654, 8762]
```

---

### Step 4: Sort by **thousands digit** (exp = 1000)

Look at the thousands digit:

| Number | Thousands digit |
| ------ | --------------- |
| 2      | 0               |
| 3008   | 3               |
| 12     | 0               |
| 65     | 0               |
| 87     | 0               |
| 234    | 0               |
| 345    | 0               |
| 654    | 0               |
| 8762   | 8               |

**Buckets:**

```
0: [2, 12, 65, 87, 234, 345, 654]
1: []
2: []
3: [3008]
4: []
5: []
6: []
7: []
8: [8762]
9: []
```

Concatenate buckets:

```
[2, 12, 65, 87, 234, 345, 654, 3008, 8762]
```

---

## Final Sorted Array:

```
[2, 12, 65, 87, 234, 345, 654, 3008, 8762]
```

---

### Summary Table:

```
Input:         [8762, 654, 3008, 345, 87, 65, 234, 12, 2]

After exp=1:   [8762, 12, 2, 654, 234, 345, 65, 87, 3008]
After exp=10:  [2, 3008, 12, 234, 345, 654, 8762, 65, 87]
After exp=100: [2, 3008, 12, 65, 87, 234, 345, 654, 8762]
After exp=1000:[2, 12, 65, 87, 234, 345, 654, 3008, 8762]

Sorted:       [2, 12, 65, 87, 234, 345, 654, 3008, 8762]
```

"""
