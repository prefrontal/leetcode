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
    for idx in range(len(nums)-2, -1, -1):
        if nums[idx] < nums[idx+1]:
            min_dist = math.inf
            swap_target = None
            for idx2 in range(idx+1, len(nums)):
                if nums[idx2] > nums[idx] and nums[idx2] - nums[idx] <  min_dist:
                    min_dist = nums[idx2] - nums[idx]
                    swap_target = idx2
            #print("Swap target: ", swap_target)
            temp = nums[idx]
            nums[idx] = nums[swap_target]
            nums[swap_target] = temp

            while True:
                modified = False
                for idx3 in range(len(nums)-2, idx, -1):
                    if nums[idx3] > nums[idx3+1]:
                        temp = nums[idx3]
                        nums[idx3] = nums[idx3+1]
                        nums[idx3+1] = temp
                        modified = True
                
                if not modified:
                    break

            return
    
    # If we get to this point, the list is already in the lexicographically greatest permutation
    # so flip the whole thing instead
    nums.reverse()
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