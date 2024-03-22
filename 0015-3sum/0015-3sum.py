class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # You could sort in ascending order
        res = []
        nums.sort()
        # enumerate over nums
        for i, v in enumerate(nums):
            
            # Where you get to a value greater than 0, you cannot 
            if v > 0:
                break
                
            # check if its same value as prev (don't wanna use)
            if i >= 1 and v == nums[i - 1]:
                continue
                
            # now solve two sum basically see if we can make v + l + r == 0
            l, r = i+1, len(nums) - 1
            while l < r:
                threeSum = v + nums[l] + nums[r]
                if threeSum == 0:
                    res.append([v, nums[l], nums[r]])
                    # when we find solution move left
                    l += 1
                    while nums[l] == nums[l-1] and l < r: # keep going until not duplicate or meet r
                        l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    l += 1
                    
        return res
        