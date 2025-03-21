# Problem Description:

"""

                                                # Four Number Sum

Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. The function
should find all quadruplets in the array that sum up to the target sum and return a two-dimensional array of all these
quadruplets in no particular order.

If no four numbers sum up to the target sum, the function should return an empty array.


## Sample Input:
```
array = [7, 6, 4, -1, 1, 2]
targetSum = 16
```

## Sample Output:
```
[[7, 6, 4, -1], [7, 6, 1, 2]] // the quadruplets could be ordered differently
```

## Optimal Time & Space Complexity:
```
Average: O(n^2) time | O(n^2) space - where `n` is the length of the input array.
Worst: O(n^3) time | O(n^3) space - where `n` is the length of the input array.
```

"""

# =========================================================================================================================== #

# Solution:


# Average: O(n^2) time | O(n^2) space
# Worst: O(n^3) time | O(n^3) space
def four_number_sum(array, target_sum):
    # Dictionary to store all possible pairs and their sums
    all_pairs_sums = {}

    # List to store all valid quadruplets that sum up to the target_sum
    quadruplets = []

    # Iterate through the array starting from the second element to the second-to-last element
    for i in range(1, len(array) - 1):

        # Iterate through the array starting from the element right after the current i
        for j in range(i + 1, len(array)):
            # Calculate the sum of the current pair (array[i], array[j])
            current_sum = array[i] + array[j]

            # Calculate the difference needed to reach the target_sum
            difference = target_sum - current_sum

            # If the difference exists in the all_pairs_sums dictionary, it means we have found
            # pairs that, when added to the current pair, sum up to the target_sum
            if difference in all_pairs_sums:
                # Iterate through all pairs that sum up to the difference
                for pair in all_pairs_sums[difference]:
                    # Add the new quadruplet (pair + current pair) to the quadruplets list
                    quadruplets.append(pair + [array[i], array[j]])

        # Now, iterate through the array from the start to the current i
        for k in range(0, i):
            # Calculate the sum of the current pair (array[k], array[i])
            current_sum = array[k] + array[i]

            # If this sum is not already in the all_pairs_sums dictionary, add it
            if current_sum not in all_pairs_sums:
                all_pairs_sums[current_sum] = [[array[k], array[i]]]
            else:
                # If the sum is already in the dictionary, append the new pair to the existing list
                all_pairs_sums[current_sum].append([array[k], array[i]])

    # Return the list of all valid quadruplets
    return quadruplets


# Test Cases:

array = [7, 6, 4, -1, 1, 2]
target_sum = 16

array_2 = [1, 2, 3, 4, 5, 6, 7]
target_sum_2 = 10

array_3 = [1, 2, 3, 4, 5]
target_sum_3 = 100

print(four_number_sum(array, target_sum))
# Output: [[7, 6, 4, -1], [7, 6, 1, 2]]

print(four_number_sum(array_2, target_sum_2))
# Output: [[1, 2, 3, 4]]

print(four_number_sum(array_3, target_sum_3))
# Output: []

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### **Time Complexity**

1. **Outer Loop (`i` loop)**:
   - The outer loop runs from `i = 1` to `len(array) - 2`, which is approximately O(n), where `n` is the length of the array.

2. **Inner Loop (`j` loop)**:
   - For each `i`, the inner loop runs from `j = i + 1` to `len(array) - 1`, which is also approximately O(n).

3. **Checking for Differences**:
   - Inside the `j` loop, the function checks if `difference` exists in `all_pairs_sums`. This operation is O(1) on average
   because it uses a dictionary for lookups.
   
   - If `difference` exists, it iterates over all pairs in `all_pairs_sums[difference]`. In the worst case, this could be
   O(n^2) because there could be up to O(n^2) pairs stored in `all_pairs_sums`.

4. **Storing Pairs**:
   - After the `j` loop, the function iterates over `k` from `0` to `i - 1` to store pairs in `all_pairs_sums`.
   This is O(n) for each `i`.

Combining these:
- The outer loop runs O(n) times.
- For each `i`, the `j` loop runs O(n) times.
- For each `j`, checking and storing pairs takes O(n^2) in the worst case.

Thus, the **time complexity** is: O(n^3)

---

### **Space Complexity**

1. **Dictionary (`all_pairs_sums`)**:
   - The dictionary stores all possible pairs of elements and their sums. In the worst case, there are O(n^2) pairs.

2. **Quadruplets List**:
   - The `quadruplets` list stores all valid quadruplets. In the worst case, there could be O(n^3) quadruplets
   (e.g., if all combinations sum to the target).

Thus, the **space complexity** is: O(n^3)

---

### **Summary**
- **Time Complexity**: O(n^3)
- **Space Complexity**: O(n^3)

- **Average-Case Time Complexity**: O(n^2)
- **Average-Case Space Complexity**: O(n^2)

This algorithm is efficient for small to medium-sized arrays but may become slow for very large arrays due to
its cubic time complexity.

"""
