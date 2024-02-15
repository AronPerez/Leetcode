class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort() # Ascending
        
        # The longest side is smaller than the sum of the two other sides
        previous_elements_sum = 0
        ans = -1
        for num in nums:
            if num < previous_elements_sum:
                ans = num + previous_elements_sum
            previous_elements_sum += num
        return ans
        