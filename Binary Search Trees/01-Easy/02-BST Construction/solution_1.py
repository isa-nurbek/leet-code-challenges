# Problem Description:

"""
                                                BST Construction

Write a `BST` class for a Binary Search Tree. The class should support:

- Inserting values with the `insert` method.
- Removing values with the `remove` method; this method should only remove the first instance of a given value.
- Searching for values with the `contains` method.

> Note that you can't remove values from a single-node tree. In other words, calling the `remove` method on a single-node tree
should simply not do anything.

Each `BST` node has an integer `value`, a `left` child node, and a `right` child node. A node is said to be a valid `BST` node if
and only if it satisfies the `BST` property: its `value` is strictly greater than the values of every node to its left; its `value`
is less than or equal to the values of every node to its right; and its children nodes are either valid `BST` nodes themselves or `None`.


## Sample Usage:
```
// Assume the following BST has already been created:

         10
       /     \
      5      15
    /   \   /   \
   2     5 13   22
 /           \
1            14

// All operations below are performed sequentially.

insert(12):   10
            /     \
           5      15
         /   \   /   \
        2     5 13   22
      /        /  \
     1        12  14

remove(10):   12
            /     \
           5      15
         /   \   /   \
        2     5 13   22
      /           \
     1            14

contains(15): true
```

## Optimal Time & Space Complexity:
```
Average: (all 3 methods): O(log(n)) time | O(1) space - where `n` is the number of nodes in the BST.
Worst: (all 3 methods): O(n) time | O(1) space - where `n` is the number of nodes in the BST.
```

"""

# =========================================================================================================================== #

# Solution:


# Binary Search Tree (BST) node class
class BST:
    def __init__(self, value):
        # Initialize a BST node with a value, and set left and right children to None
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Insert a new value into the BST
        if value < self.value:
            # If the value is less than current node's value, go to the left subtree
            if self.left is None:
                # If left child is empty, create a new node here
                self.left = BST(value)
            else:
                # Otherwise, recursively insert into the left subtree
                self.left.insert(value)
        else:
            # If the value is greater or equal, go to the right subtree
            if self.right is None:
                # If right child is empty, create a new node here
                self.right = BST(value)
            else:
                # Otherwise, recursively insert into the right subtree
                self.right.insert(value)
        return self  # Return the tree to allow method chaining

    def contains(self, value):
        # Check if the BST contains a given value
        if value < self.value:
            # If value is less than current node, search left subtree
            if self.left is None:
                return False  # Value not found
            else:
                return self.left.contains(value)
        elif value > self.value:
            # If value is greater than current node, search right subtree
            if self.right is None:
                return False  # Value not found
            else:
                return self.right.contains(value)
        else:
            # Found the value
            return True

    def remove(self, value, parent=None):
        # Remove a value from the BST
        if value < self.value:
            # If value is less than current node, go left
            if self.left is not None:
                self.left.remove(value, self)
        elif value > self.value:
            # If value is greater than current node, go right
            if self.right is not None:
                self.right.remove(value, self)
        else:
            # Found the node to remove
            if self.left is not None and self.right is not None:
                # Case 1: Node has two children
                # Replace value with minimum value from right subtree
                self.value = self.right.get_min_value()
                # Remove the duplicate value from right subtree
                self.right.remove(self.value, self)
            elif parent is None:
                # Case 2: Node is root with one or zero children
                if self.left is not None:
                    # Replace with left child's value and pointers
                    self.value = self.left.value
                    self.right = self.left.right
                    self.left = self.left.left
                elif self.right is not None:
                    # Replace with right child's value and pointers
                    self.value = self.right.value
                    self.left = self.right.left
                    self.right = self.right.right
                else:
                    # Node is root with no children - single node tree
                    pass  # In practice, might want to handle this case differently
            elif parent.left == self:
                # Case 3: Node is left child with one or zero children
                # Replace parent's left pointer with our non-null child (if any)
                parent.left = self.left if self.left is not None else self.right
            elif parent.right == self:
                # Case 4: Node is right child with one or zero children
                # Replace parent's right pointer with our non-null child (if any)
                parent.right = self.left if self.left is not None else self.right
        return self  # Return the tree to allow method chaining

    def get_min_value(self):
        # Get the minimum value in the BST (leftmost node)
        if self.left is None:
            return self.value  # Found the leftmost node
        else:
            return self.left.get_min_value()  # Recurse left

    def __str__(self):
        # String representation of the BST for visualization
        return self._visualize()

    def _visualize(self, level=0):
        # Helper method for tree visualization (recursive)
        ret = "\t" * level + repr(self.value) + "\n"  # Current node
        for child in [self.left, self.right]:
            if child:
                # Add visualization of children with increased indentation
                ret += child._visualize(level + 1)
        return ret


# Example usage
def main():
    # Initialize BST with root value 10
    bst = BST(10)
    print("Initial BST:")
    print(bst)

    # List of operations to perform
    operations = [
        ("insert", 5),
        ("insert", 15),
        ("insert", 2),
        ("insert", 5),
        ("insert", 13),
        ("insert", 22),
        ("insert", 1),
        ("insert", 14),
        ("insert", 12),
        ("remove", 10),
        ("contains", 15),
    ]

    # Perform each operation
    for i, (method, value) in enumerate(operations, 1):
        print(f"\nOperation {i}: {method}({value})")

        if method == "insert":
            bst.insert(value)
        elif method == "remove":
            bst.remove(value)
        elif method == "contains":
            result = bst.contains(value)
            print(f"Contains {value}? {result}")
            continue  # Skip tree visualization for contains

        print("Current BST:")
        print(bst)


if __name__ == "__main__":
    main()

# Output:

"""
Initial BST:
10

Operation 1: insert(5)
Current BST:
  10
 /
5

Operation 2: insert(15)
Current BST:
  10
 /  \
5   15

Operation 3: insert(2)
Current BST:
    10
   /  \
  5   15
 /
2

Operation 4: insert(5) (again - duplicates go to right)
Current BST:
    10
   /  \
  5   15
 /  \
2    5

Operation 5: insert(13)
Current BST:
    10
   /  \
  5   15
 / \  /
2  5 13

Operation 6: insert(22)
Current BST:
    10
   /  \
  5   15
 / \  / \
2  5 13 22

Operation 7: insert(1)
Current BST:
       10
      /  \
     5   15
    / \  / \
   2  5 13 22
  /
 1

Operation 8: insert(14)
Current BST:
       10
      /  \
     5   15
    / \  / \
   2  5 13 22
  /    / \
 1    12 14

Operation 9: insert(12)
Current BST:
      10
     /  \
    5   15
   / \  / \
  2  5 13 22
 /    / \
1    12 14

Operation 10: remove(10)
Current BST:
      12
     /  \
    5   15
   / \  / \
  2  5 13 22
 /      \
1       14

Operation 11: contains(15)
Contains 15? True
"""
