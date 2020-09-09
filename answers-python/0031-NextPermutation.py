# LeetCode 31 - Next Permutation
#
# Implement next permutation, which rearranges numbers into the lexicographically next
# greater permutation of numbers. If such arrangement is not possible, it must rearrange
# it as the lowest possible order (ie, sorted in ascending order). The replacement must be
# in-place and use only constant extra memory. Here are some examples. Inputs are in the left-hand
# column and its corresponding outputs are in the right-hand column.

import math
from typing import List

def nextPermutation(nums: List[int]) -> None:
    if not nums:
        return

    # Find the lowest value we can flip to meet the criteria
    flip_index = None
    for idx in range(len(nums)-2, -1, -1):
        if nums[idx] < nums[idx+1]:
            flip_index = idx
            break

    # If there is no flip_index, the list is already in the lexicographically
    # greatest permutation so reverse the entire list instead
    if flip_index == None:
        nums.reverse()
        return

    # Find the value to swap with the lowest flip value we found
    min_dist = math.inf
    swap_target = None
    for idx2 in range(flip_index+1, len(nums)):
        if nums[idx2] > nums[flip_index] and nums[idx2] - nums[flip_index] <  min_dist:
            min_dist = nums[idx2] - nums[flip_index]
            swap_target = idx2

    nums[flip_index], nums[swap_target] = nums[swap_target], nums[flip_index]

    # Now, we need to sort the rest of the values in the list to guarantee 
    # it is the next lexicographically greatest permutation
    while True:
        modified = False
        for idx3 in range(len(nums)-2, flip_index, -1):
            if nums[idx3] > nums[idx3+1]:
                nums[idx3], nums[idx3+1] = nums[idx3+1], nums[idx3]
                modified = True
        
        if not modified:
            break

    return


# Tests
input = []
nextPermutation(input)
print(input == [])

input = [1, 2, 3]
nextPermutation(input)
print(input == [1, 3 ,2])

input = [3, 2, 1]
nextPermutation(input)
print(input == [1, 2, 3])

input = [1, 1, 5]
nextPermutation(input)
print(input == [1, 5, 1])

input = [1, 2]
nextPermutation(input)
print(input == [2, 1])

input = [1, 3, 2]
nextPermutation(input)
print(input == [2, 1, 3])

input = [2, 3, 1]
nextPermutation(input)
print(input == [3, 1, 2])

input = [5,4,7,5,3,2]
nextPermutation(input)
print(input == [5,5,2,3,4,7])