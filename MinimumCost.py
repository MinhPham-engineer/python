from typing import List
import heapq


class Solution:
    def min_cost(self, nums: List[int]) -> int:
        min_cost = 0
        heapq.heapify(nums)

        while len(nums) > 1:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)

            cost = x * y
            min_cost += cost

            heapq.heappush(nums, cost)
        return min_cost


solution = Solution()
arr = [4, 5, 6, 1, 9, 3, 4, 15]
print(solution.min_cost(arr))
