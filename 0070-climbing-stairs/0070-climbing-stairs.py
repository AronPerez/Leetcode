class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1: # Can only reach these with 1 step
            return 1
        
        prev, curr = 1, 1 # Only 1 way to get to 0 and 1 (1 step)
        for i in range(2, n+1):
             #0, 1, 2, 3, 4, 5 = [1, 1, 2, 3, 5, 8]
            # Sum i-1 + i-2 values
            temp = curr
            curr = prev + curr
            prev = temp
        return curr
        