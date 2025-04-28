# Two Number Sum

Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. If any two numbers in the input array sum up to the target sum, the function should return them in an array, in any order. If no two numbers sum up to the target sum, the function should return an empty array.

Note that the target sum has to be obtained by summing two different integers in the array; you can't add a single integer to itself in order to obtain the target sum.

You can assume that there will be at most one pair of numbers summing up to the target sum.

## Sample Input

```plaintext
array = [3, 5, -4, 8, 11, 1, -1, 6]
target_sum = 10
```

## Sample Output

```plaintext
[-1, 11]

"""
The numbers could be in reverse order
"""
```

## Hints

<details>
<summary><b>Hint 1</b></summary>

Try using two for loops to sum all possible pairs of numbers in the input array. What are the time and space implications of this approach?

</details>

<details>
<summary><b>Hint 2</b></summary>

Realize that for every number X in the input array, you are essentially trying to find a corresponding number Y such that X + Y = target_sum. With two variables in this equation known to you, it shouldn't be hard to solve for Y.

</details>

<details>
<summary><b>Hint 3</b></summary>

Try storing every number in a hash table, solving the equation mentioned in Hint #2 for every number, and checking if the Y that you find is stored in the hash table. What are the time and space implications of this approach?

</details>

## Optimal Time & Space Complexity

`O(n)` time | `O(n)` space - where `n` is the length of the input array
