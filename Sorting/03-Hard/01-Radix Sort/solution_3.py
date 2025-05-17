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

from decimal import Decimal, getcontext


# O(d * (n + b)) time | O(n + b) space
def radix_sort(arr):
    """
    Radix sort implementation for decimal numbers (both positive and negative).

    Args:
        arr: List of numbers to be sorted (can be integers or floats)

    Returns:
        List of sorted numbers as Decimal objects
    """
    if not arr:
        return arr

    # Convert all numbers to Decimal for precise decimal handling
    decimal_arr = [Decimal(str(x)) for x in arr]

    # Get the scaling factor needed to convert decimals to integers
    scale = get_scale_factor(decimal_arr)

    # Scale all numbers to integers by multiplying with the scale factor
    scaled_arr = [int(x * scale) for x in decimal_arr]

    # Separate negative and non-negative numbers for proper sorting
    negatives = [
        -x for x in scaled_arr if x < 0
    ]  # Convert negatives to positives for sorting
    non_negatives = [x for x in scaled_arr if x >= 0]

    # Sort both parts separately using radix sort for non-negative integers
    sorted_negatives = radix_sort_non_negative(negatives)
    sorted_non_negatives = radix_sort_non_negative(non_negatives)

    # Convert the sorted negatives back to negative and reverse their order
    # (since we originally flipped them to positive)
    sorted_negatives = [-x for x in reversed(sorted_negatives)]

    # Combine the sorted negatives and non-negatives
    sorted_scaled = sorted_negatives + sorted_non_negatives

    # Convert back to original scale by dividing by the scale factor
    return [Decimal(x) / scale for x in sorted_scaled]


def get_scale_factor(arr):
    """
    Calculate the scaling factor needed to convert all decimal numbers in the array
    to integers by finding the maximum number of decimal places.

    Args:
        arr: List of Decimal numbers

    Returns:
        Decimal representing the scale factor (10^max_decimals)
    """
    max_decimals = 0
    for num in arr:
        # Check if the number has decimal places
        if num.as_tuple().exponent < 0:
            # Update max_decimals with the maximum number of decimal places found
            max_decimals = max(max_decimals, -num.as_tuple().exponent)
    return Decimal("1" + "0" * max_decimals)  # 10^max_decimals


def radix_sort_non_negative(arr):
    """
    Radix sort implementation for non-negative integers only.

    Args:
        arr: List of non-negative integers to be sorted

    Returns:
        List of sorted integers
    """
    if not arr:
        return arr

    # Find the maximum number to know the number of digits
    max_num = max(arr)

    # Do counting sort for every digit, starting from least significant
    exp = 1  # Current digit place (1s, 10s, 100s, etc.)
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10  # Move to next significant digit
    return arr


def counting_sort(arr, exp):
    """
    Helper function for radix sort that performs counting sort based on a specific digit.

    Args:
        arr: List of non-negative integers to be sorted
        exp: Current digit place to sort by (1, 10, 100, etc.)
    """
    n = len(arr)
    output = [0] * n  # Output array that will be sorted
    count = [0] * 10  # Count array for digits 0-9

    # Store count of occurrences of each digit (0-9) at current exp place
    for i in range(n):
        index = (arr[i] // exp) % 10  # Extract the current digit
        count[index] += 1

    # Change count[i] so it contains actual position of this digit in output
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array in sorted order for current digit
    i = n - 1
    while i >= 0:  # Processing from end to maintain stability
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    # Copy the output array back to arr, so arr is now sorted by current digit
    for i in range(n):
        arr[i] = output[i]


# Test Cases:

getcontext().prec = 30  # Up to 30 digits of precision


print(
    radix_sort(
        [
            Decimal("3.141"),
            Decimal("-2.71"),
            Decimal("1.618"),
            Decimal("0.0"),
            Decimal("-0.577"),
            Decimal("2.718"),
        ]
    )
)
# Output: [-2.71, -0.577, 0.0, 1.618, 2.718, 3.141]

print(
    radix_sort(
        [
            Decimal("-1.0"),
            Decimal("-2.25"),
            Decimal("0.5"),
            Decimal("0.25"),
            Decimal("1.5"),
            Decimal("2.0"),
        ]
    )
)
# Output: [-2.25, -1.0, 0.25, 0.5, 1.5, 2.0]

print(
    radix_sort(
        [Decimal("-0.00001"), Decimal("0.000001"), Decimal("0.0001"), Decimal("-0.1")]
    )
)
# Output: [-0.1, -0.00001, 0.000001, 0.0001]

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### Time Complexity:

1. **Scaling Phase** (converting decimals to integers):
   - `get_scale_factor()`: O(n) to examine all numbers and find max decimal places
   - Scaling operation: O(n)
   - Total for scaling: O(n)

2. **Radix Sort on Non-negative Numbers**:
   - For each digit position (d positions, where d is the number of digits in the largest number):
     - Counting sort: O(n)
   - Total: O(d * n)

3. **Negative Numbers Handling**:
   - Similar complexity as non-negative numbers: O(d * n) for the negative portion

4. **Final Conversion**:
   - Scaling back to decimals: O(n)

**Overall Time Complexity**: O(d * n),
where:
- n is the number of elements
- d is the maximum number of digits in the scaled integer representation of the numbers

### Space Complexity:

1. **Scaling Storage**:
   - Storing decimal_arr: O(n)
   - Storing scaled_arr: O(n)

2. **Counting Sort**:
   - Output array: O(n)
   - Count array: O(10) = O(1)

3. **Negative/Negative Separation**:
   - Temporary storage for negatives and non-negatives: O(n)

**Overall Space Complexity**: O(n) (linear space)

### Key Notes:

- The complexity depends heavily on the precision (number of decimal places) because it affects the number of digits (d)
in the scaled integers.
- For floating-point numbers with many decimal places, d can become large, making the algorithm less efficient.
- This implementation handles both positive and negative numbers by processing them separately.
- The Decimal conversion ensures precision is maintained during the sorting process.

This implementation is most efficient when:
1. The numbers have limited decimal places (small d)
2. The range of numbers isn't extremely large
3. Precision maintenance is more important than absolute speed

"""
