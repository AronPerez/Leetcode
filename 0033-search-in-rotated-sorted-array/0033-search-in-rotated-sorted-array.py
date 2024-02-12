class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        # what if the array is normal?
        
        while l <= r:
            m = l + (r - l) // 2 
            
         
            # Find target
            if nums[m] == target:
                return m
            # Subarray on mids left is sorted
            elif nums[m] >= nums[l]:
                # What if our mid is greater than target
                # Then it is likely to the left
                if nums[m] > target and target >= nums[l]:
                    r = m - 1
                else:
                    l = m + 1
            # subarray on mid's right is sorted
            else:
                if target > nums[m]  and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        
        return -1