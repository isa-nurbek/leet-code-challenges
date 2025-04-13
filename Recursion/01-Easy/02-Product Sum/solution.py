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
    # Initialize sum to accumulate all elements' values
    sum = 0

    # Iterate through each element in the array
    for element in array:
        # If the element is a list (nested array), recursively calculate its product sum
        if type(element) is list:
            # For nested arrays, increment the multiplier (depth) by 1
            sum += product_sum(element, multiplier + 1)
        else:
            # For regular numbers, simply add them to the sum
            sum += element

    # Multiply the accumulated sum by the current depth level
    return sum * multiplier


# Test Cases:

print(product_sum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]))
# Output: 12

print(product_sum([1, 2, 3, 4, 5]))
# Output: 15

print(product_sum([[1, 2], 3, [4, 5]]))
# Output: 27

# =========================================================================================================================== #

# Big O Analysis:

"""

## Time and Space Complexity Analysis

### Time Complexity:

- **Definition**: The function calculates a "product sum" of a special array (which may contain nested lists) where
each element is summed, but nested lists contribute to the sum multiplied by their depth level.
- **Approach**: The function processes each element of the array exactly once. For each element, it checks whether
the element is a list or not. 
  - If it's a list, the function recursively processes that list with an incremented `multiplier`.
  - If it's not a list, the element is added to the sum directly.
- **Recurrence Relation**: If we denote `n` as the total number of elements in the array (including all nested elements),
the time complexity can be expressed as `O(n)`, because each element is processed exactly once, regardless of its depth.

- **Conclusion**: The time complexity is **O(n)**, where `n` is the total number of elements (including all nested elements).

### Space Complexity:

- **Definition**: The space complexity is determined by the maximum depth of the recursion stack.
- **Approach**: The function uses recursion to handle nested lists. The recursion depth is equal to the maximum depth of
nesting in the array. For example:
  - `[1, 2, [3, [4]]]` has a maximum depth of 3 (the element `4` is nested 3 levels deep).
- **Auxiliary Space**: For each recursive call, a new stack frame is created, but no additional data structures are used that
grow with the input size.
- **Conclusion**: The space complexity is **O(d)**, where `d` is the maximum depth of nesting in the array. In the worst case, if
the array is a linear chain of nested lists (e.g., `[[[[]]]`), then `d = n`, making the space complexity **O(n)** in the worst case.

### Summary:
- **Time Complexity**: **O(n)** (where `n` is the total number of elements, including all nested elements).
- **Space Complexity**: **O(d)** (where `d` is the maximum depth of nesting, with a worst-case of **O(n)** if the array
is deeply nested).

This analysis assumes that checking `type(element) is list` and arithmetic operations are constant-time operations,
which is reasonable in Python.

"""
