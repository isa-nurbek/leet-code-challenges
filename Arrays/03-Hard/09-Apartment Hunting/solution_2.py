# Problem Description:

"""
                                            # Apartment Hunting

You're looking to move into a new apartment on specific street, and you're given a list of contiguous blocks on that street
where each block contains an apartment that you could move into.

You also have a list of requirements: a list of buildings that are important to you. For instance, you might value having a school
and a gym near your apartment. The list of blocks that you have contains information at every block about all of the buildings that
are present and absent at the block in question. For instance, for every block, you might know whether a school, a pool, an office,
and a gym are present.

In order to optimize your life, you want to pick an apartment block such that you minimize the farthest distance you'd have to walk
from your apartment to reach any of your required buildings.

Write a function that takes in a list of contiguous blocks on a specific street and a list of your required buildings and that
returns the location (the index) of the block that's most optimal for you.

If there are multiple most optimal blocks, your function can return the index of any one of them.


## Sample Input:
```
blocks = [
    {"gym": False, "school": True, "store": False},
    {"gym": True, "school": False, "store": False},
    {"gym": True, "school": True, "store": False},
    {"gym": False, "school": True, "store": False},
    {"gym": False, "school": True, "store": True},
]

reqs = ["gym", "school", "store"]
```

## Sample Output:
```
3 // at index 3, the farthest you'd have to walk to reach a gym, a school, or a store is 1 block; at any other index,
  you'd have to walk farther
```

## Optimal Time & Space Complexity:
```
O(b * r) time | O(b) space - where `b` is the number of blocks and `r` is the number of requirements.
```

"""

# =========================================================================================================================== #

# Solution:


# O(b * r) time | O(b) space
def apartment_hunting(blocks, reqs):
    # Initialize a dictionary to store minimum distances for each requirement
    # For each requirement, create a list to store min distances for each block
    num_blocks = len(blocks)
    min_distances = {req: [float("inf")] * num_blocks for req in reqs}

    # First pass: Left to Right
    # For each requirement, calculate the closest instance to the left of each block
    for req in reqs:
        closest_req = float("inf")  # Tracks the closest requirement seen so far
        for i in range(num_blocks):
            if blocks[i][req]:  # If current block has the requirement
                closest_req = i  # Update closest requirement position
            # Store distance to closest requirement (left if not found yet)
            min_distances[req][i] = (
                abs(i - closest_req) if closest_req != float("inf") else float("inf")
            )

    # Second pass: Right to Left
    # For each requirement, calculate the closest instance to the right of each block
    # and keep the minimum of left and right distances
    for req in reqs:
        closest_req = float("inf")  # Reset closest requirement tracker
        for i in range(num_blocks - 1, -1, -1):  # Iterate from right to left
            if blocks[i][req]:  # If current block has the requirement
                closest_req = i  # Update closest requirement position
            # Compare with left pass result and store the minimum distance
            min_distances[req][i] = min(
                min_distances[req][i],
                abs(i - closest_req) if closest_req != float("inf") else float("inf"),
            )

    # Calculate the maximum distance across all requirements for each block
    max_distances_at_blocks = [
        max(
            min_distances[req][i] for req in reqs
        )  # Max distance for this block across all reqs
        for i in range(num_blocks)
    ]

    # Return the index of the block with the smallest maximum distance
    return max_distances_at_blocks.index(min(max_distances_at_blocks))


# Test Cases:

blocks = [
    {"gym": False, "school": True, "store": False},
    {"gym": True, "school": False, "store": False},
    {"gym": True, "school": True, "store": False},
    {"gym": False, "school": True, "store": False},
    {"gym": False, "school": True, "store": True},
]

reqs = ["gym", "school", "store"]

blocks_2 = [
    {"gym": False, "office": True, "school": True, "store": False},
    {"gym": True, "office": False, "school": False, "store": False},
    {"gym": True, "office": False, "school": True, "store": False},
    {"gym": False, "office": False, "school": True, "store": False},
    {"gym": False, "office": False, "school": True, "store": True},
]

reqs_2 = ["gym", "office", "school", "store"]

print(apartment_hunting(blocks, reqs))  # Output: 3
print(apartment_hunting(blocks_2, reqs_2))  # Output: 2

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### **Time Complexity Analysis**

1. **Initialization of `min_distances`:**
   - We initialize a dictionary `min_distances` where each key is a requirement (`req`) and the value is a list of size
   `num_blocks` (initialized to `inf`).
   - This takes **O(R × B)** time, where:
     - `R` = number of requirements (`len(reqs)`).
     - `B` = number of blocks (`num_blocks`).

2. **First Pass (Left to Right):**
   - For each requirement (`req`), we iterate over all blocks (`B` times).
   - For each block, we perform **O(1)** operations (checking if the requirement is present and updating `min_distances`).
   - This pass takes **O(R × B)** time.

3. **Second Pass (Right to Left):**
   - Similar to the first pass, we iterate over each requirement and each block in reverse.
   - Again, this takes **O(R × B)** time.

4. **Compute `max_distances_at_blocks`:**
   - For each block (`B` iterations), we compute the maximum distance across all requirements (`R` operations per block).
   - This takes **O(B × R)** time.

5. **Finding the Minimum Maximum Distance:**
   - We find the index of the minimum value in `max_distances_at_blocks` (which is **O(B)** time).

**Total Time Complexity**:
- The dominant operations are the two passes and the computation of `max_distances_at_blocks`, each taking **O(R × B)** time.
- Thus, the total time complexity is:
  
  O(R * B) + O(R * B) + O(R * B) + O(B) = O(R * B)
  

### **Space Complexity Analysis**

1. **`min_distances` Dictionary:**
   - Stores `R` keys, each mapping to a list of size `B`.
   - This takes **O(R × B)** space.

2. **`max_distances_at_blocks` List:**
   - A list of size `B` (stores the maximum distance for each block).
   - This takes **O(B)** space.

3. **Other Variables:**
   - `closest_req`, loop counters, etc., use **O(1)** space.

**Total Space Complexity**:
- The dominant term is the `min_distances` dictionary, which takes **O(R × B)** space.
- Thus, the total space complexity is: O(R * B)

### **Final Answer**
- **Time Complexity:** **O(R × B)**
- **Space Complexity:** **O(R × B)**

Where:
- `R` = number of requirements (`len(reqs)`).
- `B` = number of blocks (`len(blocks)`).

"""
