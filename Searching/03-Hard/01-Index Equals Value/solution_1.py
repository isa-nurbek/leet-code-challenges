# Problem Description:

"""
                                             Index Equals Value

Write a function that takes in a sorted array of distinct integers and returns the first index in the array that is equal to the
value at that index. In other words, your function should return the minimum index where `index == array[index]`.

If there is no such index, your function should return `-1`.


## Sample Input:
```
array = [-5, -3, 0, 3, 4, 5, 9]
```

## Sample Output:
```
3

// 3 == array[3]
```

## Optimal Time & Space Complexity:
```
O(log(n)) time | O(1) space - where `n` is the length of the input array.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n) time | O(1) space
def index_equals_value(array):
    """
    Finds the first index in a sorted array where the value equals the index.

    Args:
        array: A sorted list of integers to search through.

    Returns:
        int: The first index where array[index] == index, or -1 if no such index exists.
    """

    # Iterate through each index in the array
    for idx in range(len(array)):
        # Get the value at the current index
        value = array[idx]

        # Check if the value matches the index
        if value == idx:
            # Return the first matching index found
            return idx

    # If no index matches its value, return -1
    return -1


# Test Cases:

print(index_equals_value([-5, -3, 0, 3, 4, 5, 9]))
# Output: 3

print(index_equals_value([-12, 1, 2, 3, 12]))
# Output: 1

print(index_equals_value([-5, -4, -3, -2, -1, 0, 1, 3, 5, 6, 7, 11, 12, 14, 19, 20]))
# Output: 11

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### Time Complexity:

The function iterates through each element of the array exactly once in the worst case (if no element satisfies `array[idx] == idx`). 

- **Best Case**: The first element satisfies the condition (`array[0] == 0`), and the function returns immediately.
Time complexity is \( O(1) \).

- **Worst Case**: No element satisfies the condition, or the matching element is at the end of the array.
The loop runs `n` times (where `n`) is the length of the array).
Time complexity is O(n).

- **Average Case**: On average, the loop may run `n/2` times, but this still simplifies to O(n).

Thus, the **time complexity is O(n)**.

### Space Complexity:

The function uses a constant amount of additional space (variables like `idx` and `value`), regardless of the input size. 

- No extra data structures or recursive calls are used.
- Thus, the **space complexity is O(1)** (constant space).

### Summary:
- **Time Complexity**: O(n) 
- **Space Complexity**: O(1) 

### Optimization Note:

The current implementation is a linear scan, which is optimal in the worst case. However, if the array is **sorted**,
a **binary search** approach could reduce the time complexity to O(log n). But for an unsorted array, O(n) is the best possible.

"""
