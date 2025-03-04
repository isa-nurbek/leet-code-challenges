# Description:

"""
                                    Valid IP Addresses

You're given a string of length 12 or smaller, containing only digits. Write a function that returns all the possible
IP addresses that can be created by inserting three `.`s in the string.

An IP address is a sequence of four positive integers that are separated by `.`s, where each individual integer is 
within the range `0 - 255`, inclusive.

An IP address isn't valid if any of the individual integers contains leading `0`s. For example, `"192.168.0.1"` is a 
valid IP address, but `"192.168.00.1"` and `"192.168.0.01"` aren't, because they contain `"00"` and `01`, respectively.
Another example of a valid IP address is `"99.1.1.10"`; conversely, `"991.1.1.0"` isn't valid, because `"991"` is greater than 255.

Your function should return the IP addresses in string format and in no particular order. If no valid IP addresses can be
created from the string, your function should return an empty list.


## Sample Input:
```
string = "1921680"
```

## Sample Output:
```
[
  "1.9.216.80",
  "1.92.16.80",
  "1.92.168.0",
  "19.2.16.80",
  "19.2.168.0",
  "19.21.6.80",
  "19.21.68.0",
  "19.216.8.0",
  "192.1.6.80",
  "192.1.68.0",
  "192.16.8.0"
]
// The IP addresses could be ordered differently.
```

## Optimal Time & Space Complexity:
```
`O(1)` time | `O(1)` space.
```

"""

# =============================================================================================== #

# Solution


# `O(1)` time | `O(1)` space.
def valid_IP_addresses(string):
    # This list will store all valid IP addresses found
    IP_addresses_found = []

    # Loop through the string to find the first part of the IP address
    # The first part can be 1 to 3 characters long (min(len(string), 4) ensures we don't go out of bounds)
    for i in range(1, min(len(string), 4)):
        # Initialize a list to store the four parts of the IP address
        current_IP_address_parts = ["", "", "", ""]

        # Assign the first part of the IP address
        current_IP_address_parts[0] = string[:i]

        # Check if the first part is valid
        if not is_valid_part(current_IP_address_parts[0]):
            continue  # If not valid, skip to the next iteration

        # Loop through the string to find the second part of the IP address
        # The second part can be 1 to 3 characters long
        for j in range(i + 1, i + min(len(string) - i, 4)):
            # Assign the second part of the IP address
            current_IP_address_parts[1] = string[i:j]

            # Check if the second part is valid
            if not is_valid_part(current_IP_address_parts[1]):
                continue  # If not valid, skip to the next iteration

            # Loop through the string to find the third part of the IP address
            # The third part can be 1 to 3 characters long
            for k in range(j + 1, j + min(len(string) - j, 4)):
                # Assign the third and fourth parts of the IP address
                current_IP_address_parts[2] = string[j:k]
                current_IP_address_parts[3] = string[k:]

                # Check if both the third and fourth parts are valid
                if is_valid_part(current_IP_address_parts[2]) and is_valid_part(
                    current_IP_address_parts[3]
                ):
                    # If all parts are valid, join them with dots to form a valid IP address
                    IP_addresses_found.append(".".join(current_IP_address_parts))

    # Return the list of all valid IP addresses found
    return IP_addresses_found


def is_valid_part(string):
    # Convert the string to an integer to check if it's a valid IP part
    string_as_int = int(string)

    # Check if the integer value is greater than 255 (invalid for an IP part)
    if string_as_int > 255:
        return False

    # Check if the length of the string matches the length of the integer when converted back to string
    # This ensures there are no leading zeros (e.g., "01" is invalid)
    return len(string) == len(str(string_as_int))


# Test Case 1
print(valid_IP_addresses("1921680"))
# Output:
# [
#     "1.9.216.80",
#     "1.92.16.80",
#     "1.92.168.0",
#     "19.2.16.80",
#     "19.2.168.0",
#     "19.21.6.80",
#     "19.21.68.0",
#     "19.216.8.0",
#     "192.1.6.80",
#     "192.1.68.0",
#     "192.16.8.0",
# ]

# Test Case 2
print(valid_IP_addresses("255255255255"))
# Output: ['255.255.255.255']

# Test Case 3
print(valid_IP_addresses("100100"))
# Output: ['1.0.0.100', '10.0.10.0', '100.1.0.0']
