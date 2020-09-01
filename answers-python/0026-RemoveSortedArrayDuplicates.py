# LeetCode 26 - Remove Duplicates from Sorted Array
#
# Given a sorted array nums, remove the duplicates in-place such that each element appear only
# once and return the new length. Do not allocate extra space for another array, you must do this
# by modifying the input array in-place with O(1) extra memory.

from typing import List

def removeDuplicates(nums: List[int]) -> int:
    if not nums:
        return 0

    if len(nums) == 1:
        return 1

    # If we iterate forward then our index values will get wonky as we pop elements
    # Instead, move backward through the list, so we are good as we pop values
    for idx in range(len(nums)-1, 0, -1):
        if nums[idx-1] == nums[idx]:
            nums.pop(idx)

    return len(nums)


# Tests
print(removeDuplicates([]) == 0)
print(removeDuplicates([1]) == 1)
print(removeDuplicates([1, 1, 1]) == 1)
print(removeDuplicates([1, 1, 2]) == 2)
print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5)
