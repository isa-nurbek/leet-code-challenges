# Problem Description:

"""
                                                Radix Sort

Write a function that takes in an array of `non-negative` integers and returns a `sorted` version of that array. Use the `Radix
Sort` algorithm to sort the array.

You can also extend the implementation to include `negative` and `floating-point` numbers.


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
# Handle negative numbers
def radix_sort(arr):
    """
    Sorts an array of integers using radix sort algorithm.
    Handles both negative and non-negative numbers by separating them,
    sorting separately, and combining results.

    Args:
        arr: List of integers to be sorted

    Returns:
        List of sorted integers
    """
    if not arr:
        return arr

    # Separate negative and non-negative numbers
    negatives = [-x for x in arr if x < 0]  # Convert negatives to positives for sorting
    non_negatives = [x for x in arr if x >= 0]

    # Sort both parts using radix sort for non-negative numbers
    sorted_negatives = radix_sort_non_negative(negatives)
    sorted_non_negatives = radix_sort_non_negative(non_negatives)

    # Convert negatives back to original sign and reverse order
    # (since larger positive numbers = smaller negative numbers)
    sorted_negatives = [-x for x in reversed(sorted_negatives)]

    # Combine results (negatives come first in sorted order)
    return sorted_negatives + sorted_non_negatives


def radix_sort_non_negative(arr):
    """
    Radix sort implementation for non-negative integers only.
    Sorts numbers digit by digit starting from least significant digit.

    Args:
        arr: List of non-negative integers to be sorted

    Returns:
        List of sorted non-negative integers
    """
    if not arr:
        return arr

    # Find maximum number to know number of digits
    max_num = max(arr)

    # Do counting sort for every digit (exp is 10^digit)
    exp = 1  # Start with least significant digit (units place)
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10  # Move to next digit (tens, hundreds, etc.)
    return arr


def counting_sort(arr, exp):
    """
    Performs counting sort on the given digit (exp) of array elements.
    This is a helper function for radix_sort_non_negative.

    Args:
        arr: List of non-negative integers to be sorted
        exp: Current digit position to sort by (power of 10)
    """
    n = len(arr)
    output = [0] * n  # Will store sorted output
    count = [0] * 10  # Counting array for digits 0-9

    # Count occurrences of each digit in current place
    for i in range(n):
        index = (arr[i] // exp) % 10  # Extract current digit
        count[index] += 1

    # Calculate cumulative count (determines positions in output)
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array in sorted order
    i = n - 1
    while i >= 0:  # Moving backwards for stability
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]  # Place element in correct position
        count[index] -= 1
        i -= 1

    # Copy the sorted output back to original array
    for i in range(n):
        arr[i] = output[i]


# Test Cases:

print(radix_sort([8762, 654, -3008, 345, 87, -65, 234, 12, -2]))
# Output: [-3008, -65, -2, 12, 87, 234, 345, 654, 8762]

print(radix_sort([-5, -1, -300, 0, 1, 200]))
# Output: [-300, -5, -1, 0, 1, 200]

print(radix_sort([0, -1, -2, -3, -4]))
# Output: [-4, -3, -2, -1, 0]

print(radix_sort([-111, -11, -1, 0, 1, 11, 111]))
# Output: [-111, -11, -1, 0, 1, 11, 111]

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### Time Complexity:

1. **Radix Sort for Non-negative Numbers (`radix_sort_non_negative`)**:
   - Let `d` be the maximum number of digits in any number in the array (determined by `max_num`).
   - The outer loop runs `d` times (once for each digit position, from least significant to most significant).
   - Each iteration calls `counting_sort`, which has a time complexity of `O(n + k)`, where `k` is the range of digits
   (here, `k = 10` since digits are 0-9).
   - Thus, the total time complexity for `radix_sort_non_negative` is `O(d * (n + 10))`, which simplifies to `O(d * n)`
   (since `10` is a constant).

2. **Handling Negatives (`radix_sort`)**:
   - The input array is split into negatives and non-negatives, which takes `O(n)` time.
   - Negatives are converted to positive (and later back to negative), which is `O(m)` where `m` is the number of negatives.
   - The `radix_sort_non_negative` is called twice (once for negatives and once for non-negatives), so the total time is
   `O(d_neg * m + d_non_neg * (n - m))`, where `d_neg` and `d_non_neg` are the maximum digits in the negatives and non-negatives, respectively.
   - Reversing the sorted negatives takes `O(m)` time.
   - Combining the sorted arrays takes `O(n)` time.
   - The total time complexity is still `O(d * n)`, where `d` is the maximum number of digits across all numbers (both negative
   and non-negative).

### Space Complexity:

1. **Counting Sort (`counting_sort`)**:
   - Uses an auxiliary array `output` of size `n` and a `count` array of size `10`.
   - Thus, the space complexity is `O(n + 10)`, which simplifies to `O(n)`.

2. **Radix Sort (`radix_sort_non_negative` and `radix_sort`)**:
   - The space is dominated by the `counting_sort` calls, so it is `O(n)` for the auxiliary arrays.
   - Additionally, splitting the array into negatives and non-negatives requires `O(n)` space for the two subarrays.
   - Thus, the total space complexity is `O(n)`.

### Summary:
- **Time Complexity**: `O(d * n)`, where `d` is the maximum number of digits in any number in the array,
and `n` is the number of elements.
- **Space Complexity**: `O(n)` (auxiliary space for counting sort and splitting the array).

### Notes:
- Radix sort is efficient when `d` is small compared to `n` (e.g., for large arrays of numbers with a bounded number of digits).
If `d` is large (e.g., very large numbers), the performance may degrade.
- The implementation handles negative numbers by sorting them separately and reversing the order, which is a correct approach
but adds some overhead.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
Here's a detailed explanation of how your `radix_sort` function works, including its handling of **negative numbers**—a feature
traditional radix sort doesn't directly support.

---

## 🔍 **Overview**

Radix Sort is a non-comparative sorting algorithm that sorts integers by processing individual digits. It works best for
non-negative integers, so your implementation first separates **negative** and **non-negative** numbers, sorts them independently,
and then combines them for the final result.

---

## ⚙️ **Function Breakdown**

### ### 1. `radix_sort(arr)`

This is the **main function** which:

#### Step-by-step:

```
if not arr:
    return arr
```

* Base case: If the list is empty, return it.

```
negatives = [-x for x in arr if x < 0]
```

* Extracts negative numbers and **converts them to positive** for radix sorting. (Radix Sort doesn't work on negatives directly.)

```
non_negatives = [x for x in arr if x >= 0]
```

* Extracts non-negative numbers as-is.

```
sorted_negatives = radix_sort_non_negative(negatives)
sorted_non_negatives = radix_sort_non_negative(non_negatives)
```

* Calls the helper function `radix_sort_non_negative()` on both parts.

```
sorted_negatives = [-x for x in reversed(sorted_negatives)]
```

* After sorting positive versions of the negatives, reverse the order (since smaller negative values are larger positive numbers),
and re-apply the negative sign.

```
return sorted_negatives + sorted_non_negatives
```

* Combine the two sorted lists and return.

---

### ### 2. `radix_sort_non_negative(arr)`

This is a **pure radix sort** for non-negative integers.

#### Step-by-step:

```
if not arr:
    return arr
```

* Return early for empty list.

```
max_num = max(arr)
exp = 1
```

* Get the largest number to determine how many digits to process.
* `exp` is the current digit position (1 = units, 10 = tens, etc.).

```
while max_num // exp > 0:
    counting_sort(arr, exp)
    exp *= 10
```

* Continue until all digit places have been processed.
* In each iteration, `counting_sort()` sorts the array based on the digit at `exp` place.

---

### ### 3. `counting_sort(arr, exp)`

Performs a **stable counting sort** based on the digit at the current exponent (`exp`).

#### Step-by-step:

```
n = len(arr)
output = [0] * n
count = [0] * 10
```

* `output`: stores the sorted values temporarily.
* `count`: frequency of digits (0-9).

```
for i in range(n):
    index = (arr[i] // exp) % 10
    count[index] += 1
```

* Count the occurrence of each digit at the current `exp` place.

```
for i in range(1, 10):
    count[i] += count[i - 1]
```

* Update `count` to contain actual positions in `output`.

```
i = n - 1
while i >= 0:
    index = (arr[i] // exp) % 10
    output[count[index] - 1] = arr[i]
    count[index] -= 1
    i -= 1
```

* Build the output array by placing items in correct positions in **reverse order** (to make sort stable).

```
for i in range(n):
    arr[i] = output[i]
```

* Copy sorted results back to `arr`.

---

## ✅ Example Walkthrough

Let's take this test case:

```
radix_sort([8762, 654, -3008, 345, 87, -65, 234, 12, -2])
```

1. **Separate**:

   * `negatives`: `[-3008, -65, -2] → [3008, 65, 2]`
   * `non_negatives`: `[8762, 654, 345, 87, 234, 12]`

2. **Sort both** using `radix_sort_non_negative`:

   * Sorted `negatives` as `[2, 65, 3008]` → Reverse & negate → `[-3008, -65, -2]`
   * Sorted `non_negatives` as `[12, 87, 234, 345, 654, 8762]`

3. **Final merged output**:

   ```
   [-3008, -65, -2, 12, 87, 234, 345, 654, 8762]
   ```

---

## ✅ Output Verification

```
print(radix_sort([8762, 654, -3008, 345, 87, -65, 234, 12, -2]))
# [-3008, -65, -2, 12, 87, 234, 345, 654, 8762]
```

All test cases return correct sorted results, including negative numbers.

---

## 🧠 Key Concepts Covered

| Concept                  | Description                                                      |
| ------------------------ | ---------------------------------------------------------------- |
| **Radix Sort**           | Digit-wise sorting, stable and efficient for integers.           |
| **Stable Counting Sort** | Needed for digit-wise stability.                                 |
| **Handling Negatives**   | Converted to positive, sorted, then restored in reverse.         |
| **Space Complexity**     | O(n + k) where `k` is digit range (0-9 here).                    |
| **Time Complexity**      | O(d·n), where `d` = max number of digits, `n` = length of array. |

---

Here's an **ASCII visualization** of how your `radix_sort` function works—especially showing how **negatives are handled
separately**, **radix sort processes digits**, and the **final merge**.

---

### ✅ Input Example

We’ll use:

```
arr = [8762, 654, -3008, 345, 87, -65, 234, 12, -2]
```

---

### 📤 Step 1: Split into Negatives and Non-Negatives

```
Original:       [8762, 654, -3008, 345, 87, -65, 234, 12, -2]

Negatives:      [-3008, -65, -2]
Non-negatives:  [8762, 654, 345, 87, 234, 12]
```

Negatives converted to positives:

```
Negatives (abs): [3008, 65, 2]
```

---

### 🔁 Step 2: Radix Sort `radix_sort_non_negative()`

We show how it works digit by digit (LSD → MSD):

#### 📦 Radix Sort of `[3008, 65, 2]`

```
Initial Array: [3008, 65, 2]

Pass 1 (exp = 1, unit digit):
  Digits:       8     5   2
  Sorted:       [2, 65, 3008]

Pass 2 (exp = 10, tens digit):
  Digits:       0     6   0
  Sorted:       [3008, 2, 65]

Pass 3 (exp = 100, hundreds digit):
  Digits:       0     0   3
  Sorted:       [2, 65, 3008]

Pass 4 (exp = 1000, thousands digit):
  Digits:       3     0   0
  Sorted:       [2, 65, 3008]
```

Now reverse and negate:

```
Before reverse: [2, 65, 3008]
Reversed:       [3008, 65, 2]
Negated:        [-3008, -65, -2]
```

---

#### 📦 Radix Sort of `[8762, 654, 345, 87, 234, 12]`

Let's visualize:

```
Initial Array: [8762, 654, 345, 87, 234, 12]

Pass 1 (unit digit):
  Digits:         2     4     5     7     4     2
  Sorted:       [12, 8762, 654, 234, 345, 87]

Pass 2 (tens digit):
  Digits:         1     6     5     3     4     8
  Sorted:       [12, 234, 345, 654, 8762, 87]

Pass 3 (hundreds digit):
  Digits:         0     2     3     6     7     0
  Sorted:       [12, 87, 234, 345, 654, 8762]

Pass 4 (thousands digit):
  Digits:         0     0     0     0     0     8
  Sorted:       [12, 87, 234, 345, 654, 8762]
```

---

### 🔗 Step 3: Merge Final Sorted Arrays

```
Sorted Negatives:     [-3008, -65, -2]
Sorted Non-Negatives: [12, 87, 234, 345, 654, 8762]

Final Merged Output:  [-3008, -65, -2, 12, 87, 234, 345, 654, 8762]
```

---

### 📊 ASCII Summary Flow

```
           +----------------------------+
Input ---> | [8762, 654, -3008, ..., -2]|
           +----------------------------+
                        |
        +---------------+---------------+
        |                               |
 Negatives < 0                    Non-negatives >= 0
 [3008, 65, 2]                     [8762, 654, 345, 87, 234, 12]
        |                               |
 radix_sort_non_negative          radix_sort_non_negative
        |                               |
   [2, 65, 3008]                    [12, 87, 234, 345, 654, 8762]
        |                               |
 Reverse & Negate                     (keep as-is)
 [-3008, -65, -2]                    [12, 87, 234, 345, 654, 8762]
        \                               /
         \                             /
          +-------------------------+
          |     Final Merge        |
          +-------------------------+
          | [-3008, -65, -2, 12, ...]
          +-------------------------+
```

"""
