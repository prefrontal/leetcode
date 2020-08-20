# LeetCode 18 - Four Sums
#
# Given an array nums of n integers and an integer target, are there elements a, b, c, and d
# in nums such that a + b + c + d = target? Find all unique quadruplets in the array which
# gives the sum of target.
#
# Note: The solution set must not contain duplicate quadruplets.

from typing import List

def fourSum(nums: List[int], target: int) -> List[List[int]]:
    # Need at least three values to have an answer
    if not nums or len(nums) < 4:
        return []

    nums.sort()
    nums_len = len(nums)
    output = []

    # This is pretty similar to Three Sums (#15) but with an additional outer loop
    # This adds the extra digit for consideration and we get O(n^3) performance
    for idx1 in range(nums_len-1):
        for idx2 in range(idx1+1, nums_len):
            remainder = target - nums[idx1] - nums[idx2]
            start = idx2 + 1
            finish = nums_len - 1

            while start < finish:
                if nums[start] + nums[finish] < remainder:
                    start += 1
                elif nums[start] + nums[finish] > remainder:
                    finish -= 1
                else:
                    output.append((nums[idx1], nums[idx2], nums[start], nums[finish]))
                    start += 1
                    finish -= 1

    return [list(i) for i in set(output)]


# Tests
print(fourSum([], 0) == [])
print(fourSum([1, 0, -1], 0) == [])
print(fourSum([0, 0, 0, 0], 0) == [[0, 0, 0, 0]])
print(fourSum([0, 0, 0, 0], 1) == [])
print(fourSum([1, 0, -1, 0, -2, 2], 0) == [[-2, -1, 1, 2], [-1, 0, 0, 1], [-2, 0, 0, 2]])
