# LeetCode 15 - Three Sums
#
# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
# Find all unique triplets in the array which gives the sum of zero.
#
# Note:
# The solution set must not contain duplicate triplets.

from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    # Need at least three values to have an answer
    if not nums or len(nums) < 3:
        return []

    nums.sort()
    nums_len = len(nums)
    output = []

    for idx in range(nums_len):
        if idx > 0 and nums[idx] == nums[idx-1]:
            continue

        target = -nums[idx]
        start = idx + 1
        finish = nums_len - 1

        while start < finish:
            if nums[start] + nums[finish] < target:
                start += 1
            elif nums[start] + nums[finish] > target:
                finish -= 1
            else:
                output.append((nums[idx], nums[start], nums[finish]))
                start += 1
                finish -= 1

    return [list(i) for i in set(output)]


# Tests
print(threeSum([]) == [])
print(threeSum([-1, 0]) == [])
print(threeSum([-1, 0, 1]) == [[-1, 0, 1]])
print(threeSum([-3, 1, 2]) == [[-3, 1, 2]])
print(threeSum([-1, -1, 0, 0, 1, 1]) == [[-1, 0, 1]])
print(threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, 0, 1], [-1, -1, 2]])
