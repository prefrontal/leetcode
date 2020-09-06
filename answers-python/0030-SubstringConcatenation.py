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

    # Generate the substring permutations
    perms = [''.join(x) for x in itertools.permutations(words, len(words))]
    substring_set = set(perms)

    substring_step = len(words[0])
    substring_len = substring_step * len(words)

    # Search for the substrings
    results = []
    start = 0

    while start < len(s)-substring_len+1:
        for end in range(start+substring_step, len(s)+1, substring_step):
            string = s[start:end]
            if string in substring_set:
                results.append(start)

        start += 1

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