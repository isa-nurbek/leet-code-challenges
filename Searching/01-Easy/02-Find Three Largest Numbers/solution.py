# Problem Description:

"""
                                             Find Three Largest Numbers

Write a function that takes in an array of at least `three integers` and, without sorting the input array, returns a sorted array
of the three largest integers in the input array.

The function should return duplicate integers if necessary; for example, it should return `[10, 10, 12]` for an input array of
`[10, 5, 9, 10, 12]`.


## Sample Input:
```
array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
```

## Sample Output:
```
[18, 141, 541]
```

## Optimal Time & Space Complexity:
```
O(n) time | O(1) space - where `n` is the length of the input array.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n) time | O(1) space
def find_three_largest_numbers(array):
    """
    Finds the three largest numbers in the input array in sorted order.

    Args:
        array: List of numbers to search through

    Returns:
        List of three largest numbers in ascending order [smallest, middle, largest]
    """
    # Initialize a list to hold our three largest numbers, starting with None values
    three_largest = [None, None, None]

    # Iterate through each number in the input array
    for num in array:
        # For each number, update our three_largest list if needed
        update_largest(three_largest, num)

    # Return the three largest numbers found
    return three_largest


def update_largest(three_largest, num):
    """
    Updates the three_largest list with the current number if it belongs in the top three.

    Args:
        three_largest: Current list of three largest numbers
        num: Number to potentially insert into the three_largest list
    """
    # Check if we should update the third position (largest number)
    if three_largest[2] is None or num > three_largest[2]:
        shift_and_update(three_largest, num, 2)
    # Else check if we should update the second position
    elif three_largest[1] is None or num > three_largest[1]:
        shift_and_update(three_largest, num, 1)
    # Else check if we should update the first position (smallest of top three)
    elif three_largest[0] is None or num > three_largest[0]:
        shift_and_update(three_largest, num, 0)


def shift_and_update(array, num, idx):
    """
    Shifts numbers to the left in the array and inserts the new number at the specified index.

    For example, if array is [a, b, c] and we insert at index 1 (for number x):
    - a gets discarded
    - b shifts to a's position
    - x is inserted at b's position
    - c remains unchanged

    Args:
        array: The array to modify
        num: The number to insert
        idx: The position where the number should be inserted
    """
    # Iterate through the array up to the specified index
    for i in range(idx + 1):
        if i == idx:
            # At the target index, insert the new number
            array[i] = num
        else:
            # For indices before the target, shift the next value left
            array[i] = array[i + 1]


# Test Cases:

print(find_three_largest_numbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]))
# Output: [18, 141, 541]

print(find_three_largest_numbers([55, 43, 11, 3, -3, 10]))
# Output: [11, 43, 55]

print(find_three_largest_numbers([7, 7, 7, 7, 7, 7, 8, 7, 7, 7, 7]))
# Output: [7, 7, 8]

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### **Time Complexity:**

1. **`find_three_largest_numbers(array)`**:
   - This function iterates over each element in the input array once (`O(n)` time, where `n` is the size of the array).
   - For each element, it calls `update_largest()`, which performs comparisons and possibly calls `shift_and_update()`.

2. **`update_largest(three_largest, num)`**:
   - This function performs at most 3 comparisons (`O(1)` time per call).

3. **`shift_and_update(array, num, idx)`**:
   - This function shifts elements in the `three_largest` array up to index `idx`. The worst case is when `idx = 2`, which
   requires shifting 3 elements (`O(1)` time since the array size is fixed at 3).

**Overall Time Complexity**:
- Since each element in the input array is processed in `O(1)` time (due to fixed-size operations),
the total time complexity is: O(n) where `n` is the number of elements in the input array.

---

### **Space Complexity:**

1. The algorithm uses an auxiliary array `three_largest` of size 3, which is **constant space**.
2. No additional space is used that scales with the input size.

**Overall Space Complexity**: O(1)

### **Summary:**
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

"""
