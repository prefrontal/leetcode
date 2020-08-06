# LeetCode 345 - Two Sum
#
# Write a function that takes a string as input and reverse only the vowels of a string.
# The vowels does not include the letter "y".

import math

def reverseVowels(s: str) -> str:
    # Don't forget that the vowels can be lowercase or uppercase
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    found_vowels = []

    # First, go through the string and identify the indices of all vowels
    for idx, _ in enumerate(s):
        if s[idx] in vowels:
            found_vowels.append(idx)

    # Check to see if we need to do any more work
    if len(found_vowels) <= 1:
        return s

    # Make the string into a list, swap the vowels, then assemble the final string
    # Work our way toward the middle from the ends. For an odd number of vowels, ignore the middle
    characters = list(s)

    for idx in range(0, math.floor(len(found_vowels)/2)):
        index1 = found_vowels[idx]
        index2 = found_vowels[len(found_vowels) - idx - 1]

        temp_vowel1 = s[index1]
        temp_vowel2 = s[index2]

        characters[index1] = temp_vowel2
        characters[index2] = temp_vowel1

    return "".join(characters)


# Tests
print(reverseVowels("bcd") == "bcd")
print(reverseVowels("ae") == "ea")
print(reverseVowels("aeio") == "oiea")
print(reverseVowels("aeiou") == "uoiea")
print(reverseVowels("abcde") == "ebcda")
print(reverseVowels("abcdefabcdef") == "ebcdafebcdaf")
