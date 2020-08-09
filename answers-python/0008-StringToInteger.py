# LeetCode 8 - String to Integer (atoi)
#
# Implement atoi which converts a string to an integer.
#
# The function first discards as many whitespace characters as necessary until the first
# non-whitespace character is found. Then, starting from this character, takes an optional
# initial plus or minus sign followed by as many numerical digits as possible, and interprets
# them as a numerical value.
#
# The string can contain additional characters after those that form the integral number, which are
# ignored and have no effect on the behavior of this function.
#
# If the first sequence of non-whitespace characters in str is not a valid integral number, or if
# no such sequence exists because either str is empty or it contains only whitespace characters,
# no conversion is performed.
#
# If no valid conversion could be performed, a zero value is returned.

def myAtoi(num_str: str) -> int:
    if not num_str:
        return 0

    # Get rid of whitespace on either side of the string first to simplify things
    num_str = num_str.strip()
    if not num_str:
        return 0

    valid_prefix = ["-", "+"]
    valid_chars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    # If it doesn't start with a valid character then return immediately
    if num_str[0] not in valid_prefix and num_str[0] not in valid_chars:
        return 0

    # If we just have one value then wrap things up now
    if len(num_str) == 1:
        if num_str[0] in valid_chars:
            return int(num_str)

        return 0

    # The string is at least two characters long if we reach this point
    # Test for a valid negative/positive prefix as a sanity check
    if num_str[0] in valid_prefix and num_str[1] not in valid_chars:
        return 0

    output = 0

    # Find all of the characters that we should consider, starting with the second character
    for idx in range(1, len(num_str)):
        if num_str[idx] not in valid_chars:
            output = int(num_str[0:idx])
            break
        if idx == len(num_str)-1:
            output = int(num_str)

    # Gotta keep things within 32 bit boundaries for the problem
    if output > 2147483647:
        output = 2147483647
    elif output < -2147483648:
        output = -2147483648

    return output


# Tests
print(myAtoi("") == 0)
print(myAtoi(" ") == 0)
print(myAtoi("0") == 0)
print(myAtoi("-") == 0)
print(myAtoi("--") == 0)
print(myAtoi("+") == 0)
print(myAtoi("++") == 0)
print(myAtoi("1") == 1)
print(myAtoi("+1") == 1)
print(myAtoi("-1") == -1)
print(myAtoi("42") == 42)
print(myAtoi("-42") == -42)
print(myAtoi("   -42") == -42)
print(myAtoi("   -42abcabc") == -42)
print(myAtoi("   abcabc-42") == 0)
print(myAtoi("   2147483648abcabc") == 2147483647)
print(myAtoi("   -21474836489abcabc") == -2147483648)
