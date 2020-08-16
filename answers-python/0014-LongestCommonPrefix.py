# LeetCode 14 - Longest Common Prefix
#
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
#
# Example 1:
# Input: ["flower","flow","flight"]
# Output: "fl"
#
# Example 2:
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note: All given inputs are in lowercase letters a-z.

import math
from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    if not strs:
        return ""

    output = ""

    min_str_len = math.inf
    for s in strs:
        if len(s) < min_str_len:
            min_str_len = len(s)

    for i in range(0, min_str_len):
        current_value = strs[0][i]

        for j in range(0, len(strs)):
            if strs[j][i] != current_value:
                return output

        output = output + current_value

    return output


# Tests
print(longestCommonPrefix([""]) == "")
print(longestCommonPrefix(["", ""]) == "")
print(longestCommonPrefix(["flower", ""]) == "")
print(longestCommonPrefix(["", "flower"]) == "")
print(longestCommonPrefix(["flower", "flow", "flight"]) == "fl")
print(longestCommonPrefix(["flower", "flower"]) == "flower")
print(longestCommonPrefix(["flowers", "flower"]) == "flower")
print(longestCommonPrefix(["flower", "flowers"]) == "flower")
print(longestCommonPrefix(["dog", "racecar", "car"]) == "")
print(longestCommonPrefix(["a", "ab", "abc", "abcd"]) == "a")
