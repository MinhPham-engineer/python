from typing import List

class ReachEndOfArrayWithMaxScore:
    def findMaximumScore(self, nums: List[int]) -> int:
        sum = maximum = 0
        for i in range(len(nums)-1):
            maximum = max(maximum, nums[i])
            sum += maximum
        return sum
    
if __name__ == "__main__":
    obj =   ReachEndOfArrayWithMaxScore()
    nums = [1,3,1,5]
    result = obj.findMaximumScore(nums);
    print(f"Maximum score of the array {nums} is: {result}")
    