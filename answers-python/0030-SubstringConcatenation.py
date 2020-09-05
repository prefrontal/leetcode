# LeetCode 30 - Substring with Concatenation of All Words
#
# You are given a string s and an array of strings words of the same length. Return all starting
# indices of substring(s) in s that is a concatenation of each word in words exactly once, in any
# order, and without any intervening characters.
# You can return the answer in any order.

import itertools
from typing import List

def findSubstring(s: str, words: List[str]) -> List[int]:
    if not s or not words:
        return []

    results = []

    # Generate the substring permutations
    substring_combos = []
    substring_len = len(words[0]) * len(words)

    els = [''.join(x) for x in itertools.permutations(words, len(words))]
    substring_combos.extend(els)

    # Find the shortest and longest substring
    max_substring_len = len(max(substring_combos, key=len))
    min_substring_len = len(min(substring_combos, key=len))

    substring_set = set(substring_combos)

    # Search for the substrings
    for i in range(0, len(s)):
        string = s[i:(i+ substring_len)]
        #print(string)
        if string in substring_set:
            longest_match = len(string)
            results.append(i)

    return results


# Tests

s = ""
words = ["foo", "bar"]
print(findSubstring(s, words) == [])

s = "barfoothefoobarman"
words = []
print(findSubstring(s, words) == [])

s = "barfoothefoobarman"
words = ["foo", "bar"]
print(findSubstring(s, words) == [0,9])

s = "wordgoodgoodgoodbestword"
words = ["word", "good", "best", "word"]
print(findSubstring(s, words) == [])

s = "barfoofoobarthefoobarman"
words = ["bar", "foo", "the"]
print(findSubstring(s, words) == [6,9,12])

s = "wordgoodgoodgoodbestword"
words = ["word", "good", "best", "good"]
print(findSubstring(s, words) == [8])