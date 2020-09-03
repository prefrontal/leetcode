# LeetCode 28 - Implement strStr()
#
# Implement strStr(). Return the index of the first occurrence of needle in haystack,
# or -1 if needle is not part of haystack.

def strStr(haystack: str, needle: str) -> int:
    if not needle:
        return 0

    if not haystack:
        return -1

    haystack_len = len(haystack)
    needle_len = len(needle)

    if needle_len > haystack_len:
        return -1

    idx = 0

    while (idx+needle_len-1) < haystack_len:
        if haystack[idx:idx+needle_len] == needle:
            return idx
        idx += 1

    return -1

# Tests
print(strStr("hello", "he") == 0)
print(strStr("hello", "lo") == 3)
print(strStr("hello", "ll") == 2)
print(strStr("aaaaa", "bba") == -1)
