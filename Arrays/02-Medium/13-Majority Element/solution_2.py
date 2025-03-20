# Problem Description:

"""

                                                # Majority Element

Write a function that takes in a non-empty, unordered `array` of positive integers and returns the array's majority element
without sorting the array and without using more than constant space.

An array's majority element is an element of the array that appears in over half of its indices. Note that the most common
element of an array (the element that appears the most times in the array) isn't necessarily the array's majority element;
for example, the arrays `[3, 2, 2, 1]` and `[3, 4, 2, 2, 1]` both have `2` as their most common element, yet neither of these
arrays have a majority element, because neither `2` nor any other element appears in over half of the respective arrays' indices.

You can assume that the input array will always have a majority element.


## Sample Input:
```
array = [1, 2, 3, 2, 2, 1, 2]
```

## Sample Output:
```
2 // 2 occurs in 4/7 array indices, making it the majority element
```

## Optimal Time & Space Complexity:
```
O(n) time | O(1) space - where `n` is the number of elements in the array.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n) time | O(1) space - where `n` is the number of elements in the array
def majority_element(array):
    # If the array is empty, return None
    if not array:
        return None

    # Initialize the answer to 0
    answer = 0

    # Iterate over each bit position (from 0 to 31)
    for current_bit in range(32):
        # Create a bitmask for the current bit
        current_bit_value = 1 << current_bit
        ones_count = 0

        # Count how many numbers in the array have the current bit set
        for num in array:
            if (num & current_bit_value) != 0:
                ones_count += 1

        # If more than half of the numbers have the current bit set,
        # set that bit in the answer
        if ones_count > len(array) / 2:
            answer += current_bit_value

    # Handle negative numbers:
    # If the answer is greater than or equal to 2^31, it means the majority element
    # is a negative number (since Python uses arbitrary precision integers, we need
    # to adjust for 32-bit signed integers)
    if answer >= 2**31:
        answer -= 2**32

    # Verify if the answer is indeed the majority element by counting its occurrences
    count = 0
    for num in array:
        if num == answer:
            count += 1

    # If the count of the answer is more than half the array length, return it
    if count > len(array) / 2:
        return answer
    else:
        # Otherwise, return None (no majority element)
        return None


# Test Cases:

print(majority_element([1, 2, 3, 2, 2, 1, 2]))
# Output: 2

print(majority_element([-1, -1, -1, -1, -1, -5, -4, -3, -2]))
# Output: -1

print(majority_element([]))
# Output: None

print(majority_element([1, 2, 3, 4, 5, 6, 7]))
# Output: None (no majority element)

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### Time Complexity Analysis

The time complexity of the `majority_element` function can be broken down as follows:

1. **Outer Loop (Bitwise Iteration):**
   - The outer loop runs 32 times (since we are considering 32-bit integers). This is a constant factor, so it
   contributes O(1) to the time complexity.

2. **Inner Loop (Array Iteration):**
   - The inner loop iterates over each element in the array. If the array has `n` elements, this loop runs `n`
   times for each of the 32 bits. Therefore, the inner loop contributes O(n) for each bit.

3. **Combining the Loops:**
   - Since the outer loop runs 32 times and the inner loop runs `n` times for each iteration of the outer loop,
   the total time complexity is O(32 * n), which simplifies to O(n).

4. **Final Verification Loop:**
   - After determining the candidate majority element, the function verifies it by iterating over the array once more.
   This loop also runs in O(n) time.

5. **Overall Time Complexity:**
   - The overall time complexity is - O(n) + O(n) = O(n).

---

### Space Complexity Analysis

The space complexity of the function is determined by the additional space used apart from the input array:

1. **Variables:**
   - The function uses a few variables (`answer`, `current_bit`, `current_bit_value`, `ones_count`, `count`),
   all of which occupy constant space O(1).

2. **No Additional Data Structures:**
   - The function does not use any additional data structures that grow with the input size.

3. **Overall Space Complexity:**
   - The space complexity is O(1), as the function uses only a constant amount of extra space.

---

### Summary

- **Time Complexity:** O(n) 
- **Space Complexity:** O(1) 

"""

# =========================================================================================================================== #
