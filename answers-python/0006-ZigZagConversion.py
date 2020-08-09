# LeetCode 6 - ZigZag Conversion
#
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
# (you may want to display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
#
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a number of rows

def convert(s: str, numRows: int) -> str:
    if not s:
        return ""

    if numRows == 1:
        return s

    # Setup a list of lists with length numRows to capture the output
    output_rows = [[] for i in range(numRows)]

    # Keep track of which row we are on and the direction we are moving
    # Fun fact, for this problem we don't need to track the current column
    row = 0
    row_direction = 1

    for val in s:
        output_rows[row].append(val)
        row += row_direction
        if row in [0, numRows-1]:
            row_direction *= -1

    # We need to bring together the list-of-lists to output
    return ''.join([''.join(x) for x in output_rows])


# Test
print(convert("S", 1) == "S")
print(convert("S", 4) == "S")
print(convert("AB", 1) == "AB")
print(convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR")
print(convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI")
