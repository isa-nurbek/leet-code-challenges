# Remove Duplicates From Linked List

You're given the head of a Singly Linked List whose nodes are in `sorted or unsorted order` with respect to their values. Write a function that returns a modified version of the linked list where `all nodes with duplicate values are removed`, leaving only distinct values. Modify the list in place (do not create a new list). The relative order of the remaining nodes should preserve their original order (whether sorted or unsorted).

Each `LinkedList` node has an integer `value` as well as a `next` node pointing to the next node in the list or to `None` / `null` if it's the tail of the list.

## Sample Input With Sorted Linked List

```plaintext
sorted_linked_list_dict = {
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

## Sample Output With Sorted Linked List

```plaintext
1 -> 3 -> 4 -> 5 -> 6 -> None // the head node with value 1
```

---

## Sample Input With Unsorted Linked List

```plaintext
unsorted_linked_list_dict = {
    "head": "a",
    "nodes": [
        {"id": "a", "next": "b", "value": 3},
        {"id": "b", "next": "c", "value": 1},
        {"id": "c", "next": "d", "value": 4},
        {"id": "d", "next": "e", "value": 1},
        {"id": "e", "next": "f", "value": 5},
        {"id": "f", "next": "g", "value": 3},
        {"id": "g", "next": None, "value": 2},
    ],
}


The List Looks Like: [3] → [1] → [4] → [1] → [5] → [3] → [2] → None  // the head node with value 3
```

## Sample Output With Unsorted Linked List

```plaintext
3 -> 1 -> 4 -> 5 -> 2 -> None  // the head node with value 3
```

## Optimal Time & Space Complexity

`O(n)` time | `O(1)` space - where `n` is the number of nodes in the Linked List.
