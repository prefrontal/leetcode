# LeetCode 16 - Three Sums Closest
#
# Given an array nums of n integers and an integer target, find three integers in nums such
# that the sum is closest to target. Return the sum of the three integers. You may assume that
# each input would have exactly one solution.

import math
from typing import List

def threeSumClosest(nums: List[int], target: int) -> int:
    # Having these two constraints (given by the problem) accelerate the execution time
    # They aren't necessary, but make the submission more competitive
    if len(nums) < 3 or len(nums) > 10E3:
        return None

    if target < -10E4 or target > 10E4:
        return None

    nums.sort()
    nums_len = len(nums)
    result = math.inf

    # Generally, use the same pointer strategy as problem #15. See where we are at with regard
    # to the target, and then adjust our pointers as necesary to get closer to the target.
    for i in range(nums_len):
        j = i + 1
        k = nums_len - 1

        while j < k:
            current_sum = nums[i] + nums[j] + nums[k]

            if current_sum == target:
                return current_sum

            if abs(current_sum - target) < abs(result - target):
                result = current_sum

            if current_sum < target:
                j += 1
            elif current_sum > target:
                k -= 1

    return result


# Tests
print(threeSumClosest([], 1) is None)
print(threeSumClosest([-1, 2], 1) is None)
print(threeSumClosest([-1, 2, 1, -4], 1) == 2)
print(threeSumClosest([-1, 2, 1, -4], 2) == 2)
print(threeSumClosest([-1, 2, 1, -4], 3) == 2)
print(threeSumClosest([-1, 2, 1, -4], -1) == -1)
print(threeSumClosest([0, 5, -1, -2, 4, -1, 0, -3, 4, -5], 1) == 1)
