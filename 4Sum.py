from re import L
from typing import List

class Solution:
  def twoPointers(self, nums: List[int], target: int) -> List[int]:
    n = len(nums)
    if n < 4:
      return []
    nums.sort()
    res = set()
    for i in range(n-3):
      while i > 0 and i < n-3 and nums[i] == nums[i-1]:
        i += 1
      if i == n-3:
        break
      for j in range(i+1, n-2):
        while j > i + 1 and j < n - 2 and nums[j] == nums[j-1]:
          j += 1
        
        k = j + 1
        q = n - 1
        while k < q:
          while k > j + 1 and nums[k] == nums[k-1]:
            k+=1
          while q < n - 1 and nums[q] == nums[q+1]:
            q-=1
          if k>=q:
            break
          sum = nums[i] + nums[j] + nums[k] + nums[q]
          if sum == target:
            res.add(tuple([nums[i],nums[j],nums[k],nums[q]]))
            k += 1
            q -= 1
          elif sum < target:
            k += 1
          else:
            q -= 1
    
    return list(res)
  
  def recursive(self, nums: List[int], target: int) -> List[List[int]]:
    n = len(nums)
    if n < 4:
      return []
    nums.sort()
    result = []
    self.helper(nums, target, 4, [], result)
    return result
  def helper(self, nums: List[int], target: int, n: int, temp: List[int], result: List[List[int]]):
    if n < 2:
      return
    if n == 2:
      output_two_sum = self.two_sum(nums, target)
      for idx in output_two_sum:
        final = temp + idx
        if final not in result:
          result.append(temp+idx)
    else:
      for i in range(len(nums) - n + 1):
        if nums[i]*n > target or nums[-1]*n < target:
          continue
        else:
          self.helper(nums[i+1:], target - nums[i], n-1, temp + [nums[i]], result)
  def two_sum(self, nums: List[int], target: int) -> List[List[int]]:
    n = len(nums)
    if n < 2:
      return []
    i = 0
    j = n - 1
    res = []
    while i < j:
      sum = nums[i] + nums[j]
      if sum == target:
        res.append([nums[i], nums[j]])
        i += 1
        j -= 1
        while i < j and nums[i] == nums[i-1]:
          i += 1
        while i < j and nums[j] == nums[j+1]:
          j -= 1
      elif sum < target:
        i += 1
      else: 
        j -= 1
        
    return res

solution = Solution()
nums = [1,0,-1,0,-2,2]
nums1 = [2,2,2,2,2]
nums2 = [-1,0,1,2,-1,-4]
# print(solution.twoPointers(nums, 0))
# print(solution.twoPointers(nums1, 8))
# print(solution.recursive(nums, 0))
print(solution.recursive(nums1, 8))