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
