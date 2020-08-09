# LeetCode 7 - Reverse Integer
#
# Given a 32-bit signed integer, reverse digits of an integer.

def reverse(x: int) -> int:
    if not x:
        return 0

    is_negative = x < 0

    # Strategy for negative numbers is to make them positive and then flip them back later
    if is_negative:
        x *= -1

    # Make the integer a string, reverse it, and then cast it back to an integer
    output = int(str(x)[::-1])

    if is_negative:
        output *= -1

    # One of the test cases is greater than a 32 bit integer can hold
    if output < -2147483648 or output > 2147483647 :
        output = 0

    return output

# Tests
print(reverse(0) == 0)
print(reverse(123) == 321)
print(reverse(-123) == -321)
print(reverse(120) == 21)
print(reverse(1200) == 21)
print(reverse(-1200) == -21)
print(reverse(1534236469) == 0)
print(reverse(-1534236469) == 0)
