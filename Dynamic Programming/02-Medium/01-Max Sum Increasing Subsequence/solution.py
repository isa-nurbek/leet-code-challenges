# Problem Description:

"""
                                               Max Sum Increasing Subsequence

Write a function that takes in a `non-empty` array of integers and returns the greatest sum that can be generated from a
strictly-increasing subsequence in the array as well as an array of the numbers in that subsequence.

A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array but that are in the same order as they
appear in the array. For instance, the numbers `[1, 3, 4]` form a subsequence of the array `[1, 2, 3, 4]`, and so do the numbers
`[2, 4]`.

> Note that a single number in an array and the array itself are both valid subsequences of the array.

You can assume that there will only be one increasing subsequence with the greatest sum.


## Sample Input:
```
array = [10, 70, 20, 30, 50, 11, 30]
```

## Sample Output:
```
[110, [10, 20, 30, 50]]

// The subsequence [10, 20, 30, 50] is strictly increasing and yields the greatest sum: 110.
```

## Optimal Time & Space Complexity:
```
O(n²) time | O(n) space - where `n` is the length of the input array.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n²) time | O(n) space
def max_sum_increasing_subsequence(array):
    """
    Finds the maximum sum increasing subsequence in the given array.
    An increasing subsequence is a sequence of elements where each element is greater than the previous.
    Among all such subsequences, this function returns the one with the maximum sum.

    Args:
        array: List of numbers to process

    Returns:
        A list where first element is the maximum sum, and second element is the subsequence as a list
    """

    # Initialize sequences array to keep track of previous indices
    # sequences[i] stores the index of the previous element in the optimal subsequence ending at i
    sequences = [None for x in array]

    # Initialize sums array to store maximum sums up to each index
    # sums[i] stores the maximum sum of increasing subsequence ending at array[i]
    sums = [num for num in array]  # Start with each element itself as base case

    max_sum_idx = 0  # Tracks index of maximum sum found so far

    for i in range(len(array)):
        current_num = array[i]

        # Compare with all previous elements to find increasing subsequences
        for j in range(0, i):
            other_num = array[j]

            # If previous element is smaller and including it gives better sum
            if other_num < current_num and sums[j] + current_num >= sums[i]:
                sums[i] = sums[j] + current_num  # Update maximum sum for current index
                sequences[i] = j  # Record that the best sequence comes from j

        # Update overall maximum sum index if current sum is larger
        if sums[i] >= sums[max_sum_idx]:
            max_sum_idx = i

    # Return both the maximum sum and the corresponding sequence
    return [sums[max_sum_idx], build_sequence(array, sequences, max_sum_idx)]


def build_sequence(array, sequences, current_idx):
    """
    Helper function to reconstruct the sequence from the sequences array.

    Args:
        array: Original input array
        sequences: Array tracking previous indices in optimal subsequences
        current_idx: Index where the maximum sum subsequence ends

    Returns:
        The reconstructed subsequence in correct order
    """
    sequence = []

    # Backtrack from current_idx following the sequence chain
    while current_idx is not None:
        sequence.append(array[current_idx])
        current_idx = sequences[current_idx]  # Move to previous element in sequence

    # Reverse to get the correct order (from start to end)
    return list(reversed(sequence))


# Test Cases:

print(max_sum_increasing_subsequence([10, 70, 20, 30, 50, 11, 30]))
# Output: [110, [10, 20, 30, 50]]

print(max_sum_increasing_subsequence([-5, -4, -3, -2, -1]))
# Output: [-1, [-1]]

print(max_sum_increasing_subsequence([8, 12, 2, 3, 15, 5, 7]))
# Output: [35, [8, 12, 15]]

# =========================================================================================================================== #

# Big O Analysis:

"""
# Time and Space Complexity Analysis:

### **Time Complexity:**

1. **Initialization:**
   - `sequences = [None for x in array]` → O(n)
   - `sums = [num for num in array]` → O(n)

2. **Main Logic (Nested Loop):**
   - The outer loop runs `n` times (`for i in range(len(array))`).
   - The inner loop runs up to `i` times (`for j in range(0, i)`).
   - In the worst case, this results in: O(n²)
   - The operations inside the inner loop (`if` condition, updates) are O(1).

3. **Building the Sequence:**
   - `build_sequence` runs in O(n) time in the worst case (if the entire array is the increasing subsequence).

**Total Time Complexity:** O(n) + O(n²) + O(n) = O(n²)

---

### **Space Complexity:**

1. **Auxiliary Arrays:**
   - `sequences` → O(n)
   - `sums` → O(n)

2. **Output Sequence:**
   - The `build_sequence` function constructs a subsequence, which in the worst case could be O(n) (entire array).

**Total Space Complexity:** O(n) + O(n) + O(n) = O(n)

---

### **Summary:**
- **Time Complexity:** O(n²)
- **Space Complexity:** O(n)

