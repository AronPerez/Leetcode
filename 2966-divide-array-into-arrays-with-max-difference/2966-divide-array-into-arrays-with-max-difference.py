class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort() # Ascending order
        n = len(nums)
        # Row inside, col outside
        # From 0 to len(n) in steps of 3
        matrix = [nums[i:i+3] for i in range(0, n, 3)]
        for row in matrix:
            if abs(row[0] - row[2]) <= k: # The largest value in the row should be able to diff smallest 
                continue
            else:
                return []
        
        return matrix
                
                
        