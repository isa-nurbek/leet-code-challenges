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
    disks.sort(key=lambda disk: disk[2])
    n = len(disks)

    heights = [disk[2] for disk in disks]
    sequences = [None for _ in range(n)]
    max_height_idx = 0

    for i in range(1, n):
        current_disk = disks[i]

        for j in range(i):
            other_disk = disks[j]

            if are_valid_dimensions(other_disk, current_disk):
                if heights[i] < heights[j] + current_disk[2]:
                    heights[i] = heights[j] + current_disk[2]
                    sequences[i] = j

        if heights[i] >= heights[max_height_idx]:
            max_height_idx = i

    return build_sequence(disks, sequences, max_height_idx)


def are_valid_dimensions(o, c):
    return o[0] < c[0] and o[1] < c[1] and o[2] < c[2]


def build_sequence(disks, sequences, current_idx):
    sequence = []

    while current_idx is not None:
        sequence.append(disks[current_idx])
        current_idx = sequences[current_idx]

    return list(reversed(sequence))


# Test Cases:

print(disk_stacking([[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [1, 3, 1], [4, 4, 5]]))
# Output: [[2, 1, 2], [3, 2, 3], [4, 4, 5]]

print(disk_stacking([[2, 1, 2], [3, 2, 3], [2, 2, 8]]))
# Output: [[2, 2, 8]]

print(disk_stacking([[2, 1, 2]]))
# Output: [[2, 1, 2]]
