# LeetCode 27 - Remove Element
#
# Given an array nums and a value val, remove all instances of that value in-place and
# return the new length.
#
# Do not allocate extra space for another array, you must do this by modifying the input
# array in-place with O(1) extra memory.
#
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.

from typing import List

def removeElement(nums: List[int], val: int) -> int:
    if not nums:
        return 0

    # If we iterate forward then our index values will get wonky as we pop elements
    # Instead, move backward through the list, so we are good as we pop values
    for idx in range(len(nums)-1, -1, -1):
        if nums[idx] == val:
            nums.pop(idx)

    return len(nums)


# Tests
nums1 = [3, 2, 2, 3]
print(removeElement(nums1, 3) == 2)
print(nums1 == [2, 2])

nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
print(removeElement(nums2, 2) == 5)
print(nums2 == [0, 1, 3, 0, 4])
