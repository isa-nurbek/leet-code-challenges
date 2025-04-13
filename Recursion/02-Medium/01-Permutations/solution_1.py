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


# Upper Bound: O(n² * n!) time | O(n * n!) space
# Roughly: O(n * n!) time | O(n * n!) space
def get_permutations(array):
    """Main function to get all permutations of an array.

    Args:
        array: The input array to generate permutations for

    Returns:
        A list of all possible permutations of the input array
    """
    permutations = []  # This will store all the permutations we generate
    permutations_helper(array, [], permutations)  # Start the recursive process
    return permutations


def permutations_helper(array, current_permutation, permutations):
    """Recursive helper function to generate permutations.

    Args:
        array: The remaining elements to permute
        current_permutation: The permutation being built in the current recursion path
        permutations: The list that accumulates all complete permutations
    """
    # Base case: if array is empty and current_permutation has elements
    if not len(array) and len(current_permutation):
        # Add the completed permutation to our results
        permutations.append(current_permutation)
    else:
        # Recursive case: build permutations by choosing each remaining element
        for i in range(len(array)):
            # Create new array without the current element (array[i])
            new_array = array[:i] + array[i + 1 :]

            # Add current element to the permutation we're building
            new_permutation = current_permutation + [array[i]]

            # Recurse with the remaining elements and updated permutation
            permutations_helper(new_array, new_permutation, permutations)


# Test Cases:

print(get_permutations([1, 2, 3]))
# Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

print(get_permutations([1]))
# Output: [[1]]

print(get_permutations([]))
# Output: []
