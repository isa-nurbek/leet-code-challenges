# Non-Constructible Change

Given an array of positive integers representing the values of coins in your possession, write a function that returns the minimum amount of change (the minimum sum of money) that you **cannot** create. The given coins can have any positive integer value and aren't necessarily unique (i.e., you can have multiple coins of the same value).

For example, if you're given `coins = [1, 2, 5]`, the minimum amount of change that you can't create is `4`. If you're given no coins, the minimum amount of change that you can't create is `1`.

## Sample Input

```plaintext
coins = [5, 7, 1, 1, 2, 3, 22]
```

## Sample Output

```plaintext
20
```

## Hints

<details>
<summary>Hint 1</summary>

One approach to solve this problem is to attempt to create every single amount of change, starting at 1 and going up until you eventually can't create an amount. While this approach works, there is a better one.

</details>

<details>
<summary>Hint 2</summary>

Start by sorting the input array. Since you're trying to find the minimum amount of change that you can't create, it makes sense to consider the smallest coins first.

</details>

<details>
<summary>Hint 3</summary>

To understand the trick to this problem, consider the following example: `coins = [1, 2, 4]`. With this set of coins, we can create `1, 2, 3, 4, 5, 6, 7` cents worth of change. Now, if we were to add a coin of value `9` to this set, we would not be able to create `8` cents. However, if we were to add a coin of value `7`, we would be able to create `8` cents, and we would also be able to create all values of change from `1` to `15`. Why is this the case?

</details>

## Optimal Time & Space Complexity

`O(n log n)` time | `O(1)` space - where `n` is the number of coins.
