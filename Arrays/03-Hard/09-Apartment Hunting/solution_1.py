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
  {
    "gym": false,
    "school": true,
    "store": false,
  },
  {
    "gym": true,
    "school": false,
    "store": false,
  },
  {
    "gym": true,
    "school": true,
    "store": false,
  },
  {
    "gym": false,
    "school": true,
    "store": false,
  },
  {
    "gym": false,
    "school": true,
    "store": true,
  },
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
O(br) time | O(br) space - where `b` is the number of blocks and `r` is the number of requirements.
```

"""

# =========================================================================================================================== #

# Solution:


# O(b² * r) time | O(b) space
def apartment_hunting(blocks, reqs):
    max_distances_at_blocks = [float("-inf") for block in blocks]

    for i in range(len(blocks)):
        for req in reqs:
            closest_req_distance = float("inf")

            for j in range(len(blocks)):
                if blocks[j][req]:
                    closest_req_distance = min(
                        closest_req_distance, distance_between(i, j)
                    )

            max_distances_at_blocks[i] = max(
                max_distances_at_blocks[i], closest_req_distance
            )

    return get_idx_at_min_value(max_distances_at_blocks)


def get_idx_at_min_value(array):
    idx_at_min_value = 0
    min_value = float("inf")

    for i in range(len(array)):
        current_value = array[i]

        if current_value < min_value:
            min_value = current_value
            idx_at_min_value = i

    return idx_at_min_value


def distance_between(a, b):
    return abs(a - b)


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
