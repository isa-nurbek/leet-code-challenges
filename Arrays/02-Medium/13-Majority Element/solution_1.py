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
    # Initialize a counter to keep track of the current candidate's lead
    count = 0
    # Initialize a variable to store the current candidate for the majority element
    answer = None

    # Iterate through each element in the array
    for value in array:
        # If the counter is 0, we choose the current element as the new candidate
        if count == 0:
            answer = value

        # If the current element is the same as the candidate, increment the counter
        if value == answer:
            count += 1
        # Otherwise, decrement the counter
        else:
            count -= 1

    # After the loop, 'answer' will hold the majority element
    return answer


# Test Cases:

print(majority_element([1, 2, 3, 2, 2, 1, 2]))
# Output: 2

print(majority_element([-1, -1, -1, -1, -1, -5, -4, -3, -2]))
# Output: -1

print(majority_element([]))
# Output: None

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### Time Complexity Analysis

The time complexity of the `majority_element` function is **O(n)**, where **n** is the length of the input array.
This is because the function iterates through the array exactly once, performing a constant amount of work
(comparisons and updates) for each element.

---

### Space Complexity Analysis

The space complexity of the `majority_element` function is **O(1)**. This is because the function uses only a constant
amount of additional space (two variables: `count` and `answer`) regardless of the size of the input array.

---

### Summary
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

---

### Limitations

This algorithm assumes that there is a majority element (i.e., an element that appears more than `n/2` times).
If no such element exists, the function will still return a value, but it may not be the true majority element.
To verify the result, we can add a second pass to count the occurrences of the returned element and confirm
if it is indeed the majority.

"""

# =========================================================================================================================== #
