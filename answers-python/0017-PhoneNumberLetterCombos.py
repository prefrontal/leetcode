# LeetCode 17 - Phone Number Letter Combinations
#
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations
# that the number could represent.
#
# A mapping of digit to letters (just like on the telephone buttons) is given below.
# Note that 1 does not map to any letters.

import itertools
from typing import List

def letterCombinations(digits: str) -> List[str]:
    if not digits:
        return []

    digits_int = [int(j) for j in digits]

    digit_map = {
        2: ["a", "b", "c"],
        3: ["d", "e", "f"],
        4: ["g", "h", "i"],
        5: ["j", "k", "l"],
        6: ["m", "n", "o"],
        7: ["p", "q", "r", "s"],
        8: ["t", "u", "v"],
        9: ["w", "x", "y", "z"]
    }

    output = []

    for digit in digits_int:
        
        if 2 > digit > 9:
            return []

        if not output:
            output = [letter for letter in digit_map[digit]]
        else:
            output = [line+letter for letter in digit_map[digit] for line in output]
        
    return sorted(output)

# Tests
print(letterCombinations("") == [])
print(letterCombinations("2") == ["a", "b", "c"])
print(letterCombinations("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])