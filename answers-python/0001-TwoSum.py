# LeetCode 1 - Two Sum
#
# Given an array of integers, return indices of the two numbers such that they add up to a specific
# target. You may assume that each input would have exactly one solution, and you may not use the
# same element twice.

from collections import defaultdict
from typing import List

# Find two elements of a list that add up to a target value
# Strategy is to have a dict with elements of the list as keys
# and lists of indices of those elements as values
def twoSum(nums: List[int], target: int) -> List[int]:

    # Load a dictionary with lists of index values
    nums_dict = defaultdict(list)
    for idx, val in enumerate(nums):
        nums_dict[val].append(idx)

    # Search for the pair that add up to the target
    for idx, val in enumerate(nums):
        diff_target = target - val
        diff_target_list = nums_dict.get(diff_target)

        if diff_target_list:
            for diff_idx in diff_target_list:
                if idx != diff_idx:
                    return [idx, diff_idx]

    return []


# Tests
print([0, 1] == twoSum([2, 7, 11, 15], 9))
print([0, 1] == twoSum([10, 10, 10, 10], 20))
print([0, 1] == twoSum([20, 0, 10, 10], 20))
print([0, 1] == twoSum([-20, 40, 10, 10], 20))
print([] == twoSum([10, 9, 8, 7], 20))
