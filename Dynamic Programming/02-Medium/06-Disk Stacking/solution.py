# Problem Description:

"""
                                            Disk Stacking

You're given a `non-empty` array of arrays where each subarray holds three integers and represents a disk. These integers denote
each disk's width, depth, and height, respectively. Your goal is to stack up the disks and to maximize the total height of the
stack. A disk must have a strictly smaller width, depth, and height than any other disk below it.

Write a function that returns an array of the disks in the final stack, starting with the top disk and ending with the bottom disk.
> Note that you can't rotate disks; in other words, the integers in each subarray must represent `[width, depth, height]` at all times.

You can assume that there will only be one stack with the greatest total height.


## Sample Input:
```
disks = [[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [1, 3, 1], [4, 4, 5]]
```

## Sample Output:
```
[[2, 1, 2], [3, 2, 3], [4, 4, 5]]

// 10 (2 + 3 + 5) is the tallest height we can get by stacking disks following the rules laid out above.
```

## Optimal Time & Space Complexity:
```
O(n²) time | O(n) space - where `n` is the number of disks.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n²) time | O(n) space
def disk_stacking(disks):
    # Sort the disks by their height (third dimension) in ascending order
    disks.sort(key=lambda disk: disk[2])
    n = len(disks)

    # Initialize an array to store the maximum achievable height when each disk is at the bottom
    heights = [disk[2] for disk in disks]

    # Initialize an array to keep track of the previous disk in the tallest stack for each position
    sequences = [None for _ in range(n)]

    # Track the index of the disk with the maximum height stack
    max_height_idx = 0

    # Dynamic programming approach to build tallest stack
    for i in range(1, n):
        current_disk = disks[i]

        # Check all disks before the current one to see if they can be placed below
        for j in range(i):
            other_disk = disks[j]

            # Check if the other disk can be placed below the current disk
            if are_valid_dimensions(other_disk, current_disk):
                # If placing the other disk below gives a taller stack, update heights and sequences
                if heights[i] < heights[j] + current_disk[2]:
                    heights[i] = heights[j] + current_disk[2]
                    sequences[i] = j

        # Update the index of the disk with maximum height if current stack is taller
        if heights[i] >= heights[max_height_idx]:
            max_height_idx = i

    # Build and return the sequence of disks in the tallest stack
    return build_sequence(disks, sequences, max_height_idx)


def are_valid_dimensions(o, c):
    """
    Helper function to check if disk 'o' can be placed below disk 'c'
    A disk can be placed below another if all its dimensions (width, depth, height)
    are strictly smaller than the corresponding dimensions of the disk above.
    """
    return o[0] < c[0] and o[1] < c[1] and o[2] < c[2]


def build_sequence(disks, sequences, current_idx):
    """
    Helper function to reconstruct the sequence of disks in the tallest stack
    by backtracking through the sequences array starting from the disk at current_idx.
    """
    sequence = []

    # Backtrack from the disk at current_idx to build the sequence
    while current_idx is not None:
        sequence.append(disks[current_idx])
        current_idx = sequences[current_idx]

    # Return the sequence in bottom-to-top order (reversed from how we built it)
    return list(reversed(sequence))


# Test Cases:

print(disk_stacking([[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [1, 3, 1], [4, 4, 5]]))
# Output: [[2, 1, 2], [3, 2, 3], [4, 4, 5]]

print(disk_stacking([[2, 1, 2], [3, 2, 3], [2, 2, 8]]))
# Output: [[2, 2, 8]]

print(disk_stacking([[2, 1, 2]]))
# Output: [[2, 1, 2]]

# =========================================================================================================================== #

# Big O Analysis:

"""
# Time and Space Complexity Analysis:

Let's analyze the time and space complexity of the `disk_stacking` algorithm.

### Time Complexity:

1. **Sorting the Disks**:  
   The algorithm starts by sorting the disks based on their height (third dimension).
   Sorting `n` disks takes **O(n log n)** time.

2. **Initialization**:  
   Initializing the `heights` and `sequences` arrays takes **O(n)** time.

3. **Nested Loop for Dynamic Programming**:  
   - The outer loop runs from `i = 1` to `n-1` → **O(n)** iterations.  
   - The inner loop runs from `j = 0` to `i-1` → in the worst case, **O(n)** iterations per outer loop.  
   - Inside the inner loop, `are_valid_dimensions` is called, which is an **O(1)** operation.  
   - Thus, the nested loops contribute **O(n²)** time.

4. **Building the Sequence**:  
   The `build_sequence` function constructs the result by backtracking, which takes **O(n)** time in the worst case
   (if the sequence includes all disks).

**Total Time Complexity** = **O(n log n) + O(n) + O(n²) + O(n)** = **O(n²)** (since **O(n²)** dominates).

---

### Space Complexity:

1. **Storage for `heights` and `sequences`**:  
   Both arrays are of size `n` → **O(n)** space.

2. **Output Sequence Storage**:  
   The `build_sequence` function returns a list that could, in the worst case, contain all `n` disks → **O(n)** space.

**Total Space Complexity** = **O(n)** (for `heights`, `sequences`, and the output sequence).

---

### Summary:
- **Time Complexity**: **O(n²)**  
- **Space Complexity**: **O(n)**  

The dominant factor is the nested loop in the dynamic programming step, making this an **O(n²)** algorithm.
The space complexity is linear due to the storage required for the DP arrays and the output sequence.

"""
