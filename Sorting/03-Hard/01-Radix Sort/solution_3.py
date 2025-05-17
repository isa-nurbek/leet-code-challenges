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
    if not arr:
        return arr

    decimal_arr = [Decimal(str(x)) for x in arr]

    scale = get_scale_factor(decimal_arr)

    scaled_arr = [int(x * scale) for x in decimal_arr]

    negatives = [-x for x in scaled_arr if x < 0]
    non_negatives = [x for x in scaled_arr if x >= 0]

    sorted_negatives = radix_sort_non_negative(negatives)
    sorted_non_negatives = radix_sort_non_negative(non_negatives)

    sorted_negatives = [-x for x in reversed(sorted_negatives)]

    sorted_scaled = sorted_negatives + sorted_non_negatives
    return [Decimal(x) / scale for x in sorted_scaled]


def get_scale_factor(arr):
    max_decimals = 0
    for num in arr:

        if num.as_tuple().exponent < 0:
            max_decimals = max(max_decimals, -num.as_tuple().exponent)
    return Decimal("1" + "0" * max_decimals)  # 10^max_decimals


def radix_sort_non_negative(arr):
    if not arr:
        return arr

    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    return arr


def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

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
