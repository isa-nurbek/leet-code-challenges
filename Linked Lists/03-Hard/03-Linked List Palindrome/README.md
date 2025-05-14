# Linked List Palindrome

Write a function that takes in the head of a Singly Linked List and returns a `boolean` representing whether the linked list's nodes form a palindrome. Your function shouldn't make use of any auxiliary data structure.

A palindrome is usually defined as a string that's written the same `forward` and `backward`. For a linked list's nodes to form a palindrome, their values must be the same when read from left to right and from right to left.
> Note that single-character strings are palindromes, which means that single-node linked lists form palindromes.

Each `LinkedList` node has an integer `value` as well as a `next` node pointing to the next node in the list or to `None` if it's the tail of the list.

You can assume that the input linked list will always have at least one node; in other words, the head will never be `None`.

## Sample Input

```plaintext
head = 0 -> 1 -> 2 -> 2 -> 1 -> 0 -> None

// The head node with value 0
```

## Sample Output

```plaintext
True
```

## Hints

<details>
<summary><b>Hint 1</b></summary>

Think about comparing two nodes at a time. To determine if the linked list's nodes form a palindrome, which two nodes should we compare?

</details>

<details>
<summary><b>Hint 2</b></summary>

Following `Hint #1`, to determine if the linked list's nodes form a palindrome, we'll want to compare the first and last node, the second and second-to-last node, the third and third-to-last node, etc.. How can we compare all of these nodes recursively?

</details>

<details>
<summary><b>Hint 3</b></summary>

Putting aside the recursive solution hinted at in `Hint #2`, we can solve this problem iteratively and with no auxiliary space if we know how to reverse a linked list. How can reversing the linked list (or part of it) help us solve this problem?

</details>

<details>
<summary><b>Hint 4</b></summary>

Try reversing the second half of the linked list and then comparing nodes in the first half and in the reversed second half by simply iterating through both halves at the same time. You'll have to figure out where the second half of the linked list begins in order to reverse it.

</details>

## Optimal Time & Space Complexity

`O(n)` time | `O(1)` space - where `n` is the number of nodes in the Linked List.
