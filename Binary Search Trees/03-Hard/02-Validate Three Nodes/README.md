# Validate Three Nodes

You're given `three nodes` that are contained in the same `Binary Search Tree`: `node_one`, `node_two`, and `node_three`. Write a function that returns a boolean representing whether one of `node_one` or `node_three` is an ancestor of `node_two` and the other node is a descendant of `node_two`. For example, if your function determines that `node_one` is an ancestor of `node_two`, then it needs to see if `node_three` is a descendant of `node_two`. If your function determines that `node_three` is an ancestor, then it needs to see if `node_one` is a descendant.

A *descendant* of a node `N` is defined as a node contained in the tree rooted at `N`. A node `N` is an ancestor of another node `M` if `M` is a descendant of `N`.

It isn't guaranteed that `node_one` or `node_three` will be ancestors or descendants of `node_two`, but it is guaranteed that all three nodes will be unique and will never be `None`. In other words, you'll be given valid input nodes.

Each `BST` node has an integer `value`, a `left` child node, and a `right` child node. A node is said to be a valid `BST` node if and only if it satisfies the `BST` property: its `value` is strictly greater than the values of every node to its left; its `value` is less than or equal to the values of every node to its right; and its children nodes are either valid `BST` nodes themselves or `None`.

## Sample Input

```plaintext
tree =    5
       /     \
      2       7
    /   \   /   \
   1     4 6     8
  /     /
 0     3  

// This tree won't actually be passed as an input; it's here to help you visualize the problem.

node_one = 5  // The actual node with value 5.
node_two = 2  // The actual node with value 2.
node_three = 3  // The actual node with value 3.
```

## Sample Output

```plaintext
True 

// node_one is an ancestor of node_two, and node_three is a descendant of node_two.
```

## Hints

<details>
<summary><b>Hint 1</b></summary>

Keep in mind that the nodes passed to you are contained in a `Binary Search Tree`—not just a normal `Binary Tree`. How might this help you traverse the tree faster?

</details>

<details>
<summary><b>Hint 2</b></summary>

There are multiple ways to solve this problem, but the simplest is to just check the possible relationships between the nodes. Since you're looking for a descendant and an ancestor, simply check if `node_one` is a descendant of `node_two`, and if it is, then check if `node_three` is an ancestor of `node_two`. If the previous checks come out negative, check if `node_three` is a descendant of `node_two`, and if it is, then check if `node_one` is an ancestor of `node_two`.

</details>

<details>
<summary><b>Hint 3</b></summary>

Although the approach mentioned in `Hint #2` is fairly efficient (it runs in `O(h)` time, where `h` is the height of the tree), there's a way to solve this problem faster. It involves realizing that, when searching for `node_two` from either `node_one` or `node_three`, if you ever reach `node_three` from `node_one` or `node_one` from `node_three` before reaching `node_two`, then you can immediately stop the algorithm, because `node_two` cannot be between these nodes.
</details>

## Optimal Time & Space Complexity

`O(d)` time | `O(1)` space - where `d` is the distance between `node_one` and `node_three`.
