# Nth Fibonacci

The Fibonacci sequence is defined as follows: the first number of the sequence is `0`, the second number is `1`, and the nth number is the sum of the (n - 1)th and (n - 2)th numbers. Write a function that takes in an integer `n` and returns the nth Fibonacci number.

Important note: the Fibonacci sequence is often defined with its first two numbers as `F0 = 0` and `F1 = 1`. For the purpose of this question, the first Fibonacci number is `F0`; therefore, `get_nth_fib(1)` is equal to `F0`, `get_nth_fib(2)` is equal to `F1`, etc..

## Sample Input #1

```plaintext
n = 2
```

## Sample Output #1

```plaintext
1

// Sequence: 0, 1
```

## Sample Input #2

```plaintext
n = 6
```

## Sample Output #2

```plaintext
5

// Sequence: 0, 1, 1, 2, 3, 5
```

## Hints

<details>
<summary><b>Hint 1</b></summary>

The formula to generate the nth Fibonacci number can be written as follows:  
`F(n) = F(n - 1) + F(n - 2)`

Think of the case(s) for which this formula doesn't apply (the base case(s)) and try to implement a simple recursive algorithm to find the nth Fibonacci number with this formula.

</details>

<details>
<summary><b>Hint 2</b></summary>

What are the runtime implications of solving this problem as described in Hint #1?  
Can you use memoization (caching) to improve the performance of your algorithm?

</details>

<details>
<summary><b>Hint 3</b></summary>

Realize that to calculate any single Fibonacci number you only need to have the two previous Fibonacci numbers. Knowing this, can you implement an iterative algorithm to solve this question, storing only the last two Fibonacci numbers at any given time?

</details>

## Optimal Time & Space Complexity

`O(n)` time | `O(1)` space - where `n` is the input number.
