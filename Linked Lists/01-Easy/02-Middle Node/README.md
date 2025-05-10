# Middle Node

You're given a Linked List with at least one node. Write a function that returns the middle node of the Linked List. If there are two middle nodes (i.e. an even length list), your function should return the second of these nodes.

Each `LinkedList` node has an integer `value` as well as a `next` node pointing to the next node in the list or to `None` if it's the tail of the list.

## Sample Input

```plaintext
linked_list = 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> None
```

## Sample Output

```plaintext
3 -> 5 -> None

// The middle could be 7 or 3, we return the second middle node
```

## Hints

<details>
<summary><b>Hint 1</b></summary>

The middle node of a Linked List will always be at index `length / 2`.

</details>

<details>
<summary><b>Hint 2</b></summary>

While the LinkedList class has no length, you can calculate it by simply iterating through the entire list.

</details>

<details>
<summary><b>Hint 3</b></summary>

If you create a slow and a fast pointer, with the fast one iterating at twice the speed, the slow one will be in the middle when the fast one reaches the end.

</details>

## Optimal Time & Space Complexity

`O(n)` time | `O(1)` space - where `n` is the number of nodes in the linked list.
