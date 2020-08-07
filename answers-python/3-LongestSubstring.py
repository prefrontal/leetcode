# 3 - Longest Substring Without Repeating Characters
#
# Given a string, find the length of the longest substring without repeating characters.

def lengthOfLongestSubstring(s: str) -> int:
    max_distance = 0

    # We're going to start iterating through the string, starting with each character
    # and then seeing the max substring we can create from that starting point
    for idx1 in range(0, len(s)):
        sequence = []

        for idx2 in range(idx1, len(s)):
            if s[idx2] in sequence:
                if len(sequence) > max_distance:
                    max_distance = len(sequence)
                break

            if idx2 == len(s)-1:
                sequence.append(s[idx2])
                if len(sequence) > max_distance:
                    max_distance = len(sequence)
                break

            sequence.append(s[idx2])

    return max_distance


# Tests
print(lengthOfLongestSubstring("b") == 1)
print(lengthOfLongestSubstring("bbbbb") == 1)
print(lengthOfLongestSubstring("abbcabcbb") == 3)
print(lengthOfLongestSubstring("pwwkew") == 3)
print(lengthOfLongestSubstring("pwwkep") == 4)
