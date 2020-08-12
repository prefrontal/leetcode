 # LeetCode 10 - Regular Expression Matching
#
# Given an input string (s) and a pattern (p), implement
# regular expression matching with support for '.' and '*'.
#
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).
#
# Note:
# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like . or *.

def isMatch(s: str, p: str) -> bool:
    s = ' '+ s
    p = ' '+ p
    s_len = len(s)
    p_len = len(p)

    # Going with a dynamic programming solution, after a bunch of research
    dp = [[0]*(p_len) for i in range(s_len)]
    dp[0][0] = 1

    for j in range(1, p_len):
        if p[j] == '*':
            dp[0][j] = dp[0][j-2]

    for i in range(1, s_len):
        for j in range(1, p_len):
            if p[j] in {s[i], '.'}:
                dp[i][j] = dp[i-1][j-1]
            elif p[j] == "*":
                dp[i][j] = dp[i][j-2] or int(dp[i-1][j] and p[j-1] in {s[i], '.'})

    return bool(dp[-1][-1])


# Tests
print(isMatch("", ""))
print(not isMatch("aa", ""))
print(not isMatch("", "a"))
print(not isMatch("aa", "**"))
print(not isMatch("aa", "a"))
print(not isMatch("a", "aa"))
print(isMatch("aa", "aa"))
print(not isMatch("a", "aaaa"))
print(not isMatch("ab", ".*c"))
print(isMatch("abcdef", ".*f"))
print(isMatch("", ".*"))
print(isMatch("bbbb", "...."))
print(isMatch("aa", "a*"))
print(isMatch("a", "ab*"))
print(isMatch("aaaa", "a*"))
print(not isMatch("a", "ab*a"))
print(isMatch("ab", ".*"))
print(isMatch("aab", "c*a*b"))
print(isMatch("aab", "c*a*b*"))
print(isMatch("abbbcd", "ab*bbbcd"))
print(isMatch("mississippi", "mis*is*ip*."))
print(not isMatch("mississippi", "mis*is*p*."))
print(not isMatch("acaabbaccbbacaabbbb", "a*.*b*.*a*aa*a*"))
