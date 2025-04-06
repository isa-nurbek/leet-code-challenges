# Remove Duplicates From Linked List

You're given the head of a Singly Linked List whose nodes are in sorted order with respect to their values. Write a function that returns a modified version of the Linked List that doesn't contain any nodes with duplicate values. The Linked List should be modified in place (i.e., you shouldn't create a brand new list), and the modified Linked List should still have its nodes sorted with respect to their values.

Each `LinkedList` node has an integer `value` as well as a `next` node pointing to the next node in the list or to `None` / `null` if it's the tail of the list.

## Sample Input

```plaintext
linked_list = {
    "head": "1",
    "nodes": [
        {"id": "1", "next": "1-2", "value": 1},
        {"id": "1-2", "next": "1-3", "value": 1},
        {"id": "1-3", "next": "2", "value": 1},
        {"id": "2", "next": "3", "value": 3},
        {"id": "3", "next": "3-2", "value": 4},
        {"id": "3-2", "next": "3-3", "value": 4},
        {"id": "3-3", "next": "4", "value": 4},
        {"id": "4", "next": "5", "value": 5},
        {"id": "5", "next": "5-2", "value": 6},
        {"id": "5-2", "next": None, "value": 6},
    ],
}

The List Looks Like: [1] -> [1] -> [3] -> [4] -> [4] -> [4] -> [5] -> [6] -> [6] -> None // the head node with value 1
```

## Sample Output

```plaintext
1 -> 3 -> 4 -> 5 -> 6 -> None // the head node with value 1
```

## Optimal Time & Space Complexity

`O(n)` time | `O(1)` space - where `n` is the number of nodes in the Linked List.
