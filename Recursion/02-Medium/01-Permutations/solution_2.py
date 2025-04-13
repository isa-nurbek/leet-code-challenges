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
