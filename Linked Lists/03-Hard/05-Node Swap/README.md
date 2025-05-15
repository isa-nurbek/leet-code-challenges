# Node Swap

Write a function that takes in the head of a Singly Linked List, swaps every pair of adjacent nodes in place (i.e., doesn't create a brand new list), and returns its new head.

If the input Linked List has an odd number of nodes, its final node should remain the same.

Each `LinkedList` node has an integer `value` as well as a `next` node pointing to the next node in the list or to `None` if it's the tail of the list.

You can assume that the input Linked List will always have at least one node; in other words, the head will never be `None`.

## Sample Input

```plaintext
head = 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> None

// The head node with value 0
```

## Sample Output

```plaintext
1 -> 0 -> 3 -> 2 -> 5 -> 4 -> None

// The new head node with value 1 
```

## Hints

<details>
<summary><b>Hint 1</b></summary>

Each node in the linked list points to the `next` node in the linked list. How would you modify the `next` pointers of two nodes in order to swap them?

</details>

<details>
<summary><b>Hint 2</b></summary>

Can you apply what you come up with from `Hint #1` in order to solve this problem recursively?

</details>

<details>
<summary><b>Hint 3</b></summary>

To solve this problem `recursively`, have each recursive call swap a pair of nodes and then return the first node of the swapped pair (the node that was originally the second node in the pair). Also, have each recursive call make the second node of the swapped pair (the node that was originally the first node in the pair) point to the result of the next recursive call. The next recursive call should take in the first node of the next pair as its input parameter.

</details>

<details>
<summary><b>Hint 4</b></summary>

Implementing this problem `iteratively` can improve the space complexity of the solution. Intuitively, you need swap nodes while traversing the entire linked list. To do this, you'll need to reference and change the pointers of three nodes at a time. You'll also need to create a placeholder node that points to the head of the linked list, so that at the end of the traversal, you can still reference the new head that you have to return.

</details>

## Optimal Time & Space Complexity

`O(n)` time | `O(1)` space - where `n` is the number of nodes in the Linked List.
