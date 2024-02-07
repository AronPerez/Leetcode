class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        values = set(nums)
        longestStreak = 0
        
        for num in values:
            if num - 1 not in values:
                currentNum = num
                currentStreak = 1
                
                while currentNum + 1 in values:
                    currentNum += 1
                    currentStreak += 1
                    
                longestStreak = max(longestStreak, currentStreak)
            
        return longestStreak
        