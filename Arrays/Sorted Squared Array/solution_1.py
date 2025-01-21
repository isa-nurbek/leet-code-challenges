# Description:

"""

                                    Sorted Squared Array

Write a function that takes in a non-empty array of integers that are sorted in ascending order and returns
a new array of the same length with the squares of the original integers also sorted in ascending order.

## Sample Input:

```
array = [1, 2, 3, 5, 6, 8, 9]
```

## Sample Output:

```
[1, 4, 9, 25, 36, 64, 81]
```

## Optimal Space & Time Complexity:

`O(n)` time | `O(n)` space - where `n` is the length of the input array

"""


# O(n log n) time | O(n) space
def sorted_squared_array(array):
    sorted_squares = [0 for _ in array]

    for idx in range(len(array)):
        value = array[idx]
        sorted_squares[idx] = value * value

    sorted_squares.sort()
    return sorted_squares


print(sorted_squared_array([1, 2, 3, 5, 6, 8, 9]))  # Output: [1, 4, 9, 25, 36, 64, 81]


# Big O:

"""

### Time and Space Complexity



"""


# Code Explanation:

"""


"""
