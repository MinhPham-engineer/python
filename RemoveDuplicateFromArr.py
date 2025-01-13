# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=problem-list-v2&envId=array
from collections import defaultdict
from typing import List


class Solution:
   # for unsorted arr
    # def unsort(self, nums: List[int]) -> int:
    #     nums_dict = defaultdict(int)
    #     next_idx = 0
    #     for num in nums:
    #         if num not in nums_dict:
    #             nums[next_idx] = num
    #             next_idx += 1
    #             nums_dict[num] += 1
    #     nums[:] = nums[:next_idx]
    #     return next_idx

    # for sorted
    def sortedArr(self, nums: List[int]) -> int:
        next_idx = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[next_idx] = nums[i]
                next_idx += 1
        nums[:] = nums[:next_idx]
        return next_idx


solution = Solution()

nums = [1, 1, 2]
print(solution.sortedArr(nums))
print(nums)

nums1 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(solution.sortedArr(nums1))
print(nums1)
