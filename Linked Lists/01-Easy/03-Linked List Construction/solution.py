# Problem Description:

"""
                                            Linked List Construction

Write a `DoublyLinkedList` class that has a `head` and a `tail`, both of which point to either a linked list `Node` or `None`.
The class should support:

- Setting the head and tail of the linked list.
- Inserting nodes before and after other nodes as well as at given positions (the position of the head node is `1`).
- Removing given nodes and removing nodes with given values.
- Searching for nodes with given values.

Note that the `setHead`, `setTail`, `insertBefore`, `insertAfter`, `insertAtPosition`, and `remove` methods all take in actual
`Node`s as input parameters—not integers (except for `insertAtPosition`, which also takes in an integer representing the position);
this means that you don't need to create any new `Node`s in these methods. The input nodes can be either stand-alone nodes or nodes
that are already in the linked list. If they're nodes that are already in the linked list, the methods will effectively be moving
the nodes within the linked list. You won't be told if the input nodes are already in the linked list, so your code will have to
defensively handle this scenario.

Each `Node` has an integer `value` as well as a `prev` node and a `next` node, both of which can point to either another node or
`None`.

## Sample Usage:
```
// Assume the following linked list has already been created:
1 <-> 2 <-> 3 <-> 4 <-> 5

// Assume that we also have the following stand-alone nodes:
3, 3, 6

setHead(4): 4 <-> 1 <-> 2 <-> 3 <-> 5 // set the existing node with value 4 as the head
setTail(6): 4 <-> 1 <-> 2 <-> 3 <-> 5 <-> 6 // set the stand-alone node with value 6 as the tail
insertBefore(6, 3): 4 <-> 1 <-> 2 <-> 5 <-> 3 <-> 6 // move the existing node with value 3 before the existing node with value 6
insertAfter(6, 3): 4 <-> 1 <-> 2 <-> 5 <-> 3 <-> 6 <-> 3 // insert a stand-alone node with value 3 after the existing node with value 6
insertAtPosition(1, 3): 3 <-> 4 <-> 1 <-> 2 <-> 5 <-> 3 <-> 6 <-> 3 // insert a stand-alone node with value 3 in position 1
removeNodesWithValue(3): 4 <-> 1 <-> 2 <-> 5 <-> 6 // remove all nodes with value 3
remove(2): 4 <-> 1 <-> 5 <-> 6 // remove the existing node with value 2
containsNodeWithValue(5): True
```

## Optimal Time & Space Complexity:
```
`setHead`, `setTail`, `insertBefore`, `insertAfter`, and `remove`: `O(1)` time | `O(1)` space.
`insertAtPosition`: `O(p)` time | `O(1)` space - where `p` is input position.
`removeNodesWithValue`, `containsNodeWithValue`: `O(n)` time | `O(1)` space - where `n` is the number of nodes in the linked list.
```

"""

# =========================================================================================================================== #

# Solution:


class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)

    def setTail(self, node):
        if self.tail is None:
            self.setHead(node)
            return
        self.insertAfter(self.tail, node)

    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)
            return
        current = self.head
        currentPosition = 1
        while current is not None and currentPosition < position:
            current = current.next
            currentPosition += 1
        if current is not None:
            self.insertBefore(current, nodeToInsert)
        else:
            self.setTail(nodeToInsert)

    def removeNodesWithValue(self, value):
        current = self.head
        while current is not None:
            nodeToRemove = current
            current = current.next
            if nodeToRemove.value == value:
                self.remove(nodeToRemove)

    def remove(self, node):
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
        self._removeNodeBindings(node)

    def containsNodeWithValue(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def _removeNodeBindings(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.prev = None
        node.next = None


# Helper function to create a node from the given dictionary
def create_node(node_dict, nodes_map):
    if node_dict["id"] in nodes_map:
        return nodes_map[node_dict["id"]]
    node = Node(node_dict["value"])
    nodes_map[node_dict["id"]] = node
    return node


# Helper function to link nodes based on the given dictionary
def link_nodes(nodes_list, nodes_map):
    for node_dict in nodes_list:
        node = nodes_map[node_dict["id"]]
        if node_dict["next"] is not None:
            node.next = nodes_map[node_dict["next"]]
        if node_dict["prev"] is not None:
            node.prev = nodes_map[node_dict["prev"]]


# Main function to test the DoublyLinkedList with the provided test case
def test_doubly_linked_list():
    nodes = [
        {"id": "1", "next": None, "prev": None, "value": 1},
        {"id": "2", "next": None, "prev": None, "value": 2},
        {"id": "3", "next": None, "prev": None, "value": 3},
        {"id": "3-2", "next": None, "prev": None, "value": 3},
        {"id": "3-3", "next": None, "prev": None, "value": 3},
        {"id": "4", "next": None, "prev": None, "value": 4},
        {"id": "5", "next": None, "prev": None, "value": 5},
        {"id": "6", "next": None, "prev": None, "value": 6},
    ]
    class_methods_to_call = [
        {"arguments": ["5"], "method": "setHead"},
        {"arguments": ["4"], "method": "setHead"},
        {"arguments": ["3"], "method": "setHead"},
        {"arguments": ["2"], "method": "setHead"},
        {"arguments": ["1"], "method": "setHead"},
        {"arguments": ["4"], "method": "setHead"},
        {"arguments": ["6"], "method": "setTail"},
        {"arguments": ["6", "3"], "method": "insertBefore"},
        {"arguments": ["6", "3-2"], "method": "insertAfter"},
        {"arguments": [1, "3-3"], "method": "insertAtPosition"},
        {"arguments": [3], "method": "removeNodesWithValue"},
        {"arguments": ["2"], "method": "remove"},
        {"arguments": [5], "method": "containsNodeWithValue"},
    ]

    nodes_map = {}
    for node_dict in nodes:
        create_node(node_dict, nodes_map)

    dll = DoublyLinkedList()

    for method_call in class_methods_to_call:
        method_name = method_call["method"]
        args = method_call["arguments"]
        if method_name == "setHead":
            dll.setHead(nodes_map[args[0]])
        elif method_name == "setTail":
            dll.setTail(nodes_map[args[0]])
        elif method_name == "insertBefore":
            dll.insertBefore(nodes_map[args[0]], nodes_map[args[1]])
        elif method_name == "insertAfter":
            dll.insertAfter(nodes_map[args[0]], nodes_map[args[1]])
        elif method_name == "insertAtPosition":
            dll.insertAtPosition(args[0], nodes_map[args[1]])
        elif method_name == "removeNodesWithValue":
            dll.removeNodesWithValue(args[0])
        elif method_name == "remove":
            dll.remove(nodes_map[args[0]])
        elif method_name == "containsNodeWithValue":
            result = dll.containsNodeWithValue(args[0])
            print(f"containsNodeWithValue({args[0]}): {result}")

    # Print the final state of the linked list
    current = dll.head
    print("Final linked list from head to tail:")
    while current is not None:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

    current = dll.tail
    print("Final linked list from tail to head:")
    while current is not None:
        print(current.value, end=" -> ")
        current = current.prev
    print("None")


test_doubly_linked_list()

# Output:

"""
containsNodeWithValue(5): True
Final linked list from head to tail:
4 -> 1 -> 5 -> 6 -> None
Final linked list from tail to head:
6 -> 5 -> 1 -> 4 -> None
"""
