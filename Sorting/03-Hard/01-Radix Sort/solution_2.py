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
    if not arr:
        return arr

    negatives = [-x for x in arr if x < 0]
    non_negatives = [x for x in arr if x >= 0]

    sorted_negatives = radix_sort_non_negative(negatives)
    sorted_non_negatives = radix_sort_non_negative(non_negatives)

    sorted_negatives = [-x for x in reversed(sorted_negatives)]

    return sorted_negatives + sorted_non_negatives


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

print(radix_sort([8762, 654, -3008, 345, 87, -65, 234, 12, -2]))
# Output: [-3008, -65, -2, 12, 87, 234, 345, 654, 8762]

print(radix_sort([-5, -1, -300, 0, 1, 200]))
# Output: [-300, -5, -1, 0, 1, 200]

print(radix_sort([0, -1, -2, -3, -4]))
# Output: [-4, -3, -2, -1, 0]

print(radix_sort([-111, -11, -1, 0, 1, 11, 111]))
# Output: [-111, -11, -1, 0, 1, 11, 111]
