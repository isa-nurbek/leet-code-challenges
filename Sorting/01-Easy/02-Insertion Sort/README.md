# Insertion Sort

Write a function that takes in an array of integers and returns a `sorted` version of that array. Use the `Insertion Sort` algorithm to sort the array.

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

Divide the input array into two subarrays in place. The first subarray should be sorted at all times and should start with a length of `1`, while the second subarray should be unsorted. Iterate through the unsorted subarray, inserting all of its elements into the sorted subarray in the correct position by swapping them into place. Eventually, the entire array will be sorted.

</details>

## Optimal Time & Space Complexity

**Best**: `O(n)` time | `O(1)` space - where `n` is the length of the input array.

**Average**: `O(n²)` time | `O(1)` space - where `n` is the length of the input array.

**Worst**: `O(n²)` time | `O(1)` space - where `n` is the length of the input array.
