# Problem Description:

"""

                                        # Smallest Difference

Write a function that takes in two non-empty arrays of integers, finds the pair of numbers (one from each array) whose
absolute difference is closest to zero, and returns an array containing these two numbers, with the number from the
first array in the first position.

Note that the absolute difference of two integers is the distance between them on the real number line. For example,
the absolute difference of `-5` and `5` is `10`, and the absolute difference of `-5` and `-4` is `1`.

You can assume that there will only be one pair of numbers with the smallest difference.


## Sample Input:
```
array_one = [-1, 5, 10, 20, 28, 3]
array_two = [26, 134, 135, 15, 17]
```

## Sample Output:
```
[28, 26]
```

## Optimal Time & Space Complexity:
```
O(n log(n) + m log(m)) time | O(1) space - where `n` is the length of the first input array and `m` is
the length of the second input array.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n log n + m log m) time | O(log n + log m) space
def smallest_difference(array_one, array_two):
    # Sort both arrays to make it easier to find the smallest difference
    array_one.sort()
    array_two.sort()

    # Initialize pointers for both arrays
    idx_one = 0
    idx_two = 0

    # Initialize variables to keep track of the smallest difference and the current difference
    smallest = float("inf")  # Start with infinity as the largest possible difference
    current = float("inf")

    # Initialize an empty list to store the pair with the smallest difference
    smallest_pair = []

    # Loop through both arrays until one of the pointers reaches the end
    while idx_one < len(array_one) and idx_two < len(array_two):
        # Get the current elements from both arrays
        first_num = array_one[idx_one]
        second_num = array_two[idx_two]

        # Calculate the difference between the current elements
        if first_num < second_num:
            current = second_num - first_num
            idx_one += 1  # Move the pointer in the first array forward
        elif second_num < first_num:
            current = first_num - second_num
            idx_two += 1  # Move the pointer in the second array forward
        else:
            # If the numbers are equal, the difference is zero, which is the smallest possible
            return [first_num, second_num]

        # Update the smallest difference and the corresponding pair if the current difference is smaller
        if smallest > current:
            smallest = current
            smallest_pair = [first_num, second_num]

    # Return the pair with the smallest difference
    return smallest_pair


# Test cases

print(smallest_difference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))
# Output: [28, 26]

print(smallest_difference([10, 0, 20, 25, 2200], [1005, 1006, 1014, 1032, 1031]))
# Output: [25, 1005]

print(smallest_difference([0, 20], [21, -2]))
# Output: [20, 21]

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### Time Complexity:

1. **Sorting**:
   - Sorting `array_one` takes O(n log n) time, where `n` is the length of `array_one`.
   - Sorting `array_two` takes O(m log m) time, where `m` is the length of `array_two`.

2. **Two-pointer traversal**:
   - After sorting, the two-pointer traversal takes O(n + m) time in the worst case, as each pointer
   (`idx_one` and `idx_two`) traverses its respective array once.

Thus, the **total time complexity** is:

    O(n log n + m log m + n + m)

Since `n log n` and `m log m` dominate `n` and `m`, the time complexity simplifies to:

    O(n log n + m log m)

---

### Space Complexity:

1. **Sorting**:
   - The space complexity of the sorting algorithm depends on the implementation. For example, Python's `sort()` uses
   Timsort, which has a space complexity of O(log n) for sorting `array_one` and O(log m) for sorting `array_two`.

2. **Additional space**:
   - The algorithm uses a constant amount of extra space for variables like `idx_one`, `idx_two`, `smallest`, `current`,
   and `smallest_pair`. This is - O(1).

Thus, the **total space complexity** is: O(log n + log m)

This is due to the space required for sorting.

---

### Summary:
- **Time Complexity**: O(n log n + m log m)
- **Space Complexity**: O(log n + log m) (due to sorting)

This is an efficient solution for finding the smallest difference between two arrays.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
### **Explanation of the Code**

The function **`smallest_difference`** finds the pair of numbers (one from each array) whose absolute difference is the smallest.
It does this efficiently using sorting and a two-pointer approach.

---

## **Step-by-Step Breakdown**

### **1. Sorting Both Arrays**
```
array_one.sort()
array_two.sort()
```
Sorting the arrays ensures that we can efficiently traverse them using two pointers, always moving in the direction that
minimizes the difference.

- Example:
  ```
  array_one = [-1, 5, 10, 20, 28, 3]
  array_two = [26, 134, 135, 15, 17]
  ```
  After sorting:
  ```
  array_one = [-1, 3, 5, 10, 20, 28]
  array_two = [15, 17, 26, 134, 135]
  ```

---

### **2. Initializing Variables**
```
idx_one = 0
idx_two = 0

smallest = float("inf")  # Tracks the smallest difference found
current = float("inf")   # Stores the current difference being calculated
smallest_pair = []       # Stores the pair of numbers with the smallest difference
```
- `idx_one` and `idx_two` are pointers to traverse `array_one` and `array_two`, respectively.
- `smallest` is initialized to a very large value (`float("inf")`) so that any valid difference found will replace it.
- `smallest_pair` is used to store the closest pair.

---

### **3. Using Two Pointers to Find the Closest Pair**
```
while idx_one < len(array_one) and idx_two < len(array_two):
```
- The loop continues until we have exhausted either `array_one` or `array_two`.

#### **Comparing Elements and Moving Pointers**
```
first_num = array_one[idx_one]
second_num = array_two[idx_two]
```
- `first_num` and `second_num` hold the current elements being compared.

##### **Three Cases**
1. **If `first_num` is smaller than `second_num`**, move `idx_one` forward.
   ```
   if first_num < second_num:
       current = second_num - first_num
       idx_one += 1
   ```
   - Since the arrays are sorted, moving `idx_one` forward brings it closer to `second_num`.

2. **If `second_num` is smaller than `first_num`**, move `idx_two` forward.
   ```
   elif second_num < first_num:
       current = first_num - second_num
       idx_two += 1
   ```
   - Moving `idx_two` forward helps in minimizing the difference.

3. **If `first_num` equals `second_num`**, return immediately.
   ```
   else:
       return [first_num, second_num]
   ```
   - If both numbers are the same, the absolute difference is `0`, which is the smallest possible difference.

---

### **4. Updating the Smallest Difference**
```
if smallest > current:
    smallest = current
    smallest_pair = [first_num, second_num]
```
- If the new `current` difference is smaller than `smallest`, update `smallest` and store the corresponding pair.

---

### **5. Returning the Result**
```
return smallest_pair
```
- Once the loop completes, the function returns the pair with the smallest difference.

---

## **Example Walkthrough**

### **Test Case 1**
```
smallest_difference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17])
```
#### **Step 1: Sort Arrays**
```
array_one = [-1, 3, 5, 10, 20, 28]
array_two = [15, 17, 26, 134, 135]
```
#### **Step 2: Traverse Using Two Pointers**

| `idx_one` | `idx_two` | `first_num` | `second_num` | `current` | `smallest` | `smallest_pair` |
|-----------|-----------|-------------|--------------|-----------|------------|-----------------|
| 0         | 0         | -1          | 15           | 16        | 16         | [-1, 15]        |
| 1         | 0         | 3           | 15           | 12        | 12         | [3, 15]         |
| 2         | 0         | 5           | 15           | 10        | 10         | [5, 15]         |
| 3         | 0         | 10          | 15           | 5         | 5          | [10, 15]        |
| 4         | 0         | 20          | 15           | 5         | 5          | [10, 15]        |
| 4         | 1         | 20          | 17           | 3         | 3          | [20, 17]        |
| 4         | 2         | 20          | 26           | 6         | 3          | [20, 17]        |
| 5         | 2         | 28          | 26           | 2         | 2          | [28, 26]        |

**Final Result: `[28, 26]`**

---

### **Test Case 2**
```
smallest_difference([10, 0, 20, 25, 2200], [1005, 1006, 1014, 1032, 1031])
```
- Sorted arrays:
  ```
  array_one = [0, 10, 20, 25, 2200]
  array_two = [1005, 1006, 1014, 1031, 1032]
  ```
- Traversing, the closest pair is `[25, 1005]` with a difference of `980`.

---

### **Test Case 3**
```
smallest_difference([0, 20], [21, -2])
```
- Sorted arrays:
  ```
  array_one = [0, 20]
  array_two = [-2, 21]
  ```
- Traversing, the closest pair is `[20, 21]` with a difference of `1`.

---

## **Key Takeaways**
1. **Sorting** allows efficient comparison using a two-pointer technique.
2. **Two-pointer approach** moves in a way that minimizes the difference.
3. **Efficient** with a time complexity of - O(N log N + M log M).
4. **Handles both positive and negative numbers** correctly.

This approach ensures an optimal solution to finding the closest pair in two arrays. 

"""
