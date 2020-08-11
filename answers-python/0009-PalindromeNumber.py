# LeetCode 9 - Palindrome Number
#
# Determine whether an integer is a palindrome.
# An integer is a palindrome when it reads the same backward as forward.

def isPalindrome(input_val: int) -> bool:
    # Negative numbers are not palindromes
    if input_val < 0:
        return False

    # Challenge: do it without casting to a string (which is easy)
    # Chop off the last digit with a modulo and add it to the output, which reverses the order
    output = 0
    remainder = input_val

    while remainder != 0:
        output = 10 * output + remainder % 10
        remainder = int(remainder / 10)

    return input_val == output


# Tests
print(not isPalindrome(-1205))
print(not isPalindrome(-121))
print(not isPalindrome(-1))
print(isPalindrome(0))
print(isPalindrome(1))
print(not isPalindrome(10))
print(isPalindrome(121))
print(not isPalindrome(123456))
print(isPalindrome(123456654321))
