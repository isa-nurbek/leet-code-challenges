# Problem Description:

"""

                                        # Move Element To End

You're given an array of integers and an integer. Write a function that moves all instances of that integer in the array
to the end of the array and returns the array.

The function should perform this in place (i.e., it should mutate the input array) and doesn't need to maintain the order
of the other integers.


## Sample Input:
```
array = [2, 1, 2, 2, 2, 3, 4, 2]
to_move = 2
```

## Sample Output:
```
[1, 3, 4, 2, 2, 2, 2, 2] // the numbers 1, 3, and 4 could be ordered differently.
```

## Optimal Time & Space Complexity:
```
O(n) time | O(1) space - where `n` is the length of the array.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n) time | O(1) space - where `n` is the length of the array
def move_element_to_end(array, to_move):
    # Initialize two pointers:
    # - `i` starts at the beginning of the array (left pointer)
    # - `j` starts at the end of the array (right pointer)
    i = 0
    j = len(array) - 1

    # Loop until the two pointers meet or cross each other
    while i < j:
        # Move the right pointer `j` leftwards until it points to an element
        # that is not equal to `to_move` (or until `i` and `j` meet)
        while i < j and array[j] == to_move:
            j -= 1

        # If the left pointer `i` points to the element `to_move`,
        # swap it with the element at the right pointer `j`
        if array[i] == to_move:
            array[i], array[j] = array[j], array[i]

        # Move the left pointer `i` rightwards
        i += 1

    # Return the modified array with all `to_move` elements moved to the end
    return array


# Test cases:

print(move_element_to_end([2, 1, 2, 2, 2, 3, 4, 2], 2))
# Output: [4, 1, 3, 2, 2, 2, 2, 2]

print(move_element_to_end([1, 2, 4, 5, 6], 3))
# Output: [1, 2, 4, 5, 6]

print(move_element_to_end([], 4))
# Output: []

# =========================================================================================================================== #
