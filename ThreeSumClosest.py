from typing import List
# https://leetcode.com/problems/3sum-closest/?envType=problem-list-v2&envId=array
class Solution:
    # brute force -> time limit
    def bruteForce(self, nums: List[int], target: int) -> int:
      n = len(nums)
      min = float('inf')
      res = 0
      for i in range(n -2):
        for j in range(i+1, n-1):
          for k in range(j+1, n):
            dis = target - (nums[i] + nums[j] + nums[k])
            if abs(dis) < min :
              min = abs(dis)
              res = target - dis
      return res
    
    # two pointers
    # time complexity: max ( O(nlogn), O(n2)) -> O(n2)
    # space complexity O(1)
    def twoPointers(self, nums: List[int], target: int) -> int:
      n = len(nums)
      if n < 3:
        return 0 
      nums.sort()
      min = float('inf')
      res = 0
      for i in range(n):
        j = i + 1
        k = n-1
        while j < k:
          dis = target - (nums[i] + nums[j] + nums[k])
          if abs(dis) < min :
            min = abs(dis)
            res = target - dis
            # opposite because if dis is larger, the sum must be smaller
          if dis > 0:
            j += 1
          else:
            k -= 1
      return res


solution = Solution()
nums = [-1,2,1,-4]
target = 1
# print(solution.bruteForce(nums, target))
print(solution.twoPointers(nums, target))