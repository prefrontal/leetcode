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
    substring_combos = []
    
    for i in range(1, len(words)+1):
        #els = [list(x) for x in itertools.combinations(words, i)]
        els = [''.join(x) for x in itertools.permutations(words, i)]
        substring_combos.extend(els)

    print(substring_combos)

    return[]






# Tests

s = "barfoothefoobarman"
words = ["foo","bar"]
print(findSubstring(s, words) == [0,9])

s = "wordgoodgoodgoodbestword"
words = ["word","good","best","word"]
print(findSubstring(s, words) == [])

s = "barfoofoobarthefoobarman"
words = ["bar","foo","the"]
print(findSubstring(s, words) == [6,9,12])
