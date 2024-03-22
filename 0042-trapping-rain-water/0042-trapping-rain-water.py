class Solution:
    def trap(self, height: List[int]) -> int:
        # Start from 0 and 1
        
        # cannot trap water from start unless has height
        
        # We need to keep going until the l finds a height of at least 1 or more
        
        # Once we find, move r until we find even or higher level
            # Get all depths between then
        
        # from l to r, get heights, take diff from water level to get how much water can store
            # add to total
        n = len(height)  # Get the length of the height array
        left = 0  # Initialize the left pointer
        right = n - 1  # Initialize the right pointer
        left_max = right_max = water = 0  # Initialize variables to store maximum heights and trapped water

        while left <= right:  # Continue until the pointers meet
            if height[left] <= height[right]:  # If the height at the left pointer is smaller or equal
                if height[left] > left_max:  # If the current height is greater than the maximum height from the left
                    left_max = height[left]  # Update the maximum height from the left
                else:
                    water += left_max - height[left]  # Calculate the trapped water at the current position
                left += 1  # Move the left pointer to the right
            else:  # If the height at the right pointer is smaller
                if height[right] > right_max:  # If the current height is greater than the maximum height from the right
                    right_max = height[right]  # Update the maximum height from the right
                else:
                    water += right_max - height[right]  # Calculate the trapped water at the current position
                right -= 1  # Move the right pointer to the left

        return water  # Return the total amount of trapped water
                    
                