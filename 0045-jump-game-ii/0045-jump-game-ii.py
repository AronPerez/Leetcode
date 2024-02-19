class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps, end, farthest = 0, 0, 0
        for i in range(len(nums) - 1):  # We don't need to iterate the last element
            farthest = max(farthest, nums[i] + i)
            if i == end:  # If we reach the end of the current jump
                jumps += 1  # We make a jump
                end = farthest  # Update the end of the current jump
                if end >= len(nums) - 1:  # If we can reach the last element
                    break  # We break the loop
        return jumps
