from typing import List

class Solution:
  # first_sol
  def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
    m = len(grid)
    n = len(grid[0])
    should_skip = False
    res = []
    for i in range(0, m):
      j = 0
      plusInt = 1
      if i % 2 == 1:
        j = n - 1
        plusInt = -1
      while -1 < j and j < n:
        if not should_skip:
          res.append(grid[i][j])
          should_skip = True
        else:
          should_skip = False
        j += plusInt
    return res
  
  
  def optimizeTraversal(self, grid: List[List[int]]) -> List[int]:
    if not grid or not grid[0]:
      return []
    m = len(grid)
    n = len(grid[0])
    should_skip = False
    res = []
    
    for i in range(m):
      if i % 2 == 0:
        row_indices = range(n)
      else:
        row_indices = range(n-1, -1, -1)
      
      for  j in row_indices:
        if not should_skip:
          res.append(grid[i][j])
          should_skip = True
        else:
          should_skip = False
    return res

solution = Solution()
grid = [[1,2],[3,4]]
grid1 = [[2,1],[2,1],[2,1]]
grid2 = [[1,2,3],[4,5,6],[7,8,9]]
print(solution.zigzagTraversal(grid))
print(solution.zigzagTraversal(grid1))
print(solution.zigzagTraversal(grid2))