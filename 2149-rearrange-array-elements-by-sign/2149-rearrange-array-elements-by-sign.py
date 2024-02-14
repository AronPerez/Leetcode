class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # Keep track of neg numbers with stack
        
        # Once we have all neg numbers, go through pos values
        
        # Is a greed algo
        negs = []
        
        for num in nums:
            if num < 0:
                negs.append(num)
            else:
                continue
                
        result = []
        i = 0
        
        for index in range(len(nums)):
            if nums[index] > 0: # Once we find pair, add and increment i
                result.append(nums[index]) # Add pos
                result.append(negs[i]) # Add neg
                i += 1 # Increment neg
            else:
                continue
                
        return result
                
                
        