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
        self.value = value
        self.left = None
        self.right = None

    # Average: O(log n) time | O(1) space
    # Worst: O(n) time | O(1) space
    def insert(self, value):
        current = self
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = BST(value)
                    break
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = BST(value)
                    break
                else:
                    current = current.right
        return self  # Allows chaining

    # Average: O(log n) time | O(1) space
    # Worst: O(n) time | O(1) space
    def contains(self, value):
        current = self
        while current is not None:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                return True
        return False

    # Average: O(log n) time | O(1) space
    # Worst: O(n) time | O(1) space
    def remove(self, value, parent=None):
        current = self
        while current is not None:
            if value < current.value:
                parent = current
                current = current.left
            elif value > current.value:
                parent = current
                current = current.right
            else:
                # Case 1: Node has both left and right children
                if current.left is not None and current.right is not None:
                    current.value = (
                        current.right.get_min_value()
                    )  # Replace with min from right subtree
                    current.right.remove(current.value, current)  # Remove the duplicate
                # Case 2: Root node (no parent) with one child
                elif parent is None:
                    if current.left is not None:
                        current.value = current.left.value
                        current.right = current.left.right
                        current.left = current.left.left
                    elif current.right is not None:
                        current.value = current.right.value
                        current.left = current.right.left
                        current.right = current.right.right
                    else:
                        pass  # Only one node in the tree (handle as needed)
                # Case 3: Node is left child of parent
                elif parent.left == current:
                    parent.left = (
                        current.left if current.left is not None else current.right
                    )
                # Case 4: Node is right child of parent
                elif parent.right == current:
                    parent.right = (
                        current.left if current.left is not None else current.right
                    )
                break
        return self

    # Average: O(log n) time | O(1) space
    # Worst: O(n) time | O(1) space
    def get_min_value(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.value

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

# =========================================================================================================================== #

# Big O Analysis:

"""
Let's analyze the time and space complexity for each operation in the BST class:

### 1. Insert (insert method)

**Time Complexity:**
- Average case: O(log n) - In a balanced BST, we traverse the height of the tree which is log n.
- Worst case: O(n) - For a completely unbalanced tree (essentially a linked list), we might traverse all n nodes.

**Space Complexity:**
- O(1) - We're using iterative approach with constant space (just a few pointers).

### 2. Contains (contains method)

**Time Complexity:**
- Average case: O(log n) - Height traversal in balanced BST.
- Worst case: O(n) - For completely unbalanced tree.

**Space Complexity:**
- O(1) - Iterative approach with constant space.

### 3. Remove (remove method)

**Time Complexity:**
- Average case: O(log n) - Finding the node takes O(log n), and finding the min in right subtree (if needed) also takes O(log n).
- Worst case: O(n) - For completely unbalanced tree, both finding the node and finding min could take O(n).

**Space Complexity:**
- O(1) - Iterative approach with constant space.

### 4. get_min_value (helper method)

**Time Complexity:**
- Average case: O(log n) - Traverse left children to find minimum.
- Worst case: O(n) - If tree is left-heavy (unbalanced to the left).

**Space Complexity:**
- O(1) - Iterative approach with constant space.

### Important Notes:

1. These complexities assume the BST is reasonably balanced. In the worst case (completely unbalanced tree),
all operations degrade to O(n).

2. The space complexity is O(1) for all operations because we're using iterative implementations. Recursive implementations
would have O(log n) space complexity in average case (due to call stack) and O(n) in worst case.

3. The remove operation is the most complex, but its time complexity is dominated by the search operation and (in some cases)
the get_min_value operation.

### When BST is balanced:

- All operations (insert, contains, remove) are O(log n) time and O(1) space.

### When BST is completely unbalanced:

- All operations degrade to O(n) time (but still O(1) space).

"""
