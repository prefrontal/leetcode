# LeetCode 30 - Substring with Concatenation of All Words
#
# You are given a string s and an array of strings words of the same length. Return all starting
# indices of substring(s) in s that is a concatenation of each word in words exactly once, in any
# order, and without any intervening characters.
# You can return the answer in any order.

from collections import Counter
from typing import List

def findSubstring(s: str, words: List[str]) -> List[int]:
    if not s or not words:
        return []

    # Working with all permutations took too much memory, so we are doing a trick where we just
    # need to match the frequency of the works in the input list and the substring we pull out
    words_counter = Counter(words)
    substring_step = len(words[0]) # All words in the list have the same length
    substring_len = substring_step * len(words)

    # Search for the substrings
    results = []
    idx = 0

    while idx < len(s)-substring_len+1:
        test_words = []
        for start in range(idx, idx+substring_len, substring_step):
            test_words.append(s[start:start+substring_step])

        if words_counter == Counter(test_words):
            results.append(idx)

        idx += 1

    return results


# Tests
test_string = ""
words = ["foo", "bar"]
print(findSubstring(test_string, words) == [])

test_string = "barfoothefoobarman"
words = []
print(findSubstring(test_string, words) == [])

test_string = "barfoothefoobarman"
words = ["foo", "bar"]
print(findSubstring(test_string, words) == [0, 9])

test_string = "wordgoodgoodgoodbestword"
words = ["word", "good", "best", "word"]
print(findSubstring(test_string, words) == [])

test_string = "barfoofoobarthefoobarman"
words = ["bar", "foo", "the"]
print(findSubstring(test_string, words) == [6, 9, 12])

test_string = "wordgoodgoodgoodbestword"
words = ["word", "good", "best", "good"]
print(findSubstring(test_string, words) == [8])
