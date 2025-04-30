# Powerset

Write a function that takes in an array of `unique` integers and returns its powerset.

The powerset `P(X)` of a set `X` is the set of all subsets of `X`. For example, the powerset of `[1, 2]` is `[[], [1], [2], [1,2]]`.

> Note that the sets in the powerset do not need to be in any particular order.

## Sample Input

```plaintext
array = [1, 2, 3]
```

## Sample Output

```plaintext
[[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
```

## Hints

<details>
<summary><b>Hint 1</b></summary>

Try thinking about the base cases. What is the powerset of the empty set? What is the powerset of sets of length 1?

</details>

<details>
<summary><b>Hint 2</b></summary>

If you were to take the input set `X` and add an element to it, how would the resulting powerset change?

</details>

<details>
<summary><b>Hint 3</b></summary>

Can you solve this problem recursively? Can you solve it iteratively? What are the advantages and disadvantages of using either approach?

</details>

## Optimal Time & Space Complexity

`O(n * 2ⁿ)` time | `O(n * 2ⁿ)` space - where `n` is the length of the input array.
