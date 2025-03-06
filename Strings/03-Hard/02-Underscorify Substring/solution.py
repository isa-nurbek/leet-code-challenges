# Description:

"""
                                        Underscorify Substring

Write a function that takes in two strings: a main string and a potential substring of the main string. The
function should return a version of the main string with every instance of the substring in it wrapped between underscores.

If two or more instances of the substring in the main string overlap each other or sit side by side, the underscores
relevant to these substrings should only appear on the far left of the leftmost substring and on the far right of the rightmost
substring. If the main string doesn't contain the other string at all, the function should return the main string intact.


## Sample Input:
```
string = "testthis is a testtest to see if testestest it works"
substring = "test"
```

## Sample Output:
```
"_test_this is a _testtest_ to see if _testestest_ it works"
```

## Optimal Time & Space Complexity:
```
Average case: `O(n + m)` | `O(n)` space - where `n` is the length of the main string
and `m` is the length of the substring.
```

"""

# =============================================================================================== #

# Solution


# Average case: `O(n + m)` | `O(n)` space - where `n` is the length
# of the main string and `m` is the length of the substring
def underscorify_substring(string, substring):
    """
    Main function to underscorify all occurrences of the substring in the string.

    Args:
        string (str): The original string.
        substring (str): The substring to be underscored.

    Returns:
        str: The modified string with underscores around the substrings.

    Raises:
        TypeError: If either argument is not a string.
    """
    if not isinstance(string, str) or not isinstance(substring, str):
        raise TypeError("Both arguments must be strings.")

    # Step 1: Get all locations where the substring occurs in the string.
    locations = get_locations(string, substring)

    # Step 2: Collapse overlapping or adjacent locations to avoid multiple underscores.
    locations = collapse(locations)

    # Step 3: Add underscores around the substrings in the original string.
    return underscorify(string, locations)


def get_locations(string, substring):
    """
    Finds all the start and end indices of the substring in the string.

    Args:
        string (str): The original string.
        substring (str): The substring to be found.

    Returns:
        list: A list of lists, where each inner list contains the start and end indices of a substring occurrence.

    Raises:
        TypeError: If the first argument is not a string.
    """
    if not isinstance(string, str):
        raise TypeError("The first argument must be a string.")

    locations = []
    start_idx = 0

    # Loop through the string to find all occurrences of the substring.
    while start_idx < len(string):
        next_idx = string.find(substring, start_idx)

        if next_idx != -1:
            # If the substring is found, record its start and end indices.
            locations.append([next_idx, next_idx + len(substring)])
            start_idx = next_idx + 1
        else:
            # If no more occurrences are found, break the loop.
            break

    return locations


def collapse(locations):
    """
    Collapses overlapping or adjacent locations to avoid multiple underscores.

    Args:
        locations (list): A list of lists, where each inner list contains the start and end indices of a substring occurrence.

    Returns:
        list: A list of lists with overlapping or adjacent locations merged.
    """
    if not len(locations):
        return locations

    # Initialize the new_locations list with the first location.
    new_locations = [locations[0]]
    previous = new_locations[0]

    # Loop through the remaining locations and merge overlapping or adjacent ones.
    for i in range(1, len(locations)):
        current = locations[i]

        if current[0] <= previous[1]:
            # If the current location overlaps or is adjacent to the previous one, merge them.
            previous[1] = current[1]
        else:
            # If not, add the current location to the new_locations list.
            new_locations.append(current)
            previous = current

    return new_locations


def underscorify(string, locations):
    """
    Adds underscores around the substrings in the original string based on the locations.

    Args:
        string (str): The original string.
        locations (list): A list of lists, where each inner list contains the start and end indices of a substring occurrence.

    Returns:
        str: The modified string with underscores around the substrings.
    """
    locations_idx = 0
    string_idx = 0
    final_chars = []

    # Loop through the string and add underscores at the specified locations.
    while string_idx < len(string) and locations_idx < len(locations):
        current_location = locations[locations_idx]

        if string_idx == current_location[0]:
            # Add an underscore at the start of the substring.
            final_chars.append("_")

        # Add the current character to the final_chars list.
        final_chars.append(string[string_idx])

        if string_idx == current_location[1] - 1:
            # Add an underscore at the end of the substring.
            final_chars.append("_")
            locations_idx += 1

        string_idx += 1

    # If there are remaining locations, add an underscore.
    if locations_idx < len(locations):
        final_chars.append("_")

    # If there are remaining characters in the string, add them to the final_chars list.
    if string_idx < len(string):
        final_chars.append(string[string_idx:])

    # Join the characters to form the final string.
    return "".join(final_chars)


# Test Cases:
string = "testthis is a testtest to see if testestest it works"
substring = "test"

string_2 = "ttttttttttttttbtttttctatawtatttttastvb"
substring_2 = "ttt"

string_3 = "ababababababababababab"
substring_3 = "a"

print(underscorify_substring(string, substring))
# Output: "_test_this is a _testtest_ to see if _testestest_ it works"

print(underscorify_substring(string_2, substring_2))
# Output: "_tttttttttttttt_b_ttttt_ctatawta_ttttt_astvb"

print(underscorify_substring(string_3, substring_3))
# Output: "_a_b_a_b_a_b_a_b_a_b_a_b_a_b_a_b_a_b_a_b_a_b"
