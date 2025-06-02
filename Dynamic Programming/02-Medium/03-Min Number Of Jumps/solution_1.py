# Problem Description:

"""
                                            Min Number Of Jumps

You're given a `non-empty` array of positive integers where each integer represents the maximum number of steps you can take
forward in the array. For example, if the element at index `1` is `3`, you can go from index `1` to index `2`, `3`, or `4`.

Write a function that returns the minimum number of jumps needed to reach the final index.

> Note that jumping from index `i` to index `i + x` always constitutes one jump, no matter how large `x` is.


## Sample Input:
```
array = [3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]
```

## Sample Output:
```
4

// 3 --> (4 or 2) --> (2 or 3) --> 7 --> 3
```

## Optimal Time & Space Complexity:
```
O(n) time | O(1) space - where `n` is the length of the input array.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n²) time | O(n) space
def min_number_of_jumps(array):
    # Initialize a jumps array to store the minimum number of jumps needed to reach each position
    # Start with infinity for all positions except the first one (which takes 0 jumps to reach)
    jumps = [float("inf") for x in array]
    jumps[0] = 0  # Base case: no jumps needed to reach first element

    # Iterate through each position in the array starting from the second element
    for i in range(1, len(array)):
        # For each position i, check all previous positions j (0 to i-1)
        for j in range(0, i):
            # Check if from position j, we can jump to position i
            # This is possible if the value at j (array[j]) is >= the distance between j and i
            if array[j] >= i - j:
                # If we can jump from j to i, update jumps[i] to be the minimum between:
                # - its current value
                # - jumps[j] + 1 (jumps to reach j plus this one jump)
                jumps[i] = min(jumps[j] + 1, jumps[i])

    # The last element of jumps array contains the minimum jumps needed to reach the end
    return jumps[-1]


# Test Cases:

print(min_number_of_jumps([3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]))
# Output: 4

print(min_number_of_jumps([2, 1, 2, 3, 1]))
# Output: 2

print(min_number_of_jumps([1]))
# Output: 0

# =========================================================================================================================== #

# Big O Analysis:

"""
# Time and Space Complexity Analysis:

Let's analyze the time and space complexity of the given `min_number_of_jumps` function.

## Time Complexity:

1. **Initialization**: The `jumps` array is initialized in O(n) time, where n is the length of the input array.
2. **Nested Loops**:
   - The outer loop runs from `i = 1` to `i = n-1` (n-1 iterations).
   - The inner loop runs from `j = 0` to `j = i-1` (i iterations for each i).
   - For each `i`, the inner loop runs `i` times.
   So, the total number of operations is roughly `1 + 2 + 3 + ... + (n-1) = (n-1)*n/2 = O(n²)`.
3. **Operations Inside Inner Loop**:
   - The `if` condition and the `min` operation are O(1) per iteration.

Thus, the **total time complexity is O(n²)**.

## Space Complexity:

1. The `jumps` array uses O(n) additional space.
2. No other significant space is used (only a few variables like `i`, `j`).

Thus, the **space complexity is O(n)**.

### Summary:
- **Time Complexity**: O(n²) (due to nested loops).
- **Space Complexity**: O(n) (for the `jumps` array).

### Note:
This is a dynamic programming approach with a quadratic time complexity. There is a more efficient O(n) greedy solution for this
problem, but this implementation follows the DP approach.

"""
