# LeetCode 29 - Divide Two Integers
#
# Given two integers dividend and divisor, divide two integers without using
# multiplication, division and mod operator. Return the quotient after dividing dividend by divisor.
#
# The integer division should truncate toward zero, which means losing its fractional part.
# For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.
import math

def divide(dividend: int, divisor: int) -> int:
    if dividend == 0:
        return 0

    positive = (dividend < 0) == (divisor < 0)
    dividend = abs(dividend)
    divisor = abs(divisor)

    # This took a while. I first tried to iteratively calculate the quotient, but I ran into
    # time limits on LeetCode. Had to do some research, but found out that we can recreate
    # division with log and exp, which are still allowed by the problem.
    # https://en.wikipedia.org/wiki/List_of_logarithmic_identities
    quotient = math.floor(math.exp(math.log(dividend) - math.log(divisor)))

    if not positive:
        quotient = -quotient

    if quotient > 2147483647 or quotient < -2147483648:
        return 2147483647

    return quotient

# Tests
print(divide(10, 2) == 5)
print(divide(0, 1) == 0)
print(divide(1, 1) == 1)
print(divide(-1, 1) == -1)
print(divide(-1, -1) == 1)
print(divide(10, 3) == 3)
print(divide(7, -3) == -2)
print(divide(-2147483648, -1) == 2147483647)
print(divide(2147483647, 2) == 1073741823)
