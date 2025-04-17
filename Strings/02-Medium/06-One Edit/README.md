# One Edit

You're given two strings `string_one` and `string_two`. Write a function that determines if these two strings can be made equal using only one edit.

There are 3 possible edits:

- **Replace:** One character in one string is swapped for a different character.
- **Add:** One character is added at any index in one string.
- **Remove:** One character is removed at any index in one string.

Note that both strings will contain at least one character. If the strings are the same, your function should return true.

## Sample Input

```plaintext
string_one = "hello"
string_two = "hollo"
```

## Sample Output

```plaintext
True // A single replace at index 1 of either string can make the strings equal.
```

## Hints

<details>
<summary><b>Hint 1</b></summary>

If the difference in lengths of the strings is greater than 1, then there is no way to make them equal with a single edit.

</details>

<details>
<summary><b>Hint 2</b></summary>

If the lengths of the strings are the same, then the only possible edit is a replace, because adding or removing a character would make the strings different lengths.

</details>

<details>
<summary><b>Hint 3</b></summary>

If the strings are different lengths, the only possible moves are adding and removing a character. These are essentially the same operation, because they represent the case where one string has a character that another does not.

</details>

## Optimal Time & Space Complexity

`O(n)` time | `O(1)` space - where `n` is the length of the shorter string.
