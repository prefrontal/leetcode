# LeetCode 5 - Longest Palindromic Substring
#
# Given a string s, find the longest palindromic substring in s.
# You may assume that the maximum length of s is 1000.

def longestPalindrome(s: str) -> str:
    if not len(s):
        return ""
    
    if len(s) == 1:
        return s

    longest_palindrome_len = 1
    longest_palindrome = s[0]

    for idx1, _ in enumerate(s):
        for idx2 in range(idx1+1, len(s)+1):
            sub_str = s[idx1:idx2]
            if sub_str == sub_str[::-1]:
                # Palindrome
                if len(sub_str) > longest_palindrome_len:
                    longest_palindrome_len = len(sub_str)
                    longest_palindrome = sub_str

    return longest_palindrome


# Tests
print(longestPalindrome("") == "")
print(longestPalindrome("a") == "a")
print(longestPalindrome("bb") == "bb")
print(longestPalindrome("ab") == "a")
print(longestPalindrome("babad") == "bab")