This is optimal for the problem using dynamic programming. There is no known O(n log n) time solution for the **maximum sum**
increasing subsequence (unlike the standard **longest increasing subsequence** problem, which can be solved in O(n log n).

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
This code finds the **maximum sum increasing subsequence** in a given array of integers. An *increasing subsequence* is a subset
of elements in which each number is greater than the previous one, and elements must appear in the same order as the original
array (though not necessarily consecutively). The goal is to find the increasing subsequence with the **largest sum**.

---

### 🔍 High-Level Idea

For each element in the array, the algorithm checks all previous elements to see if extending the subsequence ending at that element
would produce a better sum. It keeps track of:

1. **`sums[i]`** – the maximum sum of an increasing subsequence ending at index `i`.
2. **`sequences[i]`** – the index of the previous element in the increasing subsequence ending at `i`, used to reconstruct the sequence later.

---

### 📘 Function: `max_sum_increasing_subsequence(array)`

#### Initialization:

```
sequences = [None for x in array]
sums = [num for num in array]
```

* `sums[i]`: Initially set to the value of `array[i]` because the smallest increasing subsequence ending at any index is the
element itself.
* `sequences[i]`: Initialized to `None`, indicating there's no previous element yet in the subsequence.

```
max_sum_idx = 0
```

* Stores the index of the maximum sum found so far.

---

### 🔁 Main Loop:

```
for i in range(len(array)):
    current_num = array[i]

    for j in range(0, i):
        other_num = array[j]

        if other_num < current_num and sums[j] + current_num >= sums[i]:
            sums[i] = sums[j] + current_num
            sequences[i] = j
```

* Outer loop (`i`): Iterates through each element of the array.
* Inner loop (`j`): For each `i`, it checks all previous elements `j < i`.
* If `array[j] < array[i]`, then `array[i]` can extend the increasing subsequence ending at `j`.

If extending `sums[j]` with `current_num` improves the total sum at `i`, we:

* Update `sums[i]`.
* Set `sequences[i] = j` to record the path of the subsequence.

```
if sums[i] >= sums[max_sum_idx]:
    max_sum_idx = i
```

* Update the index of the maximum sum if the current `sums[i]` is larger.

---

### 📘 Function: `build_sequence(array, sequences, current_idx)`

Used to reconstruct the actual increasing subsequence.

```
sequence = []
while current_idx is not None:
    sequence.append(array[current_idx])
    current_idx = sequences[current_idx]
return list(reversed(sequence))
```

* It walks backward using the `sequences` list, appending elements to `sequence`, and then reverses it for the correct order.

---

### ✅ Output:

```
return [sums[max_sum_idx], build_sequence(array, sequences, max_sum_idx)]
```

Returns a list with:

1. The **maximum sum** of any increasing subsequence.
2. The **actual subsequence** that gives this sum.

---

### 🧪 Example: `[10, 70, 20, 30, 50, 11, 30]`

1. Possible increasing subsequences:

   * `[10, 20, 30, 50]` → sum = 110
   * `[10, 70]` → sum = 80
   * `[10, 20, 30, 50, 30]` – invalid (not increasing at the end)

2. The code returns:

   ```
   [110, [10, 20, 30, 50]]
   ```

---

### 📈 Time and Space Complexity:

* **Time Complexity:** `O(n²)`

  * For each element, it may compare to all previous elements.

* **Space Complexity:** `O(n)`

  * For storing `sums` and `sequences`.

---

Let’s visualize how the algorithm works step-by-step using **ASCII diagrams** on this input:

```
array = [10, 70, 20, 30, 50, 11, 30]
```

---

### Step 0: Initialization

We start with:

```
Index:     0   1   2   3   4   5   6
Array:    10  70  20  30  50  11  30
Sums:     10  70  20  30  50  11  30   <-- Each sum starts as the number itself
Seq:    [None]*7                      <-- No sequences yet
```

---

### Step-by-Step Update

We go from left to right and compare current element with all previous ones.

---

#### i = 1 (70)

* Compare with j = 0 (10)

  * 10 < 70 → Can extend: 10 + 70 = **80** > 70 → update
* Update:

```
Sums[1] = 80
Seq[1]  = 0
```

```
Sums:   10  80  20  30  50  11  30
Seq:   [ -   0  -   -   -   -   - ]
```

---

#### i = 2 (20)

* Compare with j = 0 (10)

  * 10 < 20 → 10 + 20 = **30** > 20 → update
* j = 1 (70) → 70 > 20 → skip

```
Sums[2] = 30
Seq[2]  = 0
```

```
Sums:   10  80  30  30  50  11  30
Seq:   [ -   0   0  -   -   -   - ]
```

---

#### i = 3 (30)

* j = 0 (10) → 10 + 30 = **40**
* j = 2 (20) → 30 + 20 = **50** > 40 → update
  → Best path: 10 → 20 → 30 = **60**

```
Sums[3] = 60
Seq[3]  = 2
```

```
Sums:   10  80  30  60  50  11  30
Seq:   [ -   0   0   2   -   -   - ]
```

---

#### i = 4 (50)

* j = 3 (30) → 60 + 50 = **110**
  → Path: 10 → 20 → 30 → 50

```
Sums[4] = 110
Seq[4]  = 3
```

```
Sums:   10  80  30  60 110  11  30
Seq:   [ -   0   0   2   3   -   - ]
```

---

#### i = 5 (11)

* j = 0 (10) → 10 + 11 = **21**

```
Sums[5] = 21
Seq[5]  = 0
```

```
Sums:   10  80  30  60 110  21  30
Seq:   [ -   0   0   2   3   0   - ]
```

---

#### i = 6 (30)

* j = 2 (20) → 30 + 30 = **60**
* j = 5 (11) → 21 + 30 = **51**
  → Best path: 10 → 20 → 30 = **60**

```
Sums[6] = 60
Seq[6]  = 2
```

```
Sums:   10  80  30  60 110  21  60
Seq:   [ -   0   0   2   3   0   2 ]
```

---

### Final Result

```
Max Sum = 110 at index 4
Backtrack: 4 → 3 → 2 → 0
```

```
Path:   [10, 20, 30, 50]
```

---

### Final Output:

```
[110, [10, 20, 30, 50]]
```

"""
