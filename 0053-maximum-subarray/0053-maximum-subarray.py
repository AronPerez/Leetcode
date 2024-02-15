class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans, currentSubarray = nums[0], 0
        
        for num in nums:
            if currentSubarray < 0: # If neg, subarray no good
                currentSubarray = 0
                
             
            currentSubarray += num
            
            # Check if max
            ans = max(ans, currentSubarray)
            
                
           
            
        return ans
            
        
        