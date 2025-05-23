# Quick Sort

Write a function that takes in an array of integers and returns a `sorted` version of that array. Use the `Quick Sort` algorithm to sort the array.

To avoid `O(n²)` worst-case time complexity you can:

- Choose a `random pivot` or `median-of-three pivot`.
- Use an `in-place partitioning` scheme to reduce space usage.

1. **Avoiding O(n²) worst-case**: Quick Sort can degrade to `O(n²)` time complexity if poorly chosen pivots (e.g., always picking the `first/last` element in an already sorted array) lead to highly unbalanced partitions. The suggestions address this:
   - **Random pivot**: Randomization makes worst-case behavior unlikely.
   - **Median-of-three pivot**: Choosing the median of the first, middle, and last elements helps avoid bad pivots.

2. **In-place partitioning**: This reduces space complexity from O(log n) (due to recursion stack) to O(1) auxiliary space (excluding the stack), making it more memory-efficient.

## Sample Input

```plaintext
array = [8, 5, 2, 9, 5, 6, 3]
```

## Sample Output

```plaintext
[2, 3, 5, 5, 6, 8, 9]
```

## Hints

<details>
<summary><b>Hint 1</b></summary>

`Quick Sort` works by picking a `"pivot"` number from an array, positioning every other number in the array in sorted order with respect to the pivot (all smaller numbers to the pivot's left; all bigger numbers to the pivot's right), and then repeating the same two steps on both sides of the pivot until the entire array is sorted.

</details>

<details>
<summary><b>Hint 2</b></summary>

Pick a random number from the input array (the first number, for instance) and let that number be the pivot. Iterate through the rest of the array using two pointers, one starting at the left extremity of the array and progressively moving to the right, and the other one starting at the right extremity of the array and progressively moving to the left. As you iterate through the array, compare the left and right pointer numbers to the pivot. If the left number is greater than the pivot and the right number is less than the pivot, swap them; this will effectively sort these numbers with respect to the pivot at the end of the iteration. If the left number is ever less than or equal to the pivot, increment the left pointer; similarly, if the right number is ever greater than or equal to the pivot, decrement the right pointer. Do this until the pointers pass each other, at which point swapping the pivot with the right number should position the pivot in its final, sorted position, where every number to its left is smaller and every number to its right is greater.

</details>

<details>
<summary><b>Hint 3</b></summary>

Repeat the process mentioned in `Hint #2` on the respective subarrays located to the left and right of your pivot, and keep on repeating the process thereafter until the input array is fully sorted.

</details>

## Optimal Time & Space Complexity

**Best**: `O(n log(n))` time | `O(log(n))` space - where `n` is the length of the input array.

**Average**: `O(n log(n))` time | `O(log(n))` space - where `n` is the length of the input array.

**Worst**: `O(n²)` time | `O(log(n))` space - where `n` is the length of the input array.
