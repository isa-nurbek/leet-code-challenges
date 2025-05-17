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


# O(d * (n + b)) time | O(n) space
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
