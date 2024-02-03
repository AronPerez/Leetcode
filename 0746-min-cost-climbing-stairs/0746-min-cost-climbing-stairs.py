class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        
        minCost = [0] * (n+1) # Index 0 -> index n + 1
        
        # Go from step 2 since the min cost of reaching step 0 and 1 is 0
        for i in range(2, n+1):  
            #0, 1, 2, 3, 4, 5 = [1, 1, 2, 3, 5, 8]
            # Take the min of the two values
            oneStep = minCost[i-1] + cost[i-1]
            twoStep = minCost[i-2] + cost[i-2]
            minCost[i] = min(oneStep, twoStep)
        
        # Final element will be the min value, specifically the top floor
        return minCost[-1]
        
        
        