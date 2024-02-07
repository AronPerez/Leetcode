class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        values = set(nums)
        longestStreak = 0
        
        for num in values:
            # If it is the start of a sequence (no left neighbor means start of seq)
            if num - 1 not in values:
                currentLength = 0
                while num + currentLength in values:
                    currentLength += 1
                
                longestStreak = max(longestStreak, currentLength)
                
        return longestStreak
                    
        