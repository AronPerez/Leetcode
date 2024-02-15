class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i, ans, currentSubarray = 0, float('-inf'), 0
        
        
        while i <= len(nums) - 1:
            currentSubarray += nums[i]
            
            # Check if max
            ans = max(ans, currentSubarray)
            
            if currentSubarray < 0: # If neg, subarray no good
                currentSubarray = 0
                
                
            # Increment subarray
            i += 1
            
        return ans
            
        
        