# Best Seat

You walk into a theatre you're about to see a show in. The usher within the theatre walks you to your row and mentions you're allowed to sit anywhere within the given row. Naturally you'd like to sit in the seat that gives you the most space. You also would prefer this space to be evenly distributed on either side of you (e.g. if there are three empty seats in a row, you would prefer to sit in the middle of those three seats).

Given the theatre row represented as an integer array, return the seat index of where you should sit. Ones represent occupied seats and zeroes represent empty seats.

You may assume that someone is always sitting in the first and last seat of the row. Whenever there are two equally good seats, you should sit in the seat with the lower index. If there is no seat to sit in, return -1. The given array will always have a length of at least one and contain only ones and zeroes.

## Sample Input

```plaintext
seats = [1, 0, 1, 0, 0, 0, 1]
```

## Sample Output

```plaintext
4
```

## Hints

<details>
<summary><b>Hint 1</b></summary>

Try thinking about this problem in real life. How would you determine what seat has the most space?

</details>

<details>
<summary><b>Hint 2</b></summary>

The best seat will always be within the longest contiguous subarray of all zeros.

</details>

<details>
<summary><b>Hint 3</b></summary>

Once you find the longest contiguous subarray of empty seats, how can you choose where to sit within that subarray?

</details>

<details>
<summary><b>Hint 4</b></summary>

How can you find the midpoint between two people?

</details>

## Optimal Time & Space Complexity

`O(n)` time | `O(1)` space - where `n` is the number of seats.
