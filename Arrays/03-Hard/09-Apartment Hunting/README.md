# Apartment Hunting

You're looking to move into a new apartment on specific street, and you're given a list of contiguous blocks on that street where each block contains an apartment that you could move into.

You also have a list of requirements: a list of buildings that are important to you. For instance, you might value having a school and a gym near your apartment. The list of blocks that you have contains information at every block about all of the buildings that are present and absent at the block in question. For instance, for every block, you might know whether a school, a pool, an office, and a gym are present.

In order to optimize your life, you want to pick an apartment block such that you minimize the farthest distance you'd have to walk from your apartment to reach any of your required buildings.

Write a function that takes in a list of contiguous blocks on a specific street and a list of your required buildings and that returns the location `(the index)` of the block that's most optimal for you.

If there are multiple most optimal blocks, your function can return the `index of any one of them`.

## Sample Input

```plaintext
blocks = [
    {"gym": False, "school": True, "store": False},
    {"gym": True, "school": False, "store": False},
    {"gym": True, "school": True, "store": False},
    {"gym": False, "school": True, "store": False},
    {"gym": False, "school": True, "store": True},
]

reqs = ["gym", "school", "store"]
```

## Sample Output

```plaintext
3

"""
At index 3, the farthest you'd have to walk to reach a gym, a school, or a store is 1 block.
At any other index, you'd have to walk farther
"""
```

## Hints

<details>
<summary><b>Hint 1</b></summary>

For every block, you want to go through every requirement, and for every requirement, you want to find the closest other block with that requirement (or rather, the smallest distance to another block with that requirement). Once you've done that for every requirement and for every block, you want to pick, for every block, the distance of the farthest requirement. You can do this with three nested "for" loops.

</details>

<details>
<summary><b>Hint 2</b></summary>

Is there a way to optimize on the solution mentioned in `Hint #1` (that uses three nested "for" loops) by precomputing the smallest distances of every requirement from every block?

</details>

<details>
<summary><b>Hint 3</b></summary>

For every requirement, you should be able to precompute its smallest distances from every block by doing two simple passes though the array of blocks: one pass from left to right and one pass from right to left. Once you have these precomputed values, you can iterate through all of the blocks and pick the biggest of all the precomputed distances at that block.

</details>

<details>
<summary><b>Hint 4</b></summary>

The slopes of the two diagonals of a square are always negative reciprocals of each other.

</details>

## Optimal Time & Space Complexity

`O(b * r)` time | `O(b)` space - where `b` is the number of blocks and `r` is the number of requirements.
