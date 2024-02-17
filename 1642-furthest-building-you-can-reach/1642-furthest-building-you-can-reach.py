class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # If the current building's height is >= to the next building's height, you do not need a ladder or bricks.
        
        # If current buildings height is < n + 1, use 1 ladder or h[i+1] - h[i] bricks
        
        ladderAlloc = []
        n = len(heights)
        
        for building in range(0, n - 1):
            climb = heights[building+1] - heights[building]
            
            if climb <= 0: # Taller than the next building, we can continue
                continue
                
            # Will need to alloc ladder for climb
            heapq.heappush(ladderAlloc, climb)
            
            # If not over the num of ladders, just keep going
            if len(ladderAlloc) <= ladders:
                continue
            # Otherwise, we gotta take a climb out of ladder alloc
            bricks -= heapq.heappop(ladderAlloc)
            
            # If bricks are neg, we cannot get to next building
            if bricks < 0:
                return building

        return len(heights) - 1 # Made it to end
                    
                    
                    
        