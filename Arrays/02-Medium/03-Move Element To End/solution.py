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

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### Time Complexity:

The time complexity of the `move_element_to_end` function is **O(n)**, where `n` is the length of the input array.

Here's why:

1. The function uses two pointers, `i` and `j`, which start at the beginning and end of the array, respectively.
2. The outer `while` loop runs until `i` and `j` meet. In the worst case, this will happen after `n` iterations.
3. The inner `while` loop decrements `j` only if `array[j]` is equal to `to_move`. This ensures that `j` only moves
when necessary, and it doesn't add extra complexity because each element is checked at most once.

4. The swapping operation (`array[i], array[j] = array[j], array[i]`) is performed in constant time, **O(1)**.

Since each element is processed at most once, the overall time complexity is linear, **O(n)**.

---

### Space Complexity:

The space complexity is **O(1)**, which means the algorithm uses constant extra space. This is because the function
modifies the input array in place and only uses a few variables (`i`, `j`, and temporary variables for swapping).
No additional data structures are used that grow with the input size.

---

### Summary:
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

This is an efficient solution for moving all instances of a given element to the end of the array.

"""

# =========================================================================================================================== #
