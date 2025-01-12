class Solution:
  def romanToInt(self, s:str) -> int:
    if len(s) == 0:
      return 0
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = roman_dict[s[0]]
    for i in range(1, len(s)):
      if roman_dict[s[i-1]] < roman_dict[s[i]]:
        sum += roman_dict[s[i]] - 2 * roman_dict[s[i-1]]
      else:
        sum += roman_dict[s[i]]
      
    return sum

solution = Solution()
print(solution.romanToInt("III")) # 3
print(solution.romanToInt('IV')) # 4
print(solution.romanToInt('XVI')) # 16
print(solution.romanToInt('MCMXCIV')) # 1000 + 900 + 40 + 4
        
        
    