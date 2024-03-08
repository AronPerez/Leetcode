class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        countFreqDict = Counter(nums) # {1: 2}
        
        ans = 0
        prevValue = float('inf')
        
        # ((1, 2), (2, 2), (3, 1), (4, 1))
        for key, value in countFreqDict.most_common():
            if prevValue != float('inf') and value < prevValue:
                break
            prevValue = value
            ans += value
            
        return ans
            
            
            
            
            
        
        
        