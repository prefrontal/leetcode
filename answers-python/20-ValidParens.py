# LeetCode 20 - Valid Parentheses
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
#
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

def isValid(s: str) -> bool:
    # Either we got an empty string, or we have reached the end of the recursive calls
    # Empty strings are valid, so in either case we can return true here
    if len(s) == 0:
        return True

    # Iterate over the string, considering characters one pair at a time
    for idx in range(0, len(s)-1):
        two_chars = s[idx:idx+2]

        if two_chars in ('()', '[]', '{}'):
            new_test = s[:idx] + s[idx+2:]
            return isValid(new_test)

    return False


# Tests
print(not isValid("("))
print(not isValid("["))
print(not isValid("{"))
print(not isValid("([)]"))
print(not isValid("abc"))
print(isValid(""))
print(isValid("()"))
print(isValid("((()))"))
print(isValid("{[()]}"))
