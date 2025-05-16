# Problem Description:

"""
                                               Three Number Sort

You're given an array of integers and another array of three distinct integers. The first array is guaranteed to only contain
integers that are in the second array, and the second array represents a desired order for the integers in the first array. For
example, a second array of `[x, y, z]` represents a desired order of `[x, x, ..., x, y, y, ..., y, z, z, ..., z]` in the first array.

Write a function that sorts the first array according to the desired order in the second array.

The function should perform this in place (i.e., it should mutate the input array), and it shouldn't use any auxiliary space
(i.e., it should run with constant space: `O(1)` space).

> Note that the desired order won't necessarily be ascending or descending and that the first array won't necessarily contain all
three integers found in the second array—it might only contain one or two.


## Sample Input:
```
array = [1, 0, 0, -1, -1, 0, 1, 1]
order = [0, 1, -1]
```

## Sample Output:
```
[0, 0, 0, 1, 1, 1, -1, -1]
```

## Optimal Time & Space Complexity:
```
O(n) time | O(1) space - where `n` is the length of the array.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n) time | O(1) space
def three_number_sort(array, order):
    # The order array contains the desired order of values: [first_value, second_value, third_value]
    first_value = order[0]
    second_value = order[1]
    # The third_value isn't needed explicitly since it's whatever remains

    # Initialize three pointers:
    # first_idx: boundary of where first_value elements end (starts at 0)
    # second_idx: current element being examined (starts at 0)
    # third_idx: boundary of where third_value elements begin (starts at end of array)
    first_idx, second_idx, third_idx = 0, 0, len(array) - 1

    # Iterate while the current pointer hasn't passed the third_value boundary
    while second_idx <= third_idx:
        value = array[second_idx]

        if value == first_value:
            # If current value belongs in the first group, swap it with the element at first_idx
            array[second_idx], array[first_idx] = array[first_idx], array[second_idx]
            # Move both first and second pointers forward
            first_idx += 1
            second_idx += 1
        elif value == second_value:
            # If current value belongs in the middle group, just move the second pointer forward
            second_idx += 1
        else:
            # If current value belongs in the third group, swap it with the element at third_idx
            array[second_idx], array[third_idx] = array[third_idx], array[second_idx]
            # Move the third pointer backward (we don't move second_idx because the swapped
            # element needs to be examined in the next iteration)
            third_idx -= 1

    return array


# Test Cases:

print(three_number_sort([1, 0, 0, -1, -1, 0, 1, 1], [0, 1, -1]))
# Output: [0, 0, 0, 1, 1, 1, -1, -1]

print(three_number_sort([7, 8, 9, 7, 8, 9, 9, 9, 9, 9, 9, 9], [8, 7, 9]))
# Output: [8, 8, 7, 7, 9, 9, 9, 9, 9, 9, 9, 9]

print(three_number_sort([], [0, 7, 9]))
# Output: []

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### Time Complexity Analysis:

The algorithm processes each element in the array exactly once using the `second_idx` and `third_idx` pointers. The `while`
loop runs until `second_idx` crosses `third_idx`, which means it processes each element in the array at most once. 

- **Comparisons and swaps**: For each element, the algorithm performs a constant amount of work (comparisons and swaps). 
- **Number of operations**: Since there are `n` elements in the array, the total number of operations is proportional to `n`.

Thus, the **time complexity is O(n)**, where `n` is the length of the array.

---

### Space Complexity Analysis:

The algorithm sorts the array in place by swapping elements and using a few extra variables (`first_idx`, `second_idx`,
`third_idx`, `first_value`, `second_value`, `value`). 

- No additional data structures (like extra arrays or hash tables) are used.
- The space used does not grow with the input size.

Thus, the **space complexity is O(1)** (constant space).

---

### Summary:
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)

This is similar to the Dutch National Flag problem, where we partition the array into three sections in a single pass.

"""
