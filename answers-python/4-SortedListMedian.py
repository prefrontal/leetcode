# LeetCode 4 - Median of Two Sorted Arrays
#
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
# You may assume nums1 and nums2 cannot be both empty.

from typing import List

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    # We need a full list of values that is then sorted
    full_list = nums1 + nums2
    full_list.sort()

    if len(full_list) % 2 == 0:
        # Need to find the midpoint of two values if there is an even number of elements
        upper = int(len(full_list) / 2)
        lower = upper - 1
        return (full_list[upper] + full_list[lower]) / 2

    # Just need to find the absolute middle if there is an odd number of elements
    return full_list[int(len(full_list) / 2)]

# Tests
print(findMedianSortedArrays([1, 3], [2]) == 2)
print(findMedianSortedArrays([1, 2], [3, 4]) == 2.5)
print(findMedianSortedArrays([1, 2, 3], [4, 5, 6]) == 3.5)
