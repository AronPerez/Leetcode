class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        elementsToDelete = 1
        for r in range(len(nums)):
            # If we included a zero in the window we reduce the value of k.
            # Since 1 max deletes we can do
            elementsToDelete -= 1 - nums[r]
            
            if elementsToDelete < 0:
                # We need to move the left element to throw out a zero
                elementsToDelete += 1 - nums[l]
                l += 1
                   
        return r - l
                
        
        