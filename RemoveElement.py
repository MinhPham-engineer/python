# https://leetcode.com/problems/remove-element/description/?envType=problem-list-v2&envId=array
from typing import List


class Solution:
    def swapLastElements(self, nums: List[int], val: int) -> int:
        n = len(nums)
        i = 0
        j = n - 1
        count = 0
        while i <= j:
            while i < j and nums[j] == val:
                j -= 1

            if i > j:
                return count

            if i == j:
                if nums[i] == val:
                    return count
                else:
                    return count + 1

            if nums[i] == val:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                j -= 1
            count += 1
            i += 1
        return count

    def swapFirstElement(self, nums: List[int], val: int) -> int:
        write_idx = 0
        for idx in range(len(nums)):
            if nums[idx] != val:
                nums[write_idx] = nums[idx]
                write_idx += 1
        return write_idx


solution = Solution()
nums = [3, 2, 3, 4, 3]
val = 3
print(solution.swapLastElements(nums, val))
print(solution.swapFirstElement(nums, val))

nums1 = [3, 2, 2, 4, 3]
val1 = 3
print(solution.swapLastElements(nums1, val1))
print(solution.swapFirstElement(nums1, val1))

nums2 = [3, 2, 2, 4, 3]
val2 = 5
print(solution.swapLastElements(nums2, val2))
print(solution.swapFirstElement(nums2, val2))

nums3 = [1]
val3 = 1
print(solution.swapLastElements(nums3, val3))
print(solution.swapFirstElement(nums3, val3))
