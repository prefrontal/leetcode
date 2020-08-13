# LeetCode 11 - Container With Most Water
#
# Given n non-negative integers a1, a2, ..., an , where each represents a point at
# coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i
# is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container,
# such that the container contains the most water.
# Note: You may not slant the container and n is at least 2.

from typing import List

def maxArea(height: List[int]) -> int:
    if not height:
        return 0

    # First solution was nested loops, but that ran in O(n^2) time and timed out
    # This solution uses pointers to move through the values and runs in O(n) time
    idx_l = 0
    idx_r = len(height) - 1
    max_volume = 0

    while idx_l < idx_r:
        height_l = height[idx_l]
        height_r = height[idx_r]
        width = idx_r - idx_l

        top = min(height_l, height_r)
        max_volume = max(max_volume, width*top)

        if height_l < height_r:
            idx_l += 1
        else:
            idx_r -= 1

    return max_volume


# Tests
print(maxArea([]) == 0)
print(maxArea([10, 10]) == 10)
print(maxArea([10, 0, 10]) == 20)
print(maxArea([0, 10, 10]) == 10)
print(maxArea([10, 10, 0]) == 10)
print(maxArea([12, 11, 10]) == 20)
print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49)
