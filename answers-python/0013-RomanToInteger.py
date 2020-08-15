# LeetCode 12 - Roman to Integer
#
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
#
# For example, two is written as II in Roman numeral, just two one's added together. Twelve
# is written as, XII, which is simply X + II. The number twenty seven is written as XXVII,
# which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right. However, the numeral
# for four is not IIII. Instead, the number four is written as IV. Because the one is before the
# five we subtract it making four. The same principle applies to the number nine, which is written
# as IX. There are six instances where subtraction is used:
#
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer. Input is guaranteed to
# be within the range from 1 to 3999.

def romanToInt(s: str) -> int:
    if not s:
        return 0

    symbol_map = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}

    output = 0
    last_val = 0

    for val in reversed(s):
        integer_val = symbol_map.get(val)

        if integer_val < last_val:
            integer_val *= -1

        output += integer_val
        last_val = integer_val

    return output



# Tests
print(romanToInt("") == 0)
print(romanToInt("I") == 1)
print(romanToInt("V") == 5)
print(romanToInt("X") == 10)
print(romanToInt("L") == 50)
print(romanToInt("C") == 100)
print(romanToInt("D") == 500)
print(romanToInt("M") == 1000)
print(romanToInt("IV") == 4)
print(romanToInt("IX") == 9)
print(romanToInt("XL") == 40)
print(romanToInt("XC") == 90)
print(romanToInt("CD") == 400)
print(romanToInt("CM") == 900)
print(romanToInt("XLIV") == 44)
print(romanToInt("MMMCMXCIX") == 3999)
