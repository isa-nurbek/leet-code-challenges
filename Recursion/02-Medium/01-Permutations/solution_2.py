# Problem Description:

"""

                                            Permutations

Write a function that takes in an array of unique integers and returns an array of all `permutations` of those integers in
no particular order.

If the input array is empty, the function should return an empty array.


## Sample Input
```
array = [1, 2, 3]
```

## Sample Output
```
[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
```

## Optimal Time & Space Complexity:
```
O(n * n!) time | O(n * n!) space - where `n` is the length of the input array.
```
"""

# =========================================================================================================================== #

# Solution:


# O(n * n!) time | O(n * n!) space
def get_permutations(array):
    """Main function to generate all permutations of an array.

    Args:
        array: The input array to generate permutations for

    Returns:
        A list containing all possible permutations of the input array
    """
    permutations = []  # This will store all the permutations we generate
    permutations_helper(0, array, permutations)  # Start the recursive process
    return permutations


def permutations_helper(i, array, permutations):
    """Recursive helper function to generate permutations.

    This works by swapping elements to generate all possible orderings.

    Args:
        i: Current index we're fixing in the permutation
        array: The array we're generating permutations for
        permutations: List to store the resulting permutations
    """
    # Base case: If we've reached the last element, we have a complete permutation
    if i == len(array) - 1:
        permutations.append(array[:])  # Add a copy of the current array state
    else:
        # Recursive case: Generate permutations for remaining elements
        for j in range(i, len(array)):
            # Swap current element with element at index j
            swap(array, i, j)
            # Recursively generate permutations for the remaining positions
            permutations_helper(i + 1, array, permutations)
            # Swap back (backtrack) to restore original array for next iteration
            swap(array, i, j)


def swap(array, i, j):
    """Helper function to swap two elements in an array in-place.

    Args:
        array: The array containing elements to swap
        i: Index of first element
        j: Index of second element
    """
    array[i], array[j] = array[j], array[i]


# Test Cases:

print(get_permutations([1, 2, 3]))
# Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

print(get_permutations([1]))
# Output: [[1]]

print(get_permutations([]))
# Output: []

# =========================================================================================================================== #

# Big O Analysis:

"""

## Time and Space Complexity Analysis

### Time Complexity:

The algorithm generates all permutations of the input array. For an array of length `n`, there are `n!` (n factorial) permutations.

1. **Base Case**: When `i == len(array) - 1`, it copies the current array (O(n) time) and appends it to `permutations`.
2. **Recursive Case**: For each index `i`, the algorithm swaps `array[i]` with `array[j]` for `j` from `i` to `n-1`, and 
recursively generates permutations for `i+1`.

- The recursion tree has `n!` leaves (one for each permutation).
- Each leaf involves an O(n) operation (copying the array).
- The total number of nodes in the recursion tree is roughly `n! + n!/1! + n!/2! + ... + n!/(n-1!)`, which is still O(n!).
- Each recursive call does O(1) work (apart from the recursive calls and the base case).

Thus, the total time complexity is **O(n! * n)**.

### Space Complexity:

1. **Output Space**: The `permutations` list stores `n!` permutations, each of size `n`, so this contributes O(n! * n) space.
2. **Recursion Stack**: The recursion depth is `n` (since `i` goes from `0` to `n-1`), and each stack frame uses O(1) space
(just storing `i`, `j`, and some pointers). Thus, the recursion stack contributes O(n) space.

The dominant term is the output space, so the total space complexity is **O(n! * n)**.

### Summary:
- **Time Complexity**: O(n! * n)
- **Space Complexity**: O(n! * n) (due to the output storage)

This is optimal for generating all permutations because you can't do better than O(n!) time (since there are n! permutations)
or O(n! * n) space (since you need to store n! permutations, each of size n).

"""
