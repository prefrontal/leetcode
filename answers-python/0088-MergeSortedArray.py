# LeetCode 88 - Merge Sorted Array
#
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
#
# Note:
# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space (size that is equal to m + n)
# to hold additional elements from nums2.
#
# Do not return anything, modify nums1 in-place instead.

from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    if n < 1:
        return

    for idx in range(m + n):
        if not nums2:
            break

        if nums1[idx] > nums2[0]:
            nums1.insert(idx, nums2.pop(0))
            nums1.pop()

    # If we still have elements in nums2, just append them
    if len(nums2) > 0:
        nums1[-len(nums2):] = nums2


# Tests
n1 = [1, 2, 3, 0, 0, 0]
n2 = [2, 5, 6]
merge(n1, 3, n2, 3)
print(n1 == [1, 2, 2, 3, 5, 6])
