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
        # Node class represents each element in the doubly linked list
        self.value = value  # The value stored in the node
        self.prev = None  # Reference to the previous node
        self.next = None  # Reference to the next node


class DoublyLinkedList:
    def __init__(self):
        # Initialize an empty doubly linked list
        self.head = None  # First node in the list
        self.tail = None  # Last node in the list

    def setHead(self, node):
        # Make the given node the new head of the list
        if self.head is None:
            # If list is empty, set both head and tail to the node
            self.head = node
            self.tail = node
            return
        # Otherwise insert the node before current head
        self.insertBefore(self.head, node)

    def setTail(self, node):
        # Make the given node the new tail of the list
        if self.tail is None:
            # If list is empty, use setHead (which handles empty list case)
            self.setHead(node)
            return
        # Otherwise insert the node after current tail
        self.insertAfter(self.tail, node)

    def insertBefore(self, node, nodeToInsert):
        # Insert nodeToInsert immediately before the given node
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            # If nodeToInsert is the only node in the list, do nothing
            return

        # First remove the node from its current position if it's in the list
        self.remove(nodeToInsert)

        # Update the nodeToInsert's pointers
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node

        # Update surrounding nodes' pointers
        if node.prev is None:
            # If inserting before head, update head
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        # Insert nodeToInsert immediately after the given node
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            # If nodeToInsert is the only node in the list, do nothing
            return

        # First remove the node from its current position if it's in the list
        self.remove(nodeToInsert)

        # Update the nodeToInsert's pointers
        nodeToInsert.prev = node
        nodeToInsert.next = node.next

        # Update surrounding nodes' pointers
        if node.next is None:
            # If inserting after tail, update tail
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        # Insert node at specified position (1-based indexing)
        if position == 1:
            self.setHead(nodeToInsert)
            return

        current = self.head
        currentPosition = 1
        # Traverse to find the node at the given position
        while current is not None and currentPosition < position:
            current = current.next
            currentPosition += 1

        if current is not None:
            # If position exists, insert before the found node
            self.insertBefore(current, nodeToInsert)
        else:
            # If position is beyond list length, append to end
            self.setTail(nodeToInsert)

    def removeNodesWithValue(self, value):
        # Remove all nodes with the given value
        current = self.head
        while current is not None:
            # Store next node before removing current
            nodeToRemove = current
            current = current.next
            if nodeToRemove.value == value:
                self.remove(nodeToRemove)

    def remove(self, node):
        # Remove the given node from the list
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
        # Clean up the node's pointers
        self._removeNodeBindings(node)

    def containsNodeWithValue(self, value):
        # Check if list contains a node with given value
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def _removeNodeBindings(self, node):
        # Helper method to clean up a node's pointers when removed
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.prev = None
        node.next = None


# Helper function to create a node from the given dictionary
def create_node(node_dict, nodes_map):
    # Check if node already exists in the map
    if node_dict["id"] in nodes_map:
        return nodes_map[node_dict["id"]]
    # Create new node and add to map
    node = Node(node_dict["value"])
    nodes_map[node_dict["id"]] = node
    return node


# Helper function to link nodes based on the given dictionary
def link_nodes(nodes_list, nodes_map):
    # Set up next and prev pointers based on the input dictionary
    for node_dict in nodes_list:
        node = nodes_map[node_dict["id"]]
        if node_dict["next"] is not None:
            node.next = nodes_map[node_dict["next"]]
        if node_dict["prev"] is not None:
            node.prev = nodes_map[node_dict["prev"]]


# Main function to test the DoublyLinkedList with the provided test case
def test_doubly_linked_list():
    # Test data: nodes and operations to perform
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

    # Create all nodes and store them in a map
    nodes_map = {}
    for node_dict in nodes:
        create_node(node_dict, nodes_map)

    # Create the doubly linked list
    dll = DoublyLinkedList()

    # Execute all the operations in the test case
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
    print("\nFinal state of the linked list:")
    # Print from head to tail
    current = dll.head
    print("Head to tail:")
    while current is not None:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

    # Print from tail to head
    current = dll.tail
    print("Tail to head:")
    while current is not None:
        print(current.value, end=" -> ")
        current = current.prev
    print("None")


test_doubly_linked_list()

# Output:

"""
containsNodeWithValue(5): True

Final state of the linked list:
Head to tail:
4 -> 1 -> 5 -> 6 -> None
Tail to head:
6 -> 5 -> 1 -> 4 -> None
"""
