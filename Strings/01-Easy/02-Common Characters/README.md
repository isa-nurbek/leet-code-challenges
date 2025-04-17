# Common Characters

Write a function that takes in a non-empty list of non-empty strings and returns a list of characters that are common to all strings in the list, ignoring multiplicity.

Note that the strings are not guaranteed to only contain alphanumeric characters. The list you return can be in any order.

## Sample Input

```plaintext
strings = ["abc", "bcd", "cbaccd"]
```

## Sample Output

```plaintext
["b", "c"] // The characters could be ordered differently.
```

## Hints

<details>
<summary><b>Hint 1</b></summary>

What data structure could be helpful to remember characters we've seen and how many strings contained those characters?

</details>

<details>
<summary><b>Hint 2</b></summary>

We can use a map to keep track of the characters we have seen and how many strings we have seen them in. If a character is seen `len(strings)` times, then it must be in every string.

</details>

<details>
<summary><b>Hint 3</b></summary>

Converting a string to a set can quickly get all of the unique characters from that string, which can be helpful since we are ignoring multiplicity in this problem.

</details>

## Optimal Time & Space Complexity

`O(n * m)` time | `O(m)` space - where `n` is the number of strings, and `m` is the length of the longest string.
