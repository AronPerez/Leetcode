class NumArray:

    def __init__(self, nums: List[int]):
        # Initialize the prefix sum array
        self.prefix_sum = [0] * (len(nums) + 1)
        
        # Calculate prefix sums
        for i in range(1, len(self.prefix_sum)):
            self.prefix_sum[i] = self.prefix_sum[i-1] + nums[i-1]
        

    def sumRange(self, left: int, right: int) -> int:
        # Return the sum of elements between left and right (inclusive)
        # by subtracting prefix sum at left from prefix sum at right+1
        return self.prefix_sum[right + 1] - self.prefix_sum[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)