# Description:

"""

                                        Run-Length Encoding

Write a function that takes in a non-empty string and returns its run-length encoding.

From Wikipedia, "run-length encoding is a form of lossless data compression in which runs of data are stored as a single
data value and count, rather than as the original run." For this problem, a run of data is any sequence of consecutive,
identical characters. So the run "AAA" would be run-length-encoded as "3A".

To make things more complicated, however, the input string can contain all sorts of special characters, including numbers.
And since encoded data must be decodable, this means that we can't naively run-length-encode long runs. For example,
the run "AAAAAAAAAAAA" (12 As), can't naively be encoded as "12A", since this string can be decoded as either "AAAAAAAAAAAA"
or "1AA". Thus, long runs (runs of 10 or more characters) should be encoded in a split fashion; the aforementioned run
should be encoded as "9A3A".

## Sample Input:
```
string = "AAAAAAAAAAAAABBCCCCDD"
```

## Sample Output:
```
"9A4A2B4C2D"
```

## Optimal Space & Time Complexity

`O(n)` time | `O(n)` space - where `n` is the length of the input string.

"""


# O (n) time | O(n) space
def run_length_encoding(strings):
    # The input string is guaranteed to be non-empty,
    # so our first run will be of at least length 1
    encoded_str_characters = []
    current_run_length = 1

    for i in range(1, len(strings)):
        current_character = strings[i]
        previous_character = strings[i - 1]

        if current_character != previous_character or current_run_length == 9:
            encoded_str_characters.append(str(current_run_length))
            encoded_str_characters.append(previous_character)
            current_run_length = 0

        current_run_length += 1

    # Handle the last run
    encoded_str_characters.append(str(current_run_length))
    encoded_str_characters.append(strings[len(strings) - 1])

    return "".join(encoded_str_characters)


print(run_length_encoding("AAAAAAAAAABBBCCDAA"))  # Output: "9A2A3B2C1D2A"
print(run_length_encoding("CCCCCCCCCCCC"))  # Output: "9C3C"
print(run_length_encoding("AABB"))  # Output: "2A2B"
print(run_length_encoding("ABC"))  # Output: "1A1B1C"
print(run_length_encoding("A"))  # Output: "1A"


# Big O:

"""

1. **Time Complexity**: O(n)  
   The algorithm iterates through the string once, making it linear in terms of time complexity.
   
2. **Space Complexity**: O(n)
   The `encoded_str_characters` list stores the result, which in the worst case could grow as large as the input string.

"""


# Code Explanation:

"""

The provided code implements **run-length encoding**, a simple form of data compression. It encodes a string
by replacing sequences of the same character with the character followed by its count.

### How the Code Works

1. **Initialization**:
   - `encoded_str_characters`: A list that will hold the run-length encoded characters and their counts.
   - `current_run_length`: A counter to track how many times the current character has appeared consecutively.

2. **Iterate Through the String**:
   - Loop starts from the second character (index `1`) and compares it with the previous character.
   - Two cases cause the current run to end:
     - The current character is different from the previous character.
     - The current run length reaches `9`. (Run-length encoding often limits the count to a single digit to simplify decoding.)
   - When a run ends:
     - Append the count of the run (`current_run_length`) and the character (`previous_character`) to `encoded_str_characters`.
     - Reset `current_run_length` to `1` for the next run.

3. **Handle the Final Run**:
   - After the loop, the final sequence is appended to `encoded_str_characters`.

4. **Return Encoded String**:
   - The list `encoded_str_characters` is joined into a single string and returned.

---

### Example Walkthrough

#### Input: `"AAAAAAAAAABBBCCDAA"`
- **Initialization**:
  - `encoded_str_characters = []`
  - `current_run_length = 1`

- **Iteration**:
  1. **Index 1–9 (Character: 'A')**:
     - Characters are identical, increment `current_run_length` until `current_run_length = 9`.
     - On index 9:
       - Append `9` and `'A'` to `encoded_str_characters`.
       - Reset `current_run_length` to `1`.

  2. **Index 10 (Character: 'A')**:
     - Current character is the same, so `current_run_length = 2`.

  3. **Index 11–13 (Character: 'B')**:
     - On index 11, `'B'` differs from `'A'`:
       - Append `2` and `'A'` to `encoded_str_characters`.
       - Reset `current_run_length = 1`.
     - Increment `current_run_length` for `'B'`.

  4. **Index 14 (Character: 'C')**:
     - `'C'` differs from `'B'`:
       - Append `3` and `'B'` to `encoded_str_characters`.
       - Reset `current_run_length = 1`.

  5. **Index 15 (Character: 'C')**:
     - Increment `current_run_length` for `'C'`.

  6. **Index 16 (Character: 'D')**:
     - `'D'` differs from `'C'`:
       - Append `2` and `'C'` to `encoded_str_characters`.
       - Reset `current_run_length = 1`.

  7. **Index 17–18 (Character: 'A')**:
     - `'A'` differs from `'D'`:
       - Append `1` and `'D'` to `encoded_str_characters`.
       - Reset `current_run_length = 1`.
     - Increment `current_run_length` for `'A'`.

- **Final Run**:
  - After the loop, append `2` and `'A'` to `encoded_str_characters`.

- **Output**:
  - `encoded_str_characters = ['9', 'A', '2', 'A', '3', 'B', '2', 'C', '1', 'D', '2', 'A']`
  - Join into string: `"9A2A3B2C1D2A"`

---

### Example Outputs

1. **Input**: `"AAAAAAAAAABBBCCDAA"`  
   **Output**: `"9A2A3B2C1D2A"`

2. **Input**: `"AABB"`  
   **Output**: `"2A2B"`

3. **Input**: `"CCCCCCCCCCCC"`  
   **Output**: `"9C3C"`  
   (The run of `'C'` is split into two parts: `9C` and `3C`, as the count is limited to 9.)

---

### Notes
- This implementation assumes the input string is non-empty.
- The limitation of a maximum run length of 9 is typical in run-length encoding for simplicity and compactness.
It can be adjusted as needed.

"""
