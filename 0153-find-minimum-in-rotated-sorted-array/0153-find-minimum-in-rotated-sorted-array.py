class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        l, r = 0, len(nums) - 1
        
        # Find out orientation of array
        # If the right is bigger than the left, the value at leftmost is the largest
        
        if nums[r] > nums[l]:
            return nums[l]
        
        
        # Binary search from left to right reversed (descending order)
        
        while r >= l:
            # mid
            m = l + (r - l) // 2
            
            # If mid greater than next element, then mid + 1 is smallest
            if nums[m] > nums[m + 1]:
                return nums[m + 1]
            # If mid element is less than previous element, then mid is smallest
            if nums[m] < nums[m - 1]:
                return nums[m]
            
            # If mid is greater than 0th element, smallest element is still somewhere to the right
            if nums[m] > nums[0]:
                l = m + 1
            else:
                r = m - 1
            
            
            
        return min(nums)