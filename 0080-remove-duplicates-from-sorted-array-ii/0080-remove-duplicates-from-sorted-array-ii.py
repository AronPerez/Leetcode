class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:    
        i = counter = 1

        while i < len(nums):
            if nums[i] == nums[i-1]: # Counts dupes
                counter += 1

                if counter > 2:
                    nums.pop(i) # Remove 3rd dupe
                    i -= 1 # Decrement i
            else: # Means we are looking at new number
                counter = 1

            i += 1


        return len(nums)

        