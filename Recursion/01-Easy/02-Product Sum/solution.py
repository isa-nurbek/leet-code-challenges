# Problem Description:

"""

                                            Product Sum

Write a function that takes in a "special" array and returns its product sum.

A "special" array is a non-empty array that contains either integers or other "special" arrays. The product sum of a "special"
array is the sum of its elements, where "special" arrays inside it are summed themselves and then multiplied by their level of depth.

The depth of a "special" array is how far nested it is. For instance, the depth of `[]` is `1`; the depth of the inner array
in `[[]]` is `2`; the depth of the innermost array in `[[[]]]` is `3`.

Therefore, the product sum of `[x, y]` is `x + y`; the product sum of `[x, [y, z]]` is `x + 2 * (y + z)`; the product sum of
`[x, [y, [z]]]` is `x + 2 * (y + 3z)`.


## Sample Input
```
array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
```

## Sample Output
```
12 // calculated as: 5 + 2 + 2 * (7 - 1) + 3 + 2 * (6 + 3 * (-13 + 8) + 4)
```

## Optimal Time & Space Complexity:
```
O(n) time | O(d) space - where `n` is the total number of elements in the array, including sub-elements,
and `d` is the greatest depth of "special" arrays in the array.
```
"""

# =========================================================================================================================== #

# Solution:


# O(n) time | O(d) space
def product_sum(array, multiplier=1):
    sum = 0

    for element in array:
        if type(element) is list:
            sum += product_sum(element, multiplier + 1)
        else:
            sum += element

    return sum * multiplier


# Test Cases:

print(product_sum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]))
# Output: 12

print(product_sum([1, 2, 3, 4, 5]))
# Output: 15

print(product_sum([[1, 2], 3, [4, 5]]))
# Output: 27
