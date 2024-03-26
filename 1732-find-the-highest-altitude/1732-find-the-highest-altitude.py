class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxAlt = 0
        tempAlt = 0
        
        for val in gain:
            tempAlt += val
            maxAlt = max(maxAlt, tempAlt)
            
        return maxAlt
            
        