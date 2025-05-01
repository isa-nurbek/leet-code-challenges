# Longest Substring Without Duplication

Write a function that takes in a string and returns its longest substring without duplicate characters.

You can assume that there will only be one longest substring without duplication.

## Sample Input

```plaintext
string = "kilimandjaro"
```

## Sample Output

```plaintext
"limandj"
```

## Hints

<details>
<summary><b>Hint 1</b></summary>

Try traversing the input string and storing the last position at which you see each character in a hash table. How can this help you solve the given problem?

</details>

<details>
<summary><b>Hint 2</b></summary>

As you traverse the input string, keep track of a starting index variable. This variable, as its name suggests, should represent the most recent index from which you could start a substring with no duplicate characters, ending at your current index. Use the hash table mentioned in `Hint #1` to update this variable correctly, and update the longest substring as you go.

</details>

## Optimal Time & Space Complexity

`O(n)` time | `O(min(n, a))` space - where `n` is the length of the input string and `a` is the length of the character alphabet represented in the input string.
