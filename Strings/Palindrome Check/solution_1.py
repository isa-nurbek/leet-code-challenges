"""
                                         Palindrome Check

Write a function that takes in a non-empty string and that returns a boolean representing whether the string is a palindrome.

A palindrome is defined as a string that's written the same forward and backward. Note that single-character strings are palindromes.

Sample Input:
string = "abcdcba"

Sample Output:
true // it's written the same forward and backward


Optimal Space & Time Complexity:
`O(n)` time | `O(1)` space - where `n` is the length of the input string.

"""


def isPalindrome(string):
    reversed_string = ""
    for i in reversed(range(len(string))):
        reversed_string += string[i]
    return string == reversed_string
