# Merging Linked Lists

You're given two Linked Lists of potentially unequal length. These Linked Lists potentially merge at a shared intersection node. Write a function that returns the intersection node or returns `None` if there is no intersection.

Each `LinkedList` node has an integer `value` as well as a `next` node pointing to the next node in the list or to `None` if it's the tail of the list.

> Note: Your function should return an existing node. It should not modify either Linked List, and it should not create any new Linked Lists.

## Sample Input

```plaintext
linkedList_one = 2 -> 3 -> 1 -> 4 -> None
linkedList_two = 8 -> 7 -> 1 -> 4 -> None
```

## Sample Output

```plaintext
1 -> 4 -> None

// The lists intersect at the node with value 1
```

## Hints

<details>
<summary><b>Hint 1</b></summary>

All of the nodes after the intersection point of two Linked Lists will be the same.

</details>

<details>
<summary><b>Hint 2</b></summary>

If the two Linked Lists are of different lengths, then none of the extra nodes of the longer list at the beginning can be the intersection point, since the ends must be the same.

</details>

<details>
<summary><b>Hint 3</b></summary>

The length of the first list + the distance of the second head from the intersection point will be equal to the length of the second list + the distance of the first head from the intersection point. This can be proven using the information from `Hints #1` and `#2`.

</details>

## Optimal Time & Space Complexity

`O(n + m)` time | `O(1)` space - where `n` is the length of the first Linked List and `m` is the length of the second Linked List.
