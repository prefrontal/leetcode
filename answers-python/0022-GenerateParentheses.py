# Leetcode 22 - Generate Perentheses
#
# Given n pairs of parentheses, write a function to generate
# all combinations of well-formed parentheses.

from typing import List

def generateParenthesis(n: int) -> List[str]:
    if not n:
        return []

    if n == 1:
        return ["()"]

    result = [["(", 1, 0]]

    for _ in range(1, 2*n):
        permutations = []

        # BFS solution to build up the valid possibilities
        # We can reduce the search space using the following rules to limit the output
        for res in result:
            s, left, right = res
            if left - right > 0:
                permutations.append([s + ")", left, right + 1])

            if left < n:
                permutations.append([s + "(", left + 1, right])
        result = permutations

    return sorted([x[0] for x in result])


# Tests
print(generateParenthesis(1) == ["()"])
print(generateParenthesis(3) == ["((()))", "(()())", "(())()", "()(())", "()()()"])
