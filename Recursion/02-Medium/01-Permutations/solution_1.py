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

# =========================================================================================================================== #

# Big O Analysis:

"""

## Time and Space Complexity Analysis

### Time Complexity:

The algorithm generates all permutations of an input array. For an array of size `n`, there are `n!` (n factorial) permutations.

1. **Base Case**: When the array is empty, it adds the current permutation to the result list (`permutations`). This operation
is `O(1)` per permutation, but since there are `n!` permutations, this contributes `O(n!)` in total.
2. **Recursive Case**: For each element in the array, the algorithm:
   - Creates a new array without the current element (`array[:i] + array[i + 1:]`), which takes `O(n)` time (since slicing and
   concatenating lists is linear).
   - Creates a new permutation by appending the current element (`current_permutation + [array[i]]`), which also takes `O(n)` time
   (since appending to a list is amortized `O(1)`, but creating a new list is `O(n)`).
   - Makes a recursive call with the new array and new permutation.

At each level of recursion, the work done is proportional to the size of the current array. The recursion tree has `n` levels
(since the array shrinks by 1 element at each level), and at the `k-th` level, there are `n! / (n - k)!` nodes (each representing
a partial permutation). The total work is the sum over all levels of the work done at each level, which is `O(n * n!)`.

Thus, the **time complexity is `O(n * n!)`**.

### Space Complexity:

The space complexity is determined by:
1. **Output Space**: The `permutations` list stores all `n!` permutations, each of size `n`, so this takes `O(n * n!)` space.
2. **Recursion Stack**: The maximum depth of the recursion is `n` (since the array shrinks by 1 element at each level). At each
level, the algorithm creates new arrays and permutations, but these are not all stored simultaneously (they are created and
discarded as the recursion proceeds). The recursion stack itself uses `O(n)` space.
3. **Auxiliary Space**: The `current_permutation` and `new_array` are temporary and take `O(n)` space at each level, but they
are not all stored simultaneously. The total auxiliary space is `O(n)` (dominated by the recursion stack).

Thus, the **space complexity is `O(n * n!)`** (dominated by the output storage).

### Summary:
- **Time Complexity**: `O(n * n!)` (since we generate `n!` permutations, and each permutation takes `O(n)` time to construct).
- **Space Complexity**: `O(n * n!)` (to store all permutations, each of size `n`). The recursion stack and auxiliary space
are `O(n)`, which is dominated by the output.

This is optimal for generating all permutations, as the output itself is of size `n * n!`.

"""
