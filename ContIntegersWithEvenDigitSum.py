# 2180

class Solution:
  # brute force
  # def countEven(self, num: int) -> int:
  #   sum = 0
  #   for i in range(2,num+1):
  #     if self.sumOfDigit(i)%2 == 0:
  #       sum += 1

  #   return sum
  # def sumOfDigit(self, num:int) -> int: 
  #   sum = 0
  #   while(num):
  #     sum += num % 10
  #     num //= 10

  #   return sum
  # def countEven(self, num: int) -> int:
  #   return sum(sum(int(x) for x in str(i)) % 2 == 0 for i in range(2,num+1))
  
# Integers:             [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
# Sums:                 [1, 2, 3, 4, 5, 6, 7, 8, 9,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10,  2,  3,  4,  5,  6]
# Sum is Even :        [0, 1, 0, 1, 0, 1, 0, 1, 0,  0,  1,  0,  1,  0,  1,  0,  1,  0,  1,  1,  0,  1,  0,  1]
# Count(Even sums):     [0, 1, 1, 2, 2, 3, 3, 4, 4,  4,  5,  5,  6,  6,  7,  7,  8,  8,  9, 10, 10, 11, 11, 12]  
# Observation:
# For a num with even sum of its digits, count of integers with even digit sum less than or equal to num is num/2, else if sum is odd then (num-1) / 2
  def countEven(self, num:int) -> int:
    return num//2 if sum(int(c) for c in str(num)) % 2 == 0 else (num-1)//2

solution = Solution()
print(solution.countEven(30))