# Problem Description:

"""

                                         # First Duplicate Value

Given an array of integers between `1` and `n`, inclusive, where `n` is the length of the array, write a function that
returns the first integer that appears more than once (when the array is read from left to right).

In other words, out of all the integers that might occur more than once in the input array, your function should return
the one whose first duplicate value has the minimum index.

If no integer appears more than once, your function should return `-1`.

Note that you're allowed to mutate the input array.


## Sample Input 1:
```
array = [2, 1, 5, 2, 3, 3, 4]
```

## Sample Output 2:
```
2 // 2 is the first integer that appears more than once.
// 3 also appears more than once, but the second 3 appears after the second 2.
```

## Sample Input 3:
```
array = [2, 1, 5, 3, 3, 2, 4]
```

## Sample Output 3:
```
3 // 3 is the first integer that appears more than once.
// 2 also appears more than once, but the second 2 appears after the second 3.
```

## Optimal Time & Space Complexity:
```
O(n) time | O(1) space - where `n` is the length of the input array.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n) time | O(n) space - where `n` is the length of the input array.
def first_duplicate_value(array):
    # Create an empty set to keep track of values we've seen so far
    seen = set()

    # Iterate through each value in the input array
    for value in array:
        # If the current value is already in the 'seen' set, it means it's a duplicate
        if value in seen:
            # Return the first duplicate value found
            return value

        # If the value is not in the 'seen' set, add it to the set
        seen.add(value)

    # If no duplicates are found after iterating through the array, return -1
    return -1


# Test Cases:

print(first_duplicate_value([2, 1, 5, 2, 3, 3, 4]))
# Output: 2

print(first_duplicate_value([2, 1, 5, 3, 3, 2, 4]))
# Output: 3

print(first_duplicate_value([6, 6, 5, 1, 3, 7, 7, 8]))
# Output: 6

print(first_duplicate_value([1]))
# Output: -1

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### Time Complexity:

- The function iterates through the `array` once using a `for` loop.
- For each element in the array, it checks if the element exists in the `seen` set using the `in` operator.
Checking for membership in a set is on average - O(1).

- If the element is not in the set, it adds the element to the set, which is also O(1) on average.
- In the worst case, the loop runs through all elements of the array without finding a duplicate, resulting in O(n)
operations, where `n` is the size of the array.

Thus, the **time complexity is O(n)**, where `n` is the length of the array.

---

### Space Complexity:

- The function uses a `set` called `seen` to store unique elements from the array.
- In the worst case, if there are no duplicates, the set will store all `n` elements of the array.
- Therefore, the space required by the `seen` set is proportional to the size of the array.

Thus, the **space complexity is O(n)**, where `n` is the length of the array.

---

### Summary:
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

This implementation is efficient for finding the first duplicate value in an array.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
### Explanation of the Code

The function `first_duplicate_value(array)` is designed to find the first duplicate value in a given array.
If no duplicates are found, it returns `-1`. Here's a detailed breakdown of how the code works:

---

### Code Breakdown

```
def first_duplicate_value(array):
    seen = set()  # Initialize an empty set to track seen values

    for value in array:  # Iterate through each value in the array
        if value in seen:  # Check if the value is already in the set
            return value  # If yes, return the value as it's the first duplicate
        seen.add(value)  # If not, add the value to the set

    return -1  # If no duplicates are found, return -1
```

---

### How It Works

1. **Initialize a Set (`seen`)**:
   - A set is used to store values that have been encountered so far in the array. Sets are ideal for this purpose
   because they allow for O(1) average-time complexity for lookups and insertions.

2. **Iterate Through the Array**:
   - The function loops through each element (`value`) in the input array.

3. **Check for Duplicates**:
   - For each `value`, the function checks if it already exists in the `seen` set.
     - If the value is found in the set, it means the value is a duplicate, and the function immediately returns that
     value as the first duplicate.
     - If the value is not in the set, it is added to the `seen` set for future reference.

4. **Return -1 if No Duplicates**:
   - If the loop completes without finding any duplicates, the function returns `-1` to indicate that no duplicates 
   exist in the array.

---

### Example Walkthroughs

#### Example 1:
```
print(first_duplicate_value([2, 1, 5, 2, 3, 3, 4]))
```
- **Step-by-Step**:
  1. Start with an empty set: `seen = {}`.
  2. Iterate through the array:
     - `2` is not in `seen`, so add it: `seen = {2}`.
     - `1` is not in `seen`, so add it: `seen = {2, 1}`.
     - `5` is not in `seen`, so add it: `seen = {2, 1, 5}`.
     - `2` is already in `seen`, so return `2`.
     
- **Output**: `2`.

#### Example 2:
```
print(first_duplicate_value([2, 1, 5, 3, 3, 2, 4]))
```
- **Step-by-Step**:
  1. Start with an empty set: `seen = {}`.
  2. Iterate through the array:
     - `2` is not in `seen`, so add it: `seen = {2}`.
     - `1` is not in `seen`, so add it: `seen = {2, 1}`.
     - `5` is not in `seen`, so add it: `seen = {2, 1, 5}`.
     - `3` is not in `seen`, so add it: `seen = {2, 1, 5, 3}`.
     - `3` is already in `seen`, so return `3`.
     
- **Output**: `3`.

#### Example 3:
```
print(first_duplicate_value([6, 6, 5, 1, 3, 7, 7, 8]))
```
- **Step-by-Step**:
  1. Start with an empty set: `seen = {}`.
  2. Iterate through the array:
     - `6` is not in `seen`, so add it: `seen = {6}`.
     - `6` is already in `seen`, so return `6`.
     
- **Output**: `6`.

#### Example 4:
```
print(first_duplicate_value([1]))
```
- **Step-by-Step**:
  1. Start with an empty set: `seen = {}`.
  2. Iterate through the array:
     - `1` is not in `seen`, so add it: `seen = {1}`.
  3. No duplicates are found, so return `-1`.
  
- **Output**: `-1`.

---

### Key Points

- The function efficiently finds the first duplicate by leveraging the properties of sets.
- It stops execution as soon as the first duplicate is found, making it optimal for large arrays.
- If no duplicates are found, it returns `-1` to indicate this.

This implementation is both simple and efficient for the problem at hand.

"""
